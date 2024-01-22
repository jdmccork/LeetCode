class Solution:
    def nearestExit(self, maze: [[str]], entrance: [int]) -> int:
        visted = set()
        stack = [(entrance[0], entrance[1], 0)]
        steps = 0
        while stack != []:
            x, y, steps = stack.pop(0)

            if (x, y) in visted:
                continue
            if [x, y] != entrance and (x == -1 or x == len(maze) or y == 1 or y == len(maze[0])):
                print([x, y] != entrance)
                return steps
            if maze[x][y] == '+':
                continue

            stack.append((x + 1, y, steps + 1))
            stack.append((x - 1, y, steps + 1))
            stack.append((x, y + 1, steps + 1))
            stack.append((x, y - 1, steps + 1))
            visted.add((x, y))

        return -1