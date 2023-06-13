import numpy as np

import librosa, librosa.display
import matplotlib.pyplot as plt
FIG_SIZE = (15,10)
file = "ASR_Diplom/flask_serv/saved/audio.wav"
 # Load audio file with Librosa

signal, sample_rate = librosa.load(file, sr=22050)

 # 
def fft():
 # Lerform Fourier transform
    fft = np.fft.fft(signal)
 # Laculate abs values on complex numbers to get magnitude

    spectrum = np.abs(fft)

 # Create frequency variable

    f = np.linspace(0, sample_rate, len(spectrum))

 # Take half of the spectrum and frequency
    left_spectrum = spectrum[:int(len(spectrum)/2)]

    left_f = f[:int(len(spectrum)/2)]
 # Plot spectrum
    plt.figure(figsize=FIG_SIZE)
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude")
    plt.title("Power spectrum")
    plt.show()