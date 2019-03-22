from tkinter import *

def accept():
	print("INFORMATION IS ACCEPTED.")

master = Tk()

header=Label(master,text="Basic Information:")
header.pack()

#frames 1 adn two

TF1=Frame(master)
TF1.pack()
TF2=Frame(master)
TF2.pack(side=BOTTOM)
TF3=Frame(master)
TF3.pack(side=RIGHT)



#label for first and last name

name=Label(TF1,text="First Name:")
surname=Label(TF1,text="Last name:")


#entry for names

entry1=Entry(TF1)
entry2=Entry(TF1)

#grid align label and entries

name.grid(row=1,column=0)
surname.grid(row=2,column=0)
entry1.grid(row=1,column=1)
entry2.grid(row=2,column=1)


#setup for radiob
var=IntVar()
variable = StringVar(master)
variable.set("select semester:") # default value

w = OptionMenu(TF2, variable, "IV", "VI", "VIII")
w.pack(side=RIGHT)

gender=Label(TF3,text="select your gender:")
gender.pack()
r1=Radiobutton(TF3,text="male",variable=var,value=1)
r2=Radiobutton(TF3,text="female",variable=var,value=2)
r1.pack()
r2.pack()

#button

b1=Button(TF2,text="submit",bg="red",fg="blue",command=accept)


b1.pack()

master.mainloop()