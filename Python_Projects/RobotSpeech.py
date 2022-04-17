'''Text to speech Talker'''

import sys

try:
    import pyttsx3
except ImportError:
    print('The pyttsx3 module needs to be installed')


tts = pyttsx3.init() #Initialize the TTS engine

print('Enter the text to speak or QUIT to quit.')

while True:
    text = input('>>')

    if text.upper() == 'QUIT':
        print('Thanks for playing')
        sys.exit()

    tts.say(text)
    tts.runAndWait()


    

