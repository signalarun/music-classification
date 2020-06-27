import scipy.io.wavfile as wavefile
import matplotlib.pyplot as plt

sample_rate, X = wavefile.read("/home/red/PycharmProjects/music-classification/dataset/Alesis-Fusion-Voice-Oohs-C4.wav")
print( "Sample rate is " + str(sample_rate), "\nNumber of samples " + str(X.shape)) # Sample rate and number of samples

plt.specgram(X[:, 1], Fs=sample_rate, xextent=(0, 30))
plt.show()