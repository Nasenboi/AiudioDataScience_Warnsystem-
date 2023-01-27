from dataclasses import dataclass
import os
import pandas as pd

csvPath = r"F:\labeled_audio_data.csv"



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
		print("Count:", df.shape[0])

	print("||||||||||||||||||||||||||||||||||||||")