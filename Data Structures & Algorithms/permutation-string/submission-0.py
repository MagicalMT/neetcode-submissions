class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = {}
        d2 = {}
        left = 0
        for i in s1:
            d1[i] = d1.get(i, 0) + 1
        for right in range(len(s2)):
            if len(s2) < len(s1):
                return False
            d2[s2[right]] = d2.get(s2[right], 0) + 1
            if right - left + 1 > len(s1):
                if d2.get(s2[left]) - 1 == 0:
                    d2.pop(s2[left])
                else:
                    d2[s2[left]] = d2.get(s2[left]) - 1
                left += 1
            if d1 == d2:
                return True
        print(d1, d2)
        return False
        