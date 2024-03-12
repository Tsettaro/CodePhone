import wave, re
from vosk import Model, KaldiRecognizer
from faster_whisper import WhisperModel

pattern = r'"text" : "([^"]+)"'
model = Model("models/vosk-model-small-ru-0.22")

# Random variables for stable work
l = 0
c = 0
def recognize_vosk(wav_file):
    wf = wave.open(wav_file, "rb")
    global l, c
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)
    rec.SetPartialWords(True)

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            l+=1
        else:
            c+=1
    result = re.search(pattern, rec.Result())
    return result.group(1)

def recognize_whisper(wav_file):
    base = WhisperModel("medium", device="cpu", compute_type="int8")
    segments, _ = base.transcribe(wav_file)
    result = ''.join(segment.text for segment in segments) 
    return result