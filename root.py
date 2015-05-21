from Tkinter import *

root = Tk()

root.geometry("600x400")
root.title("Principal")

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

add = Button(topFrame, text="Add", fg="green")
add.pack()


root.mainloop()
