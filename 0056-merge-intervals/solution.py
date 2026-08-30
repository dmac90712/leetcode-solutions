from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            # If merged is empty, or the current interval doesn't overlap
            # with the last one in merged, just append it
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # There's overlap — extend the end of the last interval
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged