# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class StartSgeJobRequest(Request):

    def __init__(self):
        super(StartSgeJobRequest, self).__init__(
            'helix', 'qcloudcliV1', 'StartSgeJob', 'helix.api.qcloud.com')

    def get_cmd(self):
        return self.get_params().get('cmd')

    def set_cmd(self, cmd):
        self.add_param('cmd', cmd)

    def get_cpu(self):
        return self.get_params().get('cpu')

    def set_cpu(self, cpu):
        self.add_param('cpu', cpu)

    def get_dataDiskPath(self):
        return self.get_params().get('dataDiskPath')

    def set_dataDiskPath(self, dataDiskPath):
        self.add_param('dataDiskPath', dataDiskPath)

    def get_dataDiskSize(self):
        return self.get_params().get('dataDiskSize')

    def set_dataDiskSize(self, dataDiskSize):
        self.add_param('dataDiskSize', dataDiskSize)

    def get_desc(self):
        return self.get_params().get('desc')

    def set_desc(self, desc):
        self.add_param('desc', desc)

    def get_extMountPathMap(self):
        return self.get_params().get('extMountPathMap')

    def set_extMountPathMap(self, extMountPathMap):
        self.add_param('extMountPathMap', extMountPathMap)

    def get_extOutputPathMap(self):
        return self.get_params().get('extOutputPathMap')

    def set_extOutputPathMap(self, extOutputPathMap):
        self.add_param('extOutputPathMap', extOutputPathMap)

    def get_imgId(self):
        return self.get_params().get('imgId')

    def set_imgId(self, imgId):
        self.add_param('imgId', imgId)

    def get_instanceType(self):
        return self.get_params().get('instanceType')

    def set_instanceType(self, instanceType):
        self.add_param('instanceType', instanceType)

    def get_mem(self):
        return self.get_params().get('mem')

    def set_mem(self, mem):
        self.add_param('mem', mem)

    def get_name(self):
        return self.get_params().get('name')

    def set_name(self, name):
        self.add_param('name', name)

    def get_priority(self):
        return self.get_params().get('priority')

    def set_priority(self, priority):
        self.add_param('priority', priority)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)

    def get_projectLocalPath(self):
        return self.get_params().get('projectLocalPath')

    def set_projectLocalPath(self, projectLocalPath):
        self.add_param('projectLocalPath', projectLocalPath)

    def get_rootPassword(self):
        return self.get_params().get('rootPassword')

    def set_rootPassword(self, rootPassword):
        self.add_param('rootPassword', rootPassword)

    def get_secretId(self):
        return self.get_params().get('secretId')

    def set_secretId(self, secretId):
        self.add_param('secretId', secretId)

    def get_secretKey(self):
        return self.get_params().get('secretKey')

    def set_secretKey(self, secretKey):
        self.add_param('secretKey', secretKey)

    def get_subnetid(self):
        return self.get_params().get('subnetid')

    def set_subnetid(self, subnetid):
        self.add_param('subnetid', subnetid)

    def get_sysDiskSize(self):
        return self.get_params().get('sysDiskSize')

    def set_sysDiskSize(self, sysDiskSize):
        self.add_param('sysDiskSize', sysDiskSize)

    def get_sysDiskType(self):
        return self.get_params().get('sysDiskType')

    def set_sysDiskType(self, sysDiskType):
        self.add_param('sysDiskType', sysDiskType)

    def get_timeout(self):
        return self.get_params().get('timeout')

    def set_timeout(self, timeout):
        self.add_param('timeout', timeout)

    def get_type(self):
        return self.get_params().get('type')

    def set_type(self, type):
        self.add_param('type', type)

    def get_useCache(self):
        return self.get_params().get('useCache')

    def set_useCache(self, useCache):
        self.add_param('useCache', useCache)

    def get_vpcid(self):
        return self.get_params().get('vpcid')

    def set_vpcid(self, vpcid):
        self.add_param('vpcid', vpcid)

    def get_workers(self):
        return self.get_params().get('workers')

    def set_workers(self, workers):
        self.add_param('workers', workers)

    def get_zone(self):
        return self.get_params().get('zone')

    def set_zone(self, zone):
        self.add_param('zone', zone)
