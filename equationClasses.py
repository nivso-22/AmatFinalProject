class LinearEquation:
    a_x = 0
    b_y = 0
    c = 0

    def __init__(self, a_x, b_y, c):
        self.a_x = a_x
        self.b_y = b_y
        self.c = c

    def __str__(self):
        return str(self.a_x) + "X + " + str(self.b_y) + "Y + " + str(self.c) + " = 0"


class QuadraticEquation:
    a_x_quad = 0
    b_x = 0
    c = 0

    def __init__(self, a_x_quad, b_x, c):
        self.a_x_quad = a_x_quad
        self.b_y = b_x
        self.c = c

    def __str__(self):
        return str(self.a_x_quad) + "X² + " + str(self.b_x) + "x + " + str(self.c) + " = 0"


class CubicEquation:
    a_x_cube = 0
    b_x = 0
    c_x = 0
    d = 0

    def __init__(self, a_x_cube, b_x_squared, c_x, d):
        self.a_x_cube = a_x_cube
        self.b_y = b_x_squared
        self.c_x = c_x
        self.d = d

    def __str__(self):
        return str(self.a_x_cube) + "X³ + " + str(self.b_x) + "x² + " + str(self.c_x) + "X + " +str(self.d) + " = 0"


class LogarithmicEquationAX:
    a = 0

    def __init__(self, a):
        self.a = a

    def __str__(self):
        return "log " + str(self.a) + " (X)"


class LogarithmicEquationXA:
    a = 0

    def __init__(self, a):
        self.a = a

    def __str__(self):
        return "log " + "X (" + str(self.a) + ")"


class ExponentialEquationAX:
    a = 0

    def __init__(self, a):
        self.a = a

    def __str__(self):
        return str(self.a) + "^X"


class ExponentialEquationXA:
    a = 0

    def __init__(self, a):
        self.a = a

    def __str__(self):
        return "X^" + str(self.a)

