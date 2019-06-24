import os
import math

from typing import List

## Directory and file names for example text files.

DATA_DIR = '/Users/ryandavis/Desktop/projects/slpc/data'
FN = {
        'amazon' : 'amazon_cells_labelled.txt',
        'imdb' : 'imdb_labelled.txt',
        'yelp' : 'yelp_labelled.txt'
}

def to_int(s: str) -> int:
    """
    If possible, convert string to int. Else, return None.
    """
    try:
        n = int(s)
    except ValueError:
        n = None
    return n

def read_dataset(name: str, directory: str=DATA_DIR) -> List[List]:
    """
    Read dataset from disk into memory
    """
    # Read raw text line by line
    fn = os.path.join(directory, FN[name])
    with open(fn) as f:
        text = f.readlines()
    # Split text from label, sanitize labels
    text_parse = []
    for line in text:
        line = line.strip().split('\t')
        print(line)
        if len(line) != 2:
            continue
        line[1] = to_int(line[1])
        if line[1] is None:
            continue
        if line[1] not in set([0,1]):
            continue
        text_parse += [line]
    return text_parse

class NaiveBayes:
    """
    Class implementing Naive Bayes for document classification.
    """
    def __init__(self):
        pass
    def train(self, data: List[List]):
        """
        Train classifier on text.
        """
        Ndoc = len(data)
        # Represent using dictionary by class
        C = {}
        for L in data:
            text = L[0]
            label = L[1]
            if label not in C:
                C[label] = []
            C[label] += [text]
        # Get log prior probababilities. Use MLE - estimate is the
        # relative frequency of the document.
        logprior = {}
        for label in C:
            logprior[label] = len(C[label]) / Ndoc

