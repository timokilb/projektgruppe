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


button_styles = {
    "animation_button": {
        "fg": "#1a1a1a",
        "bg": "#8a8a8a",
        "font": "Helvetica, 12",
        "padx": "10",
        "pady": "0"
    },
    "data_structure_button": {
        "fg": "#1a1a1a",
        "bg": "#8a8a8a",
        "font": "Helvetica, 12",
        "padx": "1",
        "pady": "0"
    },
    "log_text": {
        "font": "ariel,30"
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
    #Background Color
    background_color = "#3a3a3a"
    # Figure and plot

    fig = Figure(figsize=(10, 5), facecolor="grey", dpi=100)
    plot = fig.add_subplot(111)  # 1 by 1 grid subplot No. 1


    # Making the window elements
    # Main window
    root = tk.Tk()
    root.title("Getting laid Vol .4 mit Kohout von der Salbe 4")
    root.config(background=background_color)

    # Canvas frame
    canvas_frame = tk.Frame(master=root, bg=background_color)
    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)

    # Bottom half sub frames
    interface_frame = tk.Frame(master=root, bg="green")

    # The log
    log_frame = tk.Frame(master=interface_frame) # text="fickerjackson", font="helvetica")

    # Frame that contains every button
    button_frame = tk.Frame(master=interface_frame, bg="red")
    animation_frame = tk.Frame(master=button_frame, bg=background_color, relief="ridge", bd="3")

    data_structure_frame = tk.Frame(master=button_frame, bg=background_color)
    key_structure_frame = tk.Frame(master=data_structure_frame, bg=background_color)
    operator_frame = tk.Frame(master=data_structure_frame, bg=background_color)

    graph_structure_frame = tk.Frame(master=button_frame, bg=background_color)
    switch_algorithm_frame = tk.Frame(master=graph_structure_frame, bg=background_color)
    graph_operation_frame = tk.Frame(master=graph_structure_frame, bg=background_color)



    # Pseudocode canvas
    pseudo_canvas = tk.Canvas(master=interface_frame, width=400, height=350, background="red")
    img = ImageTk.PhotoImage(Image.open("./res/testpesudocode.jpeg"))
    pseudo_canvas.create_image(203, 253, image=img)




    interface_frame.pack(side="top", fill="x")


    skip_list_graph.draw(skip_list, plot, canvas)

    # Dropdown menu for choosing the algorithm
    algorithms = ["Skip List", "Treap"]
    algorithm = tk.StringVar(root)
    algorithm.set(algorithms[0])  # default value
    algo_dropdown = tk.OptionMenu(graph_structure_frame, algorithm, *algorithms, command=switch_algorithm)

    # Buttons

    play_pause_button = tk.Button(master=animation_frame, text="Play", command=play_command,
                                  fg=button_styles["animation_button"]["fg"],
                                  bg=button_styles["animation_button"]["bg"],
                                  font=button_styles["animation_button"]["font"])

    previous_button = tk.Button(master=animation_frame, text="Previous",
                                command=previous_command,
                                fg=button_styles["animation_button"]["fg"],
                                bg=button_styles["animation_button"]["bg"],
                                font=button_styles["animation_button"]["font"])

    next_button = tk.Button(master=animation_frame, text="Next", command=next_command,
                            fg=button_styles["animation_button"]["fg"],
                            bg=button_styles["animation_button"]["bg"],
                            font=button_styles["animation_button"]["font"])

    stop_button = tk.Button(master=animation_frame, text="Stop", command=stop_command,
                            fg=button_styles["animation_button"]["fg"],
                            bg=button_styles["animation_button"]["bg"],
                            font=button_styles["animation_button"]["font"])

    value_label = tk.Label(master=key_structure_frame, text="Key", fg="#1a1a1a", bg=background_color, font=("Helvetica", 12))
    value_entry = tk.Entry(master=key_structure_frame, width=50)
    value_entry.insert(0, "\tEnter a KEY to perform an operation")

    search_button = tk.Button(master=operator_frame, text="Search", command=search_command)
    insert_button = tk.Button(master=operator_frame, text="Insert", fg=button_styles["data_structure_button"]["fg"], command=insert_command)
    delete_button = tk.Button(master=operator_frame, text="Delete", fg=button_styles["data_structure_button"]["fg"], command=delete_command)

    open_button = tk.Button(master=graph_operation_frame, text="Open File", fg=button_styles["data_structure_button"]["fg"], bg=button_styles["data_structure_button"]["bg"],
                            command=open_file)
    clear_button = tk.Button(master=graph_operation_frame, text="Clear Graph", fg=button_styles["data_structure_button"]["fg"], bg=button_styles["data_structure_button"]["bg"],
                             command=clear_command)
    save_button = tk.Button(master=graph_operation_frame, text="Save Graph", fg=button_styles["data_structure_button"]["fg"], bg=button_styles["data_structure_button"]["bg"],
                            command=save_file)
    filename_label = tk.Label(master=graph_operation_frame, text="FILENAME", width=20, relief="sunken")

    info_button = tk.Button(root, text="?", fg="red", bg="green", command=info_command, relief="raised", bitmap="info")
    # B3 = Button(top, text="info", relief=RAISED,\ bitmap = "info")
    # Testing log output
    log_widget = lw.LogWidget()
    log_message = tk.Message(master=log_frame, text=log_widget.update(), width=500, font=button_styles["log_text"]["font"])

    # Packing everything
    canvas_frame.pack(side="top", fill="both", expand=100, anchor="e", padx=10, pady=10)
    canvas._tkcanvas.pack(fill="both", expand=100, anchor="e")

    interface_frame.pack(side="bottom")

    log_frame.pack(side="left")
    log_message.pack(side="left")

    button_frame.pack(side="left")
    animation_frame.pack(side="top")
    data_structure_frame.pack(side="top")
    key_structure_frame.pack(side="top")
    operator_frame.pack(side="top")

    graph_structure_frame.pack(side="top")
    switch_algorithm_frame.pack(side="top")
    graph_operation_frame.pack(side="bottom")

    pseudo_canvas.pack(side="left")
#    info_button.pack()

    # Packing all buttons
    stop_button.pack(side="left")
    previous_button.pack(side="left")
    play_pause_button.pack(side="left")
    next_button.pack(side="left")

    value_label.pack(side="left")
    value_entry.pack(side="left")

    insert_button.pack(side="top")
    delete_button.pack(side="top")
    search_button.pack(side="top")

    algo_dropdown.pack(side="left")
    open_button.pack(side="top")
    filename_label.pack(side="top")
    clear_button.pack(side="top")
    save_button.pack(side="top")


    value_entry.bind("<Button>", placeholder)
    # value_entry.bind("<Key>", placeholder)
    root.bind('<Return>', callor)

    # Start program
    root.mainloop()
