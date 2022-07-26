from collections import deque

def bfs(graph, start, virus):
  virus[start] = True
  queue = deque([start])
  while queue:
    data = queue.popleft()
    for i in graph[data]:
      if not virus[i]:
        queue.append(i)
        virus[i] = True
  return virus.count(True)-1

n = int(input())
lines = int(input())

virus = [False] * (n+1)

graph = [[] for _ in range(n+1)]

for i in range(lines):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

print(bfs(graph, 1, virus))