class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result =[]

        def bt (i, path):
            if i == len(nums):
                result.append(path.copy())
                return
            path.append(nums[i])
            bt(i+1, path)
            path.pop()
            bt(i+1, path)
        bt(0, [])
        return result