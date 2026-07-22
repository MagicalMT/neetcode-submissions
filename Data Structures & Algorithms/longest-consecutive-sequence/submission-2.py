class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sort_nums = sorted(nums)
        result = 1
        longest = 1
        for i in range(len(nums)-1):
            if sort_nums[i] == sort_nums[i+1]:
                continue
            if sort_nums[i] + 1 == sort_nums[i+1]:
                longest += 1
                if result <= longest:
                    result = longest
            else:
                longest = 1
        return result