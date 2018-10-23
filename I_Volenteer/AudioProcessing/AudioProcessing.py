import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import scipy.io.wavfile as wav

r,yn = wav.read('../Audio Files/AudioTest2noisy.wav')

b, a = sig.butter(2, 0.6,analog=False)

yf = sig.lfilter(b, a, yn)

yf =yf.astype('int16')
yf = yf

wav.write('AudioTest2filtered.wav',r,yf)
