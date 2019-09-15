import speech_recognition as sr 
r = sr.Recognizer() 
with sr.Microphone() as source:
    print("Say Something")
    audio = r.listen(source,timeout=3,phrase_time_limit=3)
    print("Time Over, Thanks")

try:
    print("TEXT: "+r.recognize_google(audio))
except:
    pass