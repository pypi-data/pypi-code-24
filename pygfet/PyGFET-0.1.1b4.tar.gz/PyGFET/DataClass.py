#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 17:43:50 2017

@author: aguimera
"""

import numpy as np
from scipy.interpolate import interp1d

import PlotDataClass
import sys

DebugPrint = True


class DataCharDC(object):
    PolyOrder = 10
    FEMn0 = 8e11  # 1/cm^2
    FEMq = 1.602176565e-19
    FEMRc = 300  # absolute value Ohms
    FEMCdl = 2e-6  # F/cm^2
    IntMethod = 'linear'

    def __init__(self, Data):
        for k, v in Data.iteritems():
            if k == 'Gate':
                if v is None:
                    if DebugPrint:
                        print 'No gate values'
                elif np.isnan(v['Ig']).any():
                    if DebugPrint:
                        print 'NaN in gate values'
                else:
                    self.__setattr__('Ig', v['Ig'])
            self.__setattr__(k, v)

        if 'Ud0' not in self.__dict__:
            self.CalcUd0()

    def UpdateData(self, Data):
        for k, v in Data.iteritems():
            self.__setattr__(k, v)

    def CalcUd0(self):
        if 'IdsPoly' not in self.__dict__:
            self.CalcIdsPoly()

        vgs = np.linspace(self.Vgs[0], self.Vgs[-1], len(self.Vgs)*10000)

        self.Ud0 = np.ones(len(self.Vds))*np.NaN
        for ivd, Vds in enumerate(self.Vds):
            self.Ud0[ivd] = vgs[np.argmin(np.polyval(self.IdsPoly[:, ivd], vgs))]

    def CalcIdsPoly(self, PolyOrder=None):
        if PolyOrder:
            self.PolyOrder = PolyOrder
        Ord = self.PolyOrder

        self.IdsPoly = np.ones((Ord+1, len(self.Vds)))*np.NaN
        for ivd, Vds in enumerate(self.Vds):
            self.IdsPoly[:, ivd] = np.polyfit(self.Vgs, self.Ids[:, ivd], Ord)
            

    def CalcGMPoly(self, PolyOrder=None):
        if 'IdsPoly' not in self.__dict__:
            self.CalcIdsPoly(PolyOrder=PolyOrder)

        if PolyOrder:
            self.PolyOrder = PolyOrder
        Ord = self.PolyOrder

        self.GMPoly = np.ones((Ord, len(self.Vds)))*np.NaN

        for ivd, Vds in enumerate(self.Vds):
            self.GMPoly[:, ivd] = np.polyder(self.IdsPoly[:, ivd])


    def CalcFEM(self):  # TODO interpolate IDSpoly from all vgs....
        if 'IdsPoly' not in self.__dict__:
            self.CalcIdsPoly()

        self.FEMn = np.ones((len(self.Vgs), len(self.Vds)))*np.NaN
        self.FEMmu = np.ones((len(self.Vgs), len(self.Vds)))*np.NaN
        self.FEMmuGm = np.ones((len(self.Vgs), len(self.Vds)))*np.NaN

        L = self.TrtTypes['Length']
        W = self.TrtTypes['Width']

        VgUd = np.abs(self.GetVgs(Ud0Norm=True))
        Ids = self.GetIds()
        Gm = np.abs(self.GetGM())
        for ivd, Vds in enumerate(self.Vds):
            n = (self.FEMCdl * VgUd[:, ivd])/self.FEMq
            self.FEMn[:, ivd] = np.sqrt(n**2 + self.FEMn0**2)

            Ieff = Vds/(Vds/Ids[:, ivd] - self.FEMRc)
            mu = (Ieff*L)/(W*Vds*n*self.FEMq)
            self.FEMmu[:, ivd] = mu

            Vdseff = Vds - Ids[:, ivd]*self.FEMRc
            muGM = (Gm[:, ivd]*L)/(self.FEMCdl*Vdseff*W)
            self.FEMmuGm[:, ivd] = muGM

    def GetUd0(self, Vds=None, Vgs=None, Ud0Norm=False,  Normlize=False):
        if 'Ud0' not in self.__dict__:
            self.CalcUd0()

        iVds = self.GetVdsIndexes(Vds)
        if len(iVds) == 0:
            return None

        Ud0 = np.array([])
        for ivd in iVds:
            ud0 = self.Ud0[ivd]
            if Normlize:
                ud0 = ud0-(self.Vds[ivd]/2)
            Ud0 = np.vstack((Ud0, ud0)) if Ud0.size else ud0

        if not hasattr(Ud0, '__iter__'):
            return Ud0[None, None]
        s = Ud0.shape
        if len(s) == 1:
            return Ud0[:, None]
        return Ud0.transpose()

    def GetDateTime(self, **kwargs):
        return self.DateTime

    def GetTime(self, **kwargs):
        return np.datetime64(self.DateTime)[None, None].transpose()

    def GetVds(self, **kwargs):
        return self.Vds

    def GetVgs(self, Vgs=None, Vds=None, Ud0Norm=False):
        if not Ud0Norm:
            return self.Vgs

        iVds = self.GetVdsIndexes(Vds)
        if len(iVds) == 0:
            return None

        if 'Ud0' not in self.__dict__:
            self.CalcUd0()

        Vgs = np.array([])
        for ivd in iVds:
            vgs = self.Vgs - self.Ud0[ivd]
            Vgs = np.vstack((Vgs, vgs)) if Vgs.size else vgs

        s = Vgs.shape
        if len(s) == 1:
            return Vgs[:, None]
        return Vgs.transpose()

    def GetVdsIndexes(self, Vds):
        if Vds:
            if not hasattr(Vds, '__iter__'):
                Vds = (Vds,)
            iVds = []
            for vd in Vds:
                ind = np.where(self.Vds == vd)[0]
                if len(ind) > 0:
                    iVds.append(ind[0])
                else:
                    print 'Vds = ', vd, 'Not in data'
        else:
            iVds = range(len(self.Vds))
        return iVds

    def GetIds(self, Vgs=None, Vds=None, Ud0Norm=False):
        iVds = self.GetVdsIndexes(Vds)
        if len(iVds) == 0:
            return None

        if Vgs is not None:
            vgs = Vgs  # TODO Check Vgs range
        else:
            vgs = self.Vgs

        if 'IdsPoly' not in self.__dict__:
            self.CalcIdsPoly()

        Ids = np.array([])
        for ivd in iVds:
            if Ud0Norm and Vgs is not None:
                vg = vgs + self.Ud0[ivd]
            else:
                vg = vgs
            ids = np.polyval(self.IdsPoly[:, ivd], vg)
            Ids = np.vstack((Ids, ids)) if Ids.size else ids

        if not hasattr(Ids, '__iter__'):
            return Ids[None, None]
        s = Ids.shape
        if len(s) == 1:
            return Ids[:, None]
        return Ids.transpose()

    def GetGM(self, Vgs=None, Vds=None, Normlize=False, Ud0Norm=False):
        iVds = self.GetVdsIndexes(Vds)
        if len(iVds) == 0:
            return None

        if Vgs is not None:
            vgs = Vgs  # TODO Check Vgs range
        else:
            vgs = self.Vgs

        if 'GMPoly' not in self.__dict__:
            self.CalcGMPoly()

        GM = np.array([])
        for ivd in iVds:
            if Ud0Norm and Vgs is not None:
                vg = vgs + self.Ud0[ivd]
            else:
                vg = vgs
            gm = np.polyval(self.GMPoly[:, ivd], vg)
            if Normlize:
                gm = gm/self.Vds[ivd] #*(self.TrtTypes['Length']/self.TrtTypes['Width'])/
            GM = np.vstack((GM, gm)) if GM.size else gm

        if not hasattr(GM, '__iter__'):
            return GM[None, None]
        s = GM.shape
        if len(s) == 1:
            return GM[:, None]
        return GM.transpose()

    def GetGMV(self, **kwargs):
        kwargs.update({'Normlize': True})
        return np.abs(self.GetGM(**kwargs))

    def GetGMMax(self, Vds=None, Normlize=False, Ud0Norm=False):
        iVds = self.GetVdsIndexes(Vds)
        if len(iVds) == 0:
            return None

        vgs = np.linspace(self.Vgs[0], self.Vgs[-1], len(self.Vgs)*1000)

        if 'GMPoly' not in self.__dict__:
            self.CalcGMPoly()

        GMmax = np.array([])
        VgsGMax = np.array([])
        for ivd in iVds:
            gm = np.polyval(self.GMPoly[:, ivd], vgs)
            gm = np.abs(gm)
            if Normlize:
                gm = gm/self.Vds[ivd]
            vgmax = vgs[np.argmax(gm)]
            gmmax = np.polyval(self.GMPoly[:, ivd], vgmax)
            if Normlize:
                gmmax = gmmax/self.Vds[ivd]
            GMmax = np.vstack((GMmax, gmmax)) if GMmax.size else gmmax
            if Ud0Norm:
                vgmax = vgmax - self.Ud0[ivd]
            VgsGMax = np.vstack((VgsGMax, vgmax)) if VgsGMax.size else vgmax

        if not hasattr(GMmax, '__iter__'):
            return GMmax[None, None], VgsGMax[None, None]
        s = GMmax.shape
        if len(s) == 1:
            return GMmax[:, None], VgsGMax[:, None]
        return GMmax.transpose(), VgsGMax.transpose()

    def GetRds(self, Vgs=None, Vds=None, Ud0Norm=False):
        Ids = self.GetIds(Vgs=Vgs, Vds=Vds, Ud0Norm=Ud0Norm)

        if Ids is None:
            return None

        iVds = self.GetVdsIndexes(Vds)

        Rds = np.array([])
        for iid, ivd in enumerate(iVds):
            rds = self.Vds[ivd]/Ids[:, iid]
            Rds = np.vstack((Rds, rds)) if Rds.size else rds

        if not hasattr(Rds, '__iter__'):
            return Rds[None, None]
        s = Rds.shape
        if len(s) == 1:
            return Rds[:, None]
        return Rds.transpose()
            
    def GetFEMn(self, Vgs=None, Vds=None, Ud0Norm=False):
        if 'FEMn' not in self.__dict__:
            self.CalcFEM()
        return self._GetParam('FEMn', Vgs=Vgs, Vds=Vds, Ud0Norm=Ud0Norm)

    def GetFEMmu(self, Vgs=None, Vds=None, Ud0Norm=False):
        if 'FEMmu' not in self.__dict__:
            self.CalcFEM()
        return self._GetParam('FEMmu', Vgs=Vgs, Vds=Vds, Ud0Norm=Ud0Norm)

    def GetFEMmuGm(self, Vgs=None, Vds=None, Ud0Norm=False):
        if 'FEMmuGm' not in self.__dict__:
            self.CalcFEM()
        return self._GetParam('FEMmuGm', Vgs=Vgs, Vds=Vds, Ud0Norm=Ud0Norm)

    def GetIg(self, Vgs=None, Vds=None, Ud0Norm=False):
        if 'Ig' not in self.__dict__:
#            print 'No Gate data'
            return None
        return self._GetParam('Ig', Vgs=Vgs, Vds=Vds, Ud0Norm=Ud0Norm)

    def CheckVgsRange(self, Vgs, iVds, Ud0Norm):
        if Vgs is not None:
            for ivd in iVds:
                if Ud0Norm is None or Ud0Norm == False:
                    vg = Vgs
                    VgsM = self.Vgs
                else:
                    vg = Vgs + self.Ud0[ivd]
                    VgsM = self.Vgs

                if (np.min(vg) < np.min(VgsM)) or (np.max(vg) > np.max(VgsM)):
                    print self.Name, 'Vgs range not valid', vg, VgsM, self.Ud0
                    return None
            return Vgs
        else:
            return self.Vgs

    def _GetParam(self, Param, Vgs=None, Vds=None,
                  Ud0Norm=False, Normlize=False):

        iVds = self.GetVdsIndexes(Vds)
        if len(iVds) == 0:
            return None

        vgs = self.CheckVgsRange(Vgs, iVds, Ud0Norm)
        if vgs is None:
            return None
        if len(self.Vgs) < 2:
            print 'self Vgs len error', self.Vgs
            return None

        if Param not in self.__dict__:
            print 'Not Data'
            return None
        Par = self.__getattribute__(Param)

        PAR = np.array([])
        for ivd in iVds:
            if Ud0Norm and Vgs is not None:
                vg = vgs + self.Ud0[ivd]
            else:
                vg = vgs

            par = interp1d(self.Vgs, Par[:, ivd], kind=self.IntMethod)(vg)
            if Normlize:
                par = par/self.Vds[ivd]
            PAR = np.vstack((PAR, par)) if PAR.size else par

        if not hasattr(PAR, '__iter__'):
            return PAR[None, None]
        s = PAR.shape
        if len(s) == 0:
            return PAR[None, None]
        if len(s) == 1:
            return PAR[:, None]
        return PAR.transpose()

    def GetName(self, **kwargs):
        return self.Name

    def GetWL(self, **kwargs):
        return self.TrtTypes['Width']/self.TrtTypes['Length']

    def GetPass(self, **kwargs):
        return self.TrtTypes['Pass']

    def GetLength(self, **kwargs):
        return self.TrtTypes['Length']

    def GetWidth(self, **kwargs):
        return self.TrtTypes['Width']

    def GetContact(self, **kwargs):
        return self.TrtTypes['Contact']

    def GetTypeName(self, **kwargs):
        return self.TrtTypes['Name']

    def GetPh(self, **kwargs):
        return np.array(self.Info['Ph'])[None, None]

    def GetIonStrength(self, **kwargs):
        return np.array(self.Info['IonStrength'])[None, None]

    def GetFuncStep(self, **kwargs):
        return self.Info['FuncStep']

    def GetComments(self, **kwargs):
        return self.Info['Comments']

    def GetAnalyteCon(self, **kwargs):
        return np.array(self.Info['AnalyteCon'])[None, None]

    def GetGds(self, Vgs=None, Vds=None, Ud0Norm=False):
        Gds = 1 / self.GetRds(Vgs=Vgs, Vds=Vds, Ud0Norm=Ud0Norm)
        return Gds

    def GetGMNorm(self, Vgs=None, Vds=None, Ud0Norm=False):
        GMNorm = self.GetGM(Vgs=Vgs, Vds=Vds, Ud0Norm=Ud0Norm, Normlize=True)
        return GMNorm

    def GetUd0Vds(self, Vgs=None, Vds=None, Ud0Norm=False):
        return self.GetUd0(Vgs=Vgs, Vds=Vds, Ud0Norm=Ud0Norm, Normlize=True)


class DataCharAC(DataCharDC):

    def GetFpsd(self):
        return self.Fpsd

    def GetIrms(self, Vgs=None, Vds=None, Ud0Norm=False):
        return self._GetParam('Irms', Vgs=Vgs, Vds=Vds, Ud0Norm=Ud0Norm)

    def GetIrmsVds(self, Vgs=None, Vds=None, Ud0Norm=False):
        return self._GetParam('Irms', Vgs=Vgs, Vds=Vds,
                              Ud0Norm=Ud0Norm, Normlize=True)

    def GetIrmsIds2(self, Vgs=None, Vds=None, Ud0Norm=False):
        Irms = self._GetParam('Irms', Vgs=Vgs, Vds=Vds, Ud0Norm=Ud0Norm)
        Ids = self.GetIds(Vgs=Vgs, Vds=Vds, Ud0Norm=Ud0Norm)
        return Irms/(Ids**2)

    def GetIrmsIds15(self, Vgs=None, Vds=None, Ud0Norm=False):
        Irms = self._GetParam('Irms', Vgs=Vgs, Vds=Vds, Ud0Norm=Ud0Norm)
        Ids = self.GetIds(Vgs=Vgs, Vds=Vds, Ud0Norm=Ud0Norm)
        return Irms/(Ids**1.5)

    def GetIrmsIds(self, Vgs=None, Vds=None, Ud0Norm=False):
        Irms = self._GetParam('Irms', Vgs=Vgs, Vds=Vds, Ud0Norm=Ud0Norm)
        Ids = self.GetIds(Vgs=Vgs, Vds=Vds, Ud0Norm=Ud0Norm)
        return Irms/Ids

    def GetNoA(self, Vgs=None, Vds=None, Ud0Norm=False):
        return self._GetParam('NoA', Vgs=Vgs, Vds=Vds, Ud0Norm=Ud0Norm)

    def GetNoAIds2(self, Vgs=None, Vds=None, Ud0Norm=False):
        NoA=self._GetParam('NoA', Vgs=Vgs, Vds=Vds, Ud0Norm=Ud0Norm)
        Ids = self.GetIds(Vgs=Vgs, Vds=Vds, Ud0Norm=Ud0Norm)
        return NoA/(Ids**2)
    
    def GetNoB(self, Vgs=None, Vds=None, Ud0Norm=False):
        return self._GetParam('NoB', Vgs=Vgs, Vds=Vds, Ud0Norm=Ud0Norm)

    def GetVrms(self, Vgs=None, Vds=None, Ud0Norm=False):
        Irms = self._GetParam('Irms', Vgs=Vgs, Vds=Vds, Ud0Norm=Ud0Norm)
        if Irms is None:
            return None
        gm = np.abs(self.GetGM(Vgs=Vgs, Vds=Vds, Ud0Norm=Ud0Norm))
        return Irms/gm


class PyFETPlotDataClass(PlotDataClass.PyFETPlotBase):

    # (logY, logX, X variable)
    AxsProp = {'Vrms': (1, 0, 'Vgs'),
               'Irms': (1, 0, 'Vgs'),
               'NoA': (1, 0, 'Vgs'),
               'FitErrA': (1, 0, 'Vgs'),
               'FitErrB': (1, 0, 'Vgs'),
               'NoB': (0, 0, 'Vgs'),
               'GM': (0, 0, 'Vgs'),
               'Ids': (0, 0, 'Vgs'),
               'Ig': (0, 0, 'Vgs'),
               'Rds': (0, 0, 'Vgs'),
               'FEMn': (0, 0, 'Vgs'),
               'FEMmu': (1, 0, 'Vgs'),
               'FEMmuGm': (1, 0, 'Vgs'),
               'PSD': (1, 1, 'Fpsd'),
               'GmMag': (1, 1, 'Fgm'),
               'GmPh': (0, 1, 'Fgm')}

    ColorParams = {'Contact': ('TrtTypes', 'Contact'),
                   'Length': ('TrtTypes', 'Length'),
                   'Width': ('TrtTypes', 'Width'),
                   'Pass': ('TrtTypes', 'Pass'),
                   'W/L': (None, None),
                   'Trt': (None, 'Name'),
                   'Date': (None, 'DateTime'),
                   'Ud0': (None, 'Ud0'),
                   'Device': ('TrtTypes', 'Devices.Name'),
                   'Wafer': ('TrtTypes', 'Wafers.Name')}  # TODO fix with arrays

    def __init__(self, Size=(9, 6)):
        self.CreateFigure(Size=Size)

    def GetColorValue(self, Data, ColorOn):
        if self.ColorParams[ColorOn][1]:
            if self.ColorParams[ColorOn][0]:
                p = Data.__getattribute__(self.ColorParams[ColorOn][0])
                v = p[self.ColorParams[ColorOn][1]]
            else:
                v = Data.__getattribute__(self.ColorParams[ColorOn][1])
        elif ColorOn == 'W/L':
            p = Data.__getattribute__('TrtTypes')
            v = p['Width']/p['TrtTypes']['Length']
        return v

    def PlotDataCh(self, DataDict, Trts, Vgs=None, Vds=None, Ud0Norm=False,
                   PltIsOK=True, ColorOn='Trt'):

        self.setNColors(len(DataDict))
        for Trtv in DataDict.values():
            self.color = self.NextColor()
            try:
                self.Plot(DataDict, Vgs=Vgs, Vds=Vds,
                          Ud0Norm=Ud0Norm, PltIsOK=PltIsOK)
            except:  # catch *all* exceptions
                print sys.exc_info()[0]

    def PlotDataSet(self, DataDict, Trts=None,
                    Vgs=None, Vds=None, Ud0Norm=False,
                    PltIsOK=True, ColorOn='Trt', MarkOn='Cycle'):

        if Trts is None:
            Trts = DataDict.keys()

        Par = []
        for TrtN in sorted(Trts):
            for Dat in DataDict[TrtN]:
                Par.append(self.GetColorValue(Dat, ColorOn))

        Par = sorted(set(Par))
        self.setNColors(len(Par))
        ColPar = {}
        for p in Par:
            self.NextColor()
            ColPar[p] = self.color

        for TrtN in sorted(Trts):
            self.marks.reset()
            for Dat in DataDict[TrtN]:
                self.color = ColPar[self.GetColorValue(Dat, ColorOn)]
                if MarkOn == 'Cycle':
                    self.NextMark()                    

                try:
                    self.Plot(Dat, Vgs=Vgs, Vds=Vds,
                              Ud0Norm=Ud0Norm, PltIsOK=PltIsOK)
                except:  # catch *all* exceptions
                    print TrtN, sys.exc_info()[0]

    def Plot(self, Data, Vgs=None, Vds=None,
             Ud0Norm=False, PltIsOK=True, ColorOnVgs=False):

        label = Data.Name

        for axn, ax in self.Axs.iteritems():
            Mark = self.line + self.mark
            if not Data.IsOK and PltIsOK:
                Mark = '+'

            if Vgs is None:
                Valx = Data.GetVgs(Ud0Norm=Ud0Norm)
            else:
                Valx = Vgs
                
            func = Data.__getattribute__('Get' + axn)
            Valy = func(Vgs=Vgs, Vds=Vds, Ud0Norm=Ud0Norm)

            if Valx is not None and Valy is not None:
                ax.plot(Valx, Valy, Mark, color=self.color, label=label)

                if self.AxsProp[axn][0]:
                    ax.set_yscale('log')
                if self.AxsProp[axn][1]:
                    ax.set_xscale('log')

