from collections import deque
import sys

input = sys.stdin.readline

def bfs(start):
  queue=deque([start])
  visited[start] = True

  while queue:
    node = queue.popleft()
    for i in lines[node]:
      if not visited[i]:
        queue.append(i)
        visited[i]=True

n, m = map(int, input().split())

lines = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
  n1, n2 = map(int, input().split())
  lines[n1].append(n2)
  lines[n2].append(n1)

cnt=0
for i in range(1,n+1):
  if not visited[i]:
    bfs(i)
    cnt+=1

print(cnt)