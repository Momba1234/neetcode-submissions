class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def bt (target, path, j):
            if target == 0:
                result.append(path)
                return
            if target < 0 :
                return

            
            

            for i in range(j, len(candidates)):
                if i>j and candidates[i] == candidates[i-1]:
                    continue
                bt(target - candidates[i], path+[candidates[i]], i+1)

        bt(target, [], 0)
        return result
        