# ------------------------------------------------------------------------------------------------------------------
# Rosalind problems:
# 5) Calculate Hamming distance
#
# For a give sequences s and t of equal length, Hamming distance is the number of mismatched nucleotides.
#-------------------------------------------------------------------------------------------------------------------

def HammingDistance():
    with open('C:/Users/Yamini/Documents/Rosalind/Input files/05_hamming_distance.txt', 'r') as f:
        lines = f.readlines()
        seq1 = lines[0].rstrip()
        seq2 = lines[1].rstrip()
        hammingDistance = 0

        if (len(seq1) != len(seq2)):
            print "Two sequences must be of equal length in order to calculate the Hamming Distance"
            return
        else:
            for i in range(0,len(seq1)):
                if seq1[i] != seq2[i]:
                    hammingDistance += 1
            return hammingDistance

print HammingDistance()
