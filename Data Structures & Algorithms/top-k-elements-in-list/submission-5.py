class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        res = []
        arr = []
        for n in nums:
            cnt[n] = cnt.get(n, 0) +1

        for num,freq in  cnt.items():
            arr.append([freq, num])
        arr.sort()

        while len(res) < k:
            res.append(arr.pop()[1])
        return res

        