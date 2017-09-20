from tkinter import *
from tkinter.ttk import *
import numpy as np

class Calculator(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.num = np.zeros((12), Button)
		self.num2 = np.zeros((12), int)
		self.count = 0
		self.tmp = 0
		self.grid()
		self.useCalculator()

	def useCalculator(self):
		def countNum():
			self.tmp = self.num2[5]
			self.outPut.configure(text=str(self.tmp))

		def plusNum():
			self.count = self.count + self.tmp
			self.outPut.configure(text=str(self.count))
			self.tmp = 0

		def equalNum():
			self.outPut.configure(text=str(self.count))

		self.outPut = Label(self)##, width=50)
		self.outPut.grid(row=0, column=1)##, columnspan=4)

		for i in range(4):
			for j in range(3):
				if i < 3 :
					self.num[i*3+j] = Button(self, text=i*3+j+1, command=countNum)
					self.num[i*3+j].grid(row=3-i, column=j)
					self.num2[i*3+j] = i*3+j+1
				else:
					if j == 0 :
						self.num[i*3+j] = Button(self, text=".")
						self.num[i*3+j].grid(row=4, column=j)
					elif j == 1 :
						self.num[i*3+j] = Button(self, text="0")
						self.num[i*3+j].grid(row=4, column=j)
					else:
						self.num[i*3+j] = Button(self, text="=", command=equalNum)
						self.num[i*3+j].grid(row=4, column=j)
	
		self.plusButton = Button(self, text="+", command=plusNum)
		self.plusButton.grid(row=1, column=4)
		self.minusButton = Button(self, text="-", command=minusNum)
		self.minusButton.grid(row=2, column=4)
		self.timesButton = Button(self, text="×", command=timesNum)
		self.timesButton.grid(row=3, column=4)
		self.divideButton = Button(self, text="÷")
		self.divideButton.grid(row=4, column=4)

if __name__ == '__main__':
    win = Tk()
    win.title("Calculator")
    app = Calculator(master=win)
    app.mainloop()