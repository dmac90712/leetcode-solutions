class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]

        for n in nums[1:]:
            candidates = (n, curr_max * n, curr_min * n)
            curr_max = max(candidates)
            curr_min = min(candidates)
            best = max(best, curr_max)

        return best