class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        mheap = [-int(i) for i in nums]
        heapq.heapify(mheap)
        while k > 1:
            heapq.heappop(mheap)
            k -= 1

        return str(-mheap[0])
