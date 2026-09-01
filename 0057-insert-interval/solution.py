from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i, n = 0, len(intervals)
        start, end = newInterval

        # Add all intervals that end before the new interval starts
        while i < n and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1

        # Merge all intervals that overlap with the new interval
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        result.append([start, end])

        # Add all remaining intervals (they start after the merged interval ends)
        while i < n:
            result.append(intervals[i])
            i += 1

        return result