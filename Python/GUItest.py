from tkinter import *
from tkinter.ttk import *
class GUIDemo(Frame):
	def __init__(self, master=None):
		count=0
		self.creat()

	def creat(self):
		def clickOK():
		    global count
		    count=count + 1
		    if count==5:
		    	self.Destroy()
		    else:
		    	self.label.configure(text="Click OK " + str(count) + " times")
		self.label=Label(root, text="Hello World!")
		self.button=Button(root, text="OK", command=clickOK)

if __name__ == '__main__':
    root = Tk()
    root.title("Test")
    app = GUIDemo(master=root)
    app.mainloop()