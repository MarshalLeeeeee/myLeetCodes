'''
207. Course Schedule

There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:
Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
'''

class Solution:
    def dfs(self,i,nxt,path,visited):
        if i in path: return False
        else:
            path.add(i)
            for c in nxt[i]:
                if not visited[c] and not self.dfs(c,nxt,path,visited): return False
            path.remove(i)
            visited[i] = 1
            return True
    
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        ifHasPre = [0] * numCourses
        nxt, visited = defaultdict(list), [0] * numCourses
        for pq in prerequisites:
            c, q = pq[0], pq[1]
            ifHasPre[c] = 1
            nxt[q].append(c)
        q, path = [], set()
        for i in range(numCourses):
            if not ifHasPre[i]: q.append(i)
        for c in q:
            if not self.dfs(c,nxt,path,visited): return False
        return True if sum(visited) == numCourses else False

if __name__ == '__main__':
    print(Solution().canFinish(8,[[1,0],[2,6],[1,7],[5,1],[6,4],[7,0],[0,5]]))