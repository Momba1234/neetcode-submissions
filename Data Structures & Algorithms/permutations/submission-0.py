class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def bt (path):
            if len(path) == len(nums):
                result.append(path.copy())
                return
            for n in nums:
                if n in path:
                    continue
                path.append(n)
                bt(path)
                path.pop()
        bt([])
        return result    
            



        