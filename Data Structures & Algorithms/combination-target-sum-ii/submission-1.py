class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def bt (target, path, j):
            if target == 0:
                result.append(path.copy())
                return
            if target < 0 :
                return
            for i in range(j, len(candidates)):
                if i>j and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                bt(target - candidates[i], path, i+1)
                path.pop()

        bt(target, [], 0)
        return result
        