import tkinter as tk
import json
from tkinter import messagebox as mbox

class FontSettings:
	def __init__(self, parent):
		self.parent = parent
		self.root = tk.Toplevel(self.parent)
		self.root.tk.call('wm', 'iconphoto', self.root._w, tk.PhotoImage(file='icon.png'))
		self.root.title("Font Settings")
		self.root.config(bg="#1a1a1a")
		# Make main window unclickable
		self.root.grab_set()

		self.root.resizable(0,0)

		with open("config.json", "r+") as f:
			self.config = json.loads(f.read())

		# Window Size
		self.width = 250
		self.height = 320

		# Show at the middle of the main window
		self.parent.update_idletasks()
		self.x = self.parent.winfo_x() + ((self.parent.winfo_reqwidth()//2)-self.width//3)
		self.y = self.parent.winfo_y() + ((self.parent.winfo_reqheight()//2)-self.height//3)
		self.root.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")

		# GUI
		titleSettings = tk.Label(self.root, 
			text="Font Settings", bg="#1a1a1a", fg="#fff",
			font=("Helvetica", 15, "bold"))
		fontLabel = tk.Label(self.root, 
			text="Font", bg="#1a1a1a", fg="#fff", 
			font=("Helvetica", 12, "normal"))
		self.fontEntry = tk.Entry(self.root)

		fontSizeLabel = tk.Label(self.root, 
			text="Font Size", bg="#1a1a1a", fg="#fff", 
			font=("Helvetica", 12, "normal"))
		self.fontSizeEntry = tk.Entry(self.root)

		fontWeightLabel = tk.Label(self.root, 
			text="Font Weight", bg="#1a1a1a", fg="#fff", 
			font=("Helvetica", 12, "normal"))
		self.fontWeightEntry = tk.Entry(self.root)

		submitButton = tk.Button(self.root, text="Save Changes", command=self.submitChanges)

		titleSettings.pack(pady=10)
		fontLabel.pack(pady=5)
		self.fontEntry.pack(pady=5)
		fontSizeLabel.pack(pady=5)
		self.fontSizeEntry.pack(pady=5)
		fontWeightLabel.pack(pady=5)
		self.fontWeightEntry.pack(pady=5)
		submitButton.pack(pady=20)

		self.fontEntry.insert(0, self.config["fontFamily"])
		self.fontSizeEntry.insert(0, self.config["fontSize"])
		self.fontWeightEntry.insert(0, self.config["fontWeight"])
		self.root.mainloop()


	def submitChanges(self):
		self.config["fontFamily"] = self.fontEntry.get()
		self.config["fontSize"] = self.fontSizeEntry.get()
		self.config["fontWeight"] = self.fontWeightEntry.get()

		with open("config.json", "w+") as f:
			json.dump(self.config, f)
			mbox.showinfo("DCode", "Change successful, please restart DCode to complete.")
			self.root.destroy()