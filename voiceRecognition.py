import speech_recognition as sr
import pyttsx3
import sys 

'''
recognizer = speech_recognition.Recognizer()

while True:
    
    try:
        with speech_recognition.Microphone() as mic:
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print('recognized {}'.format(text))

    except speech_recognition.UnknownValueError():
        
            recognizer = speech_recognition.Recognizer()
            continue

'''
r = sr.Recognizer()

def voiceDetec():
    with sr.Microphone() as source:
        #print('di algo')
        audio = r.listen(source)

        try:
            #print('wait..')     
            text = r.recognize_google(audio)
            return text
            '''
            print('has dicho: {}'.format(text))
            
            if "new user" in text:
                print('crear un usuario')
            
            if "close" in text:
               
               keyword = 'close'  
               return keyword
           '''
        except:
           # print('No te he entendido')
           pass
