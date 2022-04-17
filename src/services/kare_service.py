from entities.sound_object import SoundObject

import soundfile as sf


class KareService:
    def __init__(self):
        self.sound_objects = {}
        self.import_export_path = None

    def get_sound_object_names(self):
        return list(self.sound_objects.keys())

    def import_soundfile(self, filename, path=""):

        data, samplerate = sf.read(path+filename)
        path_filename = filename.rsplit(".", 1)[0]
        if "/" in path_filename:
            path, filename = path_filename.rsplit("/", 1)
        else:
            filename = path_filename

        self.sound_objects[filename] = SoundObject(data, samplerate)

    def export_soundfile(self, filename, savename):

        export_data = self.sound_objects[filename].data
        export_samplerate = self.sound_objects[filename].samplerate
        try:
            sf.write(savename, export_data, export_samplerate)
        except:
            raise RuntimeError(
                f"Something went wrong when exporting {filename} as {savename}")
