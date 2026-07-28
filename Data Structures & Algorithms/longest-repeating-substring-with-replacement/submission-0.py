class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        result = 0
        count = 0
        max_freq = 0
        d = {}
        for right in range(len(s)):
            d[s[right]] = d.get(s[right], 0) + 1
            max_freq = max(max_freq, d[s[right]])

            while (right - left + 1) - max_freq > k:
                d[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result