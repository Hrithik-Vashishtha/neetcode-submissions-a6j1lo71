class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False

        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}

        for ch in s:
            if ch in pairs:
                stack.append(pairs[ch])
            elif not stack or stack.pop() != ch:
                return False

        return not stack