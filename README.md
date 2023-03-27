
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
   - older versions of the main code and different code for testing
4. [AudioDataPackage](AudioDataPackage)
   - [ArtificialTraining](ArtificialTraining)
   - [AudioPreprocessing](AudioPreprocessing),
     - [AudioAugmentation](AudioAugmentation),
       - to augment the self recorded samples
     - [AudioSetDownloader](AudioSetDownloader),
       - to download the samples from google etc.
     - [CutAudioData](CutAudioData),
       - this cuts the audio in 
     - [DatasetSorting](DatasetSorting),
     - [DataDescription](DataDescription.py),
     - [Downloader](Downloader.py),
     - [LabelProgram](LabelProgram.py)
   - [AudioToInputData](AudioToInputData)
   - [allAudioDataToSpectrograms.py](allAudioDataToSpectrograms.py)
5. [AudioTestData](AudioTestData)
   - to test a single sample
6. [README.md](README.md)
   - in order to have a good overview of the GitHub 
7. [ToDos.txt](ToDos.txt)
   - txt file for organizing the structure and upcoming tasks
8. [basicHeader.txt](basicHeader.txt)
9. [deleteUselessFiles.py](deleteUselessFiles.py)
10. [mainCodeV6.x.ipynb](mainCodeV6.x.ipynb)
    - the final main code as Jupyter Notebook format (.ipynb)
11. [requirements.txt](requirements.txt)
    - to create an environment 



## How would you launch the code yourself?
Download the Git<br />
Get all the required libraries<br />
Follow the instructions on the mainCodeV6.x.ipynb file

## About the Authors.

Christian Böndgen & Nick Jonas Kuhoff <br />
Wi/Se 22/23 @ University of Applied Sciences Düsseldorf

## Copyright
