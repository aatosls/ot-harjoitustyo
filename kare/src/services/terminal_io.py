class TerminalIO:
    def __init__(self):
        pass

    def print_str(self, string, tab):
        if tab:
            print("\t", end="")
        print(string)

    def print_list(self, list, tab):
        [self.print_str(x, tab) for x in list]

    def print(self, args, tab=True):
        if isinstance(args, str):
            self.print_str(args, tab)
        elif isinstance(args, list):
            self.print_list(args, tab)
        else:
            raise ValueError("\"TerminalIO.print\" only takes str or list as an input")