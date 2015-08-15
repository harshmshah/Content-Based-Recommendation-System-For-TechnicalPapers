import os
import math
import sys
#idf = {}
#tf = {}
#path = sys.argv[1] #"/home/shivani/Desktop/data"


def remove_punc(s):
	punc=(",./;'?$!#()={}:<>~\"0123456789[]")
	otherpunc = ("-")
	tr = {ord(c): None for c in punc}
	tr1 = {ord(c): " " for c in otherpunc}
	strp = s.translate(tr)
	strp = strp.translate(tr1)
	return strp

def create_tf_for_doc(path):
	# path = sys.argv[1]
	idf = {}
	tf = {}
	count  = 0
	dirs = os.listdir(path)
	for file in dirs:
		count = count + 1
		tf[file] = {}
		fpath = path + "/" + file 
		fp = open(fpath,'r',errors = 'ignore')
		for lines in fp:
			#print(lines)
			if lines != " " or lines != "\n":
				line=lines.strip("\n")
				line=line.strip(" ")
				line=remove_punc(line)
				#print(line)
				s1=line.split(" ")
				for i in range(len(s1)):
					if not (s1[i] == ""):
						s = s1[i].lower()
						if(s not in idf):
							idf[s] = 0
						if(s not in tf[file]):
							tf[file][s] = 1
						else:
							tf[file][s] = tf[file][s] + 1
		

	return (tf,idf,count)
			

def idf_check(tf,idf):
			
	for word in idf:
		for key in tf:
			if(word in tf[key]):
				idf[word] = idf[word] + 1

	return idf

	
def log_freq_weighting(tf):

	for key in tf:
		for word in tf[key]:
			if(tf[key][word] > 0):
				tf[key][word] = 1 + math.log10(tf[key][word])
			else:
				tf[key][word] = 0

	return tf


def idf_weighting(idf,N):

	for key in idf:
		idf[key] = math.log10(N/idf[key])

	return idf



if __name__ == '__main__':
	folderPath = sys.argv[1]
	(tf,idf,N) = create_tf_for_doc(folderPath) # N ----> count of files in dataset
	#print(tf)
	#print(idf)
	idf = idf_check(tf,idf)
	#print("-----------------------------------------------------------------------")
	#print(idf)
	wtd = log_freq_weighting(tf)
	#print("-----------------------------------------------------------------------")
	# print(wtd)
	idfw = idf_weighting(idf,N)
	# print("-----------------------------------------------------------------------")
	# print(idfw)
