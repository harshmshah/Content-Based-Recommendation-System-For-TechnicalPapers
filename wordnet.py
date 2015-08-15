__author__ = 'harshmshah'
from nltk.corpus import  wordnet


def term_re_weighting(vector_seedDoc) :
    """
    :desc - This fucntions recomputes the weights for all the similar words who have their similarity greater then 0.8
    :param vector_seedDoc: The vector for the input document
    :return: re-weighted vectors for the document.
    """
    for words in vector_seedDoc :
        for words2 in vector_seedDoc :
            if words != words2 :
                if words.path_similarity(words2) > 0.8 :
                   vector_seedDoc[words] += vector_seedDoc[words] + ( vector_seedDoc[words2] * words.path_similarity(words2) )
    return vector_seedDoc


def term_expansion (vector_seedDoc) :
    """
    :desc: This function adds all the synonyms, hyponyms, hypernyms to the vector space of the input document.
    :param vector_seedDoc: The vector of input document for which we need to find similar documents.

    """
    synonyms = []
    hyponyms = []
    hypernymns = []
    for words in vector_seedDoc:
        for syn in wordnet.synsets(words) :
            for hypon in syn.hyponyms:
                hyponyms.append(hypon.name().split(".")[0].replace('_',' '))
            for hyper in syn.hypernyms:
                hypernymns.append(hyper.name().split(".")[0].replace('_',' '))
            synonyms.append(syn.name().split(".")[0].replace('_',' '))

    # Giving Initial Weights to expanded terms
    count_of_terms = vector_seedDoc.keys().count()
    for word in synonyms:
        if word not in vector_seedDoc:
            vector_seedDoc[word] = (1/count_of_terms)

    for word in hyponyms:
        if word not in vector_seedDoc:
            vector_seedDoc[word] = (1/count_of_terms)

    for word in hypernymns:
         if word not in vector_seedDoc:
            vector_seedDoc[word] = (1/count_of_terms)


    #Recomputing the weights for each term
    term_re_weighting(vector_seedDoc)

    return vector_seedDoc