from tkinter import *

# creating gui box
m = Tk()

# for specifying box size
m.geometry( '800x600' )

name=StringVar()
e=Entry( m, textvariable=name, width=50,borderwidth=5 ).grid(row=1,column=5)

# creating a function for button
def click():
    Button(m,text="start typing",command=flick).grid(row=2,column=3)
    Button(m,text="stop",command=flick2).grid(row=2 , column=7)
def flick():
    Entry( m, text="Clicked", width=50,borderwidth=5 ).grid(row=3,column=3)
def flick2():
    Label( m, text=e.get() ).grid(row=3,column=7)

def click2():
    Label(m,text=name.get()).grid(row=3,column=5)

#creating text for box label
mylabel = Label( m, text="Judgemental Typing",fg="Blue")
mylabel.grid(row=0,column=5)

# creating a button
mybutton = Button( m, text="TEST", padx=50, pady=10, command=click, fg="Red", bg="black" )
mybutton.grid(row=2,column=5)
#padx,pady specify box size , command executes the function,fg is colour foreground,bg is background

# to execute the box using infinite loop
m.mainloop()
#editing
