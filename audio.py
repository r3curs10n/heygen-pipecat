import pyaudio
import asyncio
import threading

# Audio recording parameters
FORMAT = pyaudio.paInt16  # 16-bit int format
CHANNELS = 1              # Mono
RATE = 16000              # 16kHz sample rate
CHUNK = 1600              # Number of frames per buffer
RECORD_SECONDS = 2        # Duration of recording
OUTPUT_FILENAME = "output.wav"

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open the stream for recording
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

print("Recording...")

async def main():
    loop = asyncio.get_running_loop()
    queue = asyncio.Queue()

    def worker(loop, queue):
        while True:
            data = stream.read(CHUNK)
            loop.call_soon_threadsafe(queue.put_nowait, data)

    thread = threading.Thread(target=worker, args=(loop, queue), daemon=True)
    thread.start()

    while True:
        data = await queue.get()
        queue.task_done()
        print(len(data))

asyncio.run(main())

print(f"Recording finished. {d}")
