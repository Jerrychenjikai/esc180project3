'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 20, 2023.
'''

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as
    described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)

def get_value(vec: dict[str, int], idx: str) -> int:
    try:
        return vec[idx]
    except KeyError:
        return 0

def increase(vec: dict[str, int], idx: str, value: int = 1) -> None:
    vec[idx] = get_value(vec, idx) + value

def cosine_similarity(vec1, vec2):
    '''This function returns the cosine similarity between the sparse vectors vec1 and vec2, stored as
dictionaries. For example,
cosine_similarity({"a": 1, "b": 2, "c": 3},
{"b": 4, "c": 5, "d": 6})
should return approximately 0.70 (as a float)'''
    keys1 = set(vec1.keys())
    keys2 = set(vec2.keys())

    keys = keys1 & keys2

    numerator = 0
    len1 = 0
    len2 = 0

    for i in keys:
        numerator += get_value(vec1, i) * get_value(vec2, i)
        len1 += get_value(vec1, i) ** 2
        len2 += get_value(vec2, i) ** 2

    return numerator / (len1**0.5) / (len2**0.5)

def build_semantic_descriptors(sentences):
    '''This function takes in a list sentences, which is a list containing lists of strings (words)
representing sentences, and returns a dictionary d such that for every word w that appears in at
least one of the sentences, d[w] is itself a dictionary which represents the semantic descriptor of
w (note: the variable names here are arbitrary).
For example, if sentences represents the opening of Notes from the Underground above:
[["i", "am", "a", "sick", "man"],
["i", "am", "a", "spiteful", "man"],
["i", "am", "an", "unattractive", "man"],
["i", "believe", "my", "liver", "is", "diseased"],
["however", "i", "know", "nothing", "at", "all", "about", "my",
"disease", "and", "do", "not", "know", "for", "certain",
"what", "ails", "me"]],
part of the dictionary returned would be:
{ "man": {"i": 3, "am": 3, "a": 2, "sick": 1, "spiteful": 1,
"an": 1, "unattractive": 1},
"liver": {"i": 1, "believe": 1, "my": 1, "is": 1,
"diseased": 1},
... }
with as many keys as there are distinct words in the passage.
Computational complexity – Avoid writing this function such that its complexity is O(n2), where
n is the total number of words in the text. This will result in not being able to run the code once all
the functions are complete.
A hint for how to achieve this is at the end of this handout.'''

    
    pass

def build_semantic_descriptors_from_files(filenames):
    '''This function takes a list filenames containing strings, with each string containing the name of
a file and returns a dictionary of the semantic descriptors of all the words in the files filenames,
with the files treated as a single text. The first file in filenames can be opened using
open(filenames[0], "r", encoding="latin1"). Assume that all text files opened
by this function are Latin-1 encoded.
You should assume that the following punctuation always separates sentences: ".", "!", "?",
and that is the only punctuation that can separate sentences. Assume that only the following
additional punctuation is present in the texts: [",", "-", "--", ":", ";"]. How your
code handles other punctuation not explicitly listed in this question is up to you.'''
    pass

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    '''This function takes in a string word, a list of strings choices, and a dictionary
semantic_descriptors, which is built according to the requirements for
build_semantic_descriptors, and returns the element of choices which has the
largest semantic similarity to word, with the semantic similarity computed using the data in
semantic_descriptors and the similarity function similarity_fn.
The similarity function is a function that takes in two sparse vectors stored as dictionaries and
returns a float. An example of such a function is cosine_similarity. If the semantic
similarity between two words cannot be computed (e.g., a word is missing from
semantic_descriptors, or its descriptor is empty), it is considered to be −1. In case of a tie
between several elements in choices, the one with the smallest index should be returned (e.g.,
if there is a tie between choices[5] and choices[7], choices[5] is returned).'''
    pass

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    '''This function takes in a string filename which is the name of a file in the same format as
test.txt, and returns the percentage (i.e., float between 0.0 and 100.0) of questions on which
most_similar_word() guesses the answer correctly using the semantic descriptors stored in
semantic_descriptors and the similarity function similarity_fn
The format of test.txt is as follows. On each line, we are given a word (all-lowercase), the
correct answer, and the choices. For example, the line
feline cat dog cat horse
represents the question:
feline:
(a) dog
(b) cat
(c) horse
and indicates that the correct answer is “cat”'''
    pass