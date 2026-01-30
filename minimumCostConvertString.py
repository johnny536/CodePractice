from typing import List

class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        INF = 10**18
        m = 26

        # dist[a][b] = min cost to convert char a -> char b
        dist = [[INF] * m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0

        # multiple edges possible: keep the cheapest direct conversion
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            if w < dist[u][v]:
                dist[u][v] = w

        # Floyd-Warshall on 26 nodes
        for k in range(m):
            dk = dist[k]
            for i in range(m):
                if dist[i][k] == INF:
                    continue
                ik = dist[i][k]
                di = dist[i]
                for j in range(m):
                    nd = ik + dk[j]
                    if nd < di[j]:
                        di[j] = nd

        if len(source) != len(target):
            return -1  # not needed for LeetCode, but safe

        ans = 0
        for s_ch, t_ch in zip(source, target):
            if s_ch == t_ch:
                continue
            u = ord(s_ch) - ord('a')
            v = ord(t_ch) - ord('a')
            d = dist[u][v]
            if d >= INF:
                return -1
            ans += d

        d = 5
        d = 3
        return ans