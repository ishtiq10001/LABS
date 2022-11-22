#!/usr/bin/python3
import unittest
from matrices import *
# --------------------------------------------------------------q3.py
# Two-dimensional arrays, simple algorithms
# --------------------------------------------------------------

# --------------------------------------------------------------
# Find the most frequent value in the matrxi
# --------------------------------------------------------------
def mostfrequent(matrix) :
    '''
    Returns the value that is most frequent in the matrix
    but in the case of a tie, return the lowest most frequent value
    '''
    vals = {}
    nList= []
    freq = []
    for i in matrix:
        for j in i:
            nList.append(j)

    for i in nList:
        countC = nList.count(i)
        vals[i] = countC
    
    
    for i,j in vals.items():
        if j == max(vals.values()):
            freq.append(i)


    freq.sort()
    return freq[0]
    
    
# ----------------------------------------------------------
# Show the matrices that we imported 
# matrix1, matrix2 and using printmx()
# --------------------------------------------------------------
printmx(matrix1)
printmx(matrix2)
printmx(matrix3)
printmx(matrix4)
printmx(matrix5)
printmx(matrix6)
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
  self.assertEqual(mostfrequent(matrix1), 16)
 def test2(self):
  self.assertEqual(mostfrequent(matrix2), 50)
 def test3(self):
  self.assertEqual(mostfrequent(matrix3), 75)
 def test4(self):
  self.assertEqual(mostfrequent(matrix4), -129)
 def test5(self):
  self.assertEqual(mostfrequent(matrix5), 95)
 def test6(self):
  self.assertEqual(mostfrequent(matrix6), 16)

if __name__ == '__main__':
    unittest.main(exit=True)
    print(mostfrequent(matrix1))
    
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
