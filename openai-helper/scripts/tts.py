from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Let's talk about setting up github copilot for your account. First, you have to go to the settings page. Next, you click on the 'Copilot' entry."
)

response.stream_to_file(speech_file_path)