class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        l = []
        for i in range(len(temperatures)):
            if l and temperatures[i] > temperatures[l[-1]]:
                while l and temperatures[i] > temperatures[l[-1]]:
                    result[l[-1]] = i-l[-1]
                    l.pop()

            l.append(i)

        return result