class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        dic_s1 = {}
        for s in s1:
            dic_s1[s] = dic_s1.get(s, 0) + 1

        i, j = 0, len(s1) - 1
        dic_s2 = {}

        # initial window
        for k in range(j + 1):
            dic_s2[s2[k]] = dic_s2.get(s2[k], 0) + 1

        while j < len(s2):
            if dic_s1 == dic_s2:
                return True

            # remove left char
            dic_s2[s2[i]] -= 1
            if dic_s2[s2[i]] == 0:
                del dic_s2[s2[i]]
            i += 1

            # move right
            j += 1
            if j < len(s2):
                dic_s2[s2[j]] = dic_s2.get(s2[j], 0) + 1

        return False
