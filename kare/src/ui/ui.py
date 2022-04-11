from services.kare_service import KareService


class UI():
    def __init__(self):
        self.kare_service = KareService()

    def start(self):
        self.print_hello()
        self.loop()

    def print_hello(self):
        print("\nHello!\nThis is Kare, soundfile processing using wavelet manipulation\nType \"help\" for help\n")

    def print_help(self):
        list = [
            "help\t\t\t\tprints this screen",
            "exit\t\t\t\texits this program",
            "setdir path\t\t\tsets the path for load/save directory ----- (todo)",
            "import filename\t\t\timports given file to the system",
            "export filename savename\texports the given file with a given name (give filename without extension)",
            "process filename\t\tprocess the given soundfile (give filename without extension) ----- (todo)",
            "list\t\t\t\tlists all uploaded files"
        ]

        print("List of commands:\n")
        [print(line) for line in list]
        print()

    def listfiles(self):
        files = self.kare_service.get_sound_object_names()
        if len(files) == 0:
            print("No saved soundfiles\n")
        else:
            print("List of saved soundfiles:\n")
            [print(file) for file in files]
            print()

    def loop(self):
        while(True):
            functions = {
                "setdir": None,
                "import": self.kare_service.import_soundfile,
                "process": None,
                "export": self.kare_service.export_soundfile
            }

            user_in = input("command: ").split()

            if len(user_in) == 0 or user_in[0] == "help":
                self.print_help()
                continue

            if user_in[0] == "exit":
                break

            if user_in[0] == "list":
                self.listfiles()
                continue

            if user_in[0] not in functions.keys():
                print(
                    f"\"{user_in[0]}\" is not a command (type \"help\" for help)")
                continue

            if len(user_in) < 2:
                print("missing arguments (type \"help\" for help)")
                continue

            functions[user_in[0]](user_in[1:])
