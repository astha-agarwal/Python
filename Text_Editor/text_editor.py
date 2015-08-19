# Notepad style  application that can open, edit and save text documents.

# Author: Astha Agarwal
# Date: 12 August, 2015
# Version: 1.0


# Tkinter is the standard GUI library for Python. 
from Tkinter import *
from ScrolledText import *
import tkFileDialog

class Application(Frame):

	def __init__(self, master):
		Frame.__init__(self, master)
		self.master = master
		self.pack(expand = True, fill = BOTH)
		self.create_widget()
		self.text = ScrolledText(self, wrap = 'word')
		self.text.focus_set()
		self.text.pack(expand = True, fill = BOTH) 

		
	def create_widget(self):
		menu_bar = Menu(self.master)
		self.master.config(menu = menu_bar)
		file_menu = Menu(menu_bar, tearoff = 0)
		file_menu.add_command(label="New", command = self.new)
		file_menu.add_command(label="Open", command = self.open)
		file_menu.add_command(label="Save", command = self.save)
		file_menu.add_separator()
		file_menu.add_command(label="Exit", command = self.exit)
		menu_bar.add_cascade(label = "File", menu = file_menu)

	def new(self):
		#text = Text(self)
		self.text.delete('1.0', END)
		
	def open(self):
		file_opt = options = {}
		options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
		options['parent'] = self.master
		file_open = tkFileDialog.askopenfile(mode='r', **file_opt)

		if file_open != None:
			contents = file_open.read()
			self.text.insert('1.0', contents)
			file_open.close()

	def save(self):
		file_opt = options = {}
		options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
		options['parent'] = self.master
		file_save = tkFileDialog.asksaveasfile(mode='w', **file_opt)

		if file_save != None:
			contents = self.text.get('1.0', END)
			file_save.write(contents)
			file_save.close()

	def exit(self):
		root.destroy()	

root = Tk()
root.title("Text Editor")
root.geometry("300x300")
app = Application(root)
root.mainloop()

