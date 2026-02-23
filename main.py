from fastapi import FastAPI
from piper import PiperVoice
import hashlib
import os

app = FastAPI()

voice = PiperVoice.load("en_GB-alan-medium.onnx")

@app.post("/speak")
def speak(text: str):
    h = hashlib.sha1(text.encode()).hexdigest()
    path = f"cache/{h}.wav"

    if not os.path.exists(path):
        voice.synthesize(text, path)

    return {"url": f"/audio/{h}.wav"}

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
