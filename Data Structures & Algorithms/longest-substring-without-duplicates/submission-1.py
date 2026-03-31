class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1

        dic = {}
        dic[s[0]] = 1

        i, j, max_len = 0, 1, 0
        while j < len(s):
            if dic.get(s[j], 0) == 1:
                max_len = max(max_len, j-i)
                while s[i] != s[j]:
                    dic[s[i]] = 0
                    i += 1
                i += 1
            dic[s[j]] = 1
            j += 1

        return max(max_len, j-i)