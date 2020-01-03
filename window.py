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


def search_command():
    global algorithm
    global index
    global skip_list_graph_list
    global treap_graph_list
    index = 0
    plot.clear()
    value = int(value_entry.get())
    if (algorithm.get() == "Skip List"):
        skip_list.find(value, skip_list_graph_list)
        update_canvas(skip_list_graph_list[index])
    elif (algorithm.get() == "Treap"):
        treap.find(value, treap_graph_list)


# Insert the value in the entry into the data structure, call the draw function
def insert_command():
    global algorithm
    global canvas
    value = int(value_entry.get())
    skip_list.insert(value)
    treap.insert(value, treap_graph_list)
    if (algorithm.get() == "Skip List"):
        skip_list_graph.draw(skip_list, plot, canvas)
    elif (algorithm.get() == "Treap"):
        treap_graph.draw(treap, plot, canvas)


def delete_command():
    global algorithm
    global canvas
    value = int(value_entry.get())
    skip_list.delete(value)
    treap.delete(value)
    if (algorithm.get() == "Skip List"):
        skip_list_graph.draw(skip_list, plot, canvas)
    elif (algorithm.get() == "Treap"):
        treap_graph.draw(treap, plot, canvas)


def play_command():
    global index
    global skip_list_graph_list
    current_button_text = play_pause_button['text']
    play_pause_button.config(text="Pause")
    while index < len(skip_list_graph_list) - 1:
        index += 1
        timestamp = int(math.floor(time.time()))
        while math.floor(time.time()) < timestamp + 1:
            pass
        update_canvas(skip_list_graph_list[index])
    play_pause_button.config(text="Play")


def previous_command():
    global index
    global skip_list_graph_list
    if index > 0:
        index -= 1
        update_canvas(skip_list_graph_list[index])


def next_command():
    global index
    global skip_list_graph_list
    if index < len(skip_list_graph_list) - 1:
        index += 1
        update_canvas(skip_list_graph_list[index])


def stop_command():
    global index
    index = 0
    return update_canvas(skip_list_graph_list[index])

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
    global canvas
    for line in data:
        skip_list.insert(int(line))
        treap.insert(int(line), treap_graph_list)
        if algorithm.get() == "Skip List":
            skip_list_graph.draw(skip_list, plot, canvas)
        else:
            treap_graph.draw(treap, plot, canvas)


# opens FileExplorer to choose ONLY .txt files
# TODO: Handle spezial chars !
def open_file():
    global data
    token = False
    file = filedialog.askopenfile(mode='r', title="Open file", filetypes=[('Text Files', '*.txt')])
    # check if file was opend successfully
    if file:
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



# TODO Mit getter und setter arbeiten!

if __name__ == "__main__":
    # Main window
    root = tk.Tk()
    root.title("testing out new waters")

    # Figure and plot
    fig = Figure(figsize=(10, 5), facecolor="white")
    plot = fig.add_subplot(111)  # 1 by 1 grid subplot No. 1

    # Init data structures and graphs
    index = 0
    skip_list_graph_list = []
    skip_list = sl.SkipList()
    skip_list_graph = SkipListGraph(skip_list)
    treap_graph_list = []
    treap = tr.Treap()
    #treap.insert(20, treap_graph_list)
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

    def callor(event):
        insert_command()

    # Buttons
    root.bind('<Return>', callor)
    """
    def swtich_color_enter(event):
        treap_graph.color_switch_enter(event, treap_graph.graph)


    def swtich_color_leave(event):
        treap_graph.color_switch_leave(event, treap_graph.graph)

    root.bind("<Button>", swtich_color_enter)
    root.bind("<Button>", swtich_color_leave)
    """

    play_pause_button = tk.Button(root, text="Play", command=play_command)
    previous_button = tk.Button(root, text="Previous", command=previous_command)
    next_button = tk.Button(root, text="Next", fg="red", bg="green", command=next_command)
    stop_button = tk.Button(root, text="Stop", fg="red", bg="green", command=stop_command)

    value_label = tk.Label(root, text="Key:")
    value_entry = tk.Entry(root)
    search_button = tk.Button(root, text="Search", fg="red", bg="green", command=search_command)
    insert_button = tk.Button(root, text="Insert", fg="red", bg="green", command=insert_command)
    delete_button = tk.Button(root, text="Delete", fg="red", bg="green", command=delete_command)
    clear_button = tk.Button(root, text="Clear", command=clear_command)
    
    read_button = tk.Button(root, text="Read", fg="blue", bg="white", command=read_data_command)
    open_button = tk.Button(root, text="Open File", fg="red", bg="green", command=open_file)
    save_button = tk.Button(root, text="Save Graph", fg="green", bg="black", command=save_file)
    info_button = tk.Button(root, text="?", fg="red", bg="green")

    # Layout
    play_pause_button.grid(row=1, column=1)
    previous_button.grid(row=1, column=2)
    next_button.grid(row=1, column=3)
    stop_button.grid(row=1, column=0)

    value_label.grid(row=2, column=2)
    value_entry.grid(row=2, column=3)
    search_button.grid(row=3, column=2, columnspan=2)
    insert_button.grid(row=4, column=2, columnspan=2)
    delete_button.grid(row=5, column=2, columnspan=2)
    clear_button.grid(row=6, column=2, columnspan=2)

    open_button.grid(row=5, column=0)
    read_button.grid(row=5, column=1)
    info_button.grid(row=6, column=6)
    save_button.grid(row=5, column=2)
    algo_dropdown.grid(row=3, column=0, columnspan=2)

    # Start program
    root.mainloop()
