# import deepspeech
from gtts import gTTS
import random
import time
import playsound
import speech_recognition as sr

def listen_command():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Орусча суйло: ")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        our_speech = r.recognize_google(audio, language="ru")
        print("Кожойун: "+our_speech)
        return our_speech
    except sr.UnknownValueError:
        return "ой! Ката"
    except sr.RequestError:
        return "Катачылык"

    # return input("Скажите вашу команду: ")

def do_this_command(message):
    message = message.lower()
    if "салам" in message:
        say_message("салам Кожоюн! иштериниз жакшыбы?")
    elif "отлично что делаешь" in message:
        say_message("Кыргызча окуй албай чарчадым")
    elif "тогда отдыхай" in message:
        say_message("Сиздагы джакшы эс алыныз!")
        exit()
    else:
        say_message("Кайталап койунузчу!")

def say_message(message):
    voice = gTTS(message, lang="ru")
    file_voice_name = "_audio_"+str(time.time())+"_"+str(random.randint(0,10000))+".mp3"
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    print("Эдельвейс: "+message)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)