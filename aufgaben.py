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
#    Achten Sie dabei darauf, die Mindest-ORF-Länge auf 1 zu seten und bei den Reading Frames "1, 2, and 3" auszuwählen.
#
#    Denken Sie bei der Lösung daran, dass Sie sich beliebig zusätzliche Hilfsfuktionen dazuimplementieren können, um
#    Ihren Code sauberer/übersichtlicher/wartbarer zu machen!

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


class DNAGenome:
    def __init__(self, seq):
        pass

    def find_orfs(self):
        pass

    def get_translations(self):
        pass