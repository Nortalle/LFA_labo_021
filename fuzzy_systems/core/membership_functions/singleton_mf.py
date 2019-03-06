from fuzzy_systems.core.membership_functions.free_shape_mf import FreeShapeMF
import numpy as np

class SingletonMF(FreeShapeMF):
    def __init__(self, x):
        self.x = x
        y = 1
        args = [x], [y] 
        super().__init__(*args)

    def fuzzify(self, in_value):

        mf = 0

        if(self.x == in_value):
            mf = 1

        return np.interp(in_value, self._in_values, [mf])

