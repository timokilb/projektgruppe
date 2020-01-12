
# Creating a Log Widget using singleton pattern
# Returns a series of strings where as the last inserted string appears on top

# How to use:
# use import LogWidget as lw
#   log_widget = LogWidget()
#   from where you want to write messages to the widget, use
#       log_widget.push("String")
#   to get the whole text, use log_widget.update()


class LogWidget:

    class __LogWidget:

        def __init__(self):
            self.lines = ["_",
                          "/\  / o o \ ",
                          "//\\ \~(*)~/ ",
                          "`  \/   ^ /",
                          "   | \|| ||  ",
                          "   \ '|| ||  ",
                          "    \)()-())"]
    __instance = None

    def __init__(self):
        if not LogWidget.__instance: # There is no instance
            LogWidget.__instance = LogWidget.__LogWidget()

    def push(self, string):
        if type(string) is not type("string"):
            print("ERR: Argument is type of", type(string), "but needs to be", type("string"))
            return
        if len(self.__instance.lines) > 6:
            self.__instance.lines.pop()
            self.__instance.lines.insert(0, string)
        else:
            self.__instance.lines.insert(0, string)

    def update(self):
        return "\n".join(self.__instance.lines)
