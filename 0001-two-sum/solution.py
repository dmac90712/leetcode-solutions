def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i


if __name__ == "__main__":
    nums = [2, 4, 6, 8, 12, 14, 16, 18, 20]
    target = 16
    print(two_sum(nums, target))
