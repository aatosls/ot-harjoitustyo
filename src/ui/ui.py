from services.kare_service import KareService


class UI():
    def __init__(self):
        self.kare_service = KareService()


    def print_hello(self):
        print("\nHello!\nThis is Kare, soundfile processing using wavelet manipulation\nType \"help\" for help\n")

    def print_help(self,_):
        list = [
            "help\t\t\t\tprints this screen",
            "exit\t\t\t\texits this program",
            "setdir \"path\"\t\t\tsets the path for load/save directory ----- (todo)",
            "import \"filename\"\t\timports given file to the system",
            "export \"filename\" 'savename'\texports the given file with a given name (give filename without extension)",
            "process \"filename\"\t\tprocess the given soundfile (give filename without extension) ----- (todo)",
            "list\t\t\t\tlists all uploaded files"
        ]

        print("List of commands:\n")
        [print(line) for line in list]
        print()

    def listfiles(self,_):
        files = self.kare_service.get_sound_object_names()
        if len(files) == 0:
            print("No saved soundfiles\n")
        else:
            print("List of saved soundfiles:\n")
            [print(file) for file in files]
            print()

    def ask_overwrite_rename(self):
        user_in = input("name is already in use, overwrite or rename [o/r] (leave empty to abort): ")
        while(True):
            if user_in == "o":
                return 1
            if user_in == "r":
                return 2
            if user_in == "":
                return 0
            user_in = input("what?: ")

    def ask_filename(self):
        while(True):
            name = input("new name: ")
            if name in self.kare_service.get_sound_object_names():
                print("name already in use")
                continue
            if len(name) < 1:
                print("name is too short")
                continue
            return name

    def do_import(self,args):
        filename = args[0]
        used_names = self.kare_service.get_sound_object_names()

        print(filename)
        
        if filename in used_names:
            ret = self.ask_overwrite_rename()
            if ret == 0: # abort
                return
            if ret == 2: # rename
                filename = self.ask_filename()

        self.kare_service.import_soundfile(filename)

    def parse(self,text):
        text = list(text)
        in_quotes = False
        for i in range(len(text)):
            if text[i] == '"':
                in_quotes = True if in_quotes == False else False
            if text[i] == " " and not in_quotes:
                text[i] = "#"
        text = "".join(text)
        text = text.replace('"','')
        text = text.split("#")
        return text

    def start(self):
        self.print_hello()
        self.loop()

    def loop(self):
        while(True):
            functions = {
                "setdir": None,
                "import": self.do_import,
                "process": None,
                "export": self.kare_service.export_soundfile,
                "help": self.print_help,
                "list": self.listfiles
            }

            user_in = input("command: ")
            in_args = self.parse(user_in)

            if len(user_in) == 0:
                self.print_help(0)
                continue

            if in_args[0] == "exit":
                break

            if in_args[0] not in functions.keys():
                print(
                    f"\"{in_args[0]}\" is not a command (type \"help\" for help)")
                continue

            ret = functions[in_args[0]](in_args[1:])

            if ret == 1:
                print("missing arguments (type \"help\" for help)")
                continue
