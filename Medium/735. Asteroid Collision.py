from math import copysign
class Solution:
    def asteroidCollision(self, asteroids: [int]) -> [int]:
        sign = lambda x: copysign(1, x)
        stack = []

        def isCollision(a, b):
            if not (sign(a) == 1 and sign(b) == -1):
                return 0
            if abs(a) == abs(b):
                return 1
            if abs(a) > abs(b):
                return 2
            else:
                return 3

        for asteroid in asteroids:
            while True:
                col = 0 if len(stack) == 0 else isCollision(stack[-1], asteroid)
                print(stack)
                match col:
                    case 0:
                        stack.append(asteroid)
                        break
                    case 1:
                        stack.pop()
                        break
                    case 2:
                        break
                    case 3:
                        stack.pop()
        
        return stack