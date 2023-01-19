#import os
import librosa
import numpy as np



def audioToInputData(samples, sampleRate, blockSize, hopSize, specBlockSize, specHopSize):
    try:
        #Calculate initial variables
        N = len(samples)
        if (N<blockSize):
            print("Error: Num samples is too short!")
            return []

        #Add zeros until a certain size
        if(N-blockSize % hopSize != 0):
            numToAdd = hopSize-((N-blockSize)%hopSize)
            toAdd = np.zeros(numToAdd)
            samples = np.append(samples, toAdd, axis = 0)

        #Collect the Audioframes
        audioFrames = librosa.util.frame(samples, frame_length=blockSize, hop_length=hopSize, axis = 0);

        #Calculate the spectrogram of every single frame
        specList = []
        for frame in audioFrames:
            spec = librosa.stft(frame, n_fft=specBlockSize, hop_length=specHopSize)
            specList.append(spec)


        return specList    
    except:
        print("Something went wrong!")
        return []