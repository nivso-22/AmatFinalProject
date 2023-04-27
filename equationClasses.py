import math
import numpy


class LinearEquation:
    a_x = 0
    b_y = 0
    c = 0
    color = ""
    range_start = 0
    range_end = 0

    def __init__(self, a_x, b_y, c, color, r_s, r_e):
        self.a_x = int(a_x)
        self.b_y = int(b_y)
        self.c = int(c)
        self.color = color
        self.range_start = int(r_s)
        self.range_end = int(r_e)

    def __str__(self):
        return str(self.a_x) + "X + " + str(self.b_y) + "Y + " + str(self.c) + " = 0"

    def get_color(self):
        return self.color

    def get_plot(self):
        x_list = []
        y_list = []
        for X in range(100*self.range_start, 100*self.range_end + 1):
            x = X/100
            x_list.append(x)
            y_list.append((-self.a_x/self.b_y)*x + -self.c/self.b_y)
        return x_list, y_list

    def get_export(self):
        return ['l', str(self.a_x), str(self.b_y), str(self.c), "0", self.color, str(self.range_start), str(self.range_end)]


class QuadraticEquation:
    a_x_quad = 0
    c = 0
    color = ""
    range_start = 0
    range_end = 0

    def __init__(self, a_x_quad, b_x, c, color, r_s, r_e):
        self.a_x_quad = int(a_x_quad)
        self.b_x = int(b_x)
        self.c = int(c)
        self.color = color
        self.range_start = int(r_s)
        self.range_end = int(r_e)

    def __str__(self):
        return str(self.a_x_quad) + "X² + " + str(self.b_x) + "x + " + str(self.c) + " = 0"

    def get_color(self):
        return self.color

    def get_plot(self):
        x_list = []
        y_list = []
        for X in range(100*self.range_start, 100*int(self.range_end)+1):
            x = X/100
            x_list.append(x)
            y_list.append(self.a_x_quad * x ** 2 + self.b_x * x + self.c)

        return x_list, y_list

    def get_extrema(self):
        return (-self.b_x) / 2*self.a_x_quad, self.c - (self.b_x**2/4*self.a_x_quad)

    def get_export(self):
        return ['q', str(self.a_x_quad), str(self.b_x), str(self.c), "0", self.color, str(self.range_start),
                str(self.range_end)]


class CubicEquation:
    a_x_cube = 0
    b_x = 0
    c_x = 0
    d = 0
    color = ""
    range_start = 0
    range_end = 0

    def __init__(self, a_x_cube, b_x_squared, c_x, d, color, r_s, r_e):
        self.a_x_cube = int(a_x_cube)
        self.b_x = int(b_x_squared)
        self.c_x = int(c_x)
        self.d = int(d)
        self.color = color
        self.range_start = int(r_s)
        self.range_end = int(r_e)
        self.x_extremum_1 = 0
        self.x_extremum_2 = 0
        self.y_extremum_1 = 0
        self.y_extremum_2 = 0

    def __str__(self):
        return str(self.a_x_cube) + "X³ + " + str(self.b_x) + "x² + " + str(self.c_x) + "X + " +str(self.d) + " = 0"

    def get_color(self):
        return self.color

    def get_plot(self):
        x_list = []
        y_list = []
        for X in range(100*self.range_start, 100*self.range_end + 1):
            x = X/100
            x_list.append(x)
            y_list.append((self.a_x_cube * x ** 3 + self.b_x * x**2 + self.c_x * x + self.d))

        return x_list, y_list

    def get_extrema(self):

        self.x_extremum_1 = (-self.b_x - math.sqrt(self.b_x ** 2 - (3 * self.a_x_cube * self.c_x))) / 3 * self.a_x_cube
        self.x_extremum_2 = (-self.b_x + math.sqrt(self.b_x ** 2 - (3 * self.a_x_cube * self.c_x))) / 3 * self.a_x_cube

        self.y_extremum_1 = self.x_extremum_1 ** 3 * self.a_x_cube + self.x_extremum_1 ** 2 * self.b_x + self.x_extremum_1 * self.c_x + self.d
        self.y_extremum_2 = self.x_extremum_2 ** 3 * self.a_x_cube + self.x_extremum_2 ** 2 * self.b_x + self.x_extremum_2 * self.c_x + self.d

        return [self.x_extremum_1, self.x_extremum_2], [self.y_extremum_1, self.y_extremum_2]

    def get_export(self):
        return ['c', str(self.a_x_cube), str(self.b_x), str(self.c_x), str(self.d), self.color, str(self.range_start), str(self.range_end)]


class LogarithmicEquationAX:
    a = 0
    color = ""
    range_start = 0
    range_end = 0

    def __init__(self, a, color, r_s, r_e):
        self.a = int(a)
        self.color = color
        self.range_start = int(r_s)
        self.range_end = int(r_e)

    def __str__(self):
        return "log " + str(self.a) + " (X)"

    def get_color(self):
        return self.color

    def get_plot(self):
        x_list = []
        y_list = []
        for X in range(100*self.range_start, 100*self.range_end + 1):
            x = X/100
            if x < 1:
                continue
            x_list.append(x)
            y_list.append(math.log(x, self.a))

        return x_list, y_list

    def get_export(self):
        return ['l-ax', str(self.a), "0", "0", "0", self.color, str(self.range_start),
                str(self.range_end)]


class LogarithmicEquationXA:
    a = 0
    color = ""
    range_start = 0
    range_end = 0

    def __init__(self, a, color, r_s, r_e):
        self.a = int(a)
        self.color = color
        self.range_start = int(r_s)
        self.range_end = int(r_e)

    def __str__(self):
        return "log X (" + str(self.a) + ")"

    def get_color(self):
        return self.color

    def get_plot(self):
        x_list = []
        y_list = []
        for X in range(100*self.range_start, 100*self.range_end + 1):
            x = X/100
            if x <= 1:
                continue
            x_list.append(x)
            y_list.append(math.log(self.a, x))

        return x_list, y_list

    def get_export(self):
        return ['l-xa', str(self.a), "0", "0", "0", self.color, str(self.range_start),
                str(self.range_end)]


class ExponentialEquationAX:
    a = 0
    color = ""
    range_start = 0
    range_end = 0

    def __init__(self, a, color, r_s, r_e):
        self.a = int(a)
        self.color = color
        self.range_start = int(r_s)
        self.range_end = int(r_e)

    def __str__(self):
        return str(self.a) + "^X"

    def get_color(self):
        return self.color

    def get_plot(self):
        x_list = []
        y_list = []
        for X in range(100*self.range_start, 100*self.range_end + 1):
            x = X/100
            if x < 1:
                continue
            x_list.append(x)
            y_list.append(self.a ** x)

        return x_list, y_list

    def get_export(self):
        return ['e-ax', str(self.a), "0", "0", "0", self.color, str(self.range_start),
                str(self.range_end)]


class ExponentialEquationXA:
    a = 0
    color = ""
    range_start = 0
    range_end = 0

    def __init__(self, a, color, r_s, r_e):
        self.a = int(a)
        self.color = color
        self.range_start = int(r_s)
        self.range_end = int(r_e)

    def __str__(self):
        return "X^ " + str(self.a)

    def get_color(self):
        return self.color

    def get_plot(self):
        x_list = []
        y_list = []
        for X in range(100*self.range_start, 100*self.range_end + 1):
            x = X/100
            if x < 0.01:
                continue
            x_list.append(x)
            y_list.append(x ** self.a)

        return x_list, y_list

    def get_export(self):
        return ['e-xa', str(self.a), "0", "0", "0", self.color, str(self.range_start),
                str(self.range_end)]


class CircleEquation:
    a = 0
    b = 2
    c = 2
    color = ""

    def __init__(self, a, b, c, color):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.color = color

    def __str__(self):
        return "(x-" + str(self.a) + ")² + (y-" + str(self.b) + ")² = " + str(self.c)+"²"

    def get_color(self):
        return self.color

    def get_plot(self):
        x_list = []
        y_list = []

        for X in range(100*(self.a - self.c), 100*(self.a + self.c)+1):
            x = X/100
            x_list.append(x)
            debug_y = self.b + math.sqrt(abs(self.c**2 - (x-self.a)**2))
            y_list.append(debug_y)
        for X in range(100*(self.a + self.c), 100*(self.a - self.c)-1, -1):
            x = X/100
            x_list.append(x)
            debug_y = self.b - math.sqrt(abs(self.c ** 2 - (x - self.a) ** 2))
            y_list.append(debug_y)

        return x_list, y_list



    def get_export(self):
        return ['cr', str(self.a),str(self.b), str(self.c), "0", self.color, 0, 0]
