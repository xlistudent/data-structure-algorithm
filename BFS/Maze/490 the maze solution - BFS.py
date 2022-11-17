from ast import List
from typing import Collection


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        m = len(maze)
        n = len(maze[0])

        Q = Collection.deque()     
        Q.append(start)

        Dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while(Q):

            x0, y0 = Q.popleft()

            for dir in Dir:
                x = x0 + dir[0]
                y = y0 + dir[1]

                while (x >= 0 and x < m and y >= 0 and y < n and maze[x][y] != 1):
                    x += dir[0]
                    y += dir[1]

                x = x - dir[0]
                y = y - dir[1]

                if x == destination[0] and y == destination[1]:
                    return True

                if maze[x][y] == 0:
                    Q.append((x, y))
                    maze[x][y] = 2

        return False

