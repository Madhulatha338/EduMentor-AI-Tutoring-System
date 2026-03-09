import queue
import sounddevice as sd
import json
from vosk import Model, KaldiRecognizer
import pyttsx3

# queue for microphone data
q = queue.Queue()

# initialize speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)
# change speed of speech
engine.setProperty('rate', 150)

def speak(text):
    try:
        engine.stop()
        engine.say(text)
        engine.runAndWait()
    except RuntimeError:
        pass


# load Vosk model
model = Model("model")

def callback(indata, frames, time, status):
    q.put(bytes(indata))


def listen():
    samplerate = 16000
    recognizer = KaldiRecognizer(model, samplerate)

    with sd.RawInputStream(
        samplerate=samplerate,
        blocksize=8000,
        dtype="int16",
        channels=1,
        callback=callback
    ):

        print("🎤 Speak your question...")

        while True:
            data = q.get()

            if recognizer.AcceptWaveform(data):

                result = json.loads(recognizer.Result())

                text = result.get("text", "")

                return text