import tkinter as tk
from DCode.MenuBar import MenuBar
from DCode.LineNumbersField import TextLineNumbers, CustomText
import tkinter.font as tkfont
import os.path
import json

__author__ = "Daniel Shan Balico"
__version__ = "1.0"
__email__ = "danielshan.balico@gmail.com"

class MainApplication(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.parent.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='icon.png'))
		self.filename = None
		if os.path.exists("config.json"):
			with open("config.json", 'r') as f: 
				self.config = json.loads(f.read())
		else:
			default = {"fontFamily": "Helvetica",
						"fontSize": 11,
						"fontWeight": "normal",
						"colors": ["#cc362b", "#2bcc73", "#2b9ccc"]}

			with open("config.json", "w") as f:
				json.dump(default, f)

			with open("config.json", "r") as data:
				self.config = json.loads(data.read())



		# Window Settings
		self.parent.geometry("800x600")
		self.parent.title(f"DCode - { self.filename }")
 
		self.parent.bind("<FocusIn>", self.checkModified)

		# Text Area with Line Numbers
		self.textarea = CustomText(self, 
			bg="#2b2b2b", fg="#fff", 
			insertbackground="#fff", 
			selectbackground="#3d424a", undo=True,
			borderwidth=0)

		# ScrollBar
		self.vsb = tk.Scrollbar(orient="vertical", command=self.textarea.yview)
		
		# For Identation
		font = tkfont.Font(font=self.textarea['font'])
		tab_width = font.measure(" " * 4)
		self.textarea.configure(yscrollcommand=self.vsb.set, tabs=tab_width, font=(self.config["fontFamily"], self.config["fontSize"], self.config["fontWeight"]))

		# Line Numbers 
		self.linenumbers = TextLineNumbers(self, width=20, bg="#262626", highlightthickness=0, relief='ridge')
		self.linenumbers.attach(self.textarea)

		# Packs
		self.vsb.pack(side="right", fill="y")
		self.linenumbers.pack(side="left", fill="y")
		self.textarea.pack(side="right", fill="both", expand=True)
		self.textarea.bind("<<Change>>", self._on_change)
		self.textarea.bind("<Configure>", self._on_change)

		# MenuBar
		self.menubar = MenuBar(self.parent, self.textarea)

		# For Syntax HighLighting
		self.updater()

	def checkModified(self, event):
		# If user presses any key then the file is modified
		self.parent.bind("<Key>", self.textModified)

	def _on_change(self, event):
		self.linenumbers.redraw()

	def textModified(self, event):
		self.parent.title(f"DCode - { self.filename }*")

	def updater(self):
		# Text Highlighting 
		self.textarea.tag_configure("red", foreground=self.config["colors"][0])
		self.textarea.tag_configure("redend", foreground=self.config["colors"][0])
		self.textarea.tag_configure("green", foreground=self.config["colors"][1])
		self.textarea.tag_configure("blue", foreground=self.config["colors"][2])
		self.textarea.highlight_pattern("#", "green")
		self.textarea.highlight_pattern("<!--", "green")
		self.textarea.highlight_pattern("-->", "green")
		self.textarea.highlight_pattern('/*', "green")
		self.textarea.highlight_pattern('*/', "green")

		self.textarea.highlight_pattern("<", "red")
		self.textarea.highlight_pattern(">", "redend")
		self.textarea.highlight_pattern("=", "red")
		self.textarea.highlight_pattern("{", "red")
		self.textarea.highlight_pattern("}", "redend")
		self.textarea.highlight_pattern("[", "red")
		self.textarea.highlight_pattern("]", "red")
		self.textarea.highlight_pattern("/", "red")
		self.textarea.highlight_pattern("+", "red")
		self.textarea.highlight_pattern("-", "red")
		self.textarea.highlight_pattern("@", "red")
		self.textarea.highlight_pattern("&", "red")
		self.textarea.highlight_pattern("*", "red")
		self.textarea.highlight_pattern("^", "red")
		self.textarea.highlight_pattern("%", "red")

		self.textarea.highlight_pattern('"', "blue")
		self.textarea.highlight_pattern("'", "blue")
		self.textarea.highlight_pattern(".", "blue")
		self.textarea.highlight_pattern(",", "blue")
		self.textarea.highlight_pattern(":", "blue")
		self.textarea.highlight_pattern(";", "blue")
		self.textarea.highlight_pattern("?", "blue")
		self.textarea.highlight_pattern("!", "blue")
		self.textarea.highlight_pattern("$", "blue")
		self.textarea.highlight_pattern("(", "blue")
		self.textarea.highlight_pattern(")", "blue")
		self.parent.after(800, self.updater)


if __name__ == "__main__":
	root = tk.Tk()
	MainApplication(root).pack(side="top", fill="both", expand=True)
	root.mainloop()


