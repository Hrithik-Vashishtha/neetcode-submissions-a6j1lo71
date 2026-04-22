class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_ = 1
        max_ = max(piles)

        time_min = max_
        while min_ <= max_:
            avg = (min_ + max_) // 2
            curr_time = 0
            for pile in piles:
                curr_time += (pile + avg - 1) // avg

            if curr_time > h:
                min_ = avg + 1

            if curr_time <= h:
                time_min = min(time_min, avg)
                max_ = avg - 1

        return time_min