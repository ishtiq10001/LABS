#!/usr/bin/python3
import unittest
from matrices import *
from q94 import repeatedrow
# --------------------------------------------------------------q4.py
# Two-dimensional arrays, simple algorithms
# --------------------------------------------------------------
def transpose(matrix) :
    '''
    Returns a matrix which is the transpose of the argument matrix.
    Assumes that the matrix is retangular
    ''' 
    t_matrix = []
    for n in range(len(matrix[0])):#column maker
        col_L = []
        for m in range(0,len(matrix)):
            col_L.append(matrix[m][n])
        t_matrix.append(col_L)
    

    return t_matrix
# --------------------------------------------------------------
# is there a repeated column?
# --------------------------------------------------------------
def repeatedcolumn(matrix) :
    '''
    Returns True if an only if at least one column is the same as another column
    False otherwise
    Use the transpose() method as a helper method, along with the
    repeatedrow() method from q4.py
    '''
    return repeatedrow(transpose(matrix))
# ----------------------------------------------------------
# Show the matrices that we imported
# matrix1, matrix2 and using printmx()
# --------------------------------------------------------------

for matrix in [matrix1, matrix2, matrix3, matrix4, matrix5]:
    printmx(matrix)
    print('transpose:')
    printmx(transpose(matrix))
    pass

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
  self.assertEqual(repeatedcolumn(matrix1), False)
 def test2(self):
  self.assertEqual(repeatedcolumn(matrix2), True)
 def test3(self):
  self.assertEqual(repeatedcolumn(matrix3), False)
 def test4(self):
  self.assertEqual(repeatedcolumn(matrix4), False)
 def test5(self):
  self.assertEqual(repeatedcolumn(matrix5), False)
if __name__ == '__main__':
    unittest.main(exit=True)
    
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
