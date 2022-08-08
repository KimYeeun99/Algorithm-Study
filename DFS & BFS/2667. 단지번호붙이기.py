from collections import deque

def bfs(x,y,graph):
  if not graph[x][y]:
    return 0
  
  n = len(graph)
  
  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]

  count = 0
  queue = deque()
  queue.append((x,y))

  while queue:
    zx, zy = queue.popleft()
    if not graph[zx][zy]:
      continue
    graph[zx][zy] = 0
    count+=1
    for i in range(4):
      if zx+dx[i]<0 or zx+dx[i]>=n or zy+dy[i]<0 or zy+dy[i]>=n:
        continue
      if(graph[zx+dx[i]][zy+dy[i]]):
        queue.append((zx+dx[i], zy+dy[i]))
  return count

n = int(input())

graph = [list(map(int,input())) for _ in range(n)]

result = []

for i in range(n):
  for j in range(n):
    if (graph[i][j]!=0):
      cnt = bfs(i,j,graph)
      result.append(cnt)

result.sort()
print(len(result))
for r in result:
  print(r)