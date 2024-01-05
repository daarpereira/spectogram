from createColorMap import*

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# Load audio file
audio_path = 'gravelWalk.mp3'
y, sr = librosa.load(audio_path)

# Generate spectrogram
D_highres = librosa.stft(y, hop_length=256, n_fft=4096)
S_db = librosa.amplitude_to_db(np.abs(D_highres), ref=np.max)

# Visualize spectrogram
plt.figure(figsize=(1920 / 100, 1080 / 100))
newcolors2 = createColorMap()
estefimagicolormap = ListedColormap(newcolors2, name='estefimagicolormap')

chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
fig, ax = plt.subplots()
img = librosa.display.specshow(chroma, y_axis='chroma', x_axis='time', ax=ax, cmap=estefimagicolormap)
ax.set(title='Chromagram demonstration')
fig.colorbar(img, ax=ax)

plt.savefig('./', dpi=1000)
plt.show()
