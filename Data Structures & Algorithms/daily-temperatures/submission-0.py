class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack:
                temp = stack[-1]
                if temperatures[temp] < temperatures[i]:
                    result[temp] = i - temp
                    stack.pop()
                else:
                    break
            stack.append(i)
        return result
                