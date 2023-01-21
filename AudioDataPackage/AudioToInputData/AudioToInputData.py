#import os
import librosa
import numpy as np
import scipy.signal as sig

def butter_lowpass(cutoff, fs, order=10):
    return sig.butter(order, cutoff, fs=fs, btype='low', analog=False)

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = sig.lfilter(b, a, data, axis = 0)
    return y


def audioToInputData(samples, sampleRateSample, blockSize, hopSize, specBlockSize, specHopSize, sampleRateSpec = None):
    try:
        if(sampleRateSpec):
            #Apply a Low-Pass Filter and resample, idk if this is nescesarry, we vould just load() librosa with a certain samplerate,
            #but idk if its LP to get rid of aliasing
            samples = butter_lowpass_filter(data=samples, cutoff=7000, fs=sampleRateSample)
            samples = librosa.resample(y=samples, orig_sr=sampleRateSample, target_sr=sampleRateSpec, axis = 0)

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