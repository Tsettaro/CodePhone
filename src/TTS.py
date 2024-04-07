from langdetect import detect, DetectorFactory
from gtts import gTTS
from src.log import log_tts

def detect_language(text):
    DetectorFactory.seed = 0
    detect_language = detect(text)
    return str(detect_language)

def tts(message):
    audio = gTTS(text=message.text, lang=detect_language(message.text), slow=True)
    log_tts(message.from_user.id, message.text)
    audio.save("audio_text.ogg")