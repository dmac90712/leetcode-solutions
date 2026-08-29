from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Maintain a min-heap of size k containing the k largest elements seen so far
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        # The root of the min-heap is the kth largest element
        return heap[0]