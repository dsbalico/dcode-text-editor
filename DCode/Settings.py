import tkinter as tk
import json

class Settings:
	def __init__(self, parent):
		self.parent = parent
		self.root = tk.Toplevel(self.parent)
		self.root.title("Settings")
		self.root.config(bg="#1a1a1a")
		self.root.tk.call('wm', 'iconphoto', self.root._w, tk.PhotoImage(file='icon.png'))

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
			text="Settings", bg="#1a1a1a", fg="#fff",
			font=("Helvetica", 15, "bold"))
		color_one = tk.Label(self.root, 
			text="Color 1", bg="#1a1a1a", fg="#fff", 
			font=("Helvetica", 12, "normal"))
		self.color_oneEntry = tk.Entry(self.root)

		color_two = tk.Label(self.root, 
			text="Color 2", bg="#1a1a1a", fg="#fff", 
			font=("Helvetica", 12, "normal"))
		self.color_twoEntry = tk.Entry(self.root)

		color_three = tk.Label(self.root, 
			text="Color 3", bg="#1a1a1a", fg="#fff", 
			font=("Helvetica", 12, "normal"))
		self.color_threeEntry = tk.Entry(self.root)

		submitButton = tk.Button(self.root, text="Save Changes", command=self.submitChanges)

		titleSettings.pack(pady=10)
		color_one.pack(pady=5)
		self.color_oneEntry.pack(pady=5)
		color_two.pack(pady=5)
		self.color_twoEntry.pack(pady=5)
		color_three.pack(pady=5)
		self.color_threeEntry.pack(pady=5)
		submitButton.pack(pady=20)

		self.color_oneEntry.insert(0, self.config["colors"][0])
		self.color_twoEntry.insert(0, self.config["colors"][1])
		self.color_threeEntry.insert(0, self.config["colors"][2])

		self.root.mainloop()


	def submitChanges(self, event):
		self.config["colors"][0] = self.color_oneEntry.get()
		self.config["colors"][1] = self.color_twoEntry.get()
		self.config["colors"][2] = self.color_threeEntry.get()

		with open("config.json", "w+") as f:
			json.dump(self.config, f)
			mbox.showinfo("DCode", "Change successful, please restart DCode to complete.")
			self.root.destroy()

		


