class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()


        def bt (j, path):
            result.append(path.copy())
         
            for i in range(j, len(nums)):
                if i > j and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                bt(i+1, path)
                path.pop()

            
        bt(0, [])
        return result
        