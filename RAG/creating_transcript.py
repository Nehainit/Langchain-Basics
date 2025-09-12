from dotenv import load_dotenv
import os
from openai import OpenAI
import openai
import time
from pydub import AudioSegment
from pydub.utils import which
from pydub import AudioSegment   # ✅ Import first
AudioSegment.converter = r"C:\ffmpeg\ffmpeg-8.0-essentials_build\bin\ffmpeg.exe"

load_dotenv()

# import os
# print("CWD:", os.getcwd())
# print("Files in CWD:", os.listdir())

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# # Trim  first 20 seconds
# audio = AudioSegment.from_file("test_exports/audio.webm")

# # Export to a temporary file (e.g., WAV or MP3)
# audio.export("trimmed.mp3", format="mp3")

with open("trimmed.mp3", "rb") as f:
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=f
    )

with open("test_exports/transcript.txt", "w", encoding="utf-8") as f:
    f.write(transcription.text)
