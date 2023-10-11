import os
import tkinter as tk
from tkinter import ttk
import sounddevice as sd
import soundfile as sf
import numpy as np
import keyboard
import subprocess
import speech_recognition as sr

# Set the output folder path
output_folder = "C:\\Users\\CarlVillbrandt\\Documents\\vscode\\voice-recorder\\audio_input"
output_text_file = "C:\\Users\\CarlVillbrandt\\Documents\\vscode\\voice-recorder\\speech_to_text_files\\output.txt"
os.makedirs(output_folder, exist_ok=True)

# Global variables
recording = False

# Function to start or stop recording
def toggle_recording():
    global recording
    if recording:
        recording = False
        record_button.config(text="Press this button to start recording and 'R' to end it")
        transcribe_saved_audio()
    else:
        audio_data = []
        text_box.delete("1.0", tk.END)  # Clear the text box
        record_button.config(text="Recording... (Press 'R' to Stop)")
        recording = True

        def audio_callback(indata, frames, time, status):
            if status:
                print("Error:", status)
            if recording:
                audio_data.append(indata.copy())

        with sd.InputStream(callback=audio_callback):
            keyboard.wait("R")
            recording = False
            record_button.config(text="Press this button to start recording and 'R' to end it")
            print("Recording stopped")

        filename = os.path.join(output_folder, "recorded_audio.wav")
        save_audio(audio_data, filename)

# Function to save audio to a file
def save_audio(audio_data, filename):
    audio_data = np.concatenate(audio_data, axis=0)
    sf.write(filename, audio_data, 44100)

# Function to transcribe saved audio file
def transcribe_saved_audio():
    try:
        # Read the saved audio file
        with sr.AudioFile(os.path.join(output_folder, "recorded_audio.wav")) as source:
            recognizer = sr.Recognizer()
            audio = recognizer.record(source)

        # Use Google Web Speech API for transcription
        text = recognizer.recognize_google(audio)

        # Display the transcribed text in the text box
        text_box.delete("1.0", tk.END)  # Clear the text box
        text_box.insert(tk.END, text)
    except Exception as e:
        print(f"Error: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Voice Recorder")

# Create and configure the record button
record_button = ttk.Button(root, text="Press this button to start recording and 'R' to end it", command=toggle_recording)
record_button.pack()

# Create a "Transcribe" button
transcribe_button = ttk.Button(root, text="Transcribe", command=transcribe_saved_audio)
transcribe_button.pack()

# Create a text box to display the transcribed text
text_box = tk.Text(root, height=10, width=40)
text_box.pack()

# Start the Tkinter main loop
root.mainloop()
