class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        l = []
        for i in nums:
            s.add(i)
            l.append(i)
            if len(s) != len(l):
                return i
        return
        