class Solution:
    def maxLength(self, arr: [str]) -> int:
        length = len(arr)
        def recurs(string, i):
            if i == length:
                return 0
            dup = True
            t = set()
            for n in arr[i]:
                if n in t:
                    dup = False
                    break
                t.add(n)

            if dup and set(string).intersection(t) == set():
                return max(len(arr[i]) + recurs(string + arr[i], i+1), recurs(string, i+1))
            else:
                return recurs(string, i+1)
        return recurs("", 0)