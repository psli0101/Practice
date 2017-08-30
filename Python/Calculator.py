from tkinter import *
from tkinter.ttk import *
import numpy as np

class Calculator(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.num = np.zeros((4, 3), Button)
		self.grid()
		self.useCalculator()

	def useCalculator(self):
		self.outputField = Entry(self, width=50)
		self.outputField.grid(row=0, column=1, columnspan=4)

		for i in range(4):
			for j in range(3):
				if i < 3 :
					self.num[i][j] = Button(self, text=i*3+j+1)
					self.num[i][j].grid(row=3-i, column=j)
				else:
					if j == 0 :
						self.num[i][j] = Button(self, text=".")
						self.num[i][j].grid(row=4, column=j)
					elif j == 1 :
						self.num[i][j] = Button(self, text="0")
						self.num[i][j].grid(row=4, column=j)
					else:
						self.num[i][j] = Button(self, text="=")
						self.num[i][j].grid(row=4, column=j)
		
		self.plusButton = Button(self, text="+")
		self.plusButton.grid(row=1, column=4)
		self.minusButton = Button(self, text="-")
		self.minusButton.grid(row=2, column=4)
		self.timesButton = Button(self, text="×")
		self.timesButton.grid(row=3, column=4)
		self.divideButton = Button(self, text="÷")
		self.divideButton.grid(row=4, column=4)

if __name__ == '__main__':
    win = Tk()
    win.title("Calculator")
    app = Calculator(master=win)
    app.mainloop()