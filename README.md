**Content Based Recommendation System for Research Papers**
----------------------------------------------------------------

**Team:**

1. Harsh Shah

2. Manan Upadhyay

3. Shivani Shah

-----------------------------------------------------------------

**Project Details:**
-----------------------------------------------------------------

**External Libraries:**

1. NLTK Wordnet Corpus
2. Apache PDFBox library

**Approach:**

1. We have used technical papers from ACM, IEEE and ScienceDirect as our dataset which are in PDF format. A text file for each technical paper   	is created which has the raw information extracted from the PDF. The extracted text is cleaned before copying it to the text file, such that 	only english words are contained in the corresponding .txt file. 

2. The dataset is then taken as input with the seed document. Pre-processing is performed on it in which TF-IDF vectors are generated together with Log frquency weighting.

3. The vectors are then augmented with semantic information. The Wordnet corpus in NLTK is used for extracting words having similar meaning (synonym and hypernym relationships). Term re-weighting and Term-expansion is performed to augment the weights of the vectors of all the technical papers in the dataset. 

4. Once the final vectors are obtained, Cosine similarity between the seed document and the dataset is calculated to recommend the 'k' most similar documents from the dataset.

5. Result shows the **'k'**** recommended papers with the similarity value in the lowest to highest similarity sequence.



**Execution:**


Run the following command on the prompt:
    
   $ python3 MainRecom.py <path_dataset_directory> <path_to_seed_document> K

where K = number of recommendations required.