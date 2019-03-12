from fuzzy_systems.core.membership_functions.free_shape_mf import FreeShapeMF
import numpy as np

class SingletonMF(FreeShapeMF):
    def __init__(self, x):
        """
        Build a singleton membership function by defining the only input value (x)
        wwhere the corresponding output values is 1

        This class is the most basic way available to create singleton membership
        functions.

        :param x: x value of the singleton membership function where it's equal to 1, the rest is 0
        """
        self.x = x
        y = 1
        args = [x], [y] 
        super().__init__(*args)

    def fuzzify(self, in_value):
        # return the 0 if the given in_value is not equal to the self.x
        mf = 0
        if(self.x == in_value):
            mf = 1

        return np.interp(in_value, self._in_values, [mf])