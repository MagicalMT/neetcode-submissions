class Solution:

    def encode(self, strs: List[str]) -> str:
        resultstr = ''
        for i in strs:
            length_i = len(i)
            i = '#' + str(length_i) + ' ' + i
            resultstr += i
        return resultstr
    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            if s[i] == '#':
                i += 1
                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1
                num = int(s[i:j])
                result.append(s[j+1:j+1+num])
                i = j + num
            i += 1
        return result
