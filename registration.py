from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

root=Tk()  #k is small
root.title('login')
root.geometry('925x500+300+200') #its x not multiplication
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
        with sqlite3.connect("insta.db") as con:
            cur = con.cursor()
            cur.execute("Insert into INSTA_USER (name,username,email_id,password,dob) values(?,?,?,?,?)",(name,username,email_id,password,dob))
            con.commit()
            print("added successfully")
    except:
        con.rollback()
        print("Cant add you")
    finally:
        root.destroy()
        import trending
#open image


#resize image





# [ height=300,width=250 ==isse label get resized not actual pic ]



imaage = ImageTk.PhotoImage(Image.open("gradient.jpg"))
bg =Label(root, image=imaage)
bg.place(x=0, y=0, relwidth=1, relheight=1)




 
frame=Frame(root,width=390,height=430,bg="white")
frame.place(x=300,y=10)


heading=Label (frame,text='Registration',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

###################
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'username')

user = Entry(frame,width=25,fg='#57a1f8',border=0,bg="white",font=('Microsoft YaHie UI Light',11))
user.place(x=30,y=50)
user.insert(0,'username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=77)
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
passw.place(x=30,y=100)
passw.insert(0,'Password')
passw.bind('<FocusIn>',on_enter)
passw.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=127)

#############
def on_enter(e):
    user1.delete(0,'end')
def on_leave(e):
    name= user1.get()
    if name=='':
        user1.insert(0,'Name')

user1 = Entry(frame,width=25,fg='#57a1f8',border=0,bg="white",font=('Microsoft YaHie UI Light',11))
user1.place(x=30,y=150)
user1.insert(0,'Name')
user1.bind('<FocusIn>',on_enter)
user1.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=180)



##############
def on_enter(e):
    email.delete(0,'end')
def on_leave(e):
    name= email.get()
    if name=='':
        email.insert(0,'Email')

email = Entry(frame,width=25,fg='#57a1f8',border=0,bg="white",font=('Microsoft YaHie UI Light',11))
email.place(x=30,y=210)
email.insert(0,'Email')
email.bind('<FocusIn>',on_enter)
email.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=240)


################
##############
def on_enter(e):
    doob.delete(0,'end')
def on_leave(e):
    name= doob.get()
    if name=='':
        doob.insert(0,'date-of-birth')

doob = Entry(frame,width=25,fg='#57a1f8',border=0,bg="white",font=('Microsoft YaHie UI Light',11))
doob.place(x=30,y=270)
doob.insert(0,'date-of-birth')
doob.bind('<FocusIn>',on_enter)
doob.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=300)


##############
Button(frame,width=39,pady=7,text='Submit',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=360)
label=Label(frame,text="Already have an account?",fg='black',bg='white',font=('Microsoft YaHie UI Light',9))
label.place(x=75,y=410)

def login():
    root.destroy()
    import login
sign_up=Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=login)
sign_up.place(x=215,y=410)

#def signin():
    


root.mainloop()