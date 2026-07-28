class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l = []
        if len(tokens) == 1:
            return int(tokens[0])
        for i in tokens:
            if i not in '+-*/':
                l.append(i)
            else:
                b = l.pop()
                a = l.pop()
                result = int(eval(str(a) + str(i) + str(b)))
                l.append(result)
        return l[-1]