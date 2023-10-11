
import openai
import os
import base64



# Set your OpenAI API key
openai.api_key = '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'

# Specify the input audio file path and output text file path
audio_file_path = r"C:\\Users\\CarlVillbrandt\\Documents\\audio_files\\recorded_audio.wav"
output_text_file_path = r"C:\\Users\\CarlVillbrandt\\Documents\\speech_to_text_files\\transcribed_text.txt"

# Function to transcribe audio to text using OpenAI API
def transcribe_audio_to_text(audio_file_path, output_text_file_path):
    try:
        # Read the audio file as binary and encode it in base64
        with open(audio_file_path, 'rb') as audio_file:
            audio_data = base64.b64encode(audio_file.read()).decode('utf-8')

        # Perform transcription using OpenAI GPT-3 API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Transcribe the following audio: {audio_data}"}
            ]
        )

        text = response['choices'][0]['message']['content']

        with open(output_text_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(text)

        print(f"Transcription completed. Text saved to {output_text_file_path}")
    except Exception as e:
        print(f"Error: {str(e)}")

# Call the transcription function
transcribe_audio_to_text(audio_file_path, output_text_file_path)

