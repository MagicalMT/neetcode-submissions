class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        right = 1
        max_length = 0
        window = set()
        window.add(s[0])
        for i in range(len(s)):
            while right != len(s) and s[right] not in window :
                window.add(s[right])
                right += 1
            if len(window) > max_length:
                max_length = len(window)
            window.remove(s[i])
        return max_length
            