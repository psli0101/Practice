from tkinter import *
from tkinter.ttk import *
class GUItest(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.count=0
		self.grid(column=0)
		self.creat()

	def creat(self):
		def clickOK():
		    self.count=self.count + 1
		    if self.count==5:
		    	self.quit()
		    else:
		    	self.label.configure(text="Click OK " + str(self.count) + " times")
		self.label=Label(self,text="Hello World!")
		self.label.grid(row=0)
		self.ok=Button(self, text="OK", command=clickOK)
		self.ok.grid(row=1)

if __name__ == '__main__':
    root = Tk()
    root.title("Test")
    app = GUItest(master=root)
    app.mainloop()