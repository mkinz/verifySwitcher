import os
import glob

class Deleter:

    def remove_stuff(self, pattern):
        for files_to_remove in glob.glob(pattern):
            os.remove(files_to_remove)

