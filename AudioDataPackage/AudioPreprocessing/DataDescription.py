'''
Title:
	DataDescription.py
Version:
    0

Author(s):
    Christian

Creation Date:
    ?
Update(s):
    Date       | Changes
    24.02.2023 | Added Header

Comment(s):
    This code gives a basic data description of the current audioset.
	It will only read the csv file of the given path, so it cannot really give
	informations about the audiofiles itself.
'''


import os
import pandas as pd
from statistics import mean

csvPath = r"F:\labeled_audio_data_old.csv"

if __name__ == "__main__":
	dataFrame  = pd.read_csv(csvPath)

	print("||||||||||||||||||||||||||||||||||||||")
	print("I will describe this dataframe for you now!")
	print("Have fun reading!")
	print("||||||||||||||||||||||||||||||||||||||")
	for key in dataFrame.keys():
		print("Key Name: " + key)
		print("Statistics:")
		print(dataFrame[key].describe())
		print("||||||||||||||||||||||||||||||||||||||")

	print("Those were the basics stats, now lets see how many sound categorys there are!")
	print("||||||||||||||||||||||||||||||||||||||")
	sounds = dataFrame['mainSound'].unique()
	print("Unique Sounds:")
	print(sounds);
	print("||||||||||||||||||||||||||||||||||||||")
	print("Now lets count them!")
	print(" ")
	for sound in sounds:
		print("Sound: " + str(sound).ljust(17), end=" | ")
		df = dataFrame[dataFrame["mainSound"] == sound]
		print("Count:    ", df.shape[0])
		allValues = [df.to_dict()['threat'].values(), df.to_dict()['salience'].values(), df.to_dict()['importance'].values()]
		valueTypes = ["threat", "salience", "importance"]
		for i in range(len(allValues)):
			averageValue = mean(allValues[i])
			print("Avg", valueTypes[i].ljust(10, " ") , ":", str(round(averageValue, 3)).ljust(5, " "), end=" | ")
		print()
		print()
	print("||||||||||||||||||||||||||||||||||||||")