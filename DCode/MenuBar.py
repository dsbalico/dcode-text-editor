import tkinter as tk
from tkinter.filedialog import *
from DCode.About import About
from DCode.FontSettings import FontSettings
from DCode.Settings import Settings

class MenuBar(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		self.parent = parent
		self.textarea = args[0]
		menu = tk.Menu(self.parent)

		# File Menu
		filemenu = tk.Menu(menu, tearoff=0)
		filemenu.add_command(label="New File", command=self.newFile, accelerator="Ctrl + N")
		filemenu.add_command(label="Open File", command=self.openFile, accelerator="Ctrl + O")
		filemenu.add_command(label="Save", command=self.saveFile, accelerator="Ctrl + S")
		filemenu.add_command(label="Save as", command=self.saveAs, accelerator="Ctrl + Shift + S")
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=self.parent.destroy)
		menu.add_cascade(label="File", menu=filemenu)

		# Edit Menu
		editmenu = tk.Menu(menu, tearoff=0)
		editmenu.add_command(label="Undo", accelerator="Ctrl + Z", command=lambda: self.parent.focus_get().event_generate('<<Undo>>'))
		editmenu.add_command(label="Redo", accelerator="Ctrl + Y", command=lambda: self.parent.focus_get().event_generate('<<Redo>>'))
		editmenu.add_separator()
		editmenu.add_command(label="Cut", accelerator="Ctrl + X", command=lambda: self.parent.focus_get().event_generate('<<Cut>>'))
		editmenu.add_command(label="Copy", accelerator="Ctrl + C", command=lambda: self.parent.focus_get().event_generate('<<Copy>>'))
		editmenu.add_command(label="Paste", accelerator="Ctrl + V", command=lambda: self.parent.focus_get().event_generate('<<Paste>>'))
		menu.add_cascade(label="Edit", menu=editmenu)

		# Preferences Menu
		prefmenu = tk.Menu(menu, tearoff=0)
		prefmenu.add_command(label="Settings", command=self.showSettings)
		prefmenu.add_command(label="Font", command=self.showFontSettings)
		menu.add_cascade(label="Preferences", menu=prefmenu)

		# Help Menu
		helpmenu = tk.Menu(menu, tearoff=0)
		helpmenu.add_command(label="About", command=self.showAbout)
		menu.add_cascade(label="Help", menu=helpmenu)

		# Show the menubar
		self.parent.config(menu=menu)

		# Shortcut Keys
		self.parent.bind("<Control-n>", self.newFile)
		self.parent.bind("<Control-Shift-S>", self.saveAs)
		self.parent.bind("<Control-s>", self.saveFile)
		self.parent.bind("<Control-o>", self.openFile)

	def newFile(self, *args, **kwargs):
		self.main.filename = None
		self.parent.title(f"DCode - { self.main.filename }")
		self.textarea.delete(0.0, END)

	def saveAs(self, *args, **kwargs):
		file = asksaveasfile(mode='w', defaultextension='.txt')
		content = self.textarea.get(0.0, END)

		if file:
			file.write(content.rstrip())
			self.main.isChanged = False
			self.parent.title(f"DCode - { self.main.filename }")

	def openFile(self, *args, **kwargs):
		file = askopenfile(mode='r')
		if file:
			self.parent.title(f"DCode - {file.name}")
			self.parent.filename = file.name
			content = file.read()
			self.textarea.delete(0.0, END)
			self.textarea.insert(0.0, content)

	def saveFile(self, *args, **kwargs):
		try:
			content = self.textarea.get(0.0, END)
			file = open(self.main.filename, 'w')
			file.write(content)
			file.close()
			self.main.isChanged = False
			self.parent.title(f"DCode - { self.main.filename }")
		except:
			self.saveAs()

	def showAbout(self, *args, **kwargs):
		about = About(self.parent)

	def showFontSettings(self, *args, **kwargs):
		font_settings = FontSettings(self.parent)

	def showSettings(self, *args, **kwargs):
		settings = Settings(self.parent)
