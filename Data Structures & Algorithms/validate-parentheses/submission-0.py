class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', ']': '[', '}': '{'}
        l = []
        for i in s:
            if i in '{([':
                l.append(i)
                continue
            if not l or l[-1] != d[i]:
                return False
            l.pop()
        return len(l) == 0
            