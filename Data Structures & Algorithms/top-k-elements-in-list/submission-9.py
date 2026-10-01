class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        heap = []
        arr = []
        for n in nums:
            cnt[n] = cnt.get(n, 0) +1
        for num,freq in cnt.items():
            heapq.heappush(heap, (freq, num))

        while len(heap) >k:
            heapq.heappop(heap)
        
        for i  in range(k):
            arr.append(heapq.heappop(heap)[1])
        return arr