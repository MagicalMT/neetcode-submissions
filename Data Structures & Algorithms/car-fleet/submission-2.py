class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        order = list(zip(position, speed))
        order = sorted(order, reverse = True)
        for i in range(len(order)):
            new_time = (target - order[i][0]) / order[i][1]
            if not stack:
                stack.append(new_time)
                continue
            current_time = stack[-1]
            if new_time > current_time:
                stack.append(new_time)
        return len(stack)
                