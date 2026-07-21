class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = [1] * len(nums)
        k = 1
        l = 1
        for i in range(len(nums)):
            temp[i] = k
            k *= nums[i]

        for j in range(len(nums)):
            temp[len(nums) - j - 1] = temp[len(nums) - j - 1] * l
            l *= nums[len(nums) - j - 1]
        return temp
