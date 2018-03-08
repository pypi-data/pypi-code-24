# -*- coding: utf-8 -*-

import shutil
import os

import numpy as np

import periods
from periods import ETERNITY
from indexed_enums import EnumArray


class InMemoryStorage(object):
    """
    Low-level class responsible for storing and retrieving calculated vectors in memory
    """

    def __init__(self, is_eternal = False):
        self._arrays = {}
        self.is_eternal = is_eternal

    def get(self, period, extra_params = None):
        if self.is_eternal:
            period = periods.period(ETERNITY)
        period = periods.period(period)

        values = self._arrays.get(period)
        if values is None:
            return None
        if extra_params:
            return values.get(tuple(extra_params))
        if isinstance(values, dict):
            return values.values()[0]
        return values

    def put(self, value, period, extra_params = None):
        if self.is_eternal:
            period = periods.period(ETERNITY)
        period = periods.period(period)

        if extra_params is None:
            self._arrays[period] = value
        else:
            if self._arrays.get(period) is None:
                self._arrays[period] = {}
            self._arrays[period][tuple(extra_params)] = value

    def delete(self, period = None):
        if period is None:
            self._arrays = {}
            return

        if self.is_eternal:
            period = periods.period(ETERNITY)
        period = periods.period(period)

        self._arrays = {
            period_item: value
            for period_item, value in self._arrays.iteritems()
            if not period.contains(period_item)
            }

    def get_known_periods(self):
        return self._arrays.keys()

    def get_memory_usage(self):
        if not self._arrays:
            return dict(
                nb_arrays = 0,
                total_nb_bytes = 0,
                cell_size = np.nan,
                )

        nb_arrays = sum([
            len(array_or_dict) if isinstance(array_or_dict, dict) else 1
            for array_or_dict in self._arrays.itervalues()
            ])

        array = self._arrays.values()[0]
        if isinstance(array, dict):
            array = array.values()[0]
        return dict(
            nb_arrays = nb_arrays,
            total_nb_bytes = array.nbytes * nb_arrays,
            cell_size = array.itemsize,
            )


class OnDiskStorage(object):
    """
    Low-level class responsible for storing and retrieving calculated vectors on disk
    """

    def __init__(self, storage_dir, is_eternal = False):
        self._files = {}
        self._enums = {}
        self.is_eternal = is_eternal
        self.storage_dir = storage_dir

    def _decode_file(self, file):
        enum = self._enums.get(file)
        if enum is not None:
            return EnumArray(np.load(file), enum)
        else:
            return np.load(file)

    def get(self, period, extra_params = None):
        if self.is_eternal:
            period = periods.period(ETERNITY)
        period = periods.period(period)

        values = self._files.get(period)
        if values is None:
            return None
        if extra_params:
            if values.get(tuple(extra_params)) is None:
                return None
            return self._decode_file(values.get(tuple(extra_params)))
        if isinstance(values, dict):
            return self._decode_file(values.values()[0])
        return self._decode_file(values)

    def put(self, value, period, extra_params = None):
        if self.is_eternal:
            period = periods.period(ETERNITY)
        period = periods.period(period)

        filename = str(period)
        if extra_params:
            filename = '{}_{}'.format(
                filename, '_'.join([str(param) for param in extra_params]))
        path = os.path.join(self.storage_dir, filename) + '.npy'
        if isinstance(value, EnumArray):
            self._enums[path] = value.possible_values
            value = value.view(np.ndarray)
        np.save(path, value)
        if extra_params is None:
            self._files[period] = path
        else:
            if self._files.get(period) is None:
                self._files[period] = {}
            self._files[period][tuple(extra_params)] = path

    def delete(self, period = None):
        if period is None:
            self._files = {}
            return

        if self.is_eternal:
            period = periods.period(ETERNITY)
        period = periods.period(period)

        if period is not None:
            self._files = {
                period_item: value
                for period_item, value in self._files.iteritems()
                if not period.contains(period_item)
                }

    def get_known_periods(self):
        return self._files.keys()

    def __del__(self):
        shutil.rmtree(self.storage_dir)  # Remove the holder temporary files
        # If the simulation temporary directory is empty, remove it
        parent_dir = os.path.abspath(os.path.join(self.storage_dir, os.pardir))
        if not os.listdir(parent_dir):
            shutil.rmtree(parent_dir)
