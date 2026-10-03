class Solution:
    def isValid(self, s: str) -> bool:
        pair = {'[':']', '(': ')', '{':'}'}
        stack = []

        for n in s:
            if n in pair:
                stack.append(n)
            else:
                if not stack or n != pair[stack[-1]]:
                    return False
                stack.pop()
        return len(stack) ==0
        