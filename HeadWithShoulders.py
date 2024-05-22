import importlib
import pydeation.imports
importlib.reload(pydeation.imports)
from pydeation.imports import *

class HeadWithShoulders(USD):

    def __init__(self, **kwargs):
        file_path = "/Users/davidrug/Library/Mobile Documents/iCloud~md~obsidian/Documents/InterBrain/LiminalMind/HeadWithShoulders/HeadWithShoulders.usdz"
        fill_color = BLACK
        outline_only = True
        super().__init__(file_path=file_path, fill_color=fill_color, outline_only=outline_only, **kwargs)