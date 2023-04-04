from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image,ImageTk
import os
from tkinter.ttk import Combobox
import openpyxl,xlrd
from openpyxl import workbook
import pathlib

root=Tk()  #k is small
root.title('login')
root.geometry('1000x600+170+100') #its x not multiplication

right_frame1 =Frame(root, borderwidth=1, bg='#C13584', relief="solid", highlightthickness=2)
right_frame1.pack(side="top", expand=False, fill="y")
container1 =Frame(right_frame1, borderwidth=1, bg="white", relief="solid")
container1.pack(expand=True, fill="y", padx=5, pady=5)
Label(container1,text='PROFILE',width=140,bg='white',fg='#C13584',font=('Helvetica', 30, 'bold')).pack(side=TOP,fill=X)

f=Frame(root,bd=3,bg="black",width=700,height=460,relief=GROOVE)
f.place(x=270,y=100)
# img=PhotoImage(file='static\\Desktop-1.png')
# lbl=Label(f,bg='black',image=img)
# lbl.place(x=0,y=0)
lbl=Label(f,text='PROFILE PICTURE',height=1,bg='white',fg='#C13584',font=('Helvetica', 10, 'bold'))
lbl.pack()

my_pic = Image.open("static\wp7810664.webp")
resized = my_pic.resize((700,460),Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)
my_label=Label(f, image=new_pic,bg='white')
my_label.pack(pady=2,padx=0)


Button(root,text="Name",width=19,height=2,font="arial 12 bold",fg='white',bg="#C13584").place(x=10,y=100)
B=Entry(root,width=25,fg='black',border=2,bg="white",font=('Microsoft YaHie UI Light',11))
B.place(x=10,y=160)
B.insert(0,'ARINA JOSH')
savebutton=Button(root,text="Username",width=19,height=2,font="arial 12 bold",fg='white',bg="#C13584")
savebutton.place(x=10,y=210)
Ba=Entry(root,width=25,fg='black',border=2,bg="white",font=('Microsoft YaHie UI Light',11))
Ba.place(x=10,y=270)
Ba.insert(0,'artistic_space8')
Button(root,text="About",width=19,height=2,font="arial 12 bold",fg='white',bg="#C13584").place(x=10,y=320)

Button(root,text="Settings",width=19,height=2,font="arial 12 bold",fg='white',bg="#C13584").place(x=10,y=400)

# left_frame = Frame(root, borderwidth=1, bg='#C13584', relief="solid", highlightthickness=2)
# left_frame.pack(side="left", expand=False, fill="y")
# container = Frame(left_frame, borderwidth=1, bg="white", relief="solid")
# container.pack(expand=True, fill="both", padx=2, pady=2)

# btn_frame = Frame(container)
# canvas =Canvas(btn_frame, height=100,bg='white', width=100)
# canvas.pack()
# btn_frame.pack(side=TOP,pady=20)
# btn_frame1 = Frame(container)
# canvas1 = Canvas(btn_frame1, height=100,bg='white', width=100)
# canvas1.pack()
# btn_frame1.pack(side=TOP, padx=20)
# btn_frame2 = Frame(container)
# canvas2 = Canvas(btn_frame2, height=100,bg='white', width=100)
# canvas2.pack()
# btn_frame2.pack(side=TOP, padx=20)
# btn_frame3 = Frame(container)
# canvas3 =Canvas(btn_frame3, height=100,bg='white', width=100)
# canvas3.pack()
# btn_frame3.pack(side=TOP, padx=20)
# def round_rectangle(obj, x1, y1, x2, y2, r=25, **kwargs):    
#     points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
#     return obj.create_polygon(points, **kwargs, smooth=True)
 
# round_rectangle(canvas, 5, 50, 100, 100, 25, fill="#E1306C")
 
# round_rectangle(canvas1, 5, 50, 100, 100, 25, fill="#E1306C")
 
# round_rectangle(canvas2, 5, 50, 100, 100, 25, fill="#E1306C")

# round_rectangle(canvas3, 5, 50, 100, 100, 25, fill="#E1306C")

 
# btn_1 = Button(btn_frame, text="Name", font=("Bold", 13),bg="#E1306C", fg="white", bd=0)
 
# btn_1.place(x=10, y=37, width=80)
# btn_1= Entry(btn_frame,width=40,fg='#57a1f8',border=2,bg="white",font=('Microsoft YaHie UI Light',11))
# btn_1.place(x=10,y=70)
 

# btn_2 = Button(btn_frame1, text="Username", font=("Bold", 11),bg="#E1306C", fg="white", bd=0)

# btn_2.place(x=10, y=57, width=80)
# btn_3 =Button(btn_frame2, text="About", font=("Bold", 11),bg="#E1306C", fg="white", bd=0)
 
# btn_3.place(x=10, y=57, width=80)


# btn_4 = Button(btn_frame3, text="Settings", font=("Bold", 13),bg="#E1306C",fg="white", bd=0)
 
# btn_4.place(x=10, y=57, width=80)

root.mainloop()
