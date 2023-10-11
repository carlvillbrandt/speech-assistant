# Project Name: ChatGPT Voice Assistant

## Overview

The ChatGPT Voice Assistant project is a simple yet powerful application that allows you to have natural language conversations with the ChatGPT language model. This GitHub repository contains the source code and instructions for building your own voice assistant, which can record audio, transcribe it to text, interact with ChatGPT, and convert responses back to speech.

The project comprises three main components:

1. **Voice Recording Interface:** An interface that allows users to start and stop audio recording using buttons. The recorded audio is saved to disk.

2. **Speech-to-Text Conversion:** Utilizes Python's speech recognition library to transcribe the recorded audio into text. This text is then displayed on the interface.

3. **Text-to-Speech Conversion:** Converts ChatGPT's responses from text to speech, making the assistant more engaging and interactive.

## Features

- Record your voice and transcribe your questions for ChatGPT.
- Interact with ChatGPT via the OpenAI API.
- Receive ChatGPT's responses as text.
- Convert ChatGPT's text responses to speech, giving the AI a voice.
  
![Alt Text](/examples/1231089.png)

Before you begin, ensure you have the following tools and libraries installed:

- Python
- SpeechRecognition Python library
- OpenAI Python library
- Any additional libraries required by your chosen text-to-speech engine

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/ChatGPT-Voice-Assistant.git
   ```

2. **Install Dependencies:**

   Install the required Python libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure OpenAI API:**

   Create an OpenAI API key if you don't have one and configure it in your project. You'll need to set up environment variables for this key.

4. **Setup Text-to-Speech Engine:**

   Choose a text-to-speech engine (e.g., gTTS, pyttsx3, or others) and install the required libraries. Ensure the chosen engine is correctly configured.

5. **Run the Application:**

   Execute the main script to start the application:

   ```bash
   python voice_recorder_tkinter.py
   ```

6. **Interact with ChatGPT:**

   - Click the "Start Recording" button to record your question or message.
   - Click the "Stop Recording" button when you're finished.
   - ChatGPT will transcribe your audio, send it to the OpenAI API, and display the response as text.
   - The response is then converted to speech and played through your chosen text-to-speech engine.

## Usage

- Feel free to customize the interface and add more features as desired.
- Modify the OpenAI API interactions for more complex interactions with ChatGPT.
- Adapt the text-to-speech engine settings for a more natural voice.

## Contributing

We welcome contributions to enhance this project. If you have any improvements, bug fixes, or new features to add, please submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions or suggestions, feel free to contact me.

Enjoy conversing with your ChatGPT Voice Assistant!
