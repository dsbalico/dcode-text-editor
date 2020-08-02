import tkinter as tk

class About:
	def __init__(self, parent, *args, **kwargs):
		self.parent = parent
		self.root = tk.Toplevel(self.parent)
		self.root.tk.call('wm', 'iconphoto', self.root._w, tk.PhotoImage(file='icon.png'))
		self.root.title("DCode")

		# Make main window unclickable
		self.root.grab_set()
		
		self.root.resizable(0,0)

		self.parent.update_idletasks()

		# Make window show at the middle of the main window screen
		self.width = 250
		self.height = 150
		self.x = self.parent.winfo_x() + ((self.parent.winfo_reqwidth()//2)-self.width//3)
		self.y = self.parent.winfo_y() + ((self.parent.winfo_reqheight()//2))
		self.root.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
		self.root.config(bg="#1a1a1a")

		# GUI
		title = tk.Label(self.root, text="DCode", pady=10, font=("Helvetica", 24, "bold"), bg="#1a1a1a", fg="#fff")
		copyright = tk.Label(self.root, text="Copyright 2020 Daniel Shan Balico", pady=0, font=("Helvetica", 10), bg="#1a1a1a", fg="#fff")
		version = tk.Label(self.root, text="Version 1.0", pady=0, font=("Helvetica", 10), bg="#1a1a1a", fg="#fff")
		build = tk.Label(self.root, text="Built using Tkinter", pady=15, font=("Helvetica", 10), bg="#1a1a1a", fg="#fff")

		title.pack()
		copyright.pack()
		version.pack()
		build.pack()