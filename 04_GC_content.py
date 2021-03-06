# ------------------------------------------------------------------------------------------------------------------
# Rosalind problems:
# 4) Compute GC content for each FASTA sequence given in the 04_GC_content.txt file and
#     display the sequence ID which has highest GC content and its GC content value
#-------------------------------------------------------------------------------------------------------------------

from Bio.SeqUtils import GC
from Bio import SeqIO

GC_content = {}

for record in SeqIO.parse('C:/Users/Yamini/Documents/Rosalind/Input files/04_GC_content.txt', "fasta"):
    GC_content.update({record.id:GC(record.seq)})

key, value = max(GC_content.iteritems(), key=lambda x:x[1])
print key
print value