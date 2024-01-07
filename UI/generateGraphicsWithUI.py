import tkinter as tk
from tkinter import ttk, filedialog
from ttkthemes import ThemedStyle  # Import ThemedStyle
from createColorMap import *
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
import sys
import os

def update_processing_label(label, text, color):
    label.config(text=text, foreground=color)
    
def generate_and_save_plot(audio_name, diagram_type, processing_label, abort_var):
    # Check if abort button was pressed
    if abort_var.get():
        print("Cancelled")
        return

    processing_label.config(text="Processing...")
    
    # Load audio file
    audio_path = 'tracks/' + audio_name + '.mp3'
    y, sr = librosa.load(audio_path)

    # Initialize diagram
    diagram = None

    # Generate diagram based on user input
    if diagram_type == "melspectrogram":
        diagram = librosa.feature.melspectrogram(y=y, sr=sr)
    elif diagram_type == "tempogram":
        diagram = librosa.feature.tempogram(y=y, sr=sr)
    elif diagram_type == "chroma_cqt":
        diagram = librosa.feature.chroma_cqt(y=y, sr=sr)
    elif diagram_type == "poly_features":
        diagram = librosa.feature.poly_features(y=y, sr=sr)
    elif diagram_type == "chroma_cens":
        diagram = librosa.feature.chroma_cens(y=y, sr=sr)
    elif diagram_type == "chroma_stft":
        diagram = librosa.feature.chroma_stft(y=y, sr=sr)
    elif diagram_type == "fourier_tempogram":
        diagram = librosa.feature.fourier_tempogram(y=y, sr=sr)
    elif diagram_type == "spectral_contrast":
        diagram = librosa.feature.spectral_contrast(y=y, sr=sr)
    elif diagram_type == "tonnetz":
        diagram = librosa.feature.tonnetz(y=y, sr=sr)
    elif diagram_type == "tempogram_ratio":
        diagram = librosa.feature.tempogram(y=y, sr=sr)  # Replace with appropriate function
    # Check if abort button was pressed
    if abort_var.get():
        print("Cancelled")
        return

    # Choose colors
    newcolors2 = createColorMap(usePink=True, useOrange=True, useGreen=True, useSkyblue=True, useBrown=True,
                                useLightgreen=True, usePurple=True, useBeje=True, useVividgreen=True,
                                useBlue=True, useLightPink=True, useBlack=True)
    estefimagic_colormap = ListedColormap(newcolors2, name='estefimagic_colormap')

    # Visualize diagram - PW
    plt.figure(figsize=(1920 / 100, 1080 / 100))
    librosa.display.specshow(diagram, sr=sr, hop_length=512, cmap=estefimagic_colormap)
    if not os.path.exists(audio_name):
        os.makedirs(audio_name)

    plt.savefig(audio_name + '/' + audio_name + '_' + diagram_type + '_PW', dpi=1000)

    # Check if abort button was pressed
    if abort_var.get():
        print("Cancelled")
        return

    # Visualize diagram - DB
    plt.figure(figsize=(1920 / 100, 1080 / 100))
    librosa.display.specshow(librosa.power_to_db(diagram, ref=np.max), sr=sr, hop_length=512, cmap=estefimagic_colormap)
    if not os.path.exists(audio_name):
        os.makedirs(audio_name)
    plt.savefig(audio_name + '/' + audio_name + '_' + diagram_type + '_DB', dpi=1000)

    processing_label.config(text="Finished", foreground="green")

def generate_all_plots(audio_name, processing_label, abort_var):
    diagram_types = ["melspectrogram", "tempogram", "chroma_cqt", "poly_features", "chroma_cens", "chroma_stft",
                     "fourier_tempogram", "spectral_contrast", "tonnetz", "tempogram_ratio"]

    for diagram_type in diagram_types:
        generate_and_save_plot(audio_name, diagram_type, processing_label, abort_var)

def browse_audio_file():
    filename = filedialog.askopenfilename(initialdir='tracks/', title='Select Audio File', filetypes=(("MP3 files", "*.mp3"), ("all files", "*.*")))
    audio_name_entry.delete(0, tk.END)
    audio_name_entry.insert(0, filename.split("/")[-1].split(".")[0])

def generate_plots():
    audio_name = audio_name_entry.get()
    generate_all = generate_all_var.get()

    if generate_all:
        abort_var.set(0)
        processing_label.config(text="Processing...", foreground="black")
        generate_all_plots(audio_name, processing_label, abort_var)
    else:
        diagram_type = diagram_type_var.get()
        abort_var.set(0)
        processing_label.config(text="Processing...", foreground="black")
        generate_and_save_plot(audio_name, diagram_type, processing_label, abort_var)

def abort_process():
    abort_var.set(1)
    processing_label.config(text="Cancelled", foreground="red")
    print("Cancelled")

def on_close():
    root.destroy()
    sys.exit()

# Create the main window
root = tk.Tk()
root.title("Audio Diagram Generator")

# Use ThemedStyle
style = ThemedStyle(root)
style.set_theme("plastik")  # You can try different themes: "aqua", "arc", "plastik", "radiance", etc.

# Create and place widgets
audio_name_label = ttk.Label(root, text="Audio Name:")
audio_name_entry = ttk.Entry(root)
browse_button = ttk.Button(root, text="Browse", command=browse_audio_file)

diagram_type_label = ttk.Label(root, text="Diagram Type:")
diagram_types = ["melspectrogram", "tempogram", "chroma_cqt", "poly_features", "chroma_cens", "chroma_stft",
                 "fourier_tempogram", "spectral_contrast", "tonnetz", "tempogram_ratio"]
diagram_type_var = tk.StringVar(value=diagram_types[0])
diagram_type_menu = ttk.Combobox(root, textvariable=diagram_type_var, values=diagram_types, state="readonly")

generate_all_var = tk.BooleanVar(value=False)
generate_all_checkbox = ttk.Checkbutton(root, text="Generate All Diagrams", variable=generate_all_var)

generate_button = ttk.Button(root, text="Generate Plot", command=generate_plots)
abort_button = ttk.Button(root, text="Abort", command=abort_process)

# Processing Label
processing_label = ttk.Label(root, text="", foreground="black")

# Place widgets in the grid
audio_name_label.grid(row=0, column=0, padx=10, pady=10)
audio_name_entry.grid(row=0, column=1, padx=10, pady=10)
browse_button.grid(row=0, column=2, padx=10, pady=10)

diagram_type_label.grid(row=1, column=0, padx=10, pady=10)
diagram_type_menu.grid(row=1, column=1, padx=10, pady=10)

generate_all_checkbox.grid(row=2, column=0, columnspan=3, pady=10)
generate_button.grid(row=3, column=0, pady=10)
abort_button.grid(row=3, column=1, pady=10)

# Processing Label
processing_label.grid(row=4, column=0, columnspan=3, pady=10)

# Abort variable
abort_var = tk.BooleanVar(value=False)

# Bind the window closing event to the on_close function
root.protocol("WM_DELETE_WINDOW", on_close)

# Start the main event loop
root.mainloop()
