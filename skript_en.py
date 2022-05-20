# Functions in Python are "first-class citizens", meaning that they can be used
# just like any other value - assigned to a variable, passed as an arugment etc.

def dostuff(what, x, y):
    print(what(x, y))


def sub(x, y):
    return x - y


function = sub
dostuff(function, 10, 5)

# This is popular e.g. in sorting:
data = ["bleblebleble", "teeest", "ein Wort"]

print(data)
data.sort(key=len)
# This sorts by length: Key is a function that is applied to each element of
# the array and that returns a number. The list is sorted by those numbers.
print(data)

# Such functions are called lambda expressions: Anonymous one-liners. This
# is useful, if one wants to pass a simple function that is only used in this
# one place. Example: Sorting an array by the number of "e" in the word:
data.sort(key=lambda x: x.count("e"))
print(data)

# Of course, there is also object oriented programming in Python.
# Special features in Python:
#  * The constructor is always called __init__
#  * The first argument of each method is immer "self" (in Java, this is
#    "this"), except in static methods (so there is no "static" declaration,
#    a method is simply static if it does not take a self argument)
#  * There is no concept of protected or private attributes. By convention,
#    attributes starting with _are protected, those starting with __ are
#    private. But this is just a convention, Python internally renames attributes
#    starting with __ to _classname__attributename, but those are still public.

class Sequence:
    def __init__(self, name, sequence):
        self.type = "Sequence"
        self.name = name
        self.sequence = sequence

    def get_description(self):
        return "{} {} is {} bases long.".format(self.type, self.name, len(self.sequence))

# __str__ is the method called when str() is called on an object

#    def __str__(self):
#        return self.get_description()

seq = Sequence("1", "ATGGCTGCGTCATGA")
print(seq.get_description())
print(seq)
# That is not pretty - uncomment __str__ above and try again.

# There is also inheritance (including multiple inheritance). Let's take a look:


# This is a trick to create a translation table in just a few lines: A dictionary that
# assigns each possible triplet to an amino acid.
# First define the bases:
Bases = "TCAG"
# Then generate all possible combinations:
Codons = [a + b + c for a in Bases for b in Bases for c in Bases]
# Then create a list of amino acids in the same order as the triplets above:
Aminoacids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
# Then zip these (creates an array of tuples from the elements of two arrays passed to it,
# # where the n-the element of each tuple is composed of the n-th elements of the
# first and second arrays), and create a dictionary:

Codontable = dict(zip(Codons, Aminoacids))


class Gene(Sequence):
    def __init__(self, name, sequence):
        super().__init__(name, sequence)  # mro!
        self.type = "Gene"
        # __: Private
        self.__translation = "".join([Codontable[self.sequence[x:x + 3]] for x in range(0, len(self.sequence), 3)])

    def get_translation(self):
        return self.__translation


mygene = Gene("Some gene", "ATGGCTGCGTCATGA")
print(mygene)
print(mygene.get_description())
print(mygene.get_translation())
isinstance(mygene, Gene)
isinstance(mygene, Sequence)
isinstance(seq, Gene)

tosort = [Gene("Gene 1", "ATGGCTGCGTCATGA"), Gene("Gene 2", "ATGCGAACGCCCCGTTGA"), Gene("Gene 3", "ATGGCCTGA")]
print(tosort[0])

# Careful: __translation is just "a bit" private:

gene = tosort[0]
print(gene.__translation)
print(gene.get_translation())
gene.__translation = "Bla"  # geht nicht
print(gene.__translation)
gene._Gene__translation = "Bla"  # Aua!
print(gene.get_translation())

### --- Working with files --- ###
# In bioinformatics, we often work with sequence files saved in the FASTA format. You can find
# a description of the format here: https://en.wikipedia.org/wiki/FASTA_format
# In short:
# * Arbitrary number of sequences per file
# * Each sequence begins with header line that starts with a ">", followed by the name of the sequence
# * Beliebig viele Sequenzen in einer Datei
# * The header is followed by an arbitraty number of lines that consist only of the baeses (A, G, T, C and N for
#   unknown) and whitespace
# For the following examples, you should download a sequence from the NCBI nucleotide database, the
# largest sequence repository:
# Link: https://www.ncbi.nlm.nih.gov/nuccore/AB052995.1
# Then in the top right cornder "Send to:"->"File"->"FASTA"->"Create file", will be saved as "sequence.fasta"

# Open a file. 2. argument is mode, often: r (read), w (write), a (append).
# b is binary, e.g. "rb" = "read binary":
infile = open("sequence.fasta", "r")  # infile is now a handle for the file
data = infile.read()
infile.close()

# It is easy to process all lines of a file one after the other:
infile = open("sequence.fasta", "r")
lines = infile.read().split("\n")
infile.close()
for line in lines[:4]:
    print(line)

# Problem: This is not good, since the whole file is read into memory.
# alternative: Iterate over the file:
for line in open("sequence.fasta", "r"):
    print(line)

# Question: Why does this show empty lines between the lines from the file? Why was this not the case in the
# example above? What can you do against it?

## Tasks
