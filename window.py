import skip_list as sl
import treap as tr
import tkinter as tk
import networkx as nx
import log_widget as lw
import time
import math
import re

from skip_list_graph import SkipListGraph
from treap_graph import TreapGraph
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image


def update_canvas(graph):
    global plot
    global figure
    plot.clear()
    pos = nx.get_node_attributes(graph, 'pos')
    label = nx.get_node_attributes(graph, 'label')
    color_dict = nx.get_node_attributes(graph, 'color')
    color_list = []
    for color in color_dict:
        color_list.append(color_dict[color])
    nx.draw(graph, pos, node_size=700, node_color=color_list, labels=label, with_labels=True, ax=plot)
    canvas.draw()


# TODO : char filter !
def search_command():
    global algorithm
    global graph_list_index
    global current_presst_button
    global log_widget
    global log_message
    global skip_list_graph_list
    global treap_graph_list
    global treap

    # Clear the old animations and reset index to zero
    skip_list_graph_list.clear()
    treap_graph_list.clear()
    graph_list_index = 0
    plot.clear()
    current_presst_button = "search"

    value = int(value_entry.get())

    # Handling the log widget:
    log_widget.push(f"Searched Key: {value}")
    log_message.config(text=log_widget.update())

    if algorithm.get() == "Skip List":
        skip_list.find(value, skip_list_graph_list)
        update_canvas(skip_list_graph_list[graph_list_index])
    elif algorithm.get() == "Treap":
        treap.find(value, treap_graph_list, treap)
        update_canvas(treap_graph_list[graph_list_index])

    value_entry.delete(0, tk.END)


# value_entry.insert(0, f"\tLast Operation was SEARCH with Key : {value}")


# Insert the value in the entry into the data structure, call the draw function
# TODO : char filter !
# TODO: Empty the graph lists here so that a new opeator is played, you dont have to skip through the earlier animation???
def insert_command():
    global algorithm
    global graph_list_index
    global current_presst_button
    global log_widget
    global log_message
    global skip_list_graph_list
    global treap_graph_list
    global treap

    # Clear the old animations and reset index to zero
    skip_list_graph_list.clear()
    treap_graph_list.clear()
    graph_list_index = 0
    plot.clear()

    value = int(value_entry.get())
    skip_list.insert(value, skip_list_graph_list)
    treap.insert(value, treap_graph_list, treap)

    # Handling the log widget:
    log_widget.push(f"Inserted Key: {value}")
    log_message.config(text=log_widget.update())

    if algorithm.get() == "Skip List":
        update_canvas(skip_list_graph_list[graph_list_index])
    elif algorithm.get() == "Treap":
        update_canvas(treap_graph_list[graph_list_index])

    value_entry.delete(0, tk.END)
    # value_entry.insert(0, f"\tLast Operation was INSERT with Key : {value}")


# TODO : char filter !
def delete_command():
    global algorithm
    global graph_list_index
    global current_presst_button
    global log_widget
    global log_message
    global skip_list_graph_list
    global treap_graph_list

    skip_list_graph_list.clear()
    treap_graph_list.clear()
    graph_list_index = 0
    plot.clear()

    value = int(value_entry.get())
    skip_list.delete(value, skip_list_graph_list)
    treap.delete(value, treap_graph_list)

    # Handling the log widget:
    log_widget.push(f"Deleted Key: {value}")
    log_message.config(text=log_widget.update())

    current_presst_button = "delete"
    if algorithm.get() == "Skip List":
        update_canvas(skip_list_graph_list[graph_list_index])
    elif algorithm.get() == "Treap":
        treap_graph.draw(treap, plot, canvas)
    value_entry.delete(0, tk.END)
    # value_entry.insert(0, f"\tLast Operation was DELETE with Key : {value}")


def play_command():
    global graph_list_index

    global skip_list_graph_list
    global treap_graph_list

    if algorithm.get() == "Skip List":
        while graph_list_index < len(skip_list_graph_list) - 1:
            graph_list_index += 1
            timestamp = int(math.floor(time.time()))
            while math.floor(time.time()) < timestamp + 1:
                update_canvas(skip_list_graph_list[graph_list_index])

    elif algorithm.get() == "Treap":
        while graph_list_index < len(treap_graph_list) - 1:
            graph_list_index += 1
            timestamp = int(math.floor(time.time()))
            while math.floor(time.time()) < timestamp + 1:
                update_canvas(treap_graph_list[graph_list_index])


def previous_command():
    global graph_list_index
    global skip_list_graph_list
    global treap_graph_list
    global algorithm
    if algorithm.get() == "Skip List":
        if graph_list_index < len(skip_list_graph_list) - 1:
            graph_list_index -= 1
            update_canvas(skip_list_graph_list[graph_list_index])
    elif algorithm.get() == "Treap":
        if graph_list_index < len(treap_graph_list):
            graph_list_index -= 1
            update_canvas(treap_graph_list[graph_list_index])


def next_command():
    global graph_list_index
    global skip_list_graph_list
    global treap_graph_list
    global algorithm
    if algorithm.get() == "Skip List":
        if graph_list_index < len(skip_list_graph_list) - 1:
            graph_list_index += 1
            update_canvas(skip_list_graph_list[graph_list_index])
    elif algorithm.get() == "Treap":
        if graph_list_index < len(treap_graph_list) - 1:
            graph_list_index += 1
            update_canvas(treap_graph_list[graph_list_index])


def stop_command():
    global graph_list_index
    graph_list_index = 0
    return update_canvas(skip_list_graph_list[graph_list_index])


def clear_command():
    global graph_list_index
    global skip_list_graph_list
    global skip_list_graph
    global treap_graph_list
    global treap_graph
    global algorithm
    graph_list_index = 0

    if algorithm.get() == "Treap":
        treap_graph_list.clear()
        treap = tr.Treap()
        treap_graph = TreapGraph(treap)
        treap_graph_list.append(treap_graph.create_graph())
        update_canvas(treap_graph_list[graph_list_index])
    elif algorithm.get() == "Skip List":
        skip_list_graph_list.clear()
        skip_list = sl.SkipList()
        skip_list_graph = SkipListGraph(skip_list)
        skip_list_graph_list.append(skip_list_graph.create_graph(skip_list))
        update_canvas(skip_list_graph_list[graph_list_index])


# TODO: Use graph list and keep track of index? Test as soon as there are animations for treap
def switch_algorithm(string):
    global treap_graph
    global skip_list_graph
    global canvas
    print(string, "is the string")
    if string == "Treap":
        treap_graph.draw(treap_graph.treap, plot, canvas)
        print("drew the treap")
    elif string == "Skip List":
        skip_list_graph.draw(skip_list_graph.skip_list, plot, canvas)
        print("derw the skip slist")


def read_data_command():
    global algorithm
    global skip_list_graph_list
    global treap_graph_list
    global treap
    global graph_list_index
    graph_list_index = 0

    for line in data:
        skip_list_graph_list.clear()
        treap_graph_list.clear()
        skip_list.insert(int(line), skip_list_graph_list)
        treap.insert(int(line), treap_graph_list, treap)

        if algorithm.get() == "Skip List":
            update_canvas(skip_list_graph_list[graph_list_index])
        else:
            update_canvas(treap_graph_list[graph_list_index])


def info_command():
    messagebox.showinfo(title="Easteregg", message="Hättste nicht gedacht Nutte")


# opens FileExplorer to choose ONLY .txt files
# TODO: Handle spezial chars !
def open_file():
    global data
    token = False
    file = filedialog.askopenfile(mode='r', title="Open file", filetypes=[('Text Files', '*.txt')])
    # check if file was opend successfully
    if file:
        # set Label with filename only if open was successful
        filename_label.config(text=file.name.split("/")[-1])
        data = []
        # append each line to DATA list, where they are stored
        for line in file:
            # check if line contains more than One char
            if len(line.split()) > 1:
                current_line = line.split(",")
                for element in current_line:
                    if re.search("[a-zA-Z]+", element):
                        data = []
                        messagebox.showerror("error", f"File contains not supported data : {element}")
                        return
                    # checks if white Space is in File and ignores it
                    elif element.isspace():
                        messagebox.showinfo("Warning", f"Your FILE : {file.name} contains Whitespace !")
                        continue
                    else:
                        data.append(int(element))

            else:
                # check if line contains letters or is Empty => not supported !!!
                if re.search("[a-zA-Z]+", line):
                    data = []
                    messagebox.showerror("error", f"File contains not supported data : {line}")
                    return
                # checks if white Space is in File and ignores it
                elif line.isspace():
                    messagebox.showinfo("Warning", f"Your FILE : {file.name} contains Whitespace !")
                    continue
                else:
                    data.append(int(line))
    if token:
        messagebox.showinfo("Warning", f"Some values appeared multiple times! Only added once to Data")
    read_data_command()


def save_file():
    global fig
    filename = filedialog.asksaveasfilename(title="Save File",
                                            filetypes=[("png files", "*.png"), ("jpeg files", "*.jpeg")])
    if filename:
        fig.savefig(filename)


def callor(event):
    insert_command()


def placeholder(event):
    value_entry.delete(0, tk.END)


style_sheet = {
    # background color: 3c3f41
    # button color:
    # Font Color:
    "animation_button": {
        # "fg": "#000000",
        "bg": "#3a4750",
        "font": "Helvetica, 12",
        "relief": "flat",
        "width": "7",
        "height": "2"
    },
    "data_structure_button": {
        "fg": "#eeeeee",
        "bg": "#3a4750",
        "font": "Helvetica, 12",
        "padx": "1",
        "pady": "0",
        "width": "10",
        "height": "2"
    },
    "log_frame": {
        "bg": "#2b2b2b",
        "highlightbackground": "#ffffff",
        "highlightcolor": "#ffffff",
        "highlightthickness": ".5"
    },
    "log_text": {
        "font": "ariel,30",
        "fg": "#a9b7c6",
        "bg": "#2b2b2b"
    },
    "button_frame": {
        "bg": "#3c3f41",
        "padx": "1",
        "pady": "1",
        "highlightbackground": "#2b2b2b",
        "highlightcolor": "#2b2b2b",
        "highlightthickness": "1"
    },
    "canvas": {
        "padx": "0",
        "bg": "#ffffff",
        "highlightbackground": "#2b2b2b",
        "highlightcolor": "#2b2b2b",
        "highlightthickness": "2"
    },
    "interface": {
        "bg": "#3c3f41",
        "highlightbackground": "#2b2b2b",
        "highlightcolor": "#2b2b2b",
        "highlightthickness": "2"
    },
    "animation_frame": {
        "padx": "0",
        "width": "120",
        "highlightbackground": "#00adb5",
        "highlightthickness": "1"
    },
    "label": {
        "font": "Helvetica, 15",
        "fg": "gold",
        "bg": "#3c3f41",
        "padx": "10"
    }
}

if __name__ == "__main__":
    # Init data structures and graphs
    graph_list_index = 0
    skip_list_graph_list = []
    skip_list = sl.SkipList()
    skip_list_graph = SkipListGraph(skip_list)

    treap_graph_list = []
    treap = tr.Treap()
    treap_graph = TreapGraph(treap)

    # Array for all numbers from Input txt
    data = []

    # Background Color
    background_color = "#3c3f41"

    # Figure and plot
    fig = Figure(figsize=(1, 4), dpi=100)
    plot = fig.add_subplot(111)  # 1 by 1 grid subplot No. 1

    # Main window
    root = tk.Tk()
    root.title("Getting laid Vol .4 mit Kohout von der Salbe 4")
    root.config(background=background_color)
    root.minsize(800, 800)

    # Canvas frame
    canvas_frame = tk.Frame(master=root, **style_sheet["canvas"])
    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)

    # Bottom half sub frames
    interface_frame = tk.Frame(master=root, **style_sheet["interface"])

    console_frame = tk.Frame(master=interface_frame)

    # The log
    log_frame = tk.Frame(master=console_frame, **style_sheet["log_frame"])
    button_frame = tk.Frame(master=console_frame, **style_sheet["button_frame"])

    # Frame that contains every button
    animation_frame = tk.Frame(master=button_frame, **style_sheet["animation_frame"])

    data_structure_frame = tk.Frame(master=button_frame, bg=background_color)
    key_structure_frame = tk.Frame(master=data_structure_frame, bg=background_color)
    operator_frame = tk.Frame(master=data_structure_frame, bg=background_color)

    graph_structure_frame = tk.Frame(master=button_frame, bg="red")#background_color
    switch_algorithm_frame = tk.Frame(master=graph_structure_frame, bg=background_color)
    graph_operation_frame = tk.Frame(master=graph_structure_frame, bg=background_color)

    # Pseudocode canvas
    pseudo_canvas = tk.Canvas(master=interface_frame, width=225, height=225, background="red")
    img = ImageTk.PhotoImage(Image.open("./res/jackson.jpeg"))
    pseudo_canvas.create_image(112.5, 112.5, image=img)

    skip_list_graph.draw(skip_list, plot, canvas)

    # Dropdown menu for choosing the algorithm
    algorithms = ["Skip List", "Treap"]
    algorithm = tk.StringVar(root)
    algorithm.set(algorithms[0])  # default value

    # Buttons

    play_pause_button = tk.Button(**style_sheet["animation_button"], master=animation_frame, text="Play",
                                  command=play_command)
    previous_button = tk.Button(**style_sheet["animation_button"], master=animation_frame, text="Previous",
                                command=previous_command)

    next_button = tk.Button(**style_sheet["animation_button"], master=animation_frame, text="Next",
                            command=next_command)
    stop_button = tk.Button(**style_sheet["animation_button"], master=animation_frame, text="Stop",
                            command=stop_command)

    value_label = tk.Label(master=key_structure_frame, text="Key", **style_sheet["label"])
    value_entry = tk.Entry(master=key_structure_frame, width=15, font="Helvetica, 12")
    value_entry.insert(0, "")

    search_button = tk.Button(master=operator_frame, text="Search", **style_sheet["data_structure_button"],
                              command=search_command)
    insert_button = tk.Button(master=operator_frame, text="Insert", **style_sheet["data_structure_button"],
                              command=insert_command)
    delete_button = tk.Button(master=operator_frame, text="Delete", **style_sheet["data_structure_button"],
                              command=delete_command)
    #TODO: FRAMES GETAUSCHT !!! LOGISCH SORIERT
    algo_dropdown = tk.OptionMenu(graph_operation_frame, algorithm, *algorithms,
                                  command=switch_algorithm)  # graph_structure_frame
    algo_dropdown.config(background="red", font=("helvetica", "12"))
    open_button = tk.Button(master=graph_operation_frame, text="Open File", **style_sheet["data_structure_button"],
                            command=open_file)
    filename_label = tk.Label(master=graph_operation_frame, text="FILENAME", width=15, height=2)


    save_button = tk.Button(master=graph_structure_frame, text="Save Graph", **style_sheet["data_structure_button"],
                            command=save_file)

    clear_button = tk.Button(master=graph_structure_frame, text="Clear Graph", **style_sheet["data_structure_button"],
                             command=clear_command)

    info_button = tk.Button(root, text="?", fg="red", bg="green", command=info_command, relief="raised", bitmap="info")
    # Testing log output
    log_widget = lw.LogWidget()
    log_message = tk.Message(master=log_frame, text=log_widget.update(), **style_sheet["log_text"], anchor='nw')

    # Packing everything
    canvas_frame.pack(side="top", fill="both", expand=1, anchor="e", padx=10, pady=10)
    canvas._tkcanvas.pack(fill="both", expand=1, anchor="e")

    interface_frame.pack(side="bottom", padx=10, pady=10, fill="x", expand=1, anchor="sw")
    console_frame.pack(side="left", fill="both")
    log_frame.pack(side="left", fill="both", expand=1, padx=0, anchor="nw")
    log_message.pack(side="left", padx=0, fill="both", expand=1)

    button_frame.pack(side="left", padx=0, anchor="n")
    animation_frame.pack(side="top", fill="x", padx=0)
    data_structure_frame.pack(side="top", fill="x")
    key_structure_frame.pack(side="top", anchor="nw")
    operator_frame.pack(side="top")

    graph_operation_frame.pack(side="top", fill="x")
    graph_structure_frame.pack(side="top", fill="x")
    switch_algorithm_frame.pack(side="top", fill="x")

    pseudo_canvas.pack(side="left", anchor="ne")
    #    info_button.pack()

    # Packing all buttons
    stop_button.pack(side="left", fill="x")
    previous_button.pack(side="left", fill="x")
    play_pause_button.pack(side="left", fill="x")
    next_button.pack(side="left", fill="x")

    value_label.pack(side="left")
    value_entry.pack(side="left")

    insert_button.pack(side="left")
    delete_button.pack(side="left")
    search_button.pack(side="left")

    algo_dropdown.pack(side="left", anchor="w")
    open_button.pack(side="left", anchor="w")
    filename_label.pack(side="left", anchor="w")

    save_button.pack(side="left", anchor="w")
    clear_button.pack(side="left", anchor="e")

    value_entry.bind("<Button>", placeholder)
    # value_entry.bind("<Key>", placeholder)
    root.bind('<Return>', callor)

    # Start program
    root.mainloop()
