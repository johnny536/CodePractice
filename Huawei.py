
# If you need to import additional packages or classes, please import here.
import sys
from collections import deque
def func():

    # please define the python3 input here. For example: a,b = map(int, input().strip().split())
    input = sys.stdin.readline
    N, M, H, S = map(int, input().split())
    w = list(map(int, input().split()))
    a = [0] + [abs(x) for x in w]

    K = (S - N*M)
    if K > N:
        K = N
    
    max_abs = max(a)
    thresholds = []
    s = 0

    while True:
        t = 1 << (M - 1 + s)
        thresholds.append(t)
        if t > max_abs:
            break
        s += 1
    T = len(thresholds)

    prefix_err = [[0] * (N + 1) for _ in range(T)]
    for s in range(T):
        if s == 0:
            continue
        d = 1 << s
        pe = prefix_err[s]
        for i in range(1, N + 1):
            r = a[i] % d
            pe[i] = pe[i - 1] + r * r

    last_gt = [[0] * (N + 1) for _ in range(T)]
    for s in range(T):
        t = thresholds[s]
        last = 0
        arr = last_gt[s]
        for i in range(1, N + 1):
            if a[i] > t:
                last = i
            arr[i] = last

    INF = 10**30

    dp_prev = [INF] * (N + 1)
    dp_prev[0] = 0

    for k in range(1, K+1):
        dp_cur = [INF] * (N + 1)
        deques = [deque() for _ in range(T)]
        added_until = [-1] * T

        for r in range(1, N+1):
            if r < k:
                continue

            best = INF

            for s in range(T):
                j_min = last_gt[s][r]

                if s == 0:
                    j_max = r - 1
                else:
                    j_max = last_gt[s-1][r] - 1

                while added_until[s] < j_max:
                    added_until[s] += 1
                    j = added_until[s]

                    val = dp_prev[j] - prefix_err[s][j]
                    dq = deques[s]
                    while dq and dq[-1][1] >= val:
                        dq.pop()
                    dq.append((j, val))

                dq = deques[s]
                while dq and dq[0][0] < j_min:
                    dq.popleft()
                if dq:
                    cand = dq[0][1] + prefix_err[s][r]
                    if cand < best:
                        best = cand
            dp_cur[r] = best
        dp_prev = dp_cur
    print(dp_prev[N])

    # please finish the function body here.
    # please define the python3 output here. For example: print().

if __name__ == "__main__":
    func()