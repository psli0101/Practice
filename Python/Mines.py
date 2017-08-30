from tkinter import *
from tkinter.ttk import *
import numpy as np

class Mines(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.mine = np.zeros((10, 10), Button)
		self.count=0
		self.grid()
		self.startGame()

	def startGame(self):
		def test():
			self.count=self.count + 1
			self.label.configure(text="Click: " + str(self.count))

		self.label = Label(self, text="Click it!")
		self.label.grid(row=0)
		for i in range(10):
			for j in range(10):
					self.mine[i][j] = Button(self, text=i, command=test)
					self.mine[i][j].grid(row=i+1, column=j)

if __name__ == '__main__':
	window = Tk()
	window.title("Mines Game")
	app = Mines(master = window)
	app = mainloop()