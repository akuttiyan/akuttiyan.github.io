# Arya Kuttiyan
# Computer Science in Healthcare
# April 30 2024
# This program looks at sequence data from bacteria and creates a phylogenetic tree

############################# Code from Tayler Lindsay's Tutorial ################################
import Bio as Bio
from Bio import SeqIO
from Bio import AlignIO
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
import matplotlib
import matplotlib.pyplot as plt

# Reads in all the sequence data of each bacteria
# the sequence is from the 16s part of the genome
s1 = SeqIO.read("bacillus.fasta", "fasta")
s2 = SeqIO.read("cyanobacteria.fasta", "fasta")
s3 = SeqIO.read("ecoli.fasta", "fasta")
s4 = SeqIO.read("helicobacter.fasta", "fasta")
s5 = SeqIO.read("salmonella.fasta", "fasta")
s6 = SeqIO.read("staphylococcus.fasta", "fasta")
s7 = SeqIO.read("streptococcus.fasta", "fasta")

# This assigns ids to each sequence so that the final tree is easier to understand
s1.id = "Bacillus"
s2.id = "Cyanobacteria"
s3.id = "Ecoli"
s4.id = "Helicobacter"
s5.id = "Salmonella"
s6.id = "Staphylococcus"
s7.id = "Streptococcus"

# This writes all the sequences to the same file
bacteria = SeqIO.write([s1, s2, s3, s4, s5, s6, s7], "bacteria.fasta", "fasta")

# I used MUSCLE, which is a website that aligns the sequences
# https://www.ebi.ac.uk/jdispatcher/msa/muscle
# I opened the file with the aligned sequences
with open("bacteria.aln-clustalw", "r") as aln:
    # reads the contents of the file
    alignment = AlignIO.read(aln, "clustal")
print(type(alignment))

# creates a distance calculator object
# this calculates the distance between each sequence so that the bacteria can be mapped
# on the tree
calculator = DistanceCalculator("identity")

# Gets a distance matrix
# The distance matrix shows the distance between all the bacteria
distance_matrix = calculator.get_distance(alignment)
print(distance_matrix)

# Creates a distance tree constructer
# This is what creates the phylogenetic tree
constructor = DistanceTreeConstructor(calculator)

# Builds the phylogenetic tree using the aligned sequences
bacteria_tree = constructor.build_tree(alignment)
# Says the tree is a rooted tree
# A rooted tree is a tree that all ties back to a common ancestor
bacteria_tree.rooted = True
print(bacteria_tree)

# Saves tree by writing it to a file
Phylo.write(bacteria_tree, "bacteria_tree.xml", "phyloxml")

# Visually plots the tree
# Changes the font size and figure size
fig = plt.figure(figsize=(13, 5), dpi=100)
matplotlib.rc("font", size=12)
matplotlib.rc("xtick", labelsize=10)
matplotlib.rc("ytick", labelsize=10)
axes = fig.add_subplot(1, 1, 1)
# Draws the tree
Phylo.draw(bacteria_tree, axes=axes)
# Saves the tree
fig.savefig("bacteria_phylogenetic_tree")
