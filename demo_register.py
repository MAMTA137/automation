from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
import re
from tkcalendar import DateEntry

root=Tk()  #k is small
root.title('login')
root.geometry('1000x800+200+50') #its x not multiplication
root.configure(bg="#fff")
root.resizable(False,False)

conn = sqlite3.connect('insta.db')


def signin():
    try:
        username=user.get()
        password=passw.get()
        name = user1.get()
        email_id = email.get()
        dob = doob.get()
        check(email_id)
        if len(password) != 8:
            messagebox.showerror("Invalid","Password should be 8 in length")
        elif len(username)==0:
            messagebox.showerror("Invalid","Please fill all the details")
        elif not any(char.isdigit() for char in password):
            messagebox.showerror("Invalid","Password should have 1 digit atleast")  
        else:
            with sqlite3.connect("insta.db") as con:
                cur = con.cursor()
                cur.execute("Insert into users (name,username,email_id,password,dob) values(?,?,?,?,?)",(name,username,email_id,password,dob))
                con.commit()
                print("added successfully")
                root.destroy()
                import login
    except:
        with sqlite3.connect("insta.db") as con:
            con.rollback()
            print("Cant add you")
#open image

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
#resize image
def check(email):
    if(re.fullmatch(regex, email)):
        print("Valid Email")
 
    else:
        messagebox.showerror("Invalid","Enter correct Email")
        return
        




# [ height=300,width=250 ==isse label get resized not actual pic ]



imaage = ImageTk.PhotoImage(Image.open("gradient.jpg"))
bg =Label(root, image=imaage)
bg.place(x=0, y=0, relwidth=1, relheight=1)




 
frame=Frame(root,width=420,height=700,bg="white")
frame.place(x=300,y=30)


heading=Label (frame,text='Registration',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',26,'bold'))
heading.place(x=100,y=5)

###################
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'username')
user_label = Label(frame,text='Username:',fg='#57a1f8',border=2,bg="white",font=('Microsoft YaHie UI Light',14))
user_label.place(x=30,y=75)
user = Entry(frame,width=40,fg='#57a1f8',border=2,bg="white",font=('Microsoft YaHie UI Light',11))
user.place(x=30,y=100)
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
passw_label.place(x=30,y=140)
passw = Entry(frame,width=40,fg='#57a1f8',show="*",border=2,bg="white",font=('Microsoft YaHie UI Light',11))
passw.place(x=30,y=165)
passw.insert(0,'Password')
passw.bind('<FocusIn>',on_enter)
passw.bind('<FocusOut>',on_leave)


#############
def on_enter(e):
    user1.delete(0,'end')
def on_leave(e):
    name= user1.get()
    if name=='':
        user1.insert(0,'Name')
name_label = Label(frame,text='Full Name:',fg='#57a1f8',border=2,bg="white",font=('Microsoft YaHie UI Light',14))
name_label.place(x=30,y=205)
user1 = Entry(frame,width=40,fg='#57a1f8',border=2,bg="white",font=('Microsoft YaHie UI Light',11))
user1.place(x=30,y=230)
user1.insert(0,'Name')
user1.bind('<FocusIn>',on_enter)
user1.bind('<FocusOut>',on_leave)




##############
def on_enter(e):
    email.delete(0,'end')
def on_leave(e):
    name= email.get()
    if name=='':
        email.insert(0,'Email')
email_label = Label(frame,text='Email-id',fg='#57a1f8',border=2,bg="white",font=('Microsoft YaHie UI Light',14))
email_label.place(x=30,y=270)
email = Entry(frame,width=40,fg='#57a1f8',border=2,bg="white",font=('Microsoft YaHie UI Light',11))
email.place(x=30,y=295)
email.insert(0,'Email')
email.bind('<FocusIn>',on_enter)
email.bind('<FocusOut>',on_leave)



################
##############

passw_label = Label(frame,text='Date of Birth',fg='#57a1f8',border=2,bg="white",font=('Microsoft YaHie UI Light',14))
passw_label.place(x=30,y=335)
doob = DateEntry(frame,width=25,foreground='#57a1f8',border=2,background="white",font=('Microsoft YaHie UI Light',11))
doob.place(x=30,y=360)



##############
Button(frame,width=50,pady=7,text='Submit',bg='#57a1f8',fg='white',border=0,command=signin).place(x=30,y=635)
label=Label(frame,text="Already have an account?",fg='black',bg='white',font=('Microsoft YaHie UI Light',9))
label.place(x=100,y=680)

def login():
    root.destroy()
    import login
sign_up=Button(frame,width=5,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=login)
sign_up.place(x=250,y=680)

#def signin():
    


root.mainloop()