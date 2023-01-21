from tkinter import *
import matplotlib.pyplot as plt
from equationClasses import *
import csv


def Import(path, add_to_history):
    print("import")
    index = len(past_equations)
    print(path)
    imported_csv = open("{path}.csv".format(path=path), "r")
    reader = csv.reader(imported_csv)
    for func in reader:
        index += 1
        Func = list(func)
        print(Func)
        if not Func:
            continue
        if Func[0] == 'l':
            function = LinearEquation(Func[1], Func[2], Func[3], Func[5], Func[6], Func[7])
            print(function)
        if Func[0] == 'q':
            function = QuadraticEquation(Func[1], Func[2], Func[3], Func[5], Func[6], Func[7])
            print(function)
        if Func[0] == 'c':
            function = CubicEquation(Func[1], Func[2], Func[3],Func[4], Func[5], Func[6], Func[7])
            print(function)
        if Func[0] == 'l-ax':
            function = LogarithmicEquationAX(Func[1], Func[5], Func[6], Func[7])
            print(function)
        if Func[0] == 'l-xa':
            function = LogarithmicEquationAX(Func[1], Func[5], Func[6], Func[7])
            print(function)
        if Func[0] == 'e-ax':
            function = LogarithmicEquationAX(Func[1], Func[5], Func[6], Func[7])
            print(function)
        if Func[0] == 'e-xa':
            function = LogarithmicEquationAX(Func[1], Func[5], Func[6], Func[7])
            print(function)

        try:
            plt.plot(function.get_plot()[0], function.get_plot()[1], c=function.get_color())
            print("plot")
            plt.axvline(x=0, c='black')
            plt.axhline(y=0, c='black')
            plt.grid(True)
            plt.xlabel("X")
            plt.ylabel("Y")
            if add_to_history.get():
                past_equations[index] = function
        except:
            print("no func")

    plt.show()


def export(path_name):
    header = ['type', 'a', 'b', 'c', 'd', 'color', 'r-s', 'r-e']
    export = open(f'{path_name}.csv', "w")
    csv_writer = csv.writer(export)
    csv_writer.writerow(header)
    for i in past_equations:
        csv_writer.writerow(past_equations[i].get_export())
        print(past_equations[i].get_export())


def import_export(*args):
    global past_equations, root, exp_imp_container

    for wid in exp_imp_container.winfo_children():
        wid.destroy()

    root.geometry("150x400")
    value = exp_imp_str.get()
    print(value)
    export_button = Button(exp_imp_container, text="export", command=lambda: export(import_export_entry.get()))
    import_button = Button(exp_imp_container, text="import", command=lambda: Import(import_export_entry.get(), add_to_history_bool))
    import_export_entry = Entry(exp_imp_container, width=15)
    add_to_history_bool = BooleanVar()
    add_to_history = Checkbutton(exp_imp_container, text="add to history", variable=add_to_history_bool, onvalue=True, offvalue=False)

    if value == 'export':
        import_export_entry.grid(row=0)
        import_export_entry.insert(0, "graph")
        export_button.grid(row=1, column=0)
        Label(exp_imp_container, text=".csv").grid(row=0, column=1)

    elif value == 'import':
        import_export_entry.grid(row=0)
        import_button.grid(row=1, column=0)
        Label(exp_imp_container, text=".csv").grid(row=0, column=1)
        add_to_history.grid(row=2)


def select_color(*args):
    global color
    print(color.get())


def change_value(*args):
    global root, beginner_entry, function_entry_frame, radio_container, color, extremum_bool, scale_graph
    root.geometry("150x350")
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
                                   log_inside,
                                   circle_x,
                                   circle_y,
                                   circle_rad_squared
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

    extremum_checkbox = Checkbutton(radio_container,
                                    text="show extremums",
                                    variable=extremum_bool,
                                    onvalue=True,
                                    offvalue=False)
    extremum_checkbox.grid(row=0, column=1)

    scale_checkbox = Checkbutton(radio_container, text="scale graph", variable=scale_graph, onvalue=True, offvalue=False)
    scale_checkbox.grid(row=1, column=1, sticky="w")
    scale_checkbox.select()

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

    circle_x = Entry(function_entry_frame, width=3)
    circle_y = Entry(function_entry_frame, width=3)
    circle_rad_squared = Entry(function_entry_frame, width=3)

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

        root.geometry("185x350")
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

        root.geometry("185x350")
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

        root.geometry("215x350")

    if drop_value == 'exponential equation a^x':
        expo_base_text = Label(function_entry_frame, text=" ^X")
        expo_base.grid(row=1, column=0)
        expo_base.insert(0, "0")
        expo_base_text.grid(row=1, column=1)

        root.geometry("180x350")

    if drop_value == 'exponential equation x^a':
        exponent_text = Label(function_entry_frame, text="X^")
        exponent_text.grid(row=1, column=0)
        exponent.insert(0, "0")
        exponent.grid(row=1, column=1)

        root.geometry("180x350")

    if drop_value == 'logarithmic equation log a (x)':
        log_text = Label(function_entry_frame, text="log")
        log_text.grid(row=1, column=0)
        log_base.insert(0, "0")
        log_base.grid(row=1, column=1)
        log_inside_text = Label(function_entry_frame, text="(x)")
        log_inside_text.grid(row=1, column=2)

        root.geometry("200x350")

    if drop_value == 'logarithmic equation log x (a)':
        log_x_text = Label(function_entry_frame, text="log x (")
        log_x_text.grid(row=1, column=0)
        log_inside.insert(0, "0")
        log_inside.grid(row=1, column=1)
        second_parenthasis_text = Label(function_entry_frame, text=")")
        second_parenthasis_text.grid(row=1, column=2)

        root.geometry("200x350")

    if drop_value == 'circle':
        x_circle_text = Label(function_entry_frame, text="(x-")
        x_closer_text = Label(function_entry_frame, text=")² + (y -")
        y_closer_text = Label(function_entry_frame, text=")² = ")

        x_circle_text.grid(row=1, column=0)
        circle_x.grid(row=1, column=1)
        circle_x.insert(0, "0")
        x_closer_text.grid(row=1, column=2)
        circle_y.grid(row=1, column=3)
        circle_y.insert(0, "0")
        y_closer_text.grid(row=1, column=4)
        circle_rad_squared.grid(row=1, column=5)
        circle_rad_squared.insert(0, "0")

        root.geometry("200x350")

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
               log_inside,
               circle_x,
               circle_y,
               circle_rad_squared
               ):
    global selected_value, color, past_equations, num_of_equations, past_equation_container,extremum_bool, extremum_dic, scale_graph
    print("imagine i made a graph here")
    num_of_equations += 1

    if selected_value.get() == 'linear equation':
        past_equations[num_of_equations] = LinearEquation(a_x.get(), b_y.get(), c.get(), color.get(), range_beginning.get(), range_end.get())
        print(past_equations[num_of_equations])

    if selected_value.get() == 'quadratic equation':
        past_equations[num_of_equations] = QuadraticEquation(a_x_quad.get(), b_quad.get(), c_quad.get(), color.get(), range_beginning.get(), range_end.get())
        print(past_equations[num_of_equations])

    if selected_value.get() == 'cubic equation':
        past_equations[num_of_equations] = CubicEquation(a_x_cube.get(), b_x_cube.get(), c_x_cube.get(), d_cube.get(), color.get(), range_beginning.get(), range_end.get())
        print(past_equations[num_of_equations])

    if selected_value.get() == 'exponential equation a^x':
        past_equations[num_of_equations] = ExponentialEquationAX(expo_base.get(), color.get(), range_beginning.get(), range_end.get())
        print(past_equations[num_of_equations])

    if selected_value.get() == 'exponential equation x^a':
        past_equations[num_of_equations] = ExponentialEquationXA(exponent.get(), color.get(), range_beginning.get(), range_end.get())
        print(past_equations[num_of_equations])

    if selected_value.get() == 'logarithmic equation log a (x)':
        past_equations[num_of_equations] = LogarithmicEquationAX(log_base.get(), color.get(), range_beginning.get(), range_end.get())
        print(past_equations[num_of_equations])

    if selected_value.get() == 'logarithmic equation log x (a)':
        past_equations[num_of_equations] = LogarithmicEquationXA(log_inside.get(), color.get(), range_beginning.get(), range_end.get())
        print(past_equations[num_of_equations])

# add a circle here at some point
    plt.close()
    for equation in past_equations:
        plt.plot(past_equations[equation].get_plot()[0], past_equations[equation].get_plot()[1], c=past_equations[equation].get_color(), scalex=scale_graph.get(), scaley=scale_graph.get())
        if extremum_bool.get():
            try:
                print("extrema")
                plt.plot(past_equations[equation].get_extrema()[0], past_equations[equation].get_extrema()[1], marker="o", c=color.get(), ls='')
            except:
                print("no extrema")
    plt.axvline(x=0, c='black')
    plt.axhline(y=0, c='black')
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")

    Label(past_equation_container, text=past_equations[num_of_equations]).pack(anchor="w")
    print("test")
    plt.show()


root = Tk()
root.geometry("150x350")

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

extremum_bool = BooleanVar()
extremum_dic = {}


exp_imp_str = StringVar()
exp_imp_str.set("select import/export")

exp_imp_ops = ['export', 'import']

exp_imp = OptionMenu(root, exp_imp_str,   *exp_imp_ops)
exp_imp.grid(row=7)
exp_imp_str.trace('w', import_export)

scale_graph = BooleanVar()

exp_imp_container = Frame(root)
exp_imp_container.grid(row=8)


root.mainloop()
