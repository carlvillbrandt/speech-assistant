import openai
openai.api_key = 'YOUR KEY'
audio_file= open("C:\\Users\\CarlVillbrandt\\Documents\\vscode\\voice-recorder\\audio_files\\recorded_audio.wav", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript)
