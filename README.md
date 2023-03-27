
# Audio Data Science Project: ***AI driven audible threat detection for deaf/hearing-impaired people***


## What is the Project about?
Building an AI for sonic recognition of dangers/treats and signal tones in daily sounds (e.g. fire alarm, vehicle sirence or car horns).<br />
<br />
Reason behind the idea: Hearing-impaired or deaf people make around 5% of the worlds population. Whereas, for using an AI in this field, the research and application possibilities are significantly little. Using this CNN as the base for an application, affected people could be instantly warned of dangers through vibrations of a smartphone.<br />
<br />
Project goal: Being able to detect sounds that could be or lead to a serious threat.

## What can you find in this GitHub?
This Git contains the following:<br />

1. [.ipynb_checkpoints](.ipynb_checkpoints)
   - older versions of the main code
2. [.vs](.vs)
   - saved settings
3. [Archive](Archive)
   - code experiments and different code for testing
4. [AudioDataPackage](AudioDataPackage)
   - [ArtificialTraining](ArtificialTraining)
   - [AudioPreprocessing](AudioPreprocessing)
     - [AudioAugmentation](AudioAugmentation)
       - to augment the self recorded samples with the audiomentations library
     - [AudioSetDownloader](AudioSetDownloader)
       - to download the samples from AudioSet etc. and organize it
     - [CutAudioData](CutAudioData)
       - this cuts the audio, so that the lengths are all the same
     - [DatasetSorting](DatasetSorting)
       - this code sorts all the downloaded audiodata to the necessary labels, like the filename, samplerate, threat, salience and importance to name a few
     - [DataDescription](DataDescription.py)
       - this code gives a basic data description of the current audioset
     - [Downloader](Downloader.py)
       - this is for downloading audio files from specific categories from Youtube
     - [LabelProgram](LabelProgram.py)
       - with this program it is possible to update the csv for the audioset to verify each audiofile for its target values, it is also possible to delete single samples (if they are not useful
   - [AudioToInputData](AudioToInputData)
     - prepares the audio data for the input of the network
   - [allAudioDataToSpectrograms.py](allAudioDataToSpectrograms.py)
     - turns all the audio data into spectrograms - each single audio files get cut into smaller segments and these audio snippets get turned into a log spectrogram
5. [AudioTestData](AudioTestData)
   - a single testsample
6. [README.md](README.md)
   - in order to have a good overview of the Git
7. [ToDos.txt](ToDos.txt)
   - document for organizing the structure and upcoming tasks (did not start from beginning of the project)
8. [basicHeader.txt](basicHeader.txt)
9. [deleteUselessFiles.py](deleteUselessFiles.py)
   - this code deletes all the unnecessary audiofiles from the csv
10. [mainCodeV6.x.ipynb](mainCodeV6.x.ipynb)
    - the final main code as Jupyter Notebook format (.ipynb)
11. [requirements.txt](requirements.txt)
    - to create the environment 



## How would you launch the code yourself?
Download the Git<br />
Get all the required libraries<br />
Follow the instructions on the mainCodeV6.x.ipynb file

## About the Authors.

Christian Böndgen & Nick Jonas Kuhoff <br />
Wi/Se 22/23 @ University of Applied Sciences Düsseldorf

## Copyright
