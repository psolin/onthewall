#!/usr/bin/env python3

import speech_recognition as sr


def say_it():
    recognition = True

    while recognition:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Waiting for the trigger...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

            try:
                if r.recognize_google(audio) == "Mirror Mirror":

                    try:
                        print("Yes, beautiful?")
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                        print("Processing...")
                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio.  Try again.")
                        recognition = True
                    except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))
                        recognition = False

                    command = r.recognize_google(audio)
                    print("Your command is: '%s'" % command)
                else:
                    print("That's not the trigger.")
                    recognition = True

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio.  Try again.")
                recognition = True
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                recognition = False


say_it()
