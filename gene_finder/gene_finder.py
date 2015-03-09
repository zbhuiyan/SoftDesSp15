# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Zarin Bhuiyan

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, aa_table
import random
from load import load_seq

def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    """
    # TODO: implement this
    if nucleotide == "A":
        return "T"
    elif nucleotide == "T":
        return "A"
    elif nucleotide == "C":
        return "G"
    elif nucleotide == "G":
         return "C"
    else:
        print("Not valid input")




    

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """
    # TODO: implement this

    if len(dna) <= 1:
        return dna
        print "Dna input is not long enough"

    else:
        reverse_dna = dna[::-1]
        reverse_list = list (reverse_dna)
        new_list = []


        for i in reverse_list:

            new_list.append(get_complement(i))

        return ''.join(new_list)







def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'
    """
    # TODO: implement this
    x = [dna[i:i+3] for i in range(0,len(dna),3)]
    
    for i in range(len(x)):
        if (x[i] == 'TAG') or (x[i] == 'TGA') or (x[i] == 'TAA'):
            return dna[0:i*3]
    

    return dna





def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    """


    # x = [dna[i:i+3] for i in range(0,len(dna),3)]
    # print "all codons"
    # print x
    all_orfs=[]
    #c = 0
    i = 0
    # for i in range(len(dna)):
    while i < len(dna):

        current_codon = dna[i:i+3]
        if current_codon == 'ATG':
            rest = rest_of_ORF(dna[i:])
            all_orfs.append(rest)
            i += len(rest)
        else:
            i +=3

    return all_orfs


def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
     >>> find_all_ORFs("ATGCATGAATGTAG")
     ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
     >>> find_all_ORFs("ATGCGAATGTAGCATCAAA")
     ['ATGCGAATG']
    """
    # TODO: implement this

    
    returned_ORFs = []
    returned_ORFs.extend(find_all_ORFs_oneframe(dna))
    returned_ORFs.extend(find_all_ORFs_oneframe(dna[1:]))
    returned_ORFs.extend(find_all_ORFs_oneframe(dna[2:]))

    return returned_ORFs





def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """

    reverse_strand = get_reverse_complement(dna)
    both_strands = []
    both_strands.extend(find_all_ORFs(dna))
    both_strands.extend(find_all_ORFs(reverse_strand))

    return both_strands
    







def longest_ORF(dna): 
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    longestorf = ""

    both_strands = find_all_ORFs_both_strands(dna)
   

    #return (both_strands)
    for i in range(len(both_strands)-1):
        
        # print "i said hey: ",len(orf)
        if len(both_strands[i]) >= len(both_strands[i+1]):

            longestorf = both_strands[i]   
        else:
            longestorf = both_strands[i+1]

    return longestorf

    


def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    

    listofshuffled = []
    listoflongestshuffled = []
    for i in range(num_trials):
        shuffled = shuffle_string(dna)
        listofshuffled.append(shuffled)
   

    for i in listofshuffled:
        longestshuffled = longest_ORF(i)
        listoflongestshuffled.append(longestshuffled)


    
    return len(max(listoflongestshuffled, key=len))





def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """

<<<<<<< HEAD

    x = [dna[i:i+3] for i in range(0,len(dna),3)]
    aminoacids = []
    for i in range(len(x)):
        if len(x[i]) != 3:
            break
        aminoacids.append(aa_table[x[i]])



    return ''.join(aminoacids)







=======
>>>>>>> 68b2965c9c5fa90bd2433f3b7f672e6b29c1bbbb
def gene_finder(dna):
    """ Returns the amino acid sequences that are likely coded by the specified dna
        
        dna: a DNA sequence
        returns: a list of all amino acid sequences coded by the sequence dna.
    """
    

    threshold = longest_ORF_noncoding(dna, 1500)

    bothstrands_ORFs = find_all_ORFs_both_strands(dna)

    AA = []
    for i in bothstrands_ORFs:
        if len(i) > threshold:
            AA.append(coding_strand_to_AA(i))


    return AA







def real_dna():

    dna = load_seq("./data/X73525.fa")
    threshold = longest_ORF_noncoding(dna, 500)

    aminoacidsequence = gene_finder(dna, threshold)
    return aminoacidsequence

print real_dna()




if __name__ == "__main__":
    import doctest
    doctest.testmod()
