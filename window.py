import treap as tr
import tkinter as tk
import networkx as nx
import log_widget as lw
import pseudocode_widget as pw
import animation_handler as ah
import skip_list as sl
from skip_list_graph import SkipListGraph
from treap_graph import TreapGraph
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import webbrowser


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
def search_command(event=None):
    global algorithm
    global animation_handler
    global graph_list_index
    global log_widget
    global log_message
    global treap
    global log_list

    # Clear the old animations and reset index to zero
    animation_handler.get_instance().skip_list_graph_list.clear()
    animation_handler.get_instance().treap_graph_list.clear()
    animation_handler.get_instance().pseudocode_list.clear()
    animation_handler.get_instance().treap_pseudocode_list.clear()
    graph_list_index = 0
    plot.clear()

    try:
        value = int(value_entry.get())
    except ValueError:
        if len(value_entry.get()) == 0:
            log_widget.push("ValueError: Enter a key to perfom an operation")
            log_message.config(text=log_widget.update())
            return
        else:
            log_widget.push(f"Invalid Key : {value_entry.get()}")
            log_message.config(text=log_widget.update())
            return

    # Handling the log widget:
    log_widget.push(f"search:{value}", log_list)
    log_message.config(text=log_widget.update())

    skip_list.find(value)
    treap.find(value, treap)

    skip_list_start = len(animation_handler.get_instance().skip_list_history[0])
    treap_start = len(animation_handler.get_instance().treap_history[0])

    for element in animation_handler.get_instance().skip_list_graph_list:
        animation_handler.get_instance().skip_list_history[0].append(element)
    for element in animation_handler.get_instance().pseudocode_list:
        animation_handler.get_instance().skip_list_history[1].append(element)

    for element in animation_handler.get_instance().treap_graph_list:
        animation_handler.get_instance().treap_history[0].append(element)
    for element in animation_handler.get_instance().treap_pseudocode_list:
        animation_handler.get_instance().treap_history[1].append(element)

    skip_list_end = len(animation_handler.get_instance().skip_list_history[0]) - 1
    treap_end = len(animation_handler.get_instance().treap_history[0]) - 1

    animation_handler.get_instance().skip_list_time_stamps.append((skip_list_start, skip_list_end))
    animation_handler.get_instance().treap_time_stamps.append((treap_start, treap_end))

    if algorithm.get() == "Skip List":
        update_canvas(animation_handler.get_instance().skip_list_graph_list[graph_list_index])
        pseudocode_obj.update(animation_handler.get_instance().pseudocode_list[graph_list_index][0],
                              animation_handler.get_instance().pseudocode_list[graph_list_index][1])
    elif algorithm.get() == "Treap":
        update_canvas(animation_handler.get_instance().treap_graph_list[graph_list_index])
        pseudocode_obj.update(animation_handler.get_instance().treap_pseudocode_list[graph_list_index][0],  # text
                              animation_handler.get_instance().treap_pseudocode_list[graph_list_index][1])  # color

    value_entry.delete(0, tk.END)

def insert_command(event=None):
    global algorithm
    global animation_handler
    global graph_list_index
    global log_widget
    global log_message
    global log_list
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
    except ValueError:
        if len(value_entry.get()) == 0:
            log_widget.push("ValueError: Enter a key to perfom an operation")
            log_message.config(text=log_widget.update())
            return
        elif value_entry.get() == "jackson":
            webbrowser.open("https://youtu.be/PfrV_6yWbEg?autoplay=1&t=210", new=1)
            return
        else:
            log_widget.push(f"Invalid Key : {value_entry.get()}")
            log_message.config(text=log_widget.update())
            return

    skip_list.insert(value)
    treap.insert(value, treap)

    skip_list_start = len(animation_handler.get_instance().skip_list_history[0])
    treap_start = len(animation_handler.get_instance().treap_history[0])

    for element in animation_handler.get_instance().skip_list_graph_list:
        animation_handler.get_instance().skip_list_history[0].append(element)
    for element in animation_handler.get_instance().pseudocode_list:
        animation_handler.get_instance().skip_list_history[1].append(element)

    for element in animation_handler.get_instance().treap_graph_list:
        animation_handler.get_instance().treap_history[0].append(element)
    for element in animation_handler.get_instance().treap_pseudocode_list:
        animation_handler.get_instance().treap_history[1].append(element)

    skip_list_end = len(animation_handler.get_instance().skip_list_history[0]) - 1
    treap_end = len(animation_handler.get_instance().treap_history[0]) - 1

    animation_handler.get_instance().skip_list_time_stamps.append((skip_list_start, skip_list_end))
    animation_handler.get_instance().treap_time_stamps.append((treap_start, treap_end))

    # Handling the log widget:
    log_widget.push(f"insert:{value}", log_list)
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


def delete_command(event=None):
    global algorithm
    global graph_list_index
    global animation_handler
    global treap
    global log_widget
    global log_message
    global log_list

    animation_handler.get_instance().skip_list_graph_list.clear()
    animation_handler.get_instance().treap_graph_list.clear()
    animation_handler.get_instance().pseudocode_list.clear()
    animation_handler.get_instance().treap_pseudocode_list.clear()

    graph_list_index = 0
    plot.clear()

    try:
        value = int(value_entry.get())
    except ValueError:
        if len(value_entry.get()) == 0:
            log_widget.push("ValueError: Enter a key to perfom an operation")
            log_message.config(text=log_widget.update())
            return
        else:
            log_widget.push(f"Invalid Key : {value_entry.get()}")
            log_message.config(text=log_widget.update())
            return

    skip_list.delete(value)
    treap.delete(value, treap)

    skip_list_start = len(animation_handler.get_instance().skip_list_history[0])
    treap_start = len(animation_handler.get_instance().treap_history[0])

    for element in animation_handler.get_instance().skip_list_graph_list:
        animation_handler.get_instance().skip_list_history[0].append(element)
    for element in animation_handler.get_instance().pseudocode_list:
        animation_handler.get_instance().skip_list_history[1].append(element)

    for element in animation_handler.get_instance().treap_graph_list:
        animation_handler.get_instance().treap_history[0].append(element)
    for element in animation_handler.get_instance().treap_pseudocode_list:
        animation_handler.get_instance().treap_history[1].append(element)

    skip_list_end = len(animation_handler.get_instance().skip_list_history[0]) - 1
    treap_end = len(animation_handler.get_instance().treap_history[0]) - 1

    animation_handler.get_instance().skip_list_time_stamps.append((skip_list_start, skip_list_end))
    animation_handler.get_instance().treap_time_stamps.append((treap_start, treap_end))

    # Handling the log widget:
    log_widget.push(f"delete:{value}", log_list)
    log_message.config(text=log_widget.update())

    if algorithm.get() == "Skip List":
        update_canvas(animation_handler.get_instance().skip_list_graph_list[graph_list_index])
        pseudocode_obj.update(animation_handler.get_instance().pseudocode_list[graph_list_index][0],
                              animation_handler.get_instance().pseudocode_list[graph_list_index][1])
    elif algorithm.get() == "Treap":
        update_canvas(animation_handler.get_instance().treap_graph_list[graph_list_index])
        pseudocode_obj.update(animation_handler.get_instance().treap_pseudocode_list[graph_list_index][0],
                              animation_handler.get_instance().treap_pseudocode_list[graph_list_index][1])
    value_entry.delete(0, tk.END)


def play_pause_command(event=None):
    global active
    global play_pause_button
    if play_pause_button["text"] == "Play":
        play_pause_button.config(text="Pause")
        active = True
        play_command()
    else:
        play_pause_button.config(text="Play")
        active = False


def play_command(event=None):
    global active
    global canvas
    global graph_list_index
    global animation_handler
    global algorithm
    global pseudocode_obj
    global mode
    global speed

    if active is False:
        return

    elif mode == "single_command":
        if algorithm.get() == "Skip List":
            if graph_list_index < len(animation_handler.get_instance().skip_list_graph_list) - 1:
                graph_list_index += 1
                update_canvas(animation_handler.get_instance().skip_list_graph_list[graph_list_index])
                pseudocode_obj.update(animation_handler.get_instance().pseudocode_list[graph_list_index][0],
                                      animation_handler.get_instance().pseudocode_list[graph_list_index][1])
                root.after(1000 - speed, play_command)

            if graph_list_index == len(animation_handler.get_instance().skip_list_graph_list) - 1:
                graph_list_index = 0
                play_pause_command()

        elif algorithm.get() == "Treap":
            if graph_list_index < len(animation_handler.get_instance().treap_graph_list) - 1:
                graph_list_index += 1
                update_canvas(animation_handler.get_instance().treap_graph_list[graph_list_index])
                pseudocode_obj.update(animation_handler.get_instance().treap_pseudocode_list[graph_list_index][0],
                                      animation_handler.get_instance().treap_pseudocode_list[graph_list_index][1])
                root.after(1000 - speed, play_command)
            if graph_list_index == len(animation_handler.get_instance().skip_list_graph_list) - 1:
                graph_list_index = 0
                play_pause_command()

    elif mode == "all_commands":
        if algorithm.get() == "Skip List":
            if graph_list_index < len(animation_handler.get_instance().skip_list_history[0]) - 1:
                graph_list_index += 1
                update_canvas(animation_handler.get_instance().skip_list_history[0][graph_list_index])
                pseudocode_obj.update(animation_handler.get_instance().skip_list_history[1][graph_list_index][0],
                                      animation_handler.get_instance().skip_list_history[1][graph_list_index][1])
                root.after(1000 - speed, play_command)

            if graph_list_index == len(animation_handler.get_instance().skip_list_history[0]) - 1:
                graph_list_index = 0
                play_pause_command()

        elif algorithm.get() == "Treap":
            if graph_list_index < len(animation_handler.get_instance().treap_history[0]) - 1:
                graph_list_index += 1
                update_canvas(animation_handler.get_instance().treap_history[0][graph_list_index])
                pseudocode_obj.update(animation_handler.get_instance().treap_history[1][graph_list_index][0],
                                      animation_handler.get_instance().treap_history[1][graph_list_index][1])
                root.after(1000 - speed, play_command)
            if graph_list_index == len(animation_handler.get_instance().treap_history[0]) - 1:
                graph_list_index = 0
                play_pause_command()



def previous_command(event=None):
    global graph_list_index
    global animation_handler
    global algorithm
    global active
    global play_pause_button
    global command_list_index
    global mode
    play_pause_button.config(text="Play")
    active = False

    if mode == "single_command":
        if algorithm.get() == "Skip List":
            if graph_list_index < len(animation_handler.get_instance().skip_list_graph_list) and graph_list_index > 0:
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

    elif mode == "all_commands":
        if command_list_index > 0:
            command_list_index -= 1
            animation_handler.load_command(command_list_index)
            if algorithm.get() == "Skip List":
                update_canvas(animation_handler.get_instance().skip_list_graph_list[0])

                pseudocode_obj.update(animation_handler.get_instance().pseudocode_list[0][0],
                                      animation_handler.get_instance().pseudocode_list[0][1])
            elif algorithm.get() == "Treap":
                update_canvas(animation_handler.get_instance().treap_graph_list[0])
                pseudocode_obj.update(animation_handler.get_instance().treap_pseudocode_list[0][0],
                                      animation_handler.get_instance().treap_pseudocode_list[0][1])
        else:
            return


def next_command(event=None):
    global graph_list_index
    global animation_handler
    global algorithm
    global active
    global play_pause_button
    global command_list_index
    global mode
    play_pause_button.config(text="Play")
    active = False
    if mode == "single_command":
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
    elif mode == "all_commands":
        if command_list_index < len(animation_handler.get_instance().treap_time_stamps) - 1:
            command_list_index += 1

            animation_handler.load_command(command_list_index)
            if algorithm.get() == "Skip List":
                update_canvas(animation_handler.get_instance().skip_list_graph_list[0])
                pseudocode_obj.update(animation_handler.get_instance().pseudocode_list[0][0],
                                      animation_handler.get_instance().pseudocode_list[0][1])
            elif algorithm.get() == "Treap":
                update_canvas(animation_handler.get_instance().treap_graph_list[0])
                pseudocode_obj.update(animation_handler.get_instance().treap_pseudocode_list[0][0],
                                      animation_handler.get_instance().treap_pseudocode_list[0][1])
        else:
            return


def stop_command(event=None):
    global treap
    global algorithm
    global graph_list_index
    global active
    global play_pause_button
    global mode
    play_pause_button.config(text="Play")
    active = False
    graph_list_index = 0

    if mode == "single_command":
        if algorithm.get() == "Skip List":
            update_canvas(animation_handler.get_instance().skip_list_graph_list[graph_list_index])
            pseudocode_obj.update(animation_handler.get_instance().pseudocode_list[graph_list_index][0],
                                  animation_handler.get_instance().pseudocode_list[graph_list_index][1])
        elif algorithm.get() == "Treap":
            update_canvas(animation_handler.get_instance().treap_graph_list[graph_list_index])
            pseudocode_obj.update(animation_handler.get_instance().treap_pseudocode_list[graph_list_index][0],
                                  animation_handler.get_instance().treap_pseudocode_list[graph_list_index][1])
    elif mode == "all_commands":

        if algorithm.get() == "Skip List":
            update_canvas(animation_handler.get_instance().skip_list_history[0][graph_list_index])
            pseudocode_obj.update(animation_handler.get_instance().skip_list_history[1][graph_list_index][0],
                                  animation_handler.get_instance().skip_list_history[1][graph_list_index][1])
        elif algorithm.get() == "Treap":
            update_canvas(animation_handler.get_instance().treap_history[0][graph_list_index])
            pseudocode_obj.update(animation_handler.get_instance().treap_history[1][graph_list_index][0],
                                  animation_handler.get_instance().treap_history[1][graph_list_index][1])


def clear_command(event=None):
    global graph_list_index
    global animation_handler
    global skip_list_graph
    global treap_graph
    global algorithm
    global treap
    global skip_list
    global active
    global play_pause_button
    global log_list
    global log_widget
    global log_message
    global plot
    global canvas
    play_pause_button.config(text="Play")
    active = False
    graph_list_index = 0

    treap = tr.Treap()
    skip_list = sl.SkipList()

    animation_handler.get_instance().skip_list_graph_list.clear()
    animation_handler.get_instance().treap_graph_list.clear()
    animation_handler.get_instance().pseudocode_list.clear()
    animation_handler.get_instance().treap_pseudocode_list.clear()

    log_widget.clear()
    log_message.config(text=log_widget.update())
    log_list.clear()

    treap_graph = TreapGraph(treap)
    skip_list_graph = SkipListGraph(skip_list)

    animation_handler.get_instance().treap_graph_list.append(treap_graph.create_graph())
    animation_handler.get_instance().skip_list_graph_list.append(skip_list_graph.create_graph(skip_list))

    if algorithm.get() == "Treap":
        # update_canvas(animation_handler.get_instance().treap_graph_list[graph_list_index])
        treap_graph.draw(treap_graph.treap, plot, canvas)

    else:
        update_canvas(animation_handler.get_instance().skip_list_graph_list[graph_list_index])


def switch_algorithm(string, event=None):
    global graph_list_index
    global active
    global play_pause_button
    global animation_handler
    global command_list_index
    global mode
    global canvas
    global plot
    play_pause_button.config(text="Play")
    active = False
    graph_list_index = 0
    if mode == "single_command":
        if string == "Treap":
            try:
                update_canvas(animation_handler.get_instance().treap_graph_list[0])
            except IndexError:
                treap_graph.draw(treap_graph.treap, plot, canvas)
        elif string == "Skip List":
            try:
                update_canvas(animation_handler.get_instance().skip_list_graph_list[0])
            except IndexError:
                skip_list_graph.draw(skip_list_graph.skip_list, plot, canvas)
    elif mode == "all_commands":
        if string == "Treap":
            try:
                update_canvas(animation_handler.get_instance().treap_graph_list[0])
            except IndexError:
                treap_graph.draw(treap_graph.treap, plot, canvas)
        elif string == "Skip List":
            try:
                update_canvas(animation_handler.get_instance().skip_list_graph_list[0])
            except IndexError:
                skip_list_graph.draw(skip_list_graph.skip_list, plot, canvas)


def read_data_command():
    global algorithm
    global animation_handler
    global treap
    global graph_list_index
    global data
    global log_message
    global log_widget
    graph_list_index = 0

    for command, key in data:
        animation_handler.get_instance().skip_list_graph_list.clear()
        animation_handler.get_instance().treap_graph_list.clear()
        animation_handler.get_instance().pseudocode_list.clear()
        animation_handler.get_instance().treap_pseudocode_list.clear()

        if command == "insert":
            if treap.root.key is not None:
                if treap.find_ohne(int(key)):
                    continue
            if skip_list.search(int(key)):
                continue
            skip_list.insert(int(key))
            treap.insert(int(key), treap)
            skip_list_start = len(animation_handler.get_instance().skip_list_history[0])
            treap_start = len(animation_handler.get_instance().treap_history[0])

            for element in animation_handler.get_instance().skip_list_graph_list:
                animation_handler.get_instance().skip_list_history[0].append(element)
            for element in animation_handler.get_instance().pseudocode_list:
                animation_handler.get_instance().skip_list_history[1].append(element)

            for element in animation_handler.get_instance().treap_graph_list:
                animation_handler.get_instance().treap_history[0].append(element)
            for element in animation_handler.get_instance().treap_pseudocode_list:
                animation_handler.get_instance().treap_history[1].append(element)

            skip_list_end = len(animation_handler.get_instance().skip_list_history[0]) - 1
            treap_end = len(animation_handler.get_instance().treap_history[0]) - 1

            animation_handler.get_instance().skip_list_time_stamps.append((skip_list_start, skip_list_end))
            animation_handler.get_instance().treap_time_stamps.append((treap_start, treap_end))
            # Handling the log widget:
            log_widget.push(f"insert:{int(key)}", log_list)
            log_message.config(text=log_widget.update())

            if algorithm.get() == "Skip List":
                update_canvas(animation_handler.get_instance().skip_list_graph_list[graph_list_index])
                pseudocode_obj.update(animation_handler.get_instance().pseudocode_list[graph_list_index][0],
                                      animation_handler.get_instance().pseudocode_list[graph_list_index][1])
            elif algorithm.get() == "Treap":
                update_canvas(animation_handler.get_instance().treap_graph_list[graph_list_index])
                pseudocode_obj.update(animation_handler.get_instance().treap_pseudocode_list[graph_list_index][0],
                                      animation_handler.get_instance().treap_pseudocode_list[graph_list_index][1])
        elif command == "search":
            skip_list.find(int(key))
            treap.find(int(key), treap)
            for element in animation_handler.get_instance().skip_list_graph_list:
                animation_handler.get_instance().skip_list_history[0].append(element)
            for element in animation_handler.get_instance().pseudocode_list:
                animation_handler.get_instance().skip_list_history[1].append(element)

            for element in animation_handler.get_instance().treap_graph_list:
                animation_handler.get_instance().treap_history[0].append(element)
            for element in animation_handler.get_instance().treap_pseudocode_list:
                animation_handler.get_instance().treap_history[1].append(element)

            log_widget.push(f"search:{int(key)}", log_list)
            log_message.config(text=log_widget.update())

            if algorithm.get() == "Skip List":
                update_canvas(animation_handler.get_instance().skip_list_graph_list[graph_list_index])
                pseudocode_obj.update(animation_handler.get_instance().pseudocode_list[graph_list_index][0],
                                      animation_handler.get_instance().pseudocode_list[graph_list_index][1])
            elif algorithm.get() == "Treap":
                update_canvas(animation_handler.get_instance().treap_graph_list[graph_list_index])
                pseudocode_obj.update(animation_handler.get_instance().treap_pseudocode_list[graph_list_index][0],
                                      animation_handler.get_instance().treap_pseudocode_list[graph_list_index][1])
        elif command == "delete":
            skip_list.delete(int(key))
            treap.delete(int(key), treap)
            skip_list_start = len(animation_handler.get_instance().skip_list_history[0])
            treap_start = len(animation_handler.get_instance().treap_history[0])

            for element in animation_handler.get_instance().skip_list_graph_list:
                animation_handler.get_instance().skip_list_history[0].append(element)
            for element in animation_handler.get_instance().pseudocode_list:
                animation_handler.get_instance().skip_list_history[1].append(element)

            for element in animation_handler.get_instance().treap_graph_list:
                animation_handler.get_instance().treap_history[0].append(element)
            for element in animation_handler.get_instance().treap_pseudocode_list:
                animation_handler.get_instance().treap_history[1].append(element)

            skip_list_end = len(animation_handler.get_instance().skip_list_history[0]) - 1
            treap_end = len(animation_handler.get_instance().treap_history[0]) - 1

            animation_handler.get_instance().skip_list_time_stamps.append((skip_list_start, skip_list_end))
            animation_handler.get_instance().treap_time_stamps.append((treap_start, treap_end))
            log_widget.push(f"delete:{int(key)}", log_list)
            log_message.config(text=log_widget.update())

            if algorithm.get() == "Skip List":
                update_canvas(animation_handler.get_instance().skip_list_graph_list[graph_list_index])
                pseudocode_obj.update(animation_handler.get_instance().pseudocode_list[graph_list_index][0],
                                      animation_handler.get_instance().pseudocode_list[graph_list_index][1])
            elif algorithm.get() == "Treap":
                update_canvas(animation_handler.get_instance().treap_graph_list[graph_list_index])
                pseudocode_obj.update(animation_handler.get_instance().treap_pseudocode_list[graph_list_index][0],
                                      animation_handler.get_instance().treap_pseudocode_list[graph_list_index][1])


def open_file():
    global active
    global play_pause_button
    play_pause_button.config(text="Play")
    active = False
    global data
    token = False

    file = tk.filedialog.askopenfile(mode='r', title="Open file", filetypes=[('Text Files', '*.txt')])
    # check if file was opend successfully
    if file:
        # set Label with filename only if open was successful
        filename_label.config(text=file.name.split("/")[-1])
        data = []
        # append each line to DATA list, where they are stored
        for line in file:
            command = line.rstrip().split(":")
            tmp = (command[0], command[1])  # command[0] ="insert", command[1]="3"
            if tmp in data:
                continue
            else:
                data.append(tmp)
        read_data_command()


def save_graph():
    global active
    global play_pause_button
    global filename
    global fig

    play_pause_button.config(text="Play")
    active = False
    filename = ""
    filename = tk.filedialog.asksaveasfilename(title="Save File",
                                               filetypes=[("png files", "*.png"), ("jpeg files", "*.jpeg")])
    if filename:
        fig.savefig(filename)


def save_graph():
    global active
    global play_pause_button
    global filename
    global fig

    play_pause_button.config(text="Play")
    active = False
    filename = ""
    filename = tk.filedialog.asksaveasfilename(title="Save File",
                                               filetypes=[("png files", "*.png"), ("jpeg files", "*.jpeg")])
    if filename:
        fig.savefig(filename)


def callor(event):
    insert_command()


def placeholder(event):
    value_entry.delete(0, tk.END)


def github():
    webbrowser.open("https://github.com/timokilb/projektgruppe", new=1)


def donate():
    global algorithm
    if algorithm.get() == "Skip List":
        webbrowser.open("https://www.paypal.me/timokilb", new=1)
    else:
        webbrowser.open("https://www.paypal.me/denizdogan94", new=1)


def instagram():
    webbrowser.open("https://www.instagram.com/resbalar.sb/?hl=de", new=1)


def how_it_works(event=None):
    how_it_works_window = tk.Toplevel()
    how_it_works_window.title("How it works")
    how_it_works_window.minsize(300, 300)
    how_it_works_window.config(padx=20, pady=20, bg=background_color)
    how_it_works_window.resizable(height=False, width=False)
    how_it_works_frame = tk.Frame(how_it_works_window, **style_sheet["how_it_works_frame"])
    how_it_works_frame.pack(side="top", anchor="nw", fill="both", expand=1)
    explanation_text = open("./res/howto.txt", "r").read()
    explanation_message = tk.Message(master=how_it_works_frame, text=explanation_text, **style_sheet["how_it_works"])
    explanation_message.pack(anchor="nw")


def check_decision():
    global filename
    global save_decision_list
    if "save_all" and True in save_decision_list[2]:
        save_graph()
        save_log()
        filename = ""
        return
    elif "save_graph" and True in save_decision_list[0]:
        save_graph()
        filename = ""
    elif "save_log" and True in save_decision_list[1]:
        save_log()
        filename = ""


def get_frame():
    global pseudocode_frame
    return pseudocode_frame


def save_log():
    global log_list
    global filename
    if filename == "":
        filename = tk.filedialog.asksaveasfilename(title="Save File",
                                                   filetypes=[("txt files", "*.txt")])
    tmp = open(filename + ".txt", mode="w")

    if tmp:
        for line in log_list:
            tmp.write(line + "\n")
    tmp.close()


def open_save():
    def save_decision():
        global save_decision_list
        save_decision_list.clear()
        save_decision_list.append(("save_graph", save_graph.get()))
        save_decision_list.append(("save_log", save_log.get()))
        save_decision_list.append(("save_all", (save_graph.get() and save_log.get() or (save_all.get()))))
        check_decision()
        choose_save_window.destroy()

    choose_save_window = tk.Toplevel()
    choose_save_window.title("Save")
    choose_save_window.minsize(300, 136)
    choose_save_window.resizable(width=False, height=False)
    choose_save_window.config(padx=10, pady=30, bg=background_color)

    save_graph = tk.BooleanVar()
    tk.Checkbutton(choose_save_window, text="Save Graph", variable=save_graph, **style_sheet["save_window_check"]).pack(
        side="top", anchor="w")
    save_log = tk.BooleanVar()
    tk.Checkbutton(choose_save_window, text="Save Logs", variable=save_log, **style_sheet["save_window_check"]).pack(
        side="top", anchor="w")

    save_all = tk.BooleanVar()
    tk.Checkbutton(choose_save_window, text="Save Graph and Logs", variable=save_all,
                   **style_sheet["save_window_check"]).pack(side="top", anchor="w")

    tk.Button(choose_save_window, text='Save', command=save_decision, **style_sheet["save_window_button"], ).pack(
        side="left", anchor="nw", fill="x", expand=1,
        padx=2, pady=6)
    tk.Button(choose_save_window, text='Cancel', command=choose_save_window.destroy,
              **style_sheet["save_window_button"], ).pack(side="left", anchor="nw",
                                                          fill="x", expand=1, padx=2,
                                                          pady=6)


def set_mode(param):
    global graph_list_index
    global algorithm
    global mode
    global log_widget
    global log_message
    if algorithm.get() == "Skip List":
        if graph_list_index > len(animation_handler.get_instance().skip_list_graph_list) - 1:
            graph_list_index = 0
    elif algorithm.get() == "Treap":
        if graph_list_index > len(animation_handler.get_instance().treap_graph_list) - 1:
            graph_list_index = 0
    mode = param
    if mode == "single_command":
        log_widget.push(f"Mode: Single Command")
        log_message.config(text=log_widget.update())
    else:
        log_widget.push(f"Mode:All Commands")
        log_message.config(text=log_widget.update())


def faster_command(event=None):
    global speed
    if speed < 800:
        speed += 150


def slower_command(event=None):
    global speed
    if speed > 0:
        speed -= 150


style_sheet = {
    "animation_button": {
        "fg": "#a9b7c6",
        "bg": "#313335",
        "activeforeground": "#313335",
        "activebackground": "#a9b7c6",
        "font": "Helvetica, 12",
        "relief": "raised",
        "bd": "2",
        "width": "10",
        "height": "2"
    },
    "save_window_button": {
        "fg": "#a9b7c6",
        "bg": "#313335",
        "activeforeground": "#313335",
        "activebackground": "#a9b7c6",
        "font": "Helvetica, 12",
        "relief": "raised",
        "bd": "2",
        "width": "5",
        "height": "1"
    },
    "save_window_check": {
        "fg": "#87929e",
        "bg": "#3c3f41",
        "font": "Helvetica, 12",
        "height": "1"
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
        "bg": "#2b2b2b",
        "width": "500"
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
    },
    "wind": {
        "fg": "#a9b7c6",
        "bg": "#313335",
        "activeforeground": "#313335",
        "activebackground": "#a9b7c6",
        "font": "Helvetica, 16",
        "relief": "raised",
        "bd": "1",
        "width": "5",
        "height": "0",
        "padx": "0"
    },
    "how_it_works": {
        "fg": "#3a3a3a",
        "font": "Helvetica, 16",
        "width": "800"
    },
    "how_it_works_frame": {
        "bd": "2",
        "relief": "sunken",
    }
}

if __name__ == "__main__":
    # Init data structures and graphs
    graph_list_index = 0
    command_list_index = 0

    treap = tr.Treap()
    treap_graph = TreapGraph(treap)

    # Array for all numbers from Input txt
    data = []
    # Save Decision List
    save_decision_list = []
    # Save all logs
    log_list = []
    # FileName
    filename = ""
    # Background Color
    background_color = "#3c3f41"

    # Figure and plot
    fig = Figure(figsize=(1, 4), dpi=100)
    plot = fig.add_subplot(111)  # 1 by 1 grid subplot No. 1

    # Main window
    root = tk.Tk()
    root.title("Projektgruppe")
    menubar = tk.Menu(root)
    root.config(background=background_color, menu=menubar)
    root.minsize(850, 850)

    social_menu = tk.Menu(menubar)
    mode_menu = tk.Menu(menubar)
    help_menu = tk.Menu(menubar)
    menubar.add_cascade(label="Social", menu=social_menu)
    menubar.add_cascade(label="Mode", menu=mode_menu)
    menubar.add_cascade(label="Help", menu=help_menu)
    social_menu.add_command(label="Git", command=github)
    social_menu.add_command(label="Donate", command=donate)
    social_menu.add_command(label="IG", command=instagram)
    mode_menu.add_command(label="Single Command", command=lambda: set_mode("single_command"))
    mode_menu.add_command(label="All Commands", command=lambda: set_mode("all_commands"))
    help_menu.add_command(label="How it works", command=how_it_works)

    # Toggles
    active = False
    # toogle for way of displaying default:single_command
    mode = "single_command"
    # Animation Speed
    speed = 200
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

    slower_button = tk.Button(master=key_structure_frame, text=u"\u23EA", **style_sheet["wind"], command=slower_command)
    faster_button = tk.Button(master=key_structure_frame, text=u"\u23E9", **style_sheet["wind"], command=faster_command)
    root.bind('+', faster_command)
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

    save_button = tk.Button(master=graph_structure_frame, text="Save ..", **style_sheet["data_structure_button"],
                            command=open_save)

    clear_button = tk.Button(master=graph_structure_frame, text="Clear Graph", **style_sheet["data_structure_button"],
                             command=clear_command)

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

    # Packing all buttons
    stop_button.pack(side="left", fill="x", padx="2", pady="2")

    previous_button.pack(side="left", fill="x", padx="2", pady="2")
    play_pause_button.pack(side="left", fill="x", padx="2", pady="2")
    next_button.pack(side="left", fill="x", padx="2", pady="2")

    value_label.pack(side="left", fill="x", padx="2", pady="2")
    value_entry.pack(side="left", fill="x", padx="2", pady="2", expand=1)
    faster_button.pack(side="right", padx="2")
    slower_button.pack(side="right", padx="2")

    insert_button.pack(side="left", fill="x", padx="2", pady="2", expand=1)
    delete_button.pack(side="left", fill="x", padx="2", pady="2", expand=1)
    search_button.pack(side="left", fill="x", padx="2", pady="2", expand=1)

    open_button.pack(side="left", fill="x", padx="2", pady="2", expand=1)
    filename_label.pack(side="left", fill="x", padx="2", pady="0", expand=1)

    algo_dropdown.pack(side="left", fill="x", padx="2", pady="2", expand=1)
    save_button.pack(side="left", fill="x", padx="2", pady="2", expand=1)
    clear_button.pack(side="left", fill="x", padx="2", pady="2", expand=1)

    # Binding keyshortcuts
    value_entry.bind("<Button>", placeholder)
    root.bind('<Return>', insert_command)
    # Start program
    root.mainloop()
