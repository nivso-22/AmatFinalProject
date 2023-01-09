from tkinter import *
import matplotlib.pyplot as plt
import math
from equationClasses import *


def select_color(*args):
    global color
    print(color.get())


def change_value(*args):
    global root, beginner_entry, function_entry_frame, radio_container, color
    root.geometry("150x300")
    drop_value = selected_value.get()
    print(drop_value)

    for widget in function_entry_frame.winfo_children():
        widget.destroy()

    equation_text = Label(root, text="equation:")
    equation_text.grid(row=1)

    # range variables
    range_label = Label(function_entry_frame, text="range: ")
    range_beginning = Entry(function_entry_frame, width=3)
    x_in_middle = Label(function_entry_frame, text="≤ X ≤")
    range_end = Entry(function_entry_frame, width=3)

    # draw range things
    range_label.grid(row=2, column=1)
    range_beginning.grid(row=3, column=0)
    range_beginning.insert(0, "0")
    x_in_middle.grid(row=3, column=1)
    range_end.grid(row=3, column=2)
    range_end.insert(0, "0")

    graph_button = Button(
        root,
        text="graph",
        command=lambda: draw_graph(a_x,
                                   b_y,
                                   c,
                                   a_x_quad,
                                   b_quad,
                                   c_quad,
                                   range_beginning,
                                   range_end,
                                   a_x_cube,
                                   b_x_cube,
                                   c_x_cube,
                                   d_cube,
                                   expo_base,
                                   exponent,
                                   log_base,
                                   log_inside
                                   )
    )
    graph_button.grid(row=4)

    black_graph_color = Radiobutton(radio_container, text="black", variable=color, value="black", command=select_color)
    black_graph_color.grid(row=0, column=0, sticky='w')
    blue_graph_color = Radiobutton(radio_container, text="blue", variable=color, value="blue", command=select_color)
    blue_graph_color.grid(row=1, column=0, sticky='w')
    yellow_graph_color = Radiobutton(radio_container, text="yellow", variable=color, value="yellow", command=select_color)
    yellow_graph_color.grid(row=2, column=0, sticky='w')
    red_graph_color = Radiobutton(radio_container, text="red", variable=color, value="red", command=select_color)
    red_graph_color.grid(row=3, column=0, sticky='w')

    root.update()

    a_x = Entry(function_entry_frame, width=3)
    b_y = Entry(function_entry_frame, width=3)
    c = Entry(function_entry_frame, width=3)

    a_x_quad = Entry(function_entry_frame, width=3)
    b_quad = Entry(function_entry_frame, width=3)
    c_quad = Entry(function_entry_frame, width=3)

    a_x_cube = Entry(function_entry_frame, width=3)
    b_x_cube = Entry(function_entry_frame, width=3)
    c_x_cube = Entry(function_entry_frame, width=3)
    d_cube = Entry(function_entry_frame, width=3)

    expo_base = Entry(function_entry_frame, width=3)
    exponent = Entry(function_entry_frame, width=3)

    log_base = Entry(function_entry_frame, width=3)
    log_inside = Entry(function_entry_frame, width=3)

    if drop_value == 'linear equation':
        root.update()
        # create the equation variables
        x_plus_text = Label(function_entry_frame, text="X + ")
        y_plus_text = Label(function_entry_frame, text="Y + ")
        equals_0_text = Label(function_entry_frame, text=" = 0")

        # draw the equation variables
        a_x.grid(row=1, column=0)
        a_x.insert(0, "0")
        x_plus_text.grid(row=1, column=1)
        b_y.grid(row=1, column=2)
        b_y.insert(0, "0")
        y_plus_text.grid(row=1, column=3)
        c.grid(row=1, column=4)
        c.insert(0, "0")
        equals_0_text.grid(row=1, column=5)

        root.geometry("185x300")
        root.update()

    if drop_value == 'quadratic equation':
        root.update()

        x_plus_text = Label(function_entry_frame, text="X² + ")
        y_plus_text = Label(function_entry_frame, text="X + ")
        equals_0_text = Label(function_entry_frame, text=" = 0")

        # draw the equation variables
        a_x_quad.grid(row=1, column=0)
        a_x_quad.insert(0, "0")
        x_plus_text.grid(row=1, column=1)
        b_quad.grid(row=1, column=2)
        b_quad.insert(0, "0")
        y_plus_text.grid(row=1, column=3)
        c_quad.grid(row=1, column=4)
        c_quad.insert(0, "0")
        equals_0_text.grid(row=1, column=5)

        root.geometry("185x300")
        root.update()

    if drop_value == 'cubic equation':
        x_cubed_text = Label(function_entry_frame, text="X³ + ")
        x_squared_text = Label(function_entry_frame, text="X² + ")
        x_single_text = Label(function_entry_frame, text="X + ")
        equals_0_text = Label(function_entry_frame, text=" = 0")

        a_x_cube.grid(row=1, column=0)
        a_x_cube.insert(0, "0")
        x_cubed_text.grid(row=1, column=1)
        b_x_cube.grid(row=1, column=2)
        b_x_cube.insert(0, "0")
        x_squared_text.grid(row=1, column=3)
        c_x_cube.grid(row=1, column=4)
        c_x_cube.insert(0, "0")
        x_single_text.grid(row=1, column=5)
        d_cube.grid(row=1, column=6)
        d_cube.insert(0, "0")
        equals_0_text.grid(row=1, column=7)

        root.geometry("215x300")

    if drop_value == 'exponential equation a^x':
        expo_base_text = Label(function_entry_frame, text=" ^X")
        expo_base.grid(row=1, column=0)
        expo_base.insert(0, "0")
        expo_base_text.grid(row=1, column=1)

        root.geometry("180x300")

    if drop_value == 'exponential equation x^a':
        exponent_text = Label(function_entry_frame, text="X^")
        exponent_text.grid(row=1, column=0)
        exponent.insert(0, "0")
        exponent.grid(row=1, column=1)

        root.geometry("180x300")

    if drop_value == 'logarithmic equation log a (x)':
        log_text = Label(function_entry_frame, text="log")
        log_text.grid(row=1, column=0)
        log_base.insert(0, "0")
        log_base.grid(row=1, column=1)
        log_inside_text = Label(function_entry_frame, text="(x)")
        log_inside_text.grid(row=1, column=2)

        root.geometry("200x300")

    if drop_value == 'logarithmic equation log x (a)':
        log_x_text = Label(function_entry_frame, text="log x (")
        log_x_text.grid(row=1, column=0)
        log_inside.insert(0, "0")
        log_inside.grid(row=1, column=1)
        second_parenthasis_text = Label(function_entry_frame, text=")")
        second_parenthasis_text.grid(row=1, column=2)

        root.geometry("200x300")

    root.update()


def draw_graph(a_x,
               b_y,
               c,
               a_x_quad,
               b_quad,
               c_quad,
               range_beginning,
               range_end,
               a_x_cube,
               b_x_cube,
               c_x_cube,
               d_cube,
               expo_base,
               exponent,
               log_base,
               log_inside
               ):
    global selected_value, color, past_equations, num_of_equations, past_equation_container
    print("imagine i made a graph here")
    num_of_equations += 1

    x_to_draw = []
    y_to_draw = []

    if selected_value.get() == 'linear equation':
        a_x_draw = int(a_x.get())
        b_y_draw = int(b_y.get())
        c_draw = int(c.get())
        print(a_x_draw, "x +", b_y_draw, "y +", c_draw, "= 0 ")

        for x in range(int(range_beginning.get()), int(range_end.get())+1):
            x_to_draw.append(x)
            y_to_draw.append((0-a_x_draw/b_y_draw)*x + 0-c_draw/b_y_draw)

        past_equations[num_of_equations] = LinearEquation(a_x_draw, b_y_draw, c_draw)
        print(past_equations[num_of_equations])

    if selected_value.get() == 'quadratic equation':
        a_x_quad_draw = int(a_x_quad.get())
        b_quad_draw = int(b_quad.get())
        c_quad_draw = int(c_quad.get())
        print(a_x_quad_draw, "x² +", b_quad_draw, "x +", c_quad_draw, "= 0 ")
        for x in range(int(range_beginning.get()), int(range_end.get())+1):
            x_to_draw.append(x)
            y_to_draw.append((a_x_quad_draw*x**2 + b_quad_draw*x + c_quad_draw))

        past_equations[num_of_equations] = QuadraticEquation(a_x_quad_draw, b_quad_draw, c_quad_draw)
        print(past_equations[num_of_equations])

    if selected_value.get() == 'cubic equation':
        a_cube_draw = int(a_x_cube.get())
        b_cube_draw = int(b_x_cube.get())
        c_cube_draw = int(c_x_cube.get())
        d_cube_draw = int(d_cube.get())
        for x in range(int(range_beginning.get()), int(range_end.get())+1):
            x_to_draw.append(x)
            y_to_draw.append((a_cube_draw*x**3 + b_cube_draw*x**2 + c_cube_draw*x + d_cube_draw))

        past_equations[num_of_equations] = CubicEquation(a_cube_draw, b_cube_draw, c_cube_draw, d_cube_draw)
        print(past_equations[num_of_equations])

    if selected_value.get() == 'exponential equation a^x':
        expo_base_draw = int(expo_base.get())
        for x in range(int(range_beginning.get()), int(range_end.get())+1):
            try:
                y_to_draw.append(expo_base_draw ** x)
            except:
                continue
            x_to_draw.append(x)

        past_equations[num_of_equations] = ExponentialEquationAX(expo_base_draw)
        print(past_equations[num_of_equations])

    if selected_value.get() == 'exponential equation x^a':
        exponent_draw = int(exponent.get())
        for x in range(int(range_beginning.get()), int(range_end.get())+1):
            try:
                y_to_draw.append(x**exponent_draw)
            except:
                continue
            x_to_draw.append(x)

        past_equations[num_of_equations] = ExponentialEquationXA(exponent_draw)
        print(past_equations[num_of_equations])

    if selected_value.get() == 'logarithmic equation log a (x)':
        log_base_draw = int(log_base.get())
        for x in range(int(range_beginning.get()), int(range_end.get())+1):
            try:
                y_to_draw.append(math.log(x, log_base_draw))
            except:
                continue
            x_to_draw.append(x)

        past_equations[num_of_equations] = LogarithmicEquationAX(log_base_draw)
        print(past_equations[num_of_equations])

    if selected_value.get() == 'logarithmic equation log x (a)':
        log_inside_draw = int(log_inside.get())
        for x in range(int(range_beginning.get()), int(range_end.get())+1):
            try:
                y_to_draw.append(math.log(log_inside_draw, x))
            except:
                continue
            x_to_draw.append(x)

        past_equations[num_of_equations] = LogarithmicEquationXA(log_inside_draw)
        print(past_equations[num_of_equations])

    print("in range: ", int(range_beginning.get()), "≤ X ≤", int(range_end.get()))
    plt.plot(x_to_draw, y_to_draw, c=color.get())
    plt.axvline(x=0, c='black')
    plt.axhline(y=0, c='black')
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")

    Label(past_equation_container, text=past_equations[num_of_equations]).pack(anchor="w")
    root.update()
    print("test")
    plt.show()


root = Tk()
root.geometry("150x300")

# dropdown menu
selected_value = StringVar()
selected_value.set("select function type")
options = ['linear equation',
           'quadratic equation',
           'cubic equation',
           'exponential equation a^x',
           'exponential equation x^a',
           'logarithmic equation log a (x)',
           'logarithmic equation log x (a)']

dropdown = OptionMenu(root, selected_value,   *options)
dropdown.grid(row=0)
selected_value.trace('w', change_value)


function_entry_frame = Frame(root)
function_entry_frame.grid(row=2)

radio_container = Frame(root)
radio_container.grid(row=3, sticky="w")

color = StringVar()
color.set("black")

beginner_entry = Entry(function_entry_frame, width=20, state='disabled')
beginner_entry.grid(row=0)

past_equation_container = Frame(root)
past_equation_container.grid(row=5, sticky="w")

past_equations = {}
num_of_equations = 0

root.mainloop()
