class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sort = sorted(nums)
        for i in range(0, len(sort)):
            for j in range(i+1, len(sort)):
                k = 0 - sort[i] - sort[j]
                if k in sort[j+1:]:
                    if [sort[i],sort[j],k] not in result:
                        result.append([sort[i],sort[j],k])
        return result