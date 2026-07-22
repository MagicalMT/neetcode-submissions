class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''
        reverse = ''
        for i in s:
            if not i.isalnum():
                continue
            i = i.lower()
            s1 += i
            reverse = i + reverse
        return s1 == reverse