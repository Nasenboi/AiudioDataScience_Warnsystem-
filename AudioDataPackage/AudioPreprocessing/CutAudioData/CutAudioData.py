import math
#import numpy as np
import librosa
#import matplotlib.pyplot as plt
#import librosa.display

def getSnippets(filename):
    waveform, samplerate = librosa.load(filename)
    #waveform, _ = librosa.effects.trim(waveform)

    snippets = []

    numSnippets = math.floor(len(waveform) / samplerate)
    print(waveform)
    '''
    for i in range(0, numSnippets, 2):
        start = i*samplerate
        stop = start + samplerate

        snippets[i] = waveform[0][start:stop]
        snippets[i+1] = waveform[1][start:stop]
'''

    return snippets