from fuzzy_systems.core.membership_functions.lin_piece_wise_mf import LinPWMF

class TrapMF(LinPWMF):
    def __init__(self, p0, p1, p2, p3):
        
        """
        Build a trapezoidal membership function by defining input values (x axis,  [p0, p1, p2, p3])
        and corresponding output values (y axis, [0.0, 1.0, 1.0, 0.0])

        This class is the most basic way available to create trapezoidal membership
        functions.

        :param p0: first vertice of the trapezoidal membership function
        :param p1: second vertice of the trapezoidal membership function
        :param p2: third vertice of the trapezoidal membership function
        :param p3: fourth vertice of the trapezoidal membership function
        """

        # We test if the trapezoidal membership function is not concave
        assert p3 >= p2, "Input p3 should be greater than or equal to p2"
        assert p2 >= p1, "Input p2 should be greater than or equal to p1"
        assert p1 >= p0, "Input p1 should be greater than or equal to p0"

        # We force the output values to be [0.0, 1.0, 1.0, 0.0] so the trapezoidal membership function is well designed
        args = [p0, 0.0], [p1, 1.0], [p2, 1.0], [p3, 0.0]
        super().__init__(*args)
