
import sys
import re


fileNameToRead = sys.argv[1]
fileToRead = open(fileNameToRead, "r")

uniqueWordsToCount = {} 

def addKeyOrIncrementCount(word):
	global uniqueWordsToCount
	uniqueWordsToCount[word] = uniqueWordsToCount.get(word, 0) + 1



for line in fileToRead:
	for word in line.split(" "):
		cleanedWord = re.sub('[^A-Za-z0-9]+', '', word.lower())
		print(">> " + cleanedWord)
		addKeyOrIncrementCount(cleanedWord)

fileToRead.close()

def generateFileName(readFileName):
	return readFileName.split(".")[0] + "-count.txt"

def generateTotalsLines():
	totalCount = 0
	uniqueCount = 0
	global uniqueWordsToCount
	for countValue in uniqueWordsToCount.values():
		uniqueCount += 1
		totalCount += countValue
	return "There are {} total words.\nThere are {} unique words.\n\n".format(totalCount, uniqueCount)

fileNameToWrite = generateFileName(fileNameToRead)
fileToWrite = open(fileNameToWrite, "w")
fileToWrite.write(generateTotalsLines())


for (key, value) in uniqueWordsToCount.items():
	fileToWrite.write(key + " - " + str(value) + "\n")

fileToWrite.close()
print("Done Writing! Check out file at : {}".format(fileToWrite.name))





