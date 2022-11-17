#Hier werde ich nur die Basics von librosa testen ^^
#import os
import librosa
import librosa.util
#from AudioDataPackage.AudioPreprocessing.CutAudioData import CutAudioData as cut



# 1. Get the file path to an included audio example
filename = 'AudioTestData/bruh.wav'

waveform, samplerate = librosa.load(filename)

frame_length = samplerate
hop_length = frame_length

snippets = librosa.util.frame(waveform, frame_length, hop_length)

print(snippets)