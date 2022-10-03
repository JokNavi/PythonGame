from distutils.core import setup
import py2exe
setup(console=['Program.py'])
excludes = ["pywin", "pywin.debugger", "pywin.debugger.dbgcon","pywin.dialogs", "pywin.dialogs.list", "Tkconstants","Tkinter","tcl", "_imagingtk", "PIL._imagingtk", "ImageTk", "PIL.ImageTk", "FixTk", "numpy", "scipy"]