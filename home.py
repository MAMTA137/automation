from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('700x600')
ws.config(bg='black')

img = PhotoImage(file="Gradientb.png")
label = Label(
    ws,
    image=img
)
label.place(x=0, y=0)

ws.title("Home page")


frm_buttons = LabelFrame(ws ,relief=RAISED, bd=2)
frm_buttons.grid(row=0, column=0)


btn_profile = Button(frm_buttons, text="Profile",bg="black",fg="white")
btn_home = Button(frm_buttons, text="Home",bg="black",fg="white")
btn1 = Button(frm_buttons, text="Button1",bg="black",fg="white")
btn2 = Button(frm_buttons, text="Button2",bg="black",fg="white")
btn3 = Button(frm_buttons, text="Logout",bg="black",fg="white")





btn_profile.grid(row=1, column=0, sticky="ew", padx=5, pady=10)
btn_home.grid(row=2, column=0, sticky="ew", padx=5, pady=10)
btn1.grid(row=5, column=0, sticky="ew", padx=5, pady=10)
btn2.grid(row=3, column=0, sticky="ew", padx=5, pady=10)
btn3.grid(row=4, column=0, sticky="ew", padx=5, pady=10)


ws.mainloop()