from createColorMap import*

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# Load audio file
audioname = 'sunnyDay'
audio_path = 'tracks/' + audioname +'.mp3'
y, sr = librosa.load(audio_path)

# Generate spectrogram
D_highres = librosa.stft(y)

#CHOOSE DIAGRAM
spectogram = librosa.feature.melspectrogram(y=y, sr=sr)

#CHOOSE COLORS
newcolors2 = createColorMap(usePink = True, useOrange = True, useGreen = True, useSkyblue = True, useBrown = True, useLightgreen = True, usePurple = True, useBeje = True, useVividgreen = True,useBlue = True, useLightPink = True, useBlack = True)
estefimagic_colormap = ListedColormap(newcolors2, name='estefimagic_colormap')

# Visualize spectrogram
plt.figure(figsize=(1920 / 100, 1080 / 100))
#PW
librosa.display.specshow(spectogram, sr=sr, hop_length=512,cmap=estefimagic_colormap)
#DB
#librosa.display.specshow(librosa.power_to_db(spectogram, ref=np.max), sr=sr, hop_length=512,cmap=estefimagic_colormap)

plt.savefig(audioname+'/'+ audioname + '_' + 'delta' + '_PW', dpi=1000)
plt.show()


