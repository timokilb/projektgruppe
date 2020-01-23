import treap as tr
import tkinter as tk
import networkx as nx
import log_widget as lw
import pseudocode_widget as pw
import animation_handler as ah
import time
import math
import re
import skip_list as sl
from skip_list_graph import SkipListGraph
from treap_graph import TreapGraph
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import filedialog, messagebox
import time


def update_canvas(graph):
    global plot
    global figure
    global canvas
    plot.clear()
    pos = nx.get_node_attributes(graph, 'pos')
    label = nx.get_node_attributes(graph, 'label')
    color_dict = nx.get_node_attributes(graph, 'color')
    color_list = []
    for color in color_dict:
        color_list.append(color_dict[color])
    nx.draw(graph, pos, node_size=1000, node_color=color_list, labels=label, with_labels=True, ax=plot)
    canvas.draw()


# TODO : char filter !
def search_command():
    global algorithm
    global animation_handler
    global graph_list_index
    global log_widget
    global log_message
    global treap


    # Clear the old animations and reset index to zero
    animation_handler.get_instance().skip_list_graph_list.clear()
    animation_handler.get_instance().treap_graph_list.clear()
    animation_handler.get_instance().pseudocode_list.clear()
    animation_handler.get_instance().treap_pseudocode_list.clear()
    graph_list_index = 0
    plot.clear()

    value = int(value_entry.get())

    # Handling the log widget:
    log_widget.push(f"Searched Key: {value}")
    log_message.config(text=log_widget.update())

    if algorithm.get() == "Skip List":
        skip_list.find(value)
        update_canvas(animation_handler.get_instance().skip_list_graph_list[graph_list_index])
        pseudocode_obj.update(animation_handler.get_instance().pseudocode_list[graph_list_index][0],
                              animation_handler.get_instance().pseudocode_list[graph_list_index][1])
    elif algorithm.get() == "Treap":
        treap.find(value, treap)
        update_canvas(animation_handler.get_instance().treap_graph_list[graph_list_index])
        pseudocode_obj.update(animation_handler.get_instance().treap_pseudocode_list[graph_list_index][0],
                              animation_handler.get_instance().treap_pseudocode_list[graph_list_index][1])
    value_entry.delete(0, tk.END)


# Insert the value in the entry into the data structure, call the draw function
# TODO : char filter !
# TODO: Empty the graph lists here so that a new opeator is played, you dont have to skip through the earlier animation???
def insert_command():
    global algorithm
    global animation_handler
    global graph_list_index
    global log_widget
    global log_message
    global treap

    # Clear the old animations and reset index to zero
    animation_handler.get_instance().skip_list_graph_list.clear()
    animation_handler.get_instance().treap_graph_list.clear()
    animation_handler.get_instance().pseudocode_list.clear()
    animation_handler.get_instance().treap_pseudocode_list.clear()
    graph_list_index = 0
    plot.clear()

    try:
        value = int(value_entry.get())
    except:
        log_widget.push("Invalid Key")
        log_message.config(text=log_widget.update())
        return

    skip_list.insert(value)
    treap.insert(value, treap)

    # Handling the log widget:
    log_widget.push(f"Inserted Key: {value}")
    log_message.config(text=log_widget.update())

    if algorithm.get() == "Skip List":
        update_canvas(animation_handler.get_instance().skip_list_graph_list[graph_list_index])
        pseudocode_obj.update(animation_handler.get_instance().pseudocode_list[graph_list_index][0],
                              animation_handler.get_instance().pseudocode_list[graph_list_index][1])
    elif algorithm.get() == "Treap":
        update_canvas(animation_handler.get_instance().treap_graph_list[graph_list_index])
        pseudocode_obj.update(animation_handler.get_instance().treap_pseudocode_list[graph_list_index][0],  # text
                              animation_handler.get_instance().treap_pseudocode_list[graph_list_index][1])  # color

    value_entry.delete(0, tk.END)
    # value_entry.insert(0, f"\tLast Operation was INSERT with Key : {value}")


# TODO : char filter !
def delete_command():
    global algorithm
    global graph_list_index
    global animation_handler
    global treap
    global log_widget
    global log_message

    animation_handler.get_instance().skip_list_graph_list.clear()
    animation_handler.get_instance().treap_graph_list.clear()
    animation_handler.get_instance().pseudocode_list.clear()
    animation_handler.get_instance().treap_pseudocode_list.clear()

    graph_list_index = 0
    plot.clear()

    value = int(value_entry.get())
    skip_list.delete(value)
    treap.delete(value, treap)

    # Handling the log widget:
    log_widget.push(f"Deleted Key: {value}")
    log_message.config(text=log_widget.update())

    current_presst_button = "delete"
    if algorithm.get() == "Skip List":
        update_canvas(animation_handler.get_instance().skip_list_graph_list[graph_list_index])
        pseudocode_obj.update(animation_handler.get_instance().pseudocode_list[graph_list_index][0],
                              animation_handler.get_instance().pseudocode_list[graph_list_index][1])
    elif algorithm.get() == "Treap":
        # TODO UPDATE CANVAS
        update_canvas(animation_handler.get_instance().treap_graph_list[graph_list_index])
        pseudocode_obj.update(animation_handler.get_instance().treap_pseudocode_list[graph_list_index][0],
                              animation_handler.get_instance().treap_pseudocode_list[graph_list_index][1])
    value_entry.delete(0, tk.END)
    # value_entry.insert(0, f"\tLast Operation was DELETE with Key : {value}")

def play_pause_command():
    global active
    global play_pause_button
    if play_pause_button["text"] == "Play":
        play_pause_button.config(text="Pause")
        active = True
        play_command()
    else:
        play_pause_button.config(text="Play")
        active = False


def play_command():
    global active
    global canvas
    global graph_list_index
    global animation_handler
    global algorithm
    global pseudocode_obj

    if active is False:
        return
    elif algorithm.get() == "Skip List":
        if graph_list_index < len(animation_handler.get_instance().skip_list_graph_list) - 1:
            graph_list_index += 1
            update_canvas(animation_handler.get_instance().skip_list_graph_list[graph_list_index])
            pseudocode_obj.update(animation_handler.get_instance().pseudocode_list[graph_list_index][0],
                                  animation_handler.get_instance().pseudocode_list[graph_list_index][1])
            root.after(400, play_command)
#        else: TODO: Change Play Pause Label to "Replay" and implement replay function


    elif algorithm.get() == "Treap":
        if graph_list_index < len(animation_handler.get_instance().treap_graph_list) -1:
            graph_list_index += 1
            update_canvas(animation_handler.get_instance().treap_graph_list[graph_list_index])
            pseudocode_obj.update(animation_handler.get_instance().treap_pseudocode_list[graph_list_index][0],
                                  animation_handler.get_instance().treap_pseudocode_list[graph_list_index][1])
            root.after(1000, play_command)
# TODO : Copy here replay code from above

def previous_command():
    global graph_list_index
    global animation_handler
    global algorithm
    global active
    global play_pause_button
    play_pause_button.config(text="Play")
    active = False

    if algorithm.get() == "Skip List":
        if graph_list_index < len(animation_handler.get_instance().skip_list_graph_list) - 1 and graph_list_index > 0:
            graph_list_index -= 1
            update_canvas(animation_handler.get_instance().skip_list_graph_list[graph_list_index])
            pseudocode_obj.update(animation_handler.get_instance().pseudocode_list[graph_list_index][0],
                                  animation_handler.get_instance().pseudocode_list[graph_list_index][1])
    elif algorithm.get() == "Treap":
        if graph_list_index < len(animation_handler.get_instance().treap_graph_list) and graph_list_index > 0:
            graph_list_index -= 1
            update_canvas(animation_handler.get_instance().treap_graph_list[graph_list_index])
            pseudocode_obj.update(animation_handler.get_instance().treap_pseudocode_list[graph_list_index][0],
                                  animation_handler.get_instance().treap_pseudocode_list[graph_list_index][1])


def next_command():
    global graph_list_index
    global animation_handler
    global algorithm
    global active
    global play_pause_button
    play_pause_button.config(text="Play")
    active = False

    if algorithm.get() == "Skip List":
        if graph_list_index < len(animation_handler.get_instance().skip_list_graph_list) - 1:
            graph_list_index += 1
            update_canvas(animation_handler.get_instance().skip_list_graph_list[graph_list_index])

            pseudocode_obj.update(animation_handler.get_instance().pseudocode_list[graph_list_index][0],
                                  animation_handler.get_instance().pseudocode_list[graph_list_index][1])
    elif algorithm.get() == "Treap":
        if graph_list_index < len(animation_handler.get_instance().treap_graph_list) - 1:
            graph_list_index += 1
            update_canvas(animation_handler.get_instance().treap_graph_list[graph_list_index])
            pseudocode_obj.update(animation_handler.get_instance().treap_pseudocode_list[graph_list_index][0],
                                  animation_handler.get_instance().treap_pseudocode_list[graph_list_index][1])


def stop_command():
    global treap
    global algorithm
    global graph_list_index
    global active
    global play_pause_button
    play_pause_button.config(text="Play")
    active = False
    graph_list_index = 0

    if algorithm.get() == "Skip List":
        update_canvas(animation_handler.get_instance().skip_list_graph_list[graph_list_index])
        pseudocode_obj.update(animation_handler.get_instance().pseudocode_list[graph_list_index][0],
                              animation_handler.get_instance().pseudocode_list[graph_list_index][1])
    elif algorithm.get() == "Treap":
        update_canvas(animation_handler.get_instance().treap_graph_list[graph_list_index])
        pseudocode_obj.update(animation_handler.get_instance().treap_pseudocode_list[graph_list_index][0],
                              animation_handler.get_instance().treap_pseudocode_list[graph_list_index][1])


def clear_command():
    global graph_list_index
    global animation_handler
    global skip_list_graph
    global treap_graph
    global algorithm
    global treap
    global skip_list
    global active
    global play_pause_button
    play_pause_button.config(text="Play")
    active = False
    graph_list_index = 0

    treap = tr.Treap()
    skip_list = sl.SkipList()

    animation_handler.get_instance().skip_list_graph_list.clear()
    animation_handler.get_instance().treap_graph_list.clear()
    animation_handler.get_instance().pseudocode_list.clear()
    animation_handler.get_instance().treap_pseudocode_list.clear()

    treap_graph = TreapGraph(treap)
    skip_list_graph = SkipListGraph(skip_list)

    animation_handler.get_instance().treap_graph_list.append(treap_graph.create_graph())
    animation_handler.get_instance().skip_list_graph_list.append(skip_list_graph.create_graph(skip_list))

    if algorithm.get() == "Treap":
        update_canvas(animation_handler.get_instance().treap_graph_list[graph_list_index])
    else:
        update_canvas(animation_handler.get_instance().skip_list_graph_list[graph_list_index])


# TODO: Use graph list and keep track of index? Test as soon as there are animations for treap

def switch_algorithm(string):
    global treap_graph
    global skip_list_graph
    global canvas
    global graph_list_index
    global plot
    global active
    global play_pause_button
    play_pause_button.config(text="Play")
    active = False
    if string == "Treap":
        treap_graph.draw(treap_graph.treap, plot, canvas)
    elif string == "Skip List":
        skip_list_graph.draw(skip_list_graph.skip_list, plot, canvas)


def read_data_command():
    global algorithm
    global animation_handler
    global treap
    global graph_list_index
    graph_list_index = 0

    for line in data:
        animation_handler.get_instance().skip_list_graph_list.clear()
        animation_handler.get_instance().treap_graph_list.clear()
        animation_handler.get_instance().pseudocode_list.clear()
        animation_handler.get_instance().treap_pseudocode_list.clear()

        skip_list.insert(int(line))
        treap.insert(int(line), treap)

        if algorithm.get() == "Skip List":
            update_canvas(animation_handler.get_instance().skip_list_graph_list[graph_list_index])
            pseudocode_obj.update(animation_handler.get_instance().pseudocode_list[graph_list_index][0],
                                  animation_handler.get_instance().pseudocode_list[graph_list_index][1])
        elif algorithm.get() == "Treap":
            update_canvas(animation_handler.get_instance().treap_graph_list[graph_list_index])
            pseudocode_obj.update(animation_handler.get_instance().treap_pseudocode_list[graph_list_index][0],
                                  animation_handler.get_instance().treap_pseudocode_list[graph_list_index][1])


# opens FileExplorer to choose ONLY .txt files
# TODO: Handle spezial chars !
def open_file():
    global active
    global play_pause_button
    play_pause_button.config(text="Play")
    active = False
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
    global active
    global play_pause_button
    play_pause_button.config(text="Play")
    active = False
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
        "fg": "#a9b7c6",
        "bg": "#313335",
        "activeforeground": "#313335",
        "activebackground": "#a9b7c6",
        "font": "Helvetica, 12",
        "relief": "raised",
        "bd": "3",
        "width": "10",
        "height": "2"
    },
    "data_structure_button": {
        "fg": "#a9b7c6",
        "bg": "#313335",
        "activeforeground": "#313335",
        "activebackground": "#a9b7c6",
        "font": "Helvetica, 12",
        "relief": "raised",
        "bd": "1",
        "padx": "0",
        "pady": "0",
        "width": "10",
        "height": "2"
    },
    "log_frame": {
        "bg": "#2b2b2b",
        "highlightbackground": "#2b2b2b",
        "highlightcolor": "#2b2b2b",
        "highlightthickness": ".5"
    },
    "log_text": {
        "font": "helvetica, 11",
        "fg": "#a9b7c6",
        "bg": "#2b2b2b"
    },
    "button_frame": {
        "bg": "#3c3f41",
        "padx": "3",
        "pady": "5",
        "highlightbackground": "#2b2b2b",
        "highlightcolor": "#2b2b2b",
        "highlightthickness": "0"
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
        "bg": "#3c3f41",
        "highlightbackground": "#00adb5",
        "highlightthickness": "0"
    },
    "label": {
        "font": "Helvetica, 15",
        "fg": "springgreen",
        "bg": "#3c3f41",
        "padx": "10"
    },
    "dropdown": {
        "fg": "#a9b7c6",
        "bg": "#313335",
        "activeforeground": "#313335",
        "activebackground": "#a9b7c6",
        "font": "Helvetica, 12",
        "relief": "raised",
        "bd": "1",
        "width": "10",
        "height": "2",
        "highlightthickness": "0"
    }
}


def get_frame():
    global pseudocode_frame
    return pseudocode_frame


if __name__ == "__main__":
    # Init data structures and graphs
    graph_list_index = 0

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
    root.title("Projektgruppe")
    root.config(background=background_color)
    root.minsize(850, 850)
    active = False

    # Canvas frame
    canvas_frame = tk.Frame(master=root, **style_sheet["canvas"])
    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)

    # Bottom half sub frames
    interface_frame = tk.Frame(master=root, **style_sheet["interface"])

    console_frame = tk.Frame(master=interface_frame)

    # The log
    button_frame = tk.Frame(master=console_frame, **style_sheet["button_frame"])
    log_frame = tk.Frame(master=button_frame, **style_sheet["log_frame"])

    # Frame that contains every button
    animation_frame = tk.Frame(master=button_frame, **style_sheet["animation_frame"])

    data_structure_frame = tk.Frame(master=button_frame, bg=background_color)
    key_structure_frame = tk.Frame(master=data_structure_frame, bg=background_color)
    operator_frame = tk.Frame(master=data_structure_frame, bg=background_color)

    graph_structure_frame = tk.Frame(master=button_frame, bg=background_color)
    switch_algorithm_frame = tk.Frame(master=graph_structure_frame, bg=background_color)
    graph_operation_frame = tk.Frame(master=graph_structure_frame, bg=background_color)
    # TODO : mit token und dann in jeder funktion öffen mit jeweiiger .txt und packen
    # Pseudocode canvas
    pseudocode_frame = tk.Frame(master=interface_frame, bg="#2b2b2b", highlightthickness=5,
                                highlightbackground=background_color)

    animation_handler = ah.AnimationHandler(pseudocode_frame)
    skip_list = sl.SkipList()
    skip_list_graph = SkipListGraph(skip_list)

    # generating Pseudocode Obj
    pseudocode_obj = pw.PseudocodeWidget(pseudocode_frame)

    skip_list_graph.draw(skip_list, plot, canvas)

    # Dropdown menu for choosing the algorithm
    algorithms = ["Skip List", "Treap"]
    algorithm = tk.StringVar(root)
    algorithm.set(algorithms[0])  # default value

    # Buttons

    play_pause_button = tk.Button(**style_sheet["animation_button"], master=animation_frame, text="Play",
                                  command=play_pause_command)
    previous_button = tk.Button(**style_sheet["animation_button"], master=animation_frame, text="Previous",
                                command=previous_command)
    next_button = tk.Button(**style_sheet["animation_button"], master=animation_frame, text="Next",
                            command=next_command)
    stop_button = tk.Button(**style_sheet["animation_button"], master=animation_frame, text="Stop",
                            command=stop_command)

    value_label = tk.Label(master=key_structure_frame, text="Key:", **style_sheet["label"])
    value_entry = tk.Entry(master=key_structure_frame, width=15, font="Helvetica, 12")

    value_entry.insert(0, "")

    search_button = tk.Button(master=operator_frame, text="Search", **style_sheet["data_structure_button"],
                              command=search_command)
    insert_button = tk.Button(master=operator_frame, text="Insert", **style_sheet["data_structure_button"],
                              command=insert_command)
    delete_button = tk.Button(master=operator_frame, text="Delete", **style_sheet["data_structure_button"],
                              command=delete_command)
    open_button = tk.Button(master=graph_operation_frame, text="Open File", **style_sheet["data_structure_button"],
                            command=open_file)
    filename_label = tk.Label(master=graph_operation_frame, text="Filename", height=2, borderwidth="3", relief="flat")
    filename_label.config(font="helvetica, 12")

    algo_dropdown = tk.OptionMenu(graph_structure_frame, algorithm, *algorithms,
                                  command=switch_algorithm)

    algo_dropdown.config(**style_sheet["dropdown"])
    algo_dropdown["menu"].config(fg="#a9b7c6", bg="#313335", activeforeground="#313335", activebackground="#a9b7c6")

    save_button = tk.Button(master=graph_structure_frame, text="Save Graph", **style_sheet["data_structure_button"],
                            command=save_file)

    clear_button = tk.Button(master=graph_structure_frame, text="Clear Graph", **style_sheet["data_structure_button"],
                             command=clear_command)

    # info_button = tk.Button(root, text="?", fg="red", bg="green", command=info_command, relief="flat", bitmap="info")
    # Testing log output
    log_widget = lw.LogWidget()
    log_message = tk.Message(master=log_frame, text=log_widget.update(), **style_sheet["log_text"], anchor='nw')

    # Packing everything
    canvas_frame.pack(side="top", fill="both", expand=1, anchor="s", padx=10, pady=10)
    canvas._tkcanvas.pack(fill="both", expand=1, anchor="s")

    interface_frame.pack(side="bottom", padx=10, pady=10, fill="x", anchor="sw")
    console_frame.pack(side="left", fill="both")
    button_frame.pack(side="left", anchor="n")

    animation_frame.pack(side="top", fill="x", padx=0)
    data_structure_frame.pack(side="top", fill="x")
    key_structure_frame.pack(side="top", fill="x")
    operator_frame.pack(side="top", fill="x")

    graph_operation_frame.pack(side="top", fill="x")
    graph_structure_frame.pack(side="top", fill="x")
    switch_algorithm_frame.pack(side="top", fill="x")

    log_frame.pack(side="top", fill="both", expand=1, padx=0, anchor="nw")
    log_message.pack(side="top", padx=0, fill="both", expand=1)

    pseudocode_frame.pack(side="left", anchor="nw", fill="both", expand=1)
    pseudocode_obj.pack_labels()

    #    info_button.pack()

    # Packing all buttons
    stop_button.pack(side="left", fill="x", padx="2", pady="2")
    previous_button.pack(side="left", fill="x", padx="2", pady="2")
    play_pause_button.pack(side="left", fill="x", padx="2", pady="2")
    next_button.pack(side="left", fill="x", padx="2", pady="2")

    value_label.pack(side="left", fill="x", padx="2", pady="2")
    value_entry.pack(side="left", fill="x", padx="2", pady="2", expand=1)

    insert_button.pack(side="left", fill="x", padx="2", pady="2", expand=1)
    delete_button.pack(side="left", fill="x", padx="2", pady="2", expand=1)
    search_button.pack(side="left", fill="x", padx="2", pady="2", expand=1)

    open_button.pack(side="left", fill="x", padx="2", pady="2", expand=1)
    filename_label.pack(side="left", fill="x", padx="2", pady="0", expand=1)

    algo_dropdown.pack(side="left", fill="x", padx="2", pady="2", expand=1)
    save_button.pack(side="left", fill="x", padx="2", pady="2", expand=1)
    clear_button.pack(side="left", fill="x", padx="2", pady="2", expand=1)

    value_entry.bind("<Button>", placeholder)
    # value_entry.bind("<Key>", placeholder)
    root.bind('<Return>', callor)

    # Start program
    root.mainloop()
