class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        dic = {')':'(', '}':'{', ']':'['}
        l = []
        for i in s:
            if i in ['(', '{', '[']:
                l.append(i)
            else:
                if not l or dic[i] != l[-1]:
                    return False
                l.pop()

        return True if not l else False