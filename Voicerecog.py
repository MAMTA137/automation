import speech_recognition as sr  

# get audio from the microphone                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)   

try:
    print(" " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))





















""" import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

with sr.Microphone() as source2:
    r.adjust_for_ambient_noise(source2, duration=0.05)
    audio2 = r.listen(source2)
    MyText = r.recognize_google(audio2)
    MyText = MyText.lower()
    print("Did you say  " +MyText)
    SpeakText(MyText) """



























""" import speech_recognition as sr

recording = sr.Recognizer()

with sr.Microphone() as source: recording.adjust_for_ambient_noise(source)
print("Please Say something:")
audio = recording.listen(source)

try:
    print("You said: n" + recording.recognize_google(audio))
except Exception as e:
    print(e) """
""" import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    data = r.record(source, duration=5)
    print(“S”)
    text = r.recognize_google(data,language=’tr’)
    print(text) """