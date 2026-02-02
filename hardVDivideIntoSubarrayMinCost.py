from typing import List
import heapq
from collections import defaultdict

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        need = k - 1                    # how many starts to pick besides index 0
        if need == 0:
            return nums[0]

        # We slide a window over indices [1..n-1] of size dist+1.
        # Maintain sum of 'need' smallest values in the window.

        small = []   # max-heap via (-value, idx): holds the chosen 'need' smallest
        large = []   # min-heap via (value, idx): holds the rest
        where = {}   # idx -> 0 if in small, 1 if in large (conceptually)
        delayed = defaultdict(int)
        sum_small = 0
        size_small = 0
        size_large = 0

        def prune(heap, is_small: bool):
            # remove elements that are marked deleted
            while heap:
                val, idx = heap[0]
                if delayed[idx] > 0:
                    heapq.heappop(heap)
                    delayed[idx] -= 1
                else:
                    break

        def move_small_to_large():
            nonlocal sum_small, size_small, size_large
            prune(small, True)
            vneg, idx = heapq.heappop(small)
            v = -vneg
            sum_small -= v
            size_small -= 1
            heapq.heappush(large, (v, idx))
            where[idx] = 1
            size_large += 1

        def move_large_to_small():
            nonlocal sum_small, size_small, size_large
            prune(large, False)
            v, idx = heapq.heappop(large)
            heapq.heappush(small, (-v, idx))
            where[idx] = 0
            sum_small += v
            size_large -= 1
            size_small += 1

        def rebalance():
            prune(small, True)
            prune(large, False)
            while size_small > need:
                move_small_to_large()
                prune(small, True)
                prune(large, False)
            while size_small < need and size_large > 0:
                move_large_to_small()
                prune(small, True)
                prune(large, False)

        def add_idx(i: int):
            nonlocal sum_small, size_small, size_large
            v = nums[i]
            if size_small < need:
                heapq.heappush(small, (-v, i))
                where[i] = 0
                sum_small += v
                size_small += 1
            else:
                prune(small, True)
                # compare with current largest among the chosen smallest
                if small and v < -small[0][0]:
                    heapq.heappush(small, (-v, i))
                    where[i] = 0
                    sum_small += v
                    size_small += 1
                    move_small_to_large()
                else:
                    heapq.heappush(large, (v, i))
                    where[i] = 1
                    size_large += 1
            rebalance()

        def remove_idx(i: int):
            nonlocal sum_small, size_small, size_large
            delayed[i] += 1
            if where.get(i, 1) == 0:
                # removing from small
                sum_small -= nums[i]
                size_small -= 1
            else:
                size_large -= 1
            # actual pop happens in prune()
            rebalance()

        # initial window: indices [1 .. min(n-1, 1+dist)]
        L = 1
        R = min(n - 1, 1 + dist)
        for i in range(L, R + 1):
            add_idx(i)

        # window must have at least 'need' elements
        ans = float("inf")
        if R - L + 1 >= need:
            ans = nums[0] + sum_small

        # slide L from 2..n-1, expanding R accordingly (keeping R-L <= dist)
        for L in range(2, n):
            remove_idx(L - 1)
            newR = min(n - 1, L + dist)
            while R < newR:
                R += 1
                add_idx(R)
            if R - L + 1 >= need:
                ans = min(ans, nums[0] + sum_small)

        return ans