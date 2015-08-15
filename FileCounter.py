import os, sys, pickle

''' 
Counts the number of files of each domain and serializes them 
to a pickle file.
NOTE: Comment Print statements in cosine_similarity.py,DocumentVectors.py,MainRecon.py.
'''

def countFileOccurances(path):
	countDict = {}
	fileList = os.listdir(path)

	for fil in fileList:
		fileClass = fil.split("_")[0]
		
		fc = str(fileClass)
		if(fc not in countDict.keys()):
			countDict[fc] = 0
		countDict[fc] += 1

	return countDict



if __name__ == '__main__':
	
	dataDir = sys.argv[1]
	counts = countFileOccurances(dataDir)
	with open("./FileCounts.pickle",'wb') as fp:
		pickle.dump(counts,fp)
	print(counts)