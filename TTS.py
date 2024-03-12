from langdetect import detect, DetectorFactory
from gtts import gTTS

def detect_language(text):
    DetectorFactory.seed = 0
    detect_language = detect(text)
    return str(detect_language)

def tts(_text):
    audio = gTTS(text=_text, lang=detect_language(_text), slow=True)
    audio.save("audio_text.ogg")