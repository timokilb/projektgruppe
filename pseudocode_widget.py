# Creating a Log Widget using singleton pattern
# Returns a series of strings where as the last inserted string appears on top

# How to use:
# use import LogWidget as lw
#   log_widget = LogWidget()
#   from where you want to write messages to the widget, use
#       log_widget.push("String")
#   to get the whole text, use log_widget.update()

import tkinter as tk


class PseudocodeWidget:
    class __PseudocodeWidget:

        def __init__(self, master):
            self.labels = [tk.Label(master=master), tk.Label(master=master), tk.Label(master=master),
                           tk.Label(master=master)
                , tk.Label(master=master), tk.Label(master=master), tk.Label(master=master), tk.Label(master=master)
                , tk.Label(master=master), tk.Label(master=master)]

            self.pseudocode_list = []

    __instance = None

    def __init__(self, master):
        if not PseudocodeWidget.__instance:  # There is no instance
            PseudocodeWidget.__instance = PseudocodeWidget.__PseudocodeWidget(master)

    def get_instance(self):
        return self.__instance

    # open File wich contains pseudocode
    def open_text_file(self, string):
        # restore default values for all labels
        for entry in PseudocodeWidget.__instance.labels:
            entry.config(text="", bg="white")

        file = open(string, mode="r")
        position = 0
        for line in file:
            PseudocodeWidget.__instance.labels[position].config(text=line, height=1, bg="#eeeeee", fg="red" )#bg="#3c3f41", fg="#a9b7c6"
            position += 1
        PseudocodeWidget.__instance.pseudocode_list.append(PseudocodeWidget.__instance.labels)

    # returns label element at given index
    def get_label(self, position ):
        return self.get_instance().labels[position]

    # returns Array/List with all labels
    def get_all_labels(self):
        all_label = []
        for element in self.get_instance().labels:
            all_label.append(element)
        return all_label

    def update_display(self):
        pass

    def update(self):
        return "\n".join(self.__instance.lines)

    def pack_labels(self):
        for element in self.get_instance().labels:
            element.pack()
