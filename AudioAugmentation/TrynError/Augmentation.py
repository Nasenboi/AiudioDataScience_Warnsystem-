"""import tensorflow_io as tfio"""
import librosa
import tensorflow as tf
import tensorflow_io as tfio
import matplotlib.pyplot as plt

"Parsed Macintosh HD/Users/nickjonas/Desktop/Aufnahmen für Uni/Feuerwehr/H2n/Edited/221202-121002_edited.WAV"

import soundfile as sf

filename = librosa.example('221202-121002_edited')
y, sr = librosa.load(filename)
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
beat_times = librosa.frames_to_time(beat_frames, sr=sr)



"""audio = tfio.audio.AudioIOTensor('gs://221202-121002_edited.WAV')
print(audio)

audio_slice = audio[100:]

# remove last dimension
audio_tensor = tf.squeeze(audio_slice, axis=[-1])

print(audio_tensor)

from IPython.display import Audio

Audio(audio_tensor.numpy(), rate=audio.rate.numpy())

tensor = tf.cast(audio_tensor, tf.float32) / 32768.0

plt.figure()
plt.plot(tensor.numpy())
"""

"""
from audiomentations import Compose, AddGaussianNoise, PitchShift, HighPassFilter

augment = Compose([
    AddGaussianNoise(min_amplitude=0.1, max_amplitude=0.2, p=1),
    PitchShift(min_semitones=-8, max_semitones=4000, p=1),
    HighPassFilter(min_cutoff_freq=2000, max_cutoff_freq=4000, p=1)
])

if __name__ == "__main__":
    signal, sr = librosa.load("221202-121002_edited.WAV")
    augmented_signal = augment(signal, sr)
    sf.write("augmented.wav", augmented_signal, sr)
"""



""""
import random
import numpy as np
import soundfile as sf

from helper import _plot_signal_and_augmented_signal

# Python 3.8
# install matplotlib, librosa
# install python3-tk -> sudo apt install python3-tk


def add_white_noise(signal, noise_percentage_factor):
    noise = np.random.normal(0, signal.std(), signal.size)
    augmented_signal = signal + noise * noise_percentage_factor
    return augmented_signal


def time_stretch(signal, time_stretch_rate):
    Time stretching implemented with librosa:
    https://librosa.org/doc/main/generated/librosa.effects.pitch_shift.html?highlight=pitch%20shift#librosa.effects.pitch_shift
    
    return librosa.effects.time_stretch(signal, time_stretch_rate)


def pitch_scale(signal, sr, num_semitones):
    Pitch scaling implemented with librosa:
    https://librosa.org/doc/main/generated/librosa.effects.pitch_shift.html?highlight=pitch%20shift#librosa.effects.pitch_shift
    
    return librosa.effects.pitch_shift(signal, sr, num_semitones)


def random_gain(signal, min_factor=0.1, max_factor=0.12):
    gain_rate = random.uniform(min_factor, max_factor)
    augmented_signal = signal * gain_rate
    return augmented_signal


def invert_polarity(signal):
    return signal * -1


if __name__ == "__main__":
    signal, sr = librosa.load("scale.wav")
    augmented_signal = invert_polarity(signal)
    sf.write("augmented_audio.wav", augmented_signal, sr)
    _plot_signal_and_augmented_signal(signal, augmented_signal, sr)

"""


"audio = tf.audio.AudioIOTensor('Macintosh HD/Users/nickjonas/Desktop/Aufnahmen für Uni/Feuerwehr/H2n/Edited/221202-121002_edited.WAV')"

"print(audio)"
""""
def build_artificial_dataset(num_samples: int):
    data = []
    sampling_rates = []

    for i in range(num_samples):
        y, sr = librosa.load(librosa.ex('nutcracker'))
        data.append(y)
        sampling_rates.append(sr)
    features_dataset = tf.data.Dataset.from_tensor_slices(data)
    labels_dataset = tf.data.Dataset.from_tensor_slices(sampling_rates)
    dataset = tf.data.Dataset.zip((features_dataset, labels_dataset))

    return dataset

ds = build_artificial_dataset(10)

from audiomentations import Compose, AddGaussianNoise, PitchShift, Shift

augmentations_pipeline = Compose(
    [
        AddGaussianNoise(min_amplitude=0.001, max_amplitude=0.015, p=0.5),
        PitchShift(min_semitones=-4, max_semitones=4, p=0.5),
        Shift(min_fraction=-0.5, max_fraction=0.5, p=0.5),
    ]
)

def apply_pipeline(y, sr):
    shifted = augmentations_pipeline(y, sr)
    return shifted


@tf.function
def tf_apply_pipeline(feature, sr, ):
    
    Applies the augmentation pipeline to audio files
    @param y: audio data
    @param sr: sampling rate
    @return: augmented audio data
    
    augmented_feature = tf.numpy_function(
        apply_pipeline, inp=[feature, sr], Tout=tf.float32, name="apply_pipeline"
    )

    return augmented_feature, sr


def augment_audio_dataset(dataset: tf.data.Dataset):
    dataset = dataset.map(tf_apply_pipeline)

    return dataset

ds = augment_audio_dataset(ds)
ds = ds.map(lambda y, sr: (tf.expand_dims(y, axis=-1), sr))"""
