from gtts import gTTS
import os

# Define the input text file path
input_text_file = "C:\\Users\\CarlVillbrandt\\Documents\\vscode\\voice-recorder\\text_for_output\\text.txt"

# Define the output audio file path
output_audio_file = "C:\\Users\\CarlVillbrandt\\Documents\\vscode\\voice-recorder\\audio_output\\output.mp3"

# Read the text from the input file
with open(input_text_file, "r", encoding="utf-8") as file:
    text = file.read()

# Create a gTTS object
tts = gTTS(text, lang="en")  # You can specify the language here

# Save the audio to the output file
tts.save(output_audio_file)

print(f"Text-to-speech conversion complete. Audio saved to: {output_audio_file}")
