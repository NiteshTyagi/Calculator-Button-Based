import tkinter as tk
from tkinter import messagebox
expression=""
operator=['+','-','*','/','=']
a=""
def fun():
    return e.get()
    
def click(par):
    global expression
    global a
    if par!='=' and par!='clear' and par!='b':
        expression+=str(par)
        expression=fun()
        e.insert(len(expression),par)
    elif par=='=':
        expression=fun()
        if expression[-1]  not in operator:
            try:
                result=str(eval(expression))
                expression=result
                messagebox.showinfo("Answer",'The Answer is '+result)
                e.delete(0,tk.END)
                e.insert(0,expression)
            except:
                messagebox.showwarning("Warning","Please Enter valid expression")
                
        else:
            messagebox.showerror("Error","Please Enter valid expression")
        
    elif par=='b':
        e.delete(len(expression),tk.END)
        expression=expression[:-1]
        
    else:
        expression=""
        e.delete(0,tk.END)
            
    
root=tk.Tk()
root.title("Calculator")
root.resizable(0,0)
root.minsize(600,400)
tk.Label(root,text="Enter the value --> ",fg="red",font=50).place(x=100,y=20)
e=tk.Entry(root,width=30,relief='sunken',disabledbackground='lightblue')
e.focus()
e.place(x=250,y=20,height=25)


b1=tk.Button(root,text="1",width=10,fg="red",bg='yellow',font=("Arial bold",15),command=(lambda e=1:click(e)))
b1.place(x=100,y=100)

b4=tk.Button(root,text="4",width=10,fg="red",bg='yellow',font=("Arial bold",15),command=(lambda e=4:click(e)))
b4.place(x=100,y=150)

b7=tk.Button(root,text="7",width=10,fg="red",bg='yellow',font=("Arial bold",15),command=(lambda e=7:click(e)))
b7.place(x=100,y=200)

b2=tk.Button(root,text="2",width=10,fg="red",bg='yellow',font=("Arial bold",15),command=(lambda e=2:click(e)))
b2.place(x=250,y=100)

b5=tk.Button(root,text="5",width=10,fg="red",bg='yellow',font=("Arial bold",15),command=(lambda e=5:click(e)))
b5.place(x=250,y=150)

b8=tk.Button(root,text="8",width=10,fg="red",bg='yellow',font=("Arial bold",15),command=(lambda e=8:click(e)))
b8.place(x=250,y=200)

b3=tk.Button(root,text="3",width=10,fg="red",bg='yellow',font=("Arial bold",15),command=(lambda e=3:click(e)))
b3.place(x=400,y=100)

b6=tk.Button(root,text="6",width=10,fg="red",bg='yellow',font=("Arial bold",15),command=(lambda e=6:click(e)))
b6.place(x=400,y=150)

b9=tk.Button(root,text="9",width=10,fg="red",bg='yellow',font=("Arial bold",15),command=(lambda e=9:click(e)))
b9.place(x=400,y=200)

bplus=tk.Button(root,text="+",width=10,fg="red",bg='yellow',font=("Arial bold",15),command=(lambda e="+":click(e)))
bplus.place(x=30,y=250)
bsub=tk.Button(root,text="-",width=10,fg="red",bg='yellow',font=("Arial bold",15),command=(lambda e="-":click(e)))
bsub.place(x=170,y=250)
bmul=tk.Button(root,text="*",width=10,fg="red",bg='yellow',font=("Arial bold",15),command=(lambda e="*":click(e)))
bmul.place(x=320,y=250)
bdiv=tk.Button(root,text="/",width=10,fg="red",bg='yellow',font=("Arial bold",15),command=(lambda e="/":click(e)))
bdiv.place(x=470,y=250)


bclear=tk.Button(root,text="CLEAR",width=10,fg="red",bg='yellow',font=("Arial bold",15),command=(lambda e="clear":click(e)))
bclear.place(x=100,y=330)

back=tk.Button(root,text="BACK",width=10,fg="red",bg='yellow',font=("Arial bold",15),command=(lambda e="b":click(e)))
back.place(x=250,y=330)

bR=tk.Button(root,text="RESULT",width=10,fg="red",bg='yellow',font=("Arial bold",15),command=(lambda e="=":click(e)))
bR.place(x=400,y=330)

root.mainloop()
