import skip_list as sl
import treap as tr
import tkinter as tk
import networkx as nx
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
    global skip_list_graph_list
    global treap_graph_list

    # Clear the old animations and reset index to zero
    skip_list_graph_list.clear()
    treap_graph_list.clear()
    graph_list_index = 0
    plot.clear()
    value = int(value_entry.get())
    if algorithm.get() == "Skip List":
        skip_list.find(value, skip_list_graph_list)
        update_canvas(skip_list_graph_list[graph_list_index])
    elif algorithm.get() == "Treap":
        treap.find(value, treap_graph_list)
    value_entry.delete(0, tk.END)
    value_entry.insert(0, f"\tLast Operation was SEARCH with Key : {value}")


# Insert the value in the entry into the data structure, call the draw function
# TODO : char filter !
# TODO: Empty the graph lists here so that a new opeator is played, you dont have to skip through the earlier animation???
def insert_command():
    global algorithm
    global graph_list_index
    global skip_list_graph_list
    global treap_graph_list

    # Clear the old animations and reset index to zero
    skip_list_graph_list.clear()
    treap_graph_list.clear()
    graph_list_index = 0
    plot.clear()

    value = int(value_entry.get())
    skip_list.insert(value, skip_list_graph_list)
    treap.insert(value, treap_graph_list)

    if algorithm.get() == "Skip List":
        update_canvas(skip_list_graph_list[graph_list_index])
    elif algorithm.get() == "Treap":
        treap_graph.draw(treap, plot, canvas)
    value_entry.delete(0, tk.END)
    value_entry.insert(0, f"\tLast Operation was INSERT with Key : {value}")

# TODO : char filter !
def delete_command():
    global algorithm
    global graph_list_index
    global skip_list_graph_list
    global treap_graph_list

    value = int(value_entry.get())
    skip_list.delete(value, skip_list_graph_list)
    treap.delete(value)

    if algorithm.get() == "Skip List":
        skip_list_graph.draw(skip_list, plot, canvas)
        update_canvas(skip_list_graph_list[graph_list_index])
    elif algorithm.get() == "Treap":
        treap_graph.draw(treap, plot, canvas)
    value_entry.delete(0, tk.END)
    value_entry.insert(0, f"\tLast Operation was DELETE with Key : {value}")


def play_command():
    global graph_list_index
    global skip_list_graph_list
    current_button_text = play_pause_button['text']
    play_pause_button.config(text="Pause")
    while graph_list_index < len(skip_list_graph_list) - 1:
        graph_list_index += 1
        timestamp = int(math.floor(time.time()))
        while math.floor(time.time()) < timestamp + 1:
            pass
        update_canvas(skip_list_graph_list[graph_list_index])
    play_pause_button.config(text="Play")


def previous_command():
    global graph_list_index
    global skip_list_graph_list
    if graph_list_index > 0:
        graph_list_index -= 1
        update_canvas(skip_list_graph_list[graph_list_index])


def next_command():
    global graph_list_index
    global skip_list_graph_list
    if graph_list_index < len(skip_list_graph_list) - 1:
        graph_list_index += 1
        update_canvas(skip_list_graph_list[graph_list_index])


def stop_command():
    global graph_list_index
    graph_list_index = 0
    return update_canvas(skip_list_graph_list[graph_list_index])


def clear_command():
    return


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
    global alogrithm
    global skip_list_graph_list
    global treap_graph_list
    global graph_list_index
    graph_list_index = 0
    for line in data:
        skip_list_graph_list.clear()
        treap_graph_list.clear()
        skip_list.insert(int(line), skip_list_graph_list)
        treap.insert(int(line), treap_graph_list)
        if algorithm.get() == "Skip List":
            update_canvas(skip_list_graph_list[graph_list_index])
            print(len(skip_list_graph_list), " IS LENGTH")
        else:
            treap_graph.draw(treap, plot, canvas)


# opens FileExplorer to choose ONLY .txt files
# TODO: Handle spezial chars !
def open_file():
    global data
    data = []
    token = False
    file = filedialog.askopenfile(mode='r', title="Open file", filetypes=[('Text Files', '*.txt')])
    # check if file was opend successfully
    if file:
        filename_label.config(text=file.name.split("/")[-1])
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


# TODO Mit getter und setter arbeiten!

if __name__ == "__main__":
    # Main window
    root = tk.Tk()
    root.title("testing out new waters")
    root.config(background="black")

    # Figure and plot
    fig = Figure(figsize=(10, 5), facecolor="white")
    plot = fig.add_subplot(111)  # 1 by 1 grid subplot No. 1

    # Init data structures and graphs
    graph_list_index = 0
    skip_list_graph_list = []
    skip_list = sl.SkipList()
    skip_list_graph = SkipListGraph(skip_list)
    treap_graph_list = []
    treap = tr.Treap()
    # treap.insert(20, treap_graph_list)
    treap_graph = TreapGraph(treap)

    # Canvas for drawing the list/ treap
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas._tkcanvas.grid(row=0, column=0, columnspan=4)
    skip_list_graph.draw(skip_list, plot, canvas)

    # Canvas for displaying the Pseudocode
    pseudo_canvas = tk.Canvas(root, width=400, height=600)
    pseudo_canvas.grid(row=0, column=5, rowspan=5)
    img = ImageTk.PhotoImage(Image.open("jackson.jpeg"))
    pseudo_canvas.create_image(225, 225, image=img)

    # Data File

    data = []

    # Dropdown menu for choosing the algorithm
    algorithms = ["Skip List", "Treap"]
    algorithm = tk.StringVar(root)
    algorithm.set(algorithms[0])  # default value
    algo_dropdown = tk.OptionMenu(root, algorithm, *algorithms, command=switch_algorithm)

    # Buttons

    play_pause_button = tk.Button(root, text="Play", command=play_command)
    previous_button = tk.Button(root, text="Previous", command=previous_command)
    next_button = tk.Button(root, text="Next", fg="red", command=next_command)
    stop_button = tk.Button(root, text="Stop", fg="red", command=stop_command)

    # value_label = tk.Label(root, text="Key:")
    value_entry = tk.Entry(root, width=50)
    value_entry.insert(0, "\tEnter a KEY to perform an operation")
    search_button = tk.Button(root, text="Search", fg="red", command=search_command)
    insert_button = tk.Button(root, text="Insert", fg="red", command=insert_command)
    delete_button = tk.Button(root, text="Delete", fg="red", command=delete_command)
    clear_button = tk.Button(root, text="Clear", command=clear_command)

    open_button = tk.Button(root, text="Open File", fg="red", command=open_file)
    read_button = tk.Button(root, text="Read", fg="blue", bg="white", command=read_data_command)
    save_button = tk.Button(root, text="Save Graph", fg="green", bg="black", command=save_file)
    # TODO : width responisve machen !!!!
    filename_label = tk.Label(root, text="FILENAME", width=20)
    info_button = tk.Button(root, text="?", fg="red", bg="green")

    # Layout
    play_pause_button.grid(row=1, column=1)
    previous_button.grid(row=1, column=2)
    next_button.grid(row=1, column=3)
    stop_button.grid(row=1, column=0)

    # value_label.grid(row=2, column=2)
    value_entry.grid(row=2, column=3)
    search_button.grid(row=3, column=2, columnspan=2)
    insert_button.grid(row=4, column=2, columnspan=2)
    delete_button.grid(row=5, column=2, columnspan=2)
    clear_button.grid(row=6, column=2, columnspan=2)

    open_button.grid(row=5, column=0)
    filename_label.grid(row=6, column=0)
    read_button.grid(row=5, column=1)
    info_button.grid(row=6, column=6)
    save_button.grid(row=5, column=2)
    algo_dropdown.grid(row=3, column=0, columnspan=2)

    value_entry.bind("<Button>", placeholder)
    # TODO : auskommi weil sonst nur ein entry möglich , try it !
    # value_entry.bind("<Key>", placeholder)
    root.bind('<Return>', callor)

    # Start program
    root.mainloop()
