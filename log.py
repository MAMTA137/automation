from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root=Tk()  #k is small
root.title('login')
root.geometry('925x500+300+200') #its x not multiplication
root.configure(bg="#fff")
root.resizable(False,False)

def signin():
    username=user.get()
    Password=code.get()

    if username== 'admin' and Password=='1234':
       screen=Toplevel(root)
       screen.title("App")
       screen.geometry('925x500+300+200')
       screen.config(bg="white")
       Label(screen,text='hello ' ,bg='#fff',font=('Calibri(Body)',50,'bold')).pack(expand=True)
       screen.mainloop()
    elif username!='admin' and Password!='1234':
        messagebox.showerror("Invalid","invalid username and password")
    elif Password!='1234':
        messagebox.showerror("Invalid","invalid username and password")
#open image


#resize image





# [ height=300,width=250 ==isse label get resized not actual pic ]



imaage = ImageTk.PhotoImage(Image.open("gradient.jpg"))
bg =Label(root, image=imaage)
bg.place(x=0, y=0, relwidth=1, relheight=1)




 
frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)


heading=Label (frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

###################
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'username')

user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHie UI Light',11))
user.place(x=30,y=80)
user.insert(0,'username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
#########################
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        user.insert(0,'Password')
def show():
    p = code.get() #get password from entry
    print(p)
        
    

     
code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHie UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

##############

Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHie UI Light',9))
label.place(x=75,y=270)


sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8')
sign_up.place(x=215,y=270)




root.mainloop()