import pyttsx3
def speak(text):
    engine = pyttsx3.init()  
    engine.say(text)
    engine.runAndWait()
inp = input("what should i speak    ")
speak(inp)
