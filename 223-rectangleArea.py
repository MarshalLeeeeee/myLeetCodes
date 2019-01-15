'''
223.Rectangle Area

Find the total area covered by two rectilinear rectangles in a 2D plane.
Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Example:
Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45

Note:
Assume that the total area is never beyond the maximum possible value of int.
'''

class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        X = [[A,0],[C,0],[E,1],[G,1]]
        Y = [[B,0],[D,0],[F,1],[H,1]]
        X.sort(key=lambda k: k[0])
        Y.sort(key=lambda k: k[0])
        #print(X,Y)
        common = (X[2][0]-X[1][0])*(Y[2][0]-Y[1][0]) if X[0][1] ^ X[1][1] and Y[0][1] ^ Y[1][1] else 0
        return (C-A)*(D-B) + (G-E)*(H-F) - common
        