import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Naslouchám...")
        try:
            audio = recognizer.listen(source, timeout=5)  # Timeout přidá 5 sekundovou prodlevu
            command = recognizer.recognize_google(audio, language="cs-CZ")
            print(f"Rozpoznaný příkaz: {command}")
            return command
        except sr.UnknownValueError:
            print("Nerozpoznáno, zkuste to znovu.")
            return None
        except sr.RequestError as e:
            print(f"Chyba při požadavku na rozpoznávání: {e}")
            return None
        except KeyboardInterrupt:
            print("Naslouchání bylo přerušeno.")
            return None