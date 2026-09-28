class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def bt(path, left, right):
            if left == right == n:
                res.append("".join(path.copy()))
                return 
            if left < n:
                path.append("(")
                bt(path, left+1, right)
                path.pop()
            if right < left:
                path.append(")")
                bt(path, left, right+1)
                path.pop()
        bt([], 0,0)
        return res


            
        