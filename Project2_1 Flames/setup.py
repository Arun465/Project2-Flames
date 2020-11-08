import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"],"include_files":["code (1).ico","man2.jpg","p1.jpg","p2.jpg","p3.jpg","p4.jpg","p5.jpg","p6.jpg"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

target=Executable(script="Flames --Pyqt Gui.py",base=base,icon="code (1).ico")

setup(  name = "Flames --Pyqt-Gui",
        version = "0.1",
        description = "FLAMES   JUST for  FUN !!!!",
        options = {"build_exe": build_exe_options},
        executables=[target])
        # executables = [Executable("arun2v33.py", base=base)])