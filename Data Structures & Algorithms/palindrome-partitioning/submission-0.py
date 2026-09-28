class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]

        def bt (path, i):
            if i >= len(s):
                res.append(path.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    path.append(s[i:j + 1])
                    bt(path, j+1)
                    path.pop()
        bt([], 0)
        return res

    def isPali(self, s, l, r):
        while l<r:
            if s[l] != s[r]:
                return False
            l +=1
            r -=1
        return True

        