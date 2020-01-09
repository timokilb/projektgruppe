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
            self.labels = [tk.Label(master=master)] * 10
            self.pseudocode_list = []

    __instance = None

    def __init__(self, master):
        if not PseudocodeWidget.__instance:  # There is no instance
            PseudocodeWidget.__instance = PseudocodeWidget.__PseudocodeWidget(master)

    def get_instance(self):
        return self.__instance

    def get_label(self, index):
        return PseudocodeWidget.__instance.labels[index]

    def get_labels(self):
        for index in range(len(PseudocodeWidget.__instance.labels)):
            print(PseudocodeWidget.get_label(index))

    def set_labels(self, array):
        PseudocodeWidget.__instance.labels = array

    def open_text_file(self, string, row):
        for entry in PseudocodeWidget.__instance.labels:
            entry.config(text="", bg="white")

        file = open(string, mode="r")
        index = 0
        for line in file:
            PseudocodeWidget.__instance.labels[index].config(text=line)
            if index == (row - 1):
                PseudocodeWidget.__instance.labels[index].config(bg="red")
            index += 1

        PseudocodeWidget.__instance.pseudocode_list.append(PseudocodeWidget.__instance.labels)

    def update_display(self):
        pass

    def update(self):
        return "\n".join(self.__instance.lines)


if __name__ == "__main__":
    root = tk.Tk()
    widget = PseudocodeWidget(root)
    widget.open_text_file("./res/treap_insert.txt", 0)
    # print(widget.get_instance().pseudocode_list)
    for element in PseudocodeWidget.pseudocode_list:
        for index in range(len(element)):
            print(element[index]["text"])
