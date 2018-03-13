from cx_Freeze import setup, Executable

base = None

executables = [Executable("main.py", base=base)]

packages = ["idna", "numpy"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "Queen's",
    options = options,
    version = "1.0.0",
    description = 'blah blah blah',
    executables = executables
)
