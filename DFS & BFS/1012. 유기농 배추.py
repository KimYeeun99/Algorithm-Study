from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
  global graph
  if graph[x][y]==1:
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0

    while queue:
      x, y = queue.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
          continue
        if graph[nx][ny]==0:
          continue
        if graph[nx][ny] == 1:
          queue.append((nx,ny))
          graph[nx][ny] = 0
    return True
  else:
    return False
      
  

t = int(input())

for _ in range(t):
  cnt = 0
  m, n, k = map(int, input().split())
  graph = [[0]*m for i in range(n) ]

  for _ in range(k):
    y, x = map(int, input().split())
    graph[x][y]=1

  for i in range(n):
    for j in range(m):
      if graph[i][j]:
        if bfs(i,j)==True:
          cnt+=1
  print(cnt)