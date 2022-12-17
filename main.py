import os
#import AudioDataPackage.AudioSetDownloader


os.chdir(os.getcwd() + "/AudioDataPackage/AudioSetDownloader");

print(os.getcwd())

destPath = input("Please give me a destination path! \n");
classDownload =  input("And give me a class to download! \n")

print("python3 process.py download -c \"" + classDownload + "\" -d \"" + destPath + "\"");
try:
    os.system("python3 process.py download -c \"" + classDownload + "\" -d \"" + destPath + "\"");
except:
    print("Error!")