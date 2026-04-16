class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ["+", "-", "*", "/"]:
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                if i == "+":
                    result = b + a
                elif i == "-":
                    result = b - a
                elif i == "*":
                    result = b * a
                elif i == "/":
                    result = int(b / a)
                stack.append(result)

        return stack[0]