#!/usr/bin/env python
# Copyright (C) 2015-2018 Swift Navigation Inc.
# Contact: Swift Navigation <dev@swiftnav.com>
#
# This source is subject to the license found in the file 'LICENSE' which must
# be be distributed together with this source. All other rights reserved.
#
# THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.


"""
Various structs shared between modules
"""

import json

import construct

from sbp.msg import SBP, SENDER_ID
from sbp.utils import fmt_repr, exclude_fields, walk_json_dict, containerize

# Automatically generated from piksi/yaml/swiftnav/sbp/gnss.yaml with generate.py.
# Please do not hand edit!


class GnssSignal(object):
  """GnssSignal.
  
  Signal identifier containing constellation, band, and satellite identifier

  
  Parameters
  ----------
  sat : int
    Constellation-specific satellite identifier
  code : int
    Signal constellation, band and code

  """
  _parser = construct.Embedded(construct.Struct(
                     'sat' / construct.Int8ul,
                     'code' / construct.Int8ul,))
  __slots__ = [
               'sat',
               'code',
              ]

  def __init__(self, payload=None, **kwargs):
    if payload:
      self.from_binary(payload)
    else:
      self.sat = kwargs.pop('sat')
      self.code = kwargs.pop('code')

  def __repr__(self):
    return fmt_repr(self)
  
  def from_binary(self, d):
    p = GnssSignal._parser.parse(d)
    for n in self.__class__.__slots__:
      setattr(self, n, getattr(p, n))

  def to_binary(self):
    d = dict([(k, getattr(obj, k)) for k in self.__slots__])
    return GnssSignal.build(d)
    
class GnssSignalDep(object):
  """GnssSignalDep.
  
  Deprecated.
  
  Parameters
  ----------
  sat : int
    Constellation-specific satellite identifier.

Note: unlike GnssSignal, GPS satellites are encoded as
(PRN - 1). Other constellations do not have this offset.

  code : int
    Signal constellation, band and code
  reserved : int
    Reserved

  """
  _parser = construct.Embedded(construct.Struct(
                     'sat' / construct.Int16ul,
                     'code' / construct.Int8ul,
                     'reserved' / construct.Int8ul,))
  __slots__ = [
               'sat',
               'code',
               'reserved',
              ]

  def __init__(self, payload=None, **kwargs):
    if payload:
      self.from_binary(payload)
    else:
      self.sat = kwargs.pop('sat')
      self.code = kwargs.pop('code')
      self.reserved = kwargs.pop('reserved')

  def __repr__(self):
    return fmt_repr(self)
  
  def from_binary(self, d):
    p = GnssSignalDep._parser.parse(d)
    for n in self.__class__.__slots__:
      setattr(self, n, getattr(p, n))

  def to_binary(self):
    d = dict([(k, getattr(obj, k)) for k in self.__slots__])
    return GnssSignalDep.build(d)
    
class GPSTimeDep(object):
  """GPSTimeDep.
  
  A wire-appropriate GPS time, defined as the number of
milliseconds since beginning of the week on the Saturday/Sunday
transition.

  
  Parameters
  ----------
  tow : int
    Milliseconds since start of GPS week
  wn : int
    GPS week number

  """
  _parser = construct.Embedded(construct.Struct(
                     'tow' / construct.Int32ul,
                     'wn' / construct.Int16ul,))
  __slots__ = [
               'tow',
               'wn',
              ]

  def __init__(self, payload=None, **kwargs):
    if payload:
      self.from_binary(payload)
    else:
      self.tow = kwargs.pop('tow')
      self.wn = kwargs.pop('wn')

  def __repr__(self):
    return fmt_repr(self)
  
  def from_binary(self, d):
    p = GPSTimeDep._parser.parse(d)
    for n in self.__class__.__slots__:
      setattr(self, n, getattr(p, n))

  def to_binary(self):
    d = dict([(k, getattr(obj, k)) for k in self.__slots__])
    return GPSTimeDep.build(d)
    
class GPSTimeSec(object):
  """GPSTimeSec.
  
  A GPS time, defined as the number of
seconds since beginning of the week on the Saturday/Sunday
transition.

  
  Parameters
  ----------
  tow : int
    Seconds since start of GPS week
  wn : int
    GPS week number

  """
  _parser = construct.Embedded(construct.Struct(
                     'tow' / construct.Int32ul,
                     'wn' / construct.Int16ul,))
  __slots__ = [
               'tow',
               'wn',
              ]

  def __init__(self, payload=None, **kwargs):
    if payload:
      self.from_binary(payload)
    else:
      self.tow = kwargs.pop('tow')
      self.wn = kwargs.pop('wn')

  def __repr__(self):
    return fmt_repr(self)
  
  def from_binary(self, d):
    p = GPSTimeSec._parser.parse(d)
    for n in self.__class__.__slots__:
      setattr(self, n, getattr(p, n))

  def to_binary(self):
    d = dict([(k, getattr(obj, k)) for k in self.__slots__])
    return GPSTimeSec.build(d)
    
class GPSTime(object):
  """GPSTime.
  
  A wire-appropriate receiver clock time, defined as the time
since the beginning of the week on the Saturday/Sunday
transition. In most cases, observations are epoch aligned
so ns field will be 0.

  
  Parameters
  ----------
  tow : int
    Milliseconds since start of GPS week
  ns_residual : int
    Nanosecond residual of millisecond-rounded TOW (ranges
from -500000 to 500000)

  wn : int
    GPS week number

  """
  _parser = construct.Embedded(construct.Struct(
                     'tow' / construct.Int32ul,
                     'ns_residual' / construct.Int32sl,
                     'wn' / construct.Int16ul,))
  __slots__ = [
               'tow',
               'ns_residual',
               'wn',
              ]

  def __init__(self, payload=None, **kwargs):
    if payload:
      self.from_binary(payload)
    else:
      self.tow = kwargs.pop('tow')
      self.ns_residual = kwargs.pop('ns_residual')
      self.wn = kwargs.pop('wn')

  def __repr__(self):
    return fmt_repr(self)
  
  def from_binary(self, d):
    p = GPSTime._parser.parse(d)
    for n in self.__class__.__slots__:
      setattr(self, n, getattr(p, n))

  def to_binary(self):
    d = dict([(k, getattr(obj, k)) for k in self.__slots__])
    return GPSTime.build(d)
    
class CarrierPhase(object):
  """CarrierPhase.
  
  Carrier phase measurement in cycles represented as a 40-bit
fixed point number with Q32.8 layout, i.e. 32-bits of whole
cycles and 8-bits of fractional cycles. This phase has the
same sign as the pseudorange.

  
  Parameters
  ----------
  i : int
    Carrier phase whole cycles
  f : int
    Carrier phase fractional part

  """
  _parser = construct.Embedded(construct.Struct(
                     'i' / construct.Int32sl,
                     'f' / construct.Int8ul,))
  __slots__ = [
               'i',
               'f',
              ]

  def __init__(self, payload=None, **kwargs):
    if payload:
      self.from_binary(payload)
    else:
      self.i = kwargs.pop('i')
      self.f = kwargs.pop('f')

  def __repr__(self):
    return fmt_repr(self)
  
  def from_binary(self, d):
    p = CarrierPhase._parser.parse(d)
    for n in self.__class__.__slots__:
      setattr(self, n, getattr(p, n))

  def to_binary(self):
    d = dict([(k, getattr(obj, k)) for k in self.__slots__])
    return CarrierPhase.build(d)
    

msg_classes = {
}