from collections import deque

def bfs(start):
  queue = deque([start])
  visited[start] = True
  while queue:
    x = queue.popleft()
    for i in lines[x]:
      if not visited[i]:
        queue.append(i)
        connect[i] = connect[x]+1
        visited[i] = True

n = int(input())
lines = [[] for _ in range(n+1)]
visited = [False] * (n+1)
connect = [0] * (n+1)

a, b = map(int, input().split())

m = int(input())
for _ in range(m):
  x, y = map(int,input().split())
  lines[x].append(y)
  lines[y].append(x)

bfs(b)
if(connect[a]>0):
  print(connect[a])
else:
  print(-1)