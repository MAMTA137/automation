from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

root=Tk()  #k is small
root.title('login')
root.geometry('925x500+300+200') #its x not multiplication
root.configure(bg="#fff")
root.resizable(False,False)



def signin():
    try:
        username=user.get()
        password=passw.get()
        with sqlite3.connect("insta.db") as con:
            cur = con.cursor()
            cur.execute("Select username, password from INSTA_USER where username=? AND password=?",(username,password))
            if cur.fetchone():
                print("Welcome")
                con.commit()
            else:
                print("Wrong username or password")
    except:
        con.rollback()
        print("Cant add you")
    finally:
        root.destroy()
        import homepage






# [ height=300,width=250 ==isse label get resized not actual pic ]



imaage = ImageTk.PhotoImage(Image.open("gradient.jpg"))
bg =Label(root, image=imaage)
bg.place(x=0, y=0, relwidth=1, relheight=1)




 
frame=Frame(root,width=390,height=400,bg="white")
frame.place(x=300,y=10)


heading=Label (frame,text='Sign-in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=120,y=30)

###################
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'username')

user = Entry(frame,width=25,fg='#57a1f8',border=0,bg="white",font=('Microsoft YaHie UI Light',11))
user.place(x=30,y=100)
user.insert(0,'username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=130)
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
        
    

     
passw = Entry(frame,width=25,fg='#57a1f8',border=0,bg="white",font=('Microsoft YaHie UI Light',11))
passw.place(x=30,y=200)
passw.insert(0,'Password')
passw.bind('<FocusIn>',on_enter)
passw.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=230)

Button(frame,width=39,pady=7,text='Submit',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=280)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHie UI Light',9))
label.place(x=75,y=320)

def register():
    root.destroy()
    import registration
sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=register)
sign_up.place(x=215,y=320)

#def signin():
    


root.mainloop()
