from tkinter import *


root=Tk()
root.title('Calculator App')

def btn_click(value):
    global data
    data=data+str(value)
    input_text.set(data)
    
def btn_equal():
    global data
    result=str(eval(data))
    input_text.set(result)


def btn_clear():
    global data
    data=''
    input_text.set('')

    
data=''
input_text=StringVar()


input_frame=Frame(root,height=20,width=300,highlightbackground='black',highlightthickness=1)
input_frame.pack(side=TOP)

input_field=Entry(input_frame,width=22,textvariable=input_text,bg='#eee',justify=RIGHT,font=('times',20,'bold'))
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)

btn_frame=Frame(root,height=220,width=300,bg='lightgreen')
btn_frame.pack()

#First row

clear=Button(btn_frame,text='c',bd=0,height=3,width=32,command=lambda:btn_clear()).grid(row=0,column=0,columnspan=3,padx=1,pady=1)
devide=Button(btn_frame,text='/',bd=0,height=3,width=10,command=lambda:btn_click('/')).grid(row=0,column=3,padx=1,pady=1)

#Second row

seven=Button(btn_frame,text=7,bd=0,height=3,width=10,command=lambda:btn_click(7)).grid(row=1,column=0,padx=1,pady=1)
Eight=Button(btn_frame,text=8,bd=0,height=3,width=10,command=lambda:btn_click(8)).grid(row=1,column=1,padx=1,pady=1)
nine=Button(btn_frame,text=9,bd=0,height=3,width=10,command=lambda:btn_click(9)).grid(row=1,column=2,padx=1,pady=1)
Multiply=Button(btn_frame,text='*',bd=0,height=3,width=10,command=lambda:btn_click('*')).grid(row=1,column=3,padx=1,pady=1)

#Third row

six=Button(btn_frame,text=6,bd=0,height=3,width=10,command=lambda:btn_click(6)).grid(row=2,column=0,padx=1,pady=1)
five=Button(btn_frame,text=5,bd=0,height=3,width=10,command=lambda:btn_click(5)).grid(row=2,column=1,padx=1,pady=1)
four=Button(btn_frame,text=4,bd=0,height=3,width=10,command=lambda:btn_click(4)).grid(row=2,column=2,padx=1,pady=1)
Plus=Button(btn_frame,text='+',bd=0,height=3,width=10,command=lambda:btn_click('+')).grid(row=2,column=3,padx=1,pady=1)

#fourth row

Three=Button(btn_frame,bd=0,height=3,width=10,text=3,command=lambda:btn_click(3)).grid(row=3,column=0,padx=1,pady=1)
Two=Button(btn_frame,bd=0,text=2,height=3,width=10,command=lambda:btn_click(2)).grid(row=3,column=1,padx=1,pady=1)
One=Button(btn_frame,bd=0,text=1,height=3,width=10,command=lambda:btn_click(1)).grid(row=3,column=2,padx=1,pady=1)
Minus=Button(btn_frame,text='-',bd=0,height=3,width=10,command=lambda:btn_click('-')).grid(row=3,column=3,padx=1,pady=1)

#Fifth row

Dot=Button(btn_frame,bd=0,height=3,width=22,text='.',command=lambda:btn_click('.')).grid(row=4,columnspan=2,padx=1,pady=1)
Zero=Button(btn_frame,bd=0,text=0,height=3,width=10,command=lambda:btn_click(0)).grid(row=4,column=2,padx=1,pady=1)
Equalsto=Button(btn_frame,bd=0,text='=',height=3,width=10,command=lambda:btn_equal()).grid(row=4,column=3,padx=1,pady=1)

root.mainloop()
