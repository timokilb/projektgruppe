
# Creating a Log Widget using singleton pattern

class LogWidget:

    class __LogWidget:

        def __init__(self):
            self.lines = []

    __instance = None

    def __init__(self):
        if not LogWidget.__instance: # There is no instance
            LogWidget.__instance = LogWidget.__LogWidget()

    def push(self, string):
        if type(string) is not type("string"):
            print("ERR: Argument is type of", type(string), "but needs to be", type("string"))
            return
        if len(len(self.__instance.lines) > 5):
            self.__instance.list.pop()
            self.__instance.list.insert(0, string)
        else:
            self.__instance.lines.insert(0, string)

    def to_string(self):
        return "\n".join(self.__instance.list)

