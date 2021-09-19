import pyttsx3

# https://pyttsx3.readthedocs.io/en/latest/index.html

engine = pyttsx3.init()

text = """
Pensez à une décision importante que votre entreprise a prise récemment.
"""

engine.setProperty('voice', 'com.apple.speech.synthesis.voice.thomas')
engine.setProperty('rate', 150)
engine.say(text)
engine.save_to_file(text , 'file.mp3')
engine.runAndWait()
