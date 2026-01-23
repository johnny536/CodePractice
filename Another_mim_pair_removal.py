from typing import List
import heapq


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # Doubly-linked list over indices (nodes survive; merges deactivate the right node)
        prev = list(range(-1, n - 1))
        nxt = list(range(1, n)) + [-1]
        alive = [True] * n

        def bad(i: int, j: int) -> int:
            return 1 if i != -1 and j != -1 and nums[i] > nums[j] else 0

        # Count current "descending" adjacent edges
        bad_count = 0
        for i in range(n):
            if nxt[i] != -1:
                bad_count += bad(i, nxt[i])

        if bad_count == 0:
            return 0

        # Min-heap of adjacent pairs: (sum, left_original_index, left_id, right_id)
        heap = []
        for i in range(n):
            j = nxt[i]
            if j != -1:
                heapq.heappush(heap, (nums[i] + nums[j], i, i, j))

        ops = 0

        while bad_count > 0:
            # Get the current minimum-sum adjacent pair (tie by smallest left index)
            while True:
                s, left_idx, a, b = heapq.heappop(heap)
                if not alive[a] or not alive[b]:
                    continue
                if nxt[a] != b:  # no longer adjacent
                    continue
                if nums[a] + nums[b] != s:  # values changed since push
                    continue
                break

            p = prev[a]
            q = nxt[b]

            # Remove old edges involving p-a, a-b, b-q
            bad_count -= bad(p, a)
            bad_count -= bad(a, b)
            bad_count -= bad(b, q)

            # Merge b into a
            nums[a] += nums[b]
            alive[b] = False

            # Relink list: p - a - q
            nxt[a] = q
            if q != -1:
                prev[q] = a

            ops += 1

            # Add new edges p-a, a-q
            bad_count += bad(p, a)
            bad_count += bad(a, q)

            # Push updated adjacent pairs that could become the new minimum
            if p != -1:
                heapq.heappush(heap, (nums[p] + nums[a], p, p, a))
            if q != -1:
                heapq.heappush(heap, (nums[a] + nums[q], a, a, q))

        return ops