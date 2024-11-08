import random
import bisect
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.w = []
        total = 0
        for weight in w:
            total += weight
            self.w.append(total)
        self.total = total

        

    def pickIndex(self) -> int:
        # this func need to pick an index randomly
        # that is within the range with higher nums
        # increasing the probablity
        r_num = random.randint(1, self.total)
        bisect.bisect_left(self.w, r_num)
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()