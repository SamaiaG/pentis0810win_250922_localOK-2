# runtime_hook_paths.py
# PyInstaller runtime hook — place in your project root
# This ensures os.chdir() in inoutput.py points to the bundled resources

import sys
import os

if getattr(sys, 'frozen', False):
    # When running as .app, set working dir to the bundle's resource folder
    os.chdir(sys._MEIPASS)
