from collections import deque, defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacency = defaultdict(list)
        closest = {}

        for source, target, w in times:
            adjacency[source].append((target, w))

        min_heap = [(0, k)]
        while min_heap:
            current_w, source = heappop(min_heap)

            if source in closest:
                continue

            closest[source] = current_w

            if len(closest) == n:
                break

            for target, w in adjacency[source]:
                if target not in closest:
                    heappush(min_heap, (current_w + w, target))

        if len(closest) != n:
            return -1
        else:
            return max(closest.values())


print(
    Solution().networkDelayTime(
        times=[
            [4, 2, 76],
            [1, 3, 79],
            [3, 1, 81],
            [4, 3, 30],
            [2, 1, 47],
            [1, 5, 61],
            [1, 4, 99],
            [3, 4, 68],
            [3, 5, 46],
            [4, 1, 6],
            [5, 4, 7],
            [5, 3, 44],
            [4, 5, 19],
            [2, 3, 13],
            [3, 2, 18],
            [1, 2, 0],
            [5, 1, 25],
            [2, 5, 58],
            [2, 4, 77],
            [5, 2, 74],
        ],
        n=5,
        k=3,
    )
)
