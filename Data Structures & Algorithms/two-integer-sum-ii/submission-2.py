class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(numbers)):
            if target - numbers[i] in numbers:
                result = [i+1, numbers.index(target-numbers[i])+1]
                return result
        return result