class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for x,y in points:
            heapq.heappush(heap,((math.sqrt(x**2 + y**2)),[x,y]))
        sum = []
        l=1
        while heap and l <= k:
            f = heapq.heappop(heap)
            sum.append(f[1]) 
            l += 1
        return sum
