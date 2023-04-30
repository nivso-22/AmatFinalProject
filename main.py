import time
t1 = time.time()
from tkinter import filedialog
import tkinter
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot
import matplotlib.pyplot as plt
from equationClasses import *
import csv
from customtkinter import *
from customtkinter import filedialog

set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
set_default_color_theme("blue")


def set_x_limit(value):
    global root, x_slider_text
    x_slider_text.configure(text=f'{10*value: .2f}')
    root.update()

def set_y_limit(value):
    global  root, y_slider_text
    y_slider_text.configure(text=f'{10 * value: .2f}')
    root.update()



def cleanFrame():
    global past_equation_container, past_equations, root
    for i in past_equation_container.winfo_children():
        i.destroy()
    past_equation_container.destroy()
    past_equation_container = CTkFrame(root)
    past_equation_container.configure(width=0, height=0)
    root.update()
    past_equation_container.grid(row=9, sticky="w")
    past_equations = {}
    root.update()
    ax.cla()
    canvas.draw()



    for equation in past_equations:
        try:
            ax.plot(past_equations[equation].get_plot()[0], past_equations[equation].get_plot()[1], c=past_equations[equation].get_color(), scalex=scale_graph.get(), scaley=scale_graph.get())
        except:
            for_deletion.append(equation)
        if extremum_bool.get():
            try:
                print("extrema")
                ax.plot(past_equations[equation].get_extrema()[0], past_equations[equation].get_extrema()[1], marker="o", c=color.get(), ls='')
            except:
                print("no extrema")
    ax.axvline(x=0, c='black')
    ax.axhline(y=0, c='black')
    ax.grid(True)
    ax.set_aspect("equal")

    print("redrawn")
    num_of_equations = len(past_equations)



    canvas.draw()
    plt.show()

def open_file(add_to_history):
    filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    Import(filepath, add_to_history)


def Import(path, add_to_history):
    global ax, canvas, x_slider_text, y_slider_text
    print("import")
    index = len(past_equations)
    print(path)
    if path[-4:] != '.csv':
        imported_csv = open("{path}.csv".format(path=path), "r")
    else:
        imported_csv = open(path, "r")
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
            function = LogarithmicEquationXA(Func[1], Func[5], Func[6], Func[7])
            print(function)
        if Func[0] == 'e-ax':
            function = LogarithmicEquationAX(Func[1], Func[5], Func[6], Func[7])
            print(function)
        if Func[0] == 'e-xa':
            function = LogarithmicEquationAX(Func[1], Func[5], Func[6], Func[7])
            print(function)
        if Func[0] == 'cr':
            function = CircleEquation(Func[1], Func[2], Func[3], Func[5])
        if Func[0] == 'e':
            function = Elipse(Func[1], Func[2], Func[5])
            print("elipsed")
        try:
            ax.plot(function.get_plot()[0],
                    function.get_plot()[1],
                    c=function.get_color())
            print("plot")
            ax.axvline(x=0, c='black')
            ax.axhline(y=0, c='black')
            ax.grid(True)
            ax.set_aspect("equal")
            ax.set_ylim(0-int(y_slider_text.cget("text")), int(y_slider_text.cget("text")))
            ax.set_xlim(0-int(x_slider_text.cget("text")), int(x_slider_text.cget("text")))
            if add_to_history.get():
                past_equations[index] = function
        except:
            print("no func")
    plt.close()


    canvas.draw()
    plt.show()


def export(path_name):
    header = ['type', 'a', 'b', 'c', 'd', 'color', 'r-s', 'r-e']
    export = open(f'{path_name}.csv', "w", newline='')
    csv_writer = csv.writer(export)
    csv_writer.writerow(header)
    for i in past_equations:
        csv_writer.writerow(past_equations[i].get_export())
        print(past_equations[i].get_export())


def import_export(*args):
    global past_equations, root, exp_imp_container

    for wid in exp_imp_container.winfo_children():
        wid.destroy()


    value = exp_imp_str.get()
    print(value)
    export_button = CTkButton(exp_imp_container, text="export", command=lambda: export(import_export_entry.get()))
    import_button = CTkButton(exp_imp_container, text="import", command=lambda: Import(import_export_entry.get(), add_to_history_bool))
    import_export_entry = CTkEntry(exp_imp_container, width=120)
    add_to_history_bool = BooleanVar()
    add_to_history = CTkCheckBox(exp_imp_container, text="editable", variable=add_to_history_bool, onvalue=True, offvalue=False)
    browse_button = CTkButton(exp_imp_container, text="browse", command=lambda: open_file(add_to_history_bool))

    if value == 'export':
        import_export_entry.grid(row=0)
        import_export_entry.insert(0, "graph")
        export_button.grid(row=1, column=0)
        CTkLabel(exp_imp_container, text=".csv").grid(row=0, column=1)

    elif value == 'import':
        import_export_entry.grid(row=0)
        import_button.grid(row=1, column=0)
        CTkLabel(exp_imp_container, text=".csv").grid(row=0, column=1)
        add_to_history.grid(row=3)
        browse_button.grid(row=2)


def select_color(*args):
    global color
    print(color.get())


def change_value(*args):
    global root, beginner_entry, function_entry_frame, radio_container, color, extremum_bool, scale_graph, x_slider_text, y_slider_text

    drop_value = selected_value.get()
    print(drop_value)

    for widget in function_entry_frame.winfo_children():
        widget.destroy()

    equation_text = CTkLabel(root, text="equation:")
    equation_text.grid(row=1)

    # range variables
    range_label = CTkLabel(function_entry_frame, text="range: ")
    range_beginning = CTkEntry(function_entry_frame, width=25)
    x_in_middle = CTkLabel(function_entry_frame, text="≤ X ≤")
    range_end = CTkEntry(function_entry_frame, width=25)

    # draw range things
    range_label.grid(row=2, column=1)
    range_beginning.grid(row=3, column=0)
    range_beginning.insert(0, "0")
    x_in_middle.grid(row=3, column=1)
    range_end.grid(row=3, column=2)
    range_end.insert(0, "0")

    graph_button = CTkButton(
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
                                   circle_rad_squared,
                                   elipse_a,
                                   elipse_b
                                   )
    )
    graph_button.grid(row=8)

    black_graph_color = CTkRadioButton(radio_container, text="black", variable=color, value="black", command=select_color)
    black_graph_color.grid(row=0, column=0, sticky='w')
    blue_graph_color = CTkRadioButton(radio_container, text="blue", variable=color, value="blue", command=select_color)
    blue_graph_color.grid(row=1, column=0, sticky='w')
    yellow_graph_color = CTkRadioButton(radio_container, text="yellow", variable=color, value="yellow", command=select_color)
    yellow_graph_color.grid(row=2, column=0, sticky='w')
    red_graph_color = CTkRadioButton(radio_container, text="red", variable=color, value="red", command=select_color)
    red_graph_color.grid(row=3, column=0, sticky='w')

    extremum_checkbox = CTkCheckBox(radio_container,
                                    text="show extremums",
                                    variable=extremum_bool,
                                    onvalue=True,
                                    offvalue=False)
    extremum_checkbox.grid(row=0, column=1)

    scale_checkbox = CTkCheckBox(radio_container, text="scale graph", variable=scale_graph, onvalue=True, offvalue=False)
    scale_checkbox.grid(row=1, column=1, sticky="w")
    scale_checkbox.select()


    x_limiter = CTkSlider(root, from_=1, to=100, command= set_x_limit)
    y_limiter = CTkSlider(root, from_=1, to=100, command=set_y_limit)

    x_limiter.grid(row=5,column=0)
    x_slider_text.grid(row=4, column=0)

    y_limiter.grid(row=7, column=0)
    y_slider_text.grid(row=6, column=0)

    root.update()

    a_x = CTkEntry(function_entry_frame, width=35)
    b_y = CTkEntry(function_entry_frame, width=35)
    c = CTkEntry(function_entry_frame, width=35)

    a_x_quad = CTkEntry(function_entry_frame, width=35)
    b_quad = CTkEntry(function_entry_frame, width=35)
    c_quad = CTkEntry(function_entry_frame, width=35)

    a_x_cube = CTkEntry(function_entry_frame, width=35)
    b_x_cube = CTkEntry(function_entry_frame, width=35)
    c_x_cube = CTkEntry(function_entry_frame, width=35)
    d_cube = CTkEntry(function_entry_frame, width=35)

    expo_base = CTkEntry(function_entry_frame, width=35)
    exponent = CTkEntry(function_entry_frame, width=35)

    log_base = CTkEntry(function_entry_frame, width=35)
    log_inside = CTkEntry(function_entry_frame, width=35)

    circle_x = CTkEntry(function_entry_frame, width=35)
    circle_y = CTkEntry(function_entry_frame, width=35)
    circle_rad_squared = CTkEntry(function_entry_frame, width=35)

    elipse_a = CTkEntry(function_entry_frame, width=35)
    elipse_b = CTkEntry(function_entry_frame, width=35)



    if drop_value == 'linear equation':
        root.update()
        # create the equation variables
        x_plus_text = CTkLabel(function_entry_frame, text="X + ")
        y_plus_text = CTkLabel(function_entry_frame, text="Y + ")
        equals_0_text = CTkLabel(function_entry_frame, text=" = 0")

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


        root.update()

    if drop_value == 'quadratic equation':
        root.update()

        x_plus_text = CTkLabel(function_entry_frame, text="X² + ")
        y_plus_text = CTkLabel(function_entry_frame, text="X + ")
        equals_0_text = CTkLabel(function_entry_frame, text=" = 0")

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


        root.update()

    if drop_value == 'cubic equation':
        x_cubed_text = CTkLabel(function_entry_frame, text="X³ + ")
        x_squared_text = CTkLabel(function_entry_frame, text="X² + ")
        x_single_text = CTkLabel(function_entry_frame, text="X + ")
        equals_0_text = CTkLabel(function_entry_frame, text=" = 0")

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



    if drop_value == 'exponential equation a^x':
        expo_base_text = CTkLabel(function_entry_frame, text=" ^X")
        expo_base.grid(row=1, column=0)
        expo_base.insert(0, "0")
        expo_base_text.grid(row=1, column=1)



    if drop_value == 'exponential equation x^a':
        exponent_text = CTkLabel(function_entry_frame, text="X^")
        exponent_text.grid(row=1, column=0)
        exponent.insert(0, "0")
        exponent.grid(row=1, column=1)



    if drop_value == 'logarithmic equation log a (x)':
        log_text = CTkLabel(function_entry_frame, text="log")
        log_text.grid(row=1, column=0)
        log_base.insert(0, "0")
        log_base.grid(row=1, column=1)
        log_inside_text = CTkLabel(function_entry_frame, text="(x)")
        log_inside_text.grid(row=1, column=2)



    if drop_value == 'logarithmic equation log x (a)':
        log_x_text = CTkLabel(function_entry_frame, text="log x (")
        log_x_text.grid(row=1, column=0)
        log_inside.insert(0, "0")
        log_inside.grid(row=1, column=1)
        second_parenthasis_text = CTkLabel(function_entry_frame, text=")")
        second_parenthasis_text.grid(row=1, column=2)



    if drop_value == 'circle':
        x_circle_text = CTkLabel(function_entry_frame, text="(x-")
        x_closer_text = CTkLabel(function_entry_frame, text=")² + (y -")
        y_closer_text = CTkLabel(function_entry_frame, text=")² = ")
        circle_squared_text = CTkLabel(function_entry_frame, text="²")

        x_circle_text.grid(row=1, column=0)
        circle_x.grid(row=1, column=1)
        circle_x.insert(0, "0")
        x_closer_text.grid(row=1, column=2)
        circle_y.grid(row=1, column=3)
        circle_y.insert(0, "0")
        y_closer_text.grid(row=1, column=4)
        circle_rad_squared.grid(row=1, column=5)
        circle_rad_squared.insert(0, "0")
        circle_squared_text.grid(row=1, column=6)

    if drop_value == 'elipse':
        x_elipse_text = CTkLabel(function_entry_frame, text="x²/")
        y_elipse_text = CTkLabel(function_entry_frame, text="y²/")
        elipse_plus_text = CTkLabel(function_entry_frame, text="² +")
        equals_1_text = CTkLabel(function_entry_frame, text="² = 1")


        x_elipse_text.grid(row=1, column=0)
        elipse_a.grid(row=1, column=1)
        elipse_a.insert(0, "0")

        elipse_plus_text.grid(row=1, column=2)
        y_elipse_text.grid(row=1, column=3)
        elipse_b.grid(row=1, column=4)
        elipse_b.insert(0, "0")
        equals_1_text.grid(row=1, column=5)



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
               circle_rad_squared,
               elipse_a,
               elipse_b
               ):
    global selected_value, color, past_equations, num_of_equations, past_equation_container,extremum_bool, extremum_dic, scale_graph, ax, graph_container, canvas, for_deletion, x_slider_text, y_slider_text
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

    if selected_value.get() == 'circle':
        past_equations[num_of_equations] = CircleEquation(circle_x.get(), circle_y.get(), circle_rad_squared.get(), color.get())
        print(past_equations[num_of_equations])
    if selected_value.get() == 'elipse':
        past_equations[num_of_equations] = Elipse(elipse_a.get(), elipse_b.get(), color.get())
        print(past_equations[num_of_equations])

# add a circle here at some point
    plt.close()

    for child in past_equation_container.winfo_children():
        child.destroy()

    frames = {}

    print("test")


    canvas.draw()

    ax.cla()

    for i in past_equations:

        frames[i] = CTkFrame(past_equation_container)
        CTkLabel(frames[i], text= past_equations[i]).grid(row=0, column=0)
        frames[i].pack()
    clear_all_button = CTkButton(past_equation_container, image=tkinter.PhotoImage(file="X.gif").subsample(7),text="",command=lambda: (cleanFrame(), ax.cla(), plt.show(),canvas.draw(), root.update()))
    clear_all_button.pack()





    for equation in past_equations:
        try:
            ax.plot(past_equations[equation].get_plot()[0], past_equations[equation].get_plot()[1], c=past_equations[equation].get_color(), scalex=scale_graph.get(), scaley=scale_graph.get())
        except:
            for_deletion.append(equation)
        if extremum_bool.get():
            try:
                print("extrema")
                ax.plot(past_equations[equation].get_extrema()[0], past_equations[equation].get_extrema()[1], marker="o", c=color.get(), ls='')
            except:
                print("no extrema")
    ax.axvline(x=0, c='black')
    ax.axhline(y=0, c='black')
    ax.grid(True)
    ax.set_aspect("equal")

    ax.set_ylim(0 - int(y_slider_text.cget("text")), int(y_slider_text.cget("text")))
    ax.set_xlim(0 - int(x_slider_text.cget("text")), int(x_slider_text.cget("text")))

    canvas.draw()
    plt.show()


root = CTk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# set the size and position of the window to cover the whole screen
root.geometry(f"{width}x{height}")



dropdownFrame = CTkFrame(root)
dropdownFrame.grid(row=0)

# dropdown menu
dropdownFrame = CTkFrame(root)
dropdownFrame.grid(row=0)

# dropdown menu
selected_value = StringVar(value="select function type")

options = ['linear equation',
           'quadratic equation',
           'cubic equation',
           'exponential equation a^x',
           'exponential equation x^a',
           'logarithmic equation log a (x)',
           'logarithmic equation log x (a)',
           'circle',
           'elipse']

dropdown = CTkComboBox(dropdownFrame, values=options, command=change_value, variable=selected_value)
dropdown.grid(row=0)


function_entry_frame = CTkFrame(root)
function_entry_frame.grid(row=2)

radio_container = CTkFrame(root)
radio_container.grid(row=3, sticky="w")

color = StringVar()
color.set("black")

beginner_entry = CTkEntry(function_entry_frame, width=20, state='disabled')
beginner_entry.grid(row=0)

past_equation_container = CTkFrame(root)
past_equation_container.grid(row=9, sticky="w")

past_equations = {}
num_of_equations = 0

extremum_bool = BooleanVar()
extremum_dic = {}

x_slider_text = CTkLabel(root, text="500")
y_slider_text = CTkLabel(root, text="500")

exp_imp_str = StringVar(value="select import/export")


exp_imp_ops = ['export', 'import']



exp_imp_dropdown = CTkComboBox(root, values=exp_imp_ops, command=import_export, variable=exp_imp_str)
exp_imp_dropdown.grid(row=10)

scale_graph = BooleanVar()

exp_imp_container = CTkFrame(root)
exp_imp_container.grid(row=11)

graph_container = CTkFrame(root)

fig = matplotlib.pyplot.figure()
ax = fig.add_subplot(111)

# Create the Tkinter canvas that will display the plot
canvas = FigureCanvasTkAgg(fig, master=graph_container)
canvas.draw()

# Add the canvas to the Tkinter window
canvas.get_tk_widget()

# Create a toolbar for the plot
toolbar = NavigationToolbar2Tk(canvas, graph_container)
toolbar.update()
canvas.get_tk_widget().pack()
graph_container.grid(row=0, column=2, rowspan=9999)

for_deletion = []


t2 = time.time()
print(f"loaded in {t2-t1} sec")
root.mainloop()
