__author__ = 'harshmshah'
import queue


def cosine_similarity(fileName,vector_doc1,docs_dataset,rank) :
    """
    Checks the cosine similarity betweeen all the documents in the dataset to the given document.
        Parameters : fineName - The input file name to which the similar documents need to be recommended.
                     vector_doc1 - The input document to which the similar documents need to be recommended.
                     docs_dataset - The documents dataset dictionary within which we need to recommend the the
                                   most 5 similar documents to the given document.
                     rank - the number of similar documents required in the output.
    """

    #Comment this line for Metrics;
    print("Finding similar doucments...")
    RANK  = rank

    # This Priority Queue maintains the rank of the top ranked  similar documents.
    # It store the items in the format of a tuple as (score, document_name)
    rank_q = queue.PriorityQueue(RANK)
    
    # Check to seee if the word contains in both the documents.
    # If it does then include its tf-idf normalized weights in the computation of cosine similarity score.

    max_score = 0
    for doc in docs_dataset.keys():
        # skip the seed document;
        if doc == str(fileName):
            continue

        doc_dict = docs_dataset[doc];
        sumi = 0.0
        for words_doc1 in vector_doc1:
            if words_doc1 in doc_dict:
                dot_product = (float(vector_doc1[words_doc1]) * float(doc_dict[words_doc1]))
                sumi = sumi + dot_product
        #get_similar_doc(sum,doc, rank_q)

        # Maintain a rank queue with the best 5 documents rank related to the given document
        # if (not rank_q.empty()):
        #     smallest_elem = rank_q.get()
        #     if (sumi > smallest_elem[0]):
        #         rank_q.put((sumi, doc))
        #     else:
        #         rank_q.put(smallest_elem)
        # else :
        #     rank_q.put((sumi,doc))
        # print("-----> " + str(doc) + " " + str(sumi))

        
        if(rank_q.qsize() < RANK):
            rank_q.put((sumi,doc))
        else:
            smallest_elem = rank_q.get()
            if(sumi < smallest_elem[0]):
                rank_q.put(smallest_elem)
            else:
                rank_q.put((sumi,doc))



    # while(not rank_q.empty()):
    #     print("in rank Q")
    #     print(rank_q.get())

    return rank_q

"""
def get_similar_doc(sum, doc, queue_q):

    smallest_elem = queue_q.get()
    if ( sum > smallest_elem):
        queue_q.put(10,'ten')
    else :
        queue_q.put(smallest_elem)

"""
