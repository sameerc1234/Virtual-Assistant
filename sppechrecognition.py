import speech_recognition as sr
import webbrowser
import time

def recognize_speech_from_mic():
    # Initialize recognizer class (for recognizing the speech)
    recognizer = sr.Recognizer()

    # Use the microphone as source for input.
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        print("Listening...")

        try:
            # Listen for the first phrase and extract it into audio data
            audio_data = recognizer.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            print("Timeout, no speech detected.")
            return

        print("Recognizing...")
        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data).lower()  # Convert the recognized text to lowercase
            print("You said: " + text)

            # Check for specific commands to open YouTube or Google
            if "youtube" in text:
                print("Opening YouTube...")
                webbrowser.open("https://www.youtube.com")
                time.sleep(2)  # Add a small delay to ensure it opens
            elif "google" in text:
                print("Opening Google...")
                webbrowser.open("https://www.google.com")
                time.sleep(2)  # Add a small delay to ensure it opens
            else:
                print("Command not recognized. Try saying 'YouTube' or 'Google'.")

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    recognize_speech_from_mic()
