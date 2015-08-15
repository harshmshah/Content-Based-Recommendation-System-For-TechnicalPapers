import sys,queue,os,pickle
import DocumentVectors as dvec
import cosine_similarity as csim
import wordnet as wn

def writeOutput(result):
    #Comment this line for Metrics;
    print("\n" + "RESULTS ----->" + "\n")
    while(not result.empty()):
        # print(result.get())
        temp = result.get()
        simScore = temp[0]
        fileName = temp[1]
        print("FileName: " + fileName + " " + "Score: " + str(simScore))

if __name__ == '__main__':
    dataPath = sys.argv[1]
    seedDocument = sys.argv[2]
    rank = int(sys.argv[3])

    pickleTf = "./tf.pickle"
    pickleIdf = "./idf.pickle"
    reComputeTfIdfFlag = False

    fileToRecommend = seedDocument.split("/").pop()
    #Comment this line for Metrics;
    print("\nSeed File: " +fileToRecommend + "\n")

    resultQueue = queue.PriorityQueue()

    tf = {}
    idf = {}

    if( os.path.exists(pickleTf) ):
        tFile = open(pickleTf,'rb')
        tf = pickle.load(tFile)
        tFile.close()
        reComputeTfIdfFlag = True

    if( os.path.exists(pickleIdf) ):
        iFile = open(pickleIdf,'rb')
        idf = pickle.load(iFile)
        iFile.close()
        reComputeTfIdfFlag = True

    #Comment this line for Metrics;
    if( reComputeTfIdfFlag ):
        print("Computing TF-IDF scores...")

    if(not reComputeTfIdfFlag):
        #Comment this line for Metrics;
        print("Computing TF-IDF scores...")
        tf,idf = dvec.getPreProcData(dataPath)

        #dump tf dictionary;
        with open(pickleTf,'wb') as tfOutFile:
            pickle.dump(tf,tfOutFile)

        #dump idf dictionary;
        with open(pickleIdf,'wb') as idfOutFile:
            pickle.dump(idf,idfOutFile)



    docVectors = dvec.createVectors(tf,idf)
    # print(docVectors.keys())

    seedVector = docVectors[fileToRecommend]

    #Recompute  wieghts for input vector to perform semantic analysis
    seedVector = wn.term_re_weighting(seedVector)
    seedVector = wn.term_expansion(seedVector)

    resultQueue = csim.cosine_similarity(fileToRecommend,seedVector,docVectors,rank)
    writeOutput(resultQueue)



