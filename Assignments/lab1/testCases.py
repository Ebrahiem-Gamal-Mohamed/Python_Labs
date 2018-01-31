# test cases for python Assignments .....

from calcArea import calcArea
from charLocator import index_Search
from listToDic import listToDic
from mulTable import mulTable
from vowelsRemoval import vowels_removal
from marioPyramid import marioPyramid

import unittest

class TestAssignmentOne(unittest.TestCase):

    def test_calcAreaFun(self):
        self.assertEqual(calcArea('t',10,20), 100.0)
        self.assertEqual(calcArea('r',10,10), 100)
        self.assertEqual(calcArea('c',10), 314.2857142857143)
        self.assertEqual(calcArea('s',10), 100) 

    def test_charLocatorFun(self):
        self.assertEqual(index_Search('ebrahiem Hima HIMA EBRAHIEM','i'), [5, 10, 15, 24])

    def test_listToDicFun(self):
        l1 = ["ahmed", "fatma", "ibrahim"]
        d1 = {'a':['ahmed'], 'f':['fatma'],'i':['ibrahim']}
        self.assertEqual(listToDic(l1), d1)                                

    def test_mulTableFun(self):
        self.assertEqual(mulTable(3), [[1],[2,4],[3,6,9]])

    def test_vowelsRemovalFun(self):
        self.assertEqual(vowels_removal("ebrahiem gamal mohammed") ,"brhm gml mhmmd")
        self.assertEqual(vowels_removal("EBRAHIEM GAMAL MOHAMMED") ,"BRHM GML MHMMD")
        self.assertEqual(vowels_removal("EBRahiem gAMAL MOHammEd") ,"BRhm gML MHmmd")        

if __name__ == '__main__':
    unittest.main()

