class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        heap = []
        q = deque()
        time =0

        for task in tasks:
            count[task] = count.get(task, 0) +1
        for freq in count.values():
            heapq.heappush(heap, -freq)
        print(heap)
        while heap or q:
            time +=1
            if heap:
                cnt = 1+ heapq.heappop(heap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        return time
        