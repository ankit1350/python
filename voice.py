import pyttsx3

engine = pyttsx3.init()

# Read text from a file
with open("codes/my_you.py", "r") as file:
    text = file.read()

engine.say(text)
engine.runAndWait()
