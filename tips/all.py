# leetcode 766
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        return all(matrix[row+1][1:] == matrix[row][:-1] for row in range(len(matrix)-1))


def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
