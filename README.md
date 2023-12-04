# Audio-to-text

This repository contains a Python script for transcribing audio files using OpenAI's Whisper AI model. It's designed to be user-friendly and efficient, suitable for various applications requiring audio-to-text conversion.

## Features

- User-Friendly File Selection: GUI-based file selection using tkinter.

- Progress Visualization: Real-time progress updates with tqdm.

- Multiple Format Support: Compatible with .mp3 and .wav files.

- Accurate Transcription: Leverages the Whisper AI model for precise transcriptions.

- Responsive Design: Runs progress simulation on a separate thread for better UI responsiveness.

  ## Requirements

- Python 3.x

- whisper

- tqdm

- audio_metadata

- tkinter

## Installation

- Clone the repository

```
git clone https://github.com/ahmadjz/Audio-to-text.git
```

- Navigate to the cloned directory:

```
cd Audio-to-text
```

- Install the required Python dependencies:

```
pip install whisper tqdm audio_metadata
```

Check if `tkinter` is already installed with your Python distribution (it's usually installed by default).

## Usage

- Run the script:

```
python whisper_transcription.py
```

- Select the model you want to use, here the differences between models [Available models and languages](https://github.com/openai/whisper#available-models-and-languages)

- Select an audio file when prompted.

- Wait for the transcription to complete.

- The transcribed text will be saved in the same directory as the audio file, with a `.txt` extension.

## Contributing

Your contributions are welcome! Feel free to fork the repository, make changes, and submit pull requests. You can also open issues for suggestions or to report bugs.
