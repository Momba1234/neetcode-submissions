class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def bt (j, target, path):
            if target< 0:
                return
            if target == 0:
                result.append(path.copy())
                return
            
            
            for i in range(j, len(nums)):  
                bt(i, target-nums[i], path+[nums[i]])
        bt(0, target, [])
        return result
