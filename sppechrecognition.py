import speech_recognition as sr

def recognize_speech_from_mic():
    # Initialize recognizer class (for recognizing the speech)
    recognizer = sr.Recognizer()

    # Use the microphone as source for input.
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("Listening...")

        # Listen for the first phrase and extract it into audio data
        audio_data = recognizer.listen(source)

        print("Recognizing...")
        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    recognize_speech_from_mic()