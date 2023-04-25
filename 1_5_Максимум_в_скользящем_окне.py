n = int(input())
listE = list(map(int, input().split()))
k = int(input())

from collections import deque

dq = deque()
for i in range(k):
    while dq and listE[i] >= listE[dq[-1]]:
        dq.pop()
    dq.append(i)

for i in range(k, n):
    print(listE[dq[0]], end=' ')
    while dq and dq[0] <= i - k:
        dq.popleft()
    while dq and listE[i] >= listE[dq[-1]]:
        dq.pop()
    dq.append(i)

print(listE[dq[0]])