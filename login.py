from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

root=Tk()  #k is small
root.title('login')
root.geometry('1000x600+170+100') #its x not multiplication
root.configure(bg="#fff")
root.resizable(False,False)


def signin():
    try:
        username=user.get()
        password=passw.get()
        if len(password) != 8:
            messagebox.showerror("Invalid","Password should be 8 in length")
        elif not any(char.isdigit() for char in password):
            messagebox.showerror("Invalid","Password should have 1 digit atleast")  
        else:
            with sqlite3.connect("insta.db") as con:
                cur = con.cursor()
                cur.execute("Select username, password from users where username=? AND password=?",(username,password))
                if cur.fetchone():
                    print("Welcome")
                    con.commit()
                else:
                    messagebox.showerror("Wrong username or password")
    except:
        with sqlite3.connect("insta.db") as con:
            con.rollback()
            print("Cant add you")
    finally:
        root.destroy()
        import Voicerecog


imaage = ImageTk.PhotoImage(Image.open("gradient.jpg"))
bg =Label(root, image=imaage)
bg.place(x=0, y=0, relwidth=1, relheight=1)




 
frame=Frame(root,width=420,height=500,bg="white")
frame.place(x=300,y=30)


heading=Label (frame,text='Sign-in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=120,y=30)

###################
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'username')

user_label = Label(frame,text='Username:',fg='#57a1f8',border=2,bg="white",font=('Microsoft YaHie UI Light',14))
user_label.place(x=40,y=100)
user = Entry(frame,width=40,fg='#57a1f8',border=2,bg="white",font=('Microsoft YaHie UI Light',11))
user.place(x=40,y=130)
user.insert(0,'username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)


#########################
def on_enter(e):
    passw.delete(0,'end')

def on_leave(e):
    name=passw.get()
    if name=='':
        passw.insert(0,'Password')
def show():
    p = passw.get() #get password from entry
    print(p)
passw_label = Label(frame,text='Password:',fg='#57a1f8',border=2,bg="white",font=('Microsoft YaHie UI Light',14))
passw_label.place(x=40,y=190)  
passw = Entry(frame,width=40,fg='#57a1f8',show="*",border=2,bg="white",font=('Microsoft YaHie UI Light',11))
passw.place(x=40,y=220)
passw.insert(0,'Password')
passw.bind('<FocusIn>',on_enter)
passw.bind('<FocusOut>',on_leave)


Button(frame,width=45,pady=7,text='Submit',bg='#57a1f8',fg='white',border=0,command=signin).place(x=40,y=280)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHie UI Light',9))
label.place(x=75,y=320)

def register():
    root.destroy()
    import demo_register
sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=register)
sign_up.place(x=215,y=320)

#def signin():
    


root.mainloop()