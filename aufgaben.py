# 1) Implementieren Sie die Methode find_orf(seq), die in einer Sequenz (als String übergeben) alle Open Reading Frames
#    (ORF) findet. Ein ORF ist definiert wie folgt:
#    * Er beginnt mit dem Codon für Methionin/Start (M): ATG
#    * Er endet mit einem der Stop-Codons (TAA, TAG, TGA)
#    * Die Anzahl von Basen zwischen Start- und Stop-Triplet ist ein Vielfaches von
#      3 (da die Polymerase ja in Triplets übersetzt - wenn sie also mit M für Start anfängt
#      und in Dreierschritten weitergehend ein Stop findet, hört sie auch auf.
#    * Zwischen dem Start und Stop ist kein weiteres Stop-Codon, dessen Abstand von dem
#      Start-Codon durch 3 teilbar ist (sonst wäre da der ORF vorbei)
#    Alle gefundenen ORFs sollen als Array von Tupeln im Format (Position erste Base des
#    Start-Codons, Position letzte Base des Stop-Codons) - beginnend bei 1 - zurückgegeben werden. Falls kein ORF
#    gefunden wurde, soll ein leeres Array zurückgegeben werden.
#    Sie können mit unterschiedlichen Sequenzen das erwartete Ergebnis auf dieser Seite nachvollziehen:
#    https://www.bioinformatics.org/sms2/orf_find.html
#    Achten Sie dabei darauf, die Mindest-ORF-Länge auf 1 zu setzen und bei den Reading Frames "1, 2, and 3" auszuwählen.
#
#    Denken Sie bei der Lösung daran, dass Sie sich beliebig zusätzliche Hilfsfuktionen dazuimplementieren können, um
#    Ihren Code sauberer/übersichtlicher/wartbarer zu machen!
#
# 1) Implement the method find_orf(seq) that finds all open reading frames (ORFs) in a sequence that is passed in as
#    a string. An ORF is defined as follows:
#    * It begins with the codon for Methionin (M)/Start: ATG
#    * It ends with one of the possible stop codons (TAA, TAG, TGA)
#    * The number of bases between the start and stop codon is a multiple of 3 (since the polymerase always translates
#      3 bases at a time)
#    * There are no other in-frame stop codons between the start and the stop codon (i.e. other stop codons satisfying
#      the above condition)
#    All found ORFs should be returned as an array of tuples in the following format:
#    (position of the first base of the start codon, position of the last base of the stop codon)
#    with the positions 1-based (i.e. the position of the first base is 1, not 0). If on ORFs are found, an empty
#    array should be returned.
#    You can test the function with different sequences using the following web page:
#    https://www.bioinformatics.org/sms2/orf_find.html
#    If you do that, make sure to set the minimum ORF length to 1 and to select "1, 2 and 3" under "Reading Frames".
#
#    When implementing the solution, please remember that you are allowed to implement additional helper methods in
#    order to keep your code clean and readable!

def find_orfs(seq):
    pass

# 2) Schreiben Sie eine Klasse "DNAGenome", die:
#    * Im Constructur die DNA-Sequenz als String nimmt
#    * Eine Methode "get_cds()" anbietet, die wie unter 1 beschrieben die CDS in dem
#      Genom findet und zurückgibt
#    * Eine Methode "get_translations()" anbietet, die ein Array von Aminosäuresequenzen
#      zurückliefert: Für jede CDS in dem Genom einen String mit der translation
#    Testen Sie diese Klasse mit dem SARS-Cov-2-Genom hier:
#    https://www.ncbi.nlm.nih.gov/nuccore/MT394864.1
#    Hinweis: Auf der Seite wird standardmäßig das Genom im Genbank-Format dargestellt.
#    Dieses listet nach den allgemeinen Informationen auch alle CDS (scrollen Sie nach unten
#    und schauen Sie auf der rechten Seite nach "CDS") mit ihren Translationen und dem Namen des
#    daraus entstehenden Proteins (/product="...") auf. Ihre Klasse
#    muss die erste, zusammengesetzte CDS nicht finden, aber die CDS für "ORF1a polyprotein",
#    "surface glycoprotein" etc. sollten Sie finden.
#
# 2) Implement a class "DNAGenome" that:
#    * Takes a DNA sequence as a string in the constructor
#    * Has a method "get_cds()" that behaves exactly like find_orfs() above (except that it does not take a sequence
#    as an argument, instead it operates on the genome sequence passed to the constructor)
#    * Has a method "get_translations()" that returns an array of amino acid sequences: One for each CDS in the genome.
#    Test your class using the following SARS-CoV-2 genome:
#    https://www.ncbi.nlm.nih.gov/nuccore/MT394864.1
#    That page shows genomes in the GenBank format. This format includes, among other information, details on all CDS
#    (scroll down and look for "CDS" on the left-hand side) including the translation and the name of the resulting
#    protein (/product="..."). Your class does not need to be able to find the first CDS (it is a CDS that is split
#    among different parts of the genome, the simple algorithm you implement here is not goind to be able to
#    handle that), but it should be able to find CDS for e.g. "ORF1a polyprotein" "surface glycoprotein".

class DNAGenome:
    def __init__(self, seq):
        pass

    def find_orfs(self):
        pass

    def get_translations(self):
        pass