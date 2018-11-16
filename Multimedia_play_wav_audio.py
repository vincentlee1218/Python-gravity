"""PyAudio Example: Play a WAVE file."""

import pyaudio
import wave
import sys

CHUNK = 1024
# <a href="/redirect/s3?bucket=uploads&prefix=attach%2Fjnkjs3pfsd750v%2Fjjyfuyn1ezs3ox%2Fjok6szjg6ly0%2FHomer.wav" target="_blank">Homer.wav</a>

wf = wave.open("Homer.wav", 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)

while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()

p.terminate()
