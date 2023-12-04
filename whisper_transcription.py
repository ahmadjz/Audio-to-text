import whisper
from tqdm import tqdm
import time
import audio_metadata
from threading import Thread
import tkinter as tk
from tkinter import filedialog, ttk

# Function to simulate progress
def simulate_progress(duration, interval=0.1):
    for _ in tqdm(range(int(duration / interval)), desc="Transcribing"):
        time.sleep(interval)

# Function to select model
def select_model():
    def on_closing():
        if model_var.get():
            root.destroy()

    root = tk.Tk()
    root.title("Select Whisper Model")
    model_var = tk.StringVar(value="medium")  # Default value

    ttk.Label(root, text="Choose a model:").pack(pady=10)
    model_dropdown = ttk.Combobox(root, textvariable=model_var, values=["tiny", "base", "small", "medium", "large"])
    model_dropdown.pack(pady=10)
    model_dropdown.current(3)  # Default selection (medium)

    ttk.Button(root, text="Select", command=on_closing).pack(pady=10)

    root.protocol("WM_DELETE_WINDOW", on_closing)  # Handle window closing
    root.mainloop()
    return model_var.get()

# Function to select file
def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    root.destroy()  # Close the Tkinter window
    return file_path

# Get model from user
selected_model = select_model()
if not selected_model:
    print("No model selected. Exiting.")
    exit()

# Load whisper model
print(f"Start loading {selected_model} model")
model = whisper.load_model(selected_model)
print("Model loaded")

# Get file from user
audio_file = select_file()
if not audio_file:  # Check if a file was selected
    print("No file selected. Exiting.")
    exit()

# Get duration of audio file for progress simulation
metadata = audio_metadata.load(audio_file)
duration = metadata.streaminfo.duration

# Start a separate thread for progress simulation
progress_thread = Thread(target=simulate_progress, args=(duration,))
progress_thread.start()

# Transcribe audio
result = model.transcribe(audio_file)

# Wait for progress simulation to complete
progress_thread.join()

# Output file path
output_file = audio_file.rsplit('.', 1)[0] + ".txt"

# Write result to file
with open(output_file, "w", encoding="utf-8") as file:
    file.write(result["text"])

print("Done")
