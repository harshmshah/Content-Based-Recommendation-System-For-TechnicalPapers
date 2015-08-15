import math,pre_processing as pre

def getPreProcData(folderPath):
    # Get dictionaries for TF-IDF;
    (tf,idf,N) = pre.create_tf_for_doc(folderPath)
    idf = pre.idf_check(tf,idf)
    wtd = pre.log_freq_weighting(tf)
    idfw = pre.idf_weighting(idf,N)

    return wtd,idfw

def createVectors(tfDict , idfDict):
    #Comment this line for Metrics;
    print("Creating document vectors...")
    vectorDict = {}

    for doc in tfDict:
        docTermFreqDict = tfDict[doc]

        vector = {}
        for wrd in docTermFreqDict:
            if wrd in idfDict.keys():
                vector[wrd] = (float(docTermFreqDict[wrd]) * float(idfDict[wrd]))

        # normalize vector
        normalizationFactor = 0
        for item in vector.keys():
            normalizationFactor += (vector[item] * vector[item])
        normalizationFactor = math.sqrt(normalizationFactor)

        normalizedVector = {}
        for itm in vector.keys():
            normalizedVector[itm] = float(vector[itm]/normalizationFactor)

        # store in the vectorDict;
        vectorDict[doc] = normalizedVector

        # if(len(vectorDict) != len(tfDict)):
        #     print("Error in createVectors: dictionary size mismatch")

    return vectorDict


if __name__ == '__main__':
    print("FileName: DocumentVectors.py")
    tf,idf = getPreProcData()
    normVectorDict = createVectors(tf,idf)