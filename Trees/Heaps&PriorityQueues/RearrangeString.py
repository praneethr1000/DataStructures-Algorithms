'''
Given a string S, check if the letters can be rearranged so that two
characters that are adjacent to each other are not the same.
If possible, output any possible result.  If not possible, return the empty string.

'''

from collections import Counter
from heapq import heappop, heappush

class Solution:
    def reorganizeString(self, S: str) -> str:
        counter = Counter(S)
        heap = []
        for key, value in counter.items():
            heappush(heap, (-value, key))
        print(heap)
        held = None
        ans = ''
        while heap:
            popped_value, popped_key = heappop(heap)
            ans += popped_key
            if held:
                heappush(heap, held)
                held = None
            popped_value += 1
            if popped_value != 0:
                held = (popped_value, popped_key)

        if len(S) != len(ans):
            return ''
        return ans

s = Solution()
print(s.reorganizeString("geeksforgeeks"))