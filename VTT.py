import speech_recognition as sp

def recognize(path):
    AUDIO_FILE = path
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)