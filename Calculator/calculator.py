# This program implements a calculator on GUI

# Author: Astha Agarwal
# Date: 7 august, 2015
# Version: 1.0

from Tkinter import *

class Application(Frame):
	'''GUI interface for calculator'''
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.create_widget()
		self.num1 = 0
		self.num2 = 0
		self.operation = ''
		self.isnum1 = False
		self.result = 0
		self.message = '0'
		self.isdecimal = False
		self.place_of_decimal = 0.1
		self.message = '0'

	def create_widget(self):

		self.result_box = Text(self, width = 20, height = 2)
		self.result_box.grid(row = 0, column = 0, columnspan = 4)

		self.ac_button = Button(self, text = "AC", command = self.ac) #.grid(row = 1, column = 0)
		self.ac_button.pack()
		self.ac_button.grid(row = 1, column = 0)
	
		Button(self, text = "+/-").grid(row = 1, column = 1)
		Button(self, text = "%", command = self.modulo).grid(row = 1, column = 2)
		Button(self, text = "/", command = self.divide).grid(row = 1, column = 3)
		Button(self, text = "7", command = lambda: self.number(7)).grid(row = 2, column = 0)
		Button(self, text = "8", command = lambda: self.number(8)).grid(row = 2, column = 1)
		Button(self, text = "9", command = lambda: self.number(9)).grid(row = 2, column = 2)
		Button(self, text = "x", command = self.multiply).grid(row = 2, column = 3)
		Button(self, text = "4", command = lambda: self.number(4)).grid(row = 3, column = 0)
		Button(self, text = "5", command = lambda: self.number(5)).grid(row = 3, column = 1)
		Button(self, text = "6", command = lambda: self.number(6)).grid(row = 3, column = 2)
		Button(self, text = "-", command = self.minus).grid(row = 3, column = 3)
		Button(self, text = "1", command = lambda: self.number(1)).grid(row = 4, column = 0)
		Button(self, text = "2", command = lambda: self.number(2)).grid(row = 4, column = 1)
		Button(self, text = "3", command = lambda: self.number(3)).grid(row = 4, column = 2)
		Button(self, text = "+", command = self.plus).grid(row = 4, column = 3)
		Button(self, text = "0", command = lambda: self.number(0)).grid(row = 5, column = 0, columnspan = 2)
		Button(self, text = ".", command = self.decimal).grid(row = 5, column = 2)	
		Button(self, text = "=", command = self.equal).grid(row = 5, column = 3)


	def ac(self):
		self.num1 = 0
		self.num2 = 0
		self.operation = ''
		self.isnum1 = False
		self.result = 0
		self.message  = '0'
		self.result_box.delete(0.0, END)
		self.result_box.insert(0.0, self.message)
		self.place_of_decimal = 0.1
		self.isdecimal = False

	def number(self, num):
		if not self.isnum1:
			if not self.isdecimal:
				self.num1 = self.num1 * 10 + num
			else:
				self.num1 = self.num1 + num * self.place_of_decimal
				self.place_of_decimal *= 0.1
			self.message  = str(self.num1)
			self.result_box.delete(0.0, END)
			self.result_box.insert(0.0, self.message)
			#print self.num1
		else:
			if not self.isdecimal:
				self.num2 = self.num2 * 10 + num
			else:
				self.num2 = self.num2 + num * self.place_of_decimal
				self.place_of_decimal *= 0.1
			self.message  = str(self.num2)
			self.result_box.delete(0.0, END)
			self.result_box.insert(0.0, self.message)

	def decimal(self):
		self.isdecimal = True
		self.message = self.message + '.'
		self.result_box.delete(0.0, END)
		self.result_box.insert(0.0, self.message)
		

	def plus(self):
		self.operation = '+'
		self.isnum1 = True
		self.place_of_decimal = 0.1
		self.isdecimal = False


	def minus(self):
		self.operation = '-'
		self.isnum1 = True
		self.place_of_decimal = 0.1
		self.isdecimal = False

	def multiply(self):
		self.operation = 'x'
		self.isnum1 = True
		self.place_of_decimal = 0.1
		self.isdecimal = False

	def divide(self):
		self.operation = '/'
		self.isnum1 = True
		self.place_of_decimal = 0.1
		self.isdecimal = False

	def modulo(self):
		self.operation = '%'
		self.isnum1 = True
		self.place_of_decimal = 0.1
		self.isdecimal = False

	def equal(self):
		if self.operation == '+':
			self.result = self.num1 + self.num2 * 1.0

		if self.operation == '-':
			self.result = self.num1 - self.num2 * 1.0

		if self.operation == 'x':
			self.result = self.num1 * self.num2 * 1.0

		if self.operation == '/':
			self.result = self.num1 / (self.num2 * 1.0)

		if self.operation == '%':
			self.result = self.num1 %  self.num2 * 1.0

		self.message  = str(self.result)
		self.result_box.delete(0.0, END)
		self.result_box.insert(0.0, self.message)
		self.num1 = self.result
		self.num2 = 0
		self.isnum1 = True
		self.place_of_decimal = 0.1
		self.isdecimal = False



root = Tk()
root.title("Calculator")
#root.geometry("300x300")
app = Application(root)
root.mainloop()