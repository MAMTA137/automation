from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk,Image


root = tk.Tk()
root.geometry("1100x700")

root.resizable(False,False)

imaage = ImageTk.PhotoImage(Image.open("static\\gradient.jpg"))
bg =Label(root, image=imaage)
bg.place(x=0, y=0, relwidth=1, relheight=1)

left_frame = tk.Frame(root, borderwidth=1, bg='#C13584', relief="solid", highlightthickness=2)
left_frame.pack(side="left", expand=False, fill="y")
container = tk.Frame(left_frame, borderwidth=1, bg="white", relief="solid")
container.pack(expand=True, fill="both", padx=5, pady=5)



right_frame1 = tk.Frame(root, borderwidth=1, bg='#C13584', relief="solid", highlightthickness=2)
right_frame1.pack(side="top", expand=False, fill="y")

container1 = tk.Frame(right_frame1, borderwidth=1, bg="white", relief="solid")
container1.pack(expand=True, fill="y", padx=5, pady=5)

Label(container1,text='AUTOGRAM',width=140,height=2,bg='white',fg='#C13584',font=('Helvetica', 30, 'bold')).pack(side=TOP,fill=X)
container1.config(width=800)



#8FBC8F
btn_frame = tk.Frame(container)
canvas = tk.Canvas(btn_frame, height=100,bg='white', width=100)
canvas.pack()
btn_frame.pack(side=tk.TOP,padx=20)
btn_frame1 = tk.Frame(container)
canvas1 = tk.Canvas(btn_frame1, height=100,bg='white', width=100)
canvas1.pack()
btn_frame1.pack(side=tk.TOP, padx=20)
btn_frame2 = tk.Frame(container)
canvas2 = tk.Canvas(btn_frame2, height=100,bg='white', width=100)
canvas2.pack()
btn_frame2.pack(side=tk.TOP, padx=20)
btn_frame3 = tk.Frame(container)
canvas3 = tk.Canvas(btn_frame3, height=100,bg='white', width=100)
canvas3.pack()
btn_frame3.pack(side=tk.TOP, padx=20)
def round_rectangle(obj, x1, y1, x2, y2, r=25, **kwargs):    
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    return obj.create_polygon(points, **kwargs, smooth=True)
 
round_rectangle(canvas, 5, 50, 100, 100, 25, fill="#E1306C")
 
round_rectangle(canvas1, 5, 50, 100, 100, 25, fill="#E1306C")
 
round_rectangle(canvas2, 5, 50, 100, 100, 25, fill="#E1306C")

round_rectangle(canvas3, 5, 50, 100, 100, 25, fill="#E1306C")
def voice():
  root.destroy()
  import voice
 
btn_1 = tk.Button(btn_frame, text=" Speak ", font=("Bold", 13),command=voice,bg="#E1306C", fg="white", bd=0)
 
btn_1.place(x=10, y=57, width=80)
 
 
def trend():
  root.destroy()
  import trending
btn_2 = tk.Button(btn_frame1, text="Trendings", font=("Bold", 11),bg="#E1306C", fg="white", bd=0,command=trend)
def search():
   root.destroy()
   import search
btn_2.place(x=10, y=57, width=80)
btn_3 = tk.Button(btn_frame2, text="Search", font=("Bold", 11),bg="#E1306C", fg="white", bd=0,command=search)
 
btn_3.place(x=10, y=57, width=80)

def post():
  root.destroy()
  import post
btn_4 = tk.Button(btn_frame3, text="Post", font=("Bold", 13),bg="#E1306C", command=post,fg="white", bd=0)
 
btn_4.place(x=10, y=57, width=80)


my_pic = Image.open("static\\WhatsApp Image 2023-04-04 at 9.20.58 PM.jpeg")

#resize image

resized = my_pic.resize((900,560),Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)
my_label=Label(root, image=new_pic,bg='white')
my_label.pack(pady=10,padx=5)

root.mainloop()
