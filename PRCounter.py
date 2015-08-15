import os, sys, pickle

''' 
1. Calculates the Precision/Recall of the files recommended by the system.
2. Accepts the terminal output of recommendation system as command line agument.
3. Calculates metrics for all classes found on the output.
4. NOTE: Comment Print statements in cosine_similarity.py,DocumentVectors.py,MainRecon.py.
'''


def readPickle(pickleFile):
	pf = open(pickleFile,'rb')
	fDict = pickle.load(pf)
	pf.close()
	return fDict


def countOccurances(inFile):
	classDict = {}
	lineCount = 0

	fl = open(inFile,'r')
	for line in fl:
		lineCount += 1
		fname = line.split()[1]
		className = fname.split("_")[0]
		
		if(className not in classDict.keys()):
			classDict[className] = 0
		classDict[className] += 1
	fl.close()
	return classDict,lineCount


def calculatePR(clDict,totDict,rank):
	precision = {}
	recall = {}

	for cls in clDict.keys():
		if cls in totDict.keys():
			print("\nCLASS: " + str(cls) + " " + "Rank: " + str(rank))
			precision[cls] = float(clDict[cls] / rank)
			recall[cls] = float(clDict[cls] / totDict[cls])
			print("Precision: " + str(precision[cls]))
			print("Recall: " + str(recall[cls]))




if __name__ == '__main__':
	inFileRecomOutput = sys.argv[1]
	pickleFile = "./FileCounts.pickle"

	clsDict,count = countOccurances(inFileRecomOutput)
	totalDict = readPickle(pickleFile)

	calculatePR(clsDict,totalDict,count)


