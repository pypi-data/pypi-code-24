import pip
from repository_v3.util.base_singleton import BaseSingleton
from repository_v3.base_constants import *

class LibraryChecker(BaseSingleton):
    def __init__(self):
        self.supported_libs = [PYSPARK,
                               SCIKIT,
                               PANDAS,
                               XGBOOST,
                               MLPIPELINE,
                               IBMSPARKPIPELINE,
                               TENSORFLOW]
        self.installed_libs = {PYSPARK: False,
                               SCIKIT: False,
                               PANDAS: False,
                               XGBOOST: False,
                               MLPIPELINE: False,
                               TENSORFLOW: False,
                               IBMSPARKPIPELINE: False}
        atleast_one_lib_installed = self._check_if_lib_installed(self.supported_libs)
        if not atleast_one_lib_installed:
            supported_lib_str = self.supported_libs[0]
            lib_num = len(self.supported_libs)
            for i in range(1, lib_num-1):
                supported_lib_str += ', ' + self.supported_libs[i]
            supported_lib_str += ' and ' + self.supported_libs[lib_num-1]
            raise ImportError("The system lacks installations of " + supported_lib_str +
                              ". At least one of the libraries is required for the repository-client to be used")

    def _check_if_lib_installed(self, lib_names):
        atleast_one_lib_installed = False

        # Using try except method as these libraries aren't present in the
        # PyPI repository for pip
        try:
            import pyspark
            self.installed_libs[PYSPARK] = True
            atleast_one_lib_installed = True
        except ImportError:
            pass
        try:
            import mlpipelinepy
            self.installed_libs[MLPIPELINE] = True
            atleast_one_lib_installed = True
        except ImportError:
            pass
        try:
            import pipeline
            self.installed_libs[IBMSPARKPIPELINE] = True
            atleast_one_lib_installed = True
        except ImportError:
            pass
        pkg_list = pip.get_installed_distributions()
        for name in lib_names:
            for pkg in pkg_list:
                if name in str(pkg):
                    self.installed_libs[name] = True
                    atleast_one_lib_installed = True
        return atleast_one_lib_installed

    def check_lib(self, lib_name):
        lib_display_names={PYSPARK: DISPLAY_PYSPARK,
                           SCIKIT: DISPLAY_SCIKIT,
                           PANDAS: DISPLAY_PANDAS,
                           XGBOOST: DISPLAY_XGBOOST,
                           MLPIPELINE: DISPLAY_MLPIPELINE,
                           TENSORFLOW: DISPLAY_TENSORFLOW,
                           IBMSPARKPIPELINE: DISPLAY_IBMSPARKPIPELINE}
        if not self.installed_libs[lib_name]:
            raise NameError('{} Library is not installed. Please install it and execute the command'.
                            format(lib_display_names[lib_name]))