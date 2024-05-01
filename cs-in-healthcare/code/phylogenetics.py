import Bio as Bio
from Bio import SeqIO
from Bio import AlignIO
from Bio import Phylo


s1 = SeqIO.read("bacillus.fasta", "fasta")
s2 = SeqIO.read("cyanobacteria.fasta", "fasta")
s3 = SeqIO.read("ecoli.fasta", "fasta")
s4 = SeqIO.read("helicobacter.fasta", "fasta")
s5 = SeqIO.read("salmonella.fasta", "fasta")
s6 = SeqIO.read("staphylococcus.fasta", "fasta")
s7 = SeqIO.read("staphylococcus.fasta", "fasta")
s8 = SeqIO.read("streptococcus.fasta", "fasta")
