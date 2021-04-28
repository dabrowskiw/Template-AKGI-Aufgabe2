# Funktionen sind in PYthon first-class citizens (heißt: eine Funktion kann
# genau so wie jeder andere Wert verwendet, einer Variable zugewiesen, übergeben
# werden):

def dostuff(what, x, y):
    print(what(x, y))


def sub(x, y):
    return x - y


function = sub
dostuff(function, 10, 5)

# Wird gerne zum Sortieren eingesetzt:
data = ["bleblebleble", "teeest", "ein Wort"]

print(data)
data.sort(key=len)
# Sortiert nach Länge: key ist eine Funktion, die auf jedem Element des Arrays
# aufgerufen wird und eine Zahl zurückliefert. Nach diesen Zahlen wird dann
# das Array sortiert.
print(data)

# Mit lambda expressions kann man anonyme Einzeiler-Funktionen definieren, das
# ist nützlich, wenn man eine einfache Funktion übergeben will, die man nur
# an dieser Stelle braucht. Beispiel: Sortieren des Arrays nach Anzahl der
# "e" in dem Wort:
data.sort(key=lambda x: x.count("e"))
print(data)


# Natürlich geht in Python auch objektorientiertes Programmieren
# Besonderheiten in Python:
#  * Constructor heißt immer __init__
#  * Erstes Argument einer Methode ist immer self (in Java wäre das this),
#    außer bei statischen Methoden (es wird also nicht "static" davor geschrieben,
#    sondern einfach kein self als erstes Argument übergeben).
#  * Keine protected-Attribute (per Konvention _attribut), keine private-Attribute
#    (per Konvention __attribut). Aber: Das ist nur Konvention, wenn man sich
#    nicht daran halten will, kann man "protected"-Attribute so verwenden wie public.
#    "Private"-Attribute werden einfach intern von __attribut auf _klasse__attribut
#    umgemappt, um das nicht-Einhalten der Konvention etwas unbequemer zu machen...

class Sequence:
    def __init__(self, name, sequence):
        self.type = "Sequence"
        self.name = name
        self.sequence = sequence

    def get_description(self):
        return "{} {} is {} bases long.".format(self.type, self.name, len(self.sequence))

    # __str__ ist die Standard-Methode, die verwendet wird, wenn str() auf einem
    # Objekt aufgerufen wird.


#    def __str__(self):
#        return self.get_description()

seq = Sequence("1", "ATGGCTGCGTCATGA")
print(seq.get_description())
print(seq)
# Geht das nicht schicker? 5-6 Zeilen drüber __str__ einkommentieren und nochmal
# probieren!

# Vererbung geht natürlich auch (beliebige Mehrfachvererbung)!

# Das ist ein Trick, um eine Translationstabelle in wenigen Zeilen zu erstellen:
# Eine Dictionary, die jedem Triplet eine Aminosäure zuordnet
# Erstens: DNA-Basen definieren
Bases = "TCAG"
# Zweitens: In Codons alle möglichen Codons generieren
Codons = [a + b + c for a in Bases for b in Bases for c in Bases]
# Drittens: In Aminoacids entsprechend der Reihenfolge, in der die Codons aus
# Bases generiert wurden, die dazu passenden Aminosäuren aufschreiben
Aminoacids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
# Viertens: Über zip (nimmt zwei Arrays und macht ein Array von Tupeln, in dem
# jeweils das n-te Element des ersten Arrays und das n-te Element vom zweiten
# Array zusammen stehen) ein Array von Tupeln erstellen, in dem jeweils in einem
# Tupel immer ein Triplet und die dazu gehörende Aminosäure stehen. Und daraus dann
# eine Dictionary bauen.

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

# Vorsicht: __translation ist wie gesagt nur "ein bisschen" private!

gene = tosort[0]
print(gene.__translation)
print(gene.get_translation())
gene.__translation = "Bla"  # geht nicht
print(gene.__translation)
gene._Gene__translation = "Bla"  # Aua!
print(gene.get_translation())

### --- Dateiverarbeitung --- ###
# In der Bioinformatik wollen wir mit Python Dateien verarbeiten, in denen DNA-Sequenzen stehen.
# Sequenzdateien werden häufig im FASTA-Format abgespeichert.
# Formatbeschreibungen ausführlich:
# FASTA: https://de.wikipedia.org/wiki/FASTA-Format
# Zusammengefasst:
# * Beliebig viele Sequenzen in einer Datei
# * Jede Sequenz fängt mit einer Header-Zeile an, die daran erkannt wird, dass sie
#   mit einem ">" beginnt. Der Rest der Zeile ist der Name der Sequenz
# * Nach dem Header kommen beliebig viele Zeilen, die nur aus den Basen bei DNA
#   im einfachsten Fall A, G, T und C sowie N für "nicht bekannt" und Leerzeichen bestehen.
# Für folgenden Beispiele sollte von Nuccore, einer der größten und bekanntesten Datenbanken
# von Genomsequenzen, eine HIV-Sequenz heruntergeladen werden:
# Link hier: https://www.ncbi.nlm.nih.gov/nuccore/AB052995.1
# Dann oben rechts "Send to:"->"File"->"FASTA"->"Create file", wird als "sequence.fasta" gespeichert

# Datei öffnen. 2. Argument ist mode, haufig: r (read), w (write), a (append).
# b ist binary, z.B. "rb" = "read binary":
infile = open("sequence.fasta", "r")  # infile ist jetzt ein "handle" für die Datei
data = infile.read()
infile.close()

# Man kann wunderschön einfach alle Zeilen aus einer Textdatei hintereinander verarbeiten:
infile = open("sequence.fasta", "r")
lines = infile.read().split("\n")
infile.close()
for line in lines[:4]:
    print(line)

# Problem: Bei sehr großen Dateien nicht gut, da die gesamte Datei in den Speicher
# geladen wird.
# Alternative: auch eine Text-Datei ist iterierbar:
for line in open("sequence.fasta", "r"):
    print(line)

# Zum selber überlegen: Warum sind da Leerzeilen dazwischen? Warum waren da bei dem
# Beispiel vorher keine? Was kann man dagegen tun?

# --- Aufgabe ---

