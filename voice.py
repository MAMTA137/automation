from tkinter import Tk, Label,Frame, Button
from PIL import Image, ImageTk
import speech_recognition as sr 


# create a Tkinter window
root = Tk()
root.title("Voice recognizer")
root.geometry('800x600+250+100')
root.configure(bg="#fff")
root.resizable(False,False)

imaage = ImageTk.PhotoImage(Image.open("gradient.jpg"))
bg =Label(root, image=imaage)
bg.place(x=0, y=0, relwidth=1, relheight=1)

frame=Frame(root,width=420,height=400,bg="white")
frame.place(x=200,y=30)

# load the image
img = Image.open("microphone.png")

# resize the image
resized_img = img.resize((150, 150))

# convert the image to a Tkinter-compatible photo image
tkimage = ImageTk.PhotoImage(resized_img)

def voice():
    voice_label = Label(frame,text='Speak:',fg='#57a1f8',border=2,bg="white",font=('Microsoft YaHie UI Light',16))
    voice_label.place(x=90,y=200)
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                                                                                                         
        audio = r.listen(source)   
    try:
        txt = r.recognize_google(audio)
        result_label = Label(frame, text=txt,fg='#57a1f8',bg='white',font=('Microsoft YaHie UI Light',16))
        result_label.place(x=90,y=230)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))


# display the image on a Tkinter label
label = Button(frame, image=tkimage, bg='#fff', relief='groove',activebackground='white',activeforeground='black', borderwidth=2,command=voice)
label.place(x=135,y=30)


def next():
    root.destroy()
    import homepage
next_button = Button(frame, text="Next",fg='#57a1f8',bg='white',font=('Microsoft YaHie UI Light',16),command=next)
next_button.place(x=260,y=320)




# start the Tkinter event loop
root.mainloop()
