import sounddevice as sd
from scipy.io.wavfile import write  
import time

def record_voice(duration, filename):
    print("\n🎙️  Starting voice recording...")
    print(f"📁 Saving as: {filename}")
    print(f"⏱️  Duration: {duration} seconds\n")

    recording = sd.rec(int(duration * 44100), samplerate=44100, channels=2)

    for remaining in range(duration, 0, -1):
        print(f"⏳ Recording... {remaining:2d} seconds left", end="\r", flush=True)
        time.sleep(1)

    sd.wait()
    write(filename, 44100, recording)
    print("\n✅ Recording complete! File saved successfully.")

filename = input("Enter a file name (without extension): ").strip()
filename = f"{filename}.wav"
duration = int(input("Enter the recording duration (in seconds): "))
record_voice(duration, filename)
