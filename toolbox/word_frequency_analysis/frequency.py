""" Analyzes the word frequencies in a book downloaded from
    Project Gutenberg """

import string
from collections import Counter

def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
        punctuation, and whitespace are stripped away.  The function
        returns a list of the words used in the book as a list.
        All words are converted to lower case.
    """
    f = open('huckleberry.txt','r')
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    
    lines = lines[curr_line+1:]
    
    
    #    print lines 

    lines = str(lines)
    punctuationlist = []
    for thing in string.punctuation:
        punctuationlist.append(thing)

    lines.strip("") #strips whitespace in beginning and end of book
    
    for x in punctuationlist:
        lines.strip(x) #strips each punctuation thingy from book
    
    lines = lines.lower()
    return lines
    

  
def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
        occurring words ordered from most to least frequently occurring.

        word_list: a list of words (assumed to all be in lower case with no
                    punctuation
        n: the number of words to return
        returns: a list of n most frequently occurring words ordered from most
                 frequently to least frequentlyoccurring
    """
    

    # word_list = lines

    words_to_count = (word for word in word_list if word[:1].isupper())
    c = Counter(words_to_count)
    print c.most_common(n)





get_word_list('huckleberry.txt')
get_top_n_words(lines, 5)