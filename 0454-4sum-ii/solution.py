from typing import List
from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_counts = defaultdict(int)

        # Tally every possible sum of one element from nums1 and one from nums2
        for a in nums1:
            for b in nums2:
                sum_counts[a + b] += 1

        count = 0
        # For each pair from nums3/nums4, check how many ab-pairs negate it
        for c in nums3:
            for d in nums4:
                count += sum_counts[-(c + d)]

        return count