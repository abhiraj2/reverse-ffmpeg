from cx_Freeze import setup, Executable

base = None    

executables = [Executable("reverse-ffmpeg.py", base=base)]

packages = ["idna", "os", "sys"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "revrse-video",
    options = options,
    version = "0.1",
    description = 'Program to reverse video using FFMPEG',
    executables = executables
)