from entities.sound_object import SoundObject

import soundfile as sf

class KareService:
    def __init__(self):
        self.sound_objects = {}
        self.import_export_path = None

    def get_sound_object_names(self):
        return list(self.sound_objects.keys())

    def import_soundfile(self, args):
        filename = args[0]
        
        data, samplerate = sf.read(filename)

        path_filename = filename.rsplit(".", 1)[0]
        if "/" in path_filename:
            path, filename = path_filename.rsplit("/", 1)
        else:
            filename = path_filename

        """ 
        Tee myöhemmin..
        if filename[0] in self.sound_objects.keys():
            self.ui...
        """ 

        self.sound_objects[filename] = SoundObject(data, samplerate)

    def export_soundfile(self, args):
        filename, savename = args
        if not isinstance(filename, str) or not isinstance(savename, str):
            raise ValueError("\"filename\" and \"savename\" must be string objects")

        export_data = self.sound_objects[filename].data
        export_samplerate = self.sound_objects[filename].samplerate
        try:
            sf.write(savename, export_data, export_samplerate)
        except:
            raise RuntimeError(f"Something went wrong when exporting {filename} as {savename}")