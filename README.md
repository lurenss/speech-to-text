# Whisper Speech to Text Converter

A Streamlit web application that converts speech from audio files to text using OpenAI's Whisper model.

## Features

- Upload audio files (supports multiple formats: MP3, WAV, M4A, OGG)
- Choose from different Whisper model sizes (tiny, base, small, medium, large)
- Convert speech to text using state-of-the-art Whisper model
- Preview uploaded audio files
- Download transcribed text
- Clean and modern user interface with real-time updates

## Installation

1. Clone this repository

2. Install FFmpeg (required for audio processing):
   - On macOS: `brew install ffmpeg`
   - On Ubuntu: `sudo apt update && sudo apt install ffmpeg`
   - On Windows: Download from [FFmpeg website](https://ffmpeg.org/download.html)

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Your web browser will automatically open to the application
3. Select a Whisper model size from the sidebar (larger models are more accurate but slower)
4. Upload an audio file and click "Transcribe Audio"
5. The transcribed text will appear below and can be downloaded as a text file

## Model Sizes

- **tiny**: Fastest, least accurate
- **base**: Fast, reasonable accuracy
- **small**: Good balance of speed and accuracy
- **medium**: More accurate, slower
- **large**: Most accurate, slowest

## Requirements

- Python 3.7 or higher
- FFmpeg
- Streamlit
- OpenAI Whisper
- PyTorch
- FFmpeg-python

## Note

The first time you use a particular model size, it will be downloaded automatically. Larger models require more disk space and memory.
