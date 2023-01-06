from tkinter import *
import matplotlib.pyplot as plt

def change_value(*args):
    global root, beginner_entry, function_entry_frame
    root.geometry("150x300")
    drop_value = selected_value.get()
    print(drop_value)

    for widget in function_entry_frame.winfo_children():
        widget.destroy()

    equation_text = Label(function_entry_frame, text="equation:")
    equation_text.grid(row=0)

    # range variables
    range_label = Label(function_entry_frame, text="range: ")
    range_beginning = Entry(function_entry_frame, width=3)
    x_in_middle = Label(function_entry_frame, text="≤ X ≤")
    range_end = Entry(function_entry_frame, width=3)

    # draw range things
    range_label.grid(row=2, column=0)
    range_beginning.grid(row=3, column=0)
    x_in_middle.grid(row=3, column=1)
    range_end.grid(row=3, column=2)

    graph_button = Button(function_entry_frame, text="graph", command= lambda: draw_graph(a_x, b_y, c, a_x_quad, b_quad, c_quad))
    graph_button.grid(row=4)

    root.update()

    a_x = Entry(function_entry_frame, width=3)
    b_y = Entry(function_entry_frame, width=3)
    c = Entry(function_entry_frame, width=3)

    a_x_quad = Entry(function_entry_frame, width=3)
    b_quad = Entry(function_entry_frame, width=3)
    c_quad = Entry(function_entry_frame, width=3)

    if drop_value == 'linear equation':
        root.update()
        # create the equation variables


        x_plus_text = Label(function_entry_frame, text="X + ")
        y_plus_text = Label(function_entry_frame, text="Y + ")
        equals_0_text = Label(function_entry_frame, text=" = 0")

        # draw the equation variables
        a_x.grid(row=1,column=0)
        a_x.insert(0, "0")
        x_plus_text.grid(row=1,column=1)
        b_y.grid(row=1,column=2)
        b_y.insert(0, "0")
        y_plus_text.grid(row=1,column=3)
        c.grid(row=1,column=4)
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

    root.update()


def draw_graph(a_x, b_y, c, a_x_quad, b_quad, c_quad):
    global selected_value
    print("imagine i made a graph here")
    if selected_value.get() == 'linear equation':
        a_x_draw = int(a_x.get())
        b_y_draw = int(b_y.get())
        c_draw = int(c.get())
        print(a_x_draw, "x +", b_y_draw, "y +", c_draw, "= 0 ")

    if selected_value.get() == 'quadratic equation':
        a_x_quad_draw = int(a_x_quad.get())
        b_quad_draw = int(b_quad.get())
        c_quad_draw = int(c_quad.get())
        print(a_x_quad_draw, "x² +", b_quad_draw, "x +", c_quad_draw, "= 0 ")




root = Tk()
root.geometry("150x300")


# dropdown menu
selected_value = StringVar()
selected_value.set("select function type")
options = ['linear equation', 'quadratic equation']
dropdown = OptionMenu(root, selected_value,   *options)
dropdown.grid(row=0)
selected_value.trace('w', change_value)


function_entry_frame = Frame(root)
function_entry_frame.grid(row=1)

beginner_entry = Entry(function_entry_frame, width=20, state='disabled')
beginner_entry.grid(row=0)


root.mainloop()
