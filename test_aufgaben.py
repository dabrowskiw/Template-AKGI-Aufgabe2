from unittest import TestCase
import pytest

import aufgaben


class MyTestCase(TestCase):
    @pytest.mark.findorfs
    def test_find_orfs_nocds(self):
        self.assertListEqual([], aufgaben.find_orfs("AGTTGTAGGGTA"))

    @pytest.mark.findorfs
    def test_find_orfs_frame1(self):
        self.assertListEqual([(1, 12)], aufgaben.find_orfs("ATGTGTAGGTAAGTAGTG"))

    @pytest.mark.findorfs
    def test_find_orfs_frame2(self):
        self.assertListEqual([(5, 16)], aufgaben.find_orfs("AGGCATGTGTAGGTAAGTAGTG"))

    @pytest.mark.findorfs
    def test_find_orfs_frame3(self):
        self.assertListEqual([(3, 14)], aufgaben.find_orfs("GCATGTGTAGGTAAGTAGTG"))

    @pytest.mark.findorfs
    def test_find_orfs_multiple(self):
        self.assertListEqual([(4, 15), (19, 27)], aufgaben.find_orfs("GGCATGTGTAGGTAAGTAATGATCTAA"))

    @pytest.mark.findorfs
    def test_find_orfs_overlapping(self):
        self.assertListEqual([(4, 15), (9, 23)], aufgaben.find_orfs("GGCATGCTATGTTAAGTAATTAA"))

    @pytest.mark.translation
    def test_DNAGenome_get_translations_nocds(self):
        genome = aufgaben.DNAGenome("AGTTGTAGGGTA")
        self.assertListEqual([], genome.get_translations())

    @pytest.mark.translation
    def test_DNAGenome_get_translations_frame1(self):
        genome = aufgaben.DNAGenome("ATGTGTAGGTAAGTAGTG")
        self.assertListEqual(["MCR*"], genome.get_translations())

    @pytest.mark.translation
    def test_DNAGenome_get_translations_frame2(self):
        genome = aufgaben.DNAGenome("ATGTGTAGGTAAGTAGTG")
        self.assertListEqual(["MCR*"], genome.get_translations())

    @pytest.mark.translation
    def test_DNAGenome_get_translations_frame3(self):
        genome = aufgaben.DNAGenome("GCATGTGTAGGTAAGTAGTG")
        self.assertListEqual(["MCR*"], genome.get_translations())

    @pytest.mark.translation
    def test_DNAGenome_get_translations_multiple(self):
        genome = aufgaben.DNAGenome("GGCATGTGTAGGTAAGTAATGATCTAA")
        self.assertListEqual(["MCR*", "MI*"], genome.get_translations())

    @pytest.mark.translation
    def test_DNAGenome_get_translations_overlapping(self):
        genome = aufgaben.DNAGenome("GGCATGCTATGTTAAGTAATTAA")
        self.assertListEqual(["MLC*", "MLSN*"], genome.get_translations())
