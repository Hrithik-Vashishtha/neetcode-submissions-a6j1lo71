class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        dic = {"]":"[", ')':'(', '}':'{'}
        for i in s:
            if i in ["(", '[', '{']:
                l.append(i)
            else:
                if not l:
                    return False
                elem = l.pop()
                if dic[i] != elem:
                    return  False
        return True if not l else False