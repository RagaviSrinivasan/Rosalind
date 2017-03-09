from Bio.SeqUtils import GC
from Bio import SeqIO

GC_content = {}

for record in SeqIO.parse('C:/Users/Yamini/Documents/Rosalind/Input files/rosalind_gc.txt', "fasta"):
    GC_content.update({record.id:GC(record.seq)})

key, value = max(GC_content.iteritems(), key=lambda x:x[1])
print key
print value