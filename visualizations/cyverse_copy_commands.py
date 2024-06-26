from data_loader import *
import subprocess

class CyverseFileCopier:
    def __init__(self):
        self.data_loader = DataLoader()
    
    # copies file from a cyverse path to your local data dir 
    def copy_cyverse_file_to_personal(self, fp):
        out = subprocess.run(["gocmd", "cp", fp, "."])    
        return out

    # copies file from a cyverse path to our repo data dir
    def copy_cyverse_file_to_group(self, fp):
        dest = "/Innovation-Summit-2024_1_Climate-extremes-and-natural-disasters/data"
        out = subprocess.run(["gocmd", "cp", fp, dest])    
        return out 