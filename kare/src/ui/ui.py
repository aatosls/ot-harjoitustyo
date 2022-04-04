class UI():
    def __init__(self):
        pass

    def start(self):
        self.print_hello()
        self.loop()

    def print_hello(self):
        print("\nHello!\nThis is Kare, soundfile processing using wavelet manipulation\nType \"help\" for help\n")

    def print_help(self):
        list = [
            "help\t\t\t\tprints this screen",
            "exit\t\t\t\texits this program",
            "upload filename\t\t\tuploads given file to the system",
            "process filename\t\tprocess the given soundfile (give filename without extension)",
            "get filename savename\t\tsaves the given file with a given name (give filename without extension)"
        ]

        print("List of commands:\n")
        [print(line) for line in list]
        print()

    def loop(self):
        while(True):
            functions = {
                "upload": None,
                "process": None,
                "get": None}

            user_in = input("command: ").split()

            if len(user_in) == 0 or user_in[0] == "help":
                self.print_help()
                continue

            if user_in[0] == "exit":
                break

            if user_in[0] not in functions.keys():
                print(f"\"{user_in[0]}\" is not a command (type \"help\" for help)")

            functions[user_in[0]](user_in[1:])
