from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토 없음
# 1과 인접한 토마토는 하루가 지나면 익게 된다.
m, n = map(int, input().split()) #가로, 세로

graph = [ list(map(int,input().split())) for _ in range(n)]

queue = deque()
for i in range(n):
  for j in range(m):
    if graph[i][j]==1:
      queue.append((i,j))

while queue:
  x, y = queue.popleft()
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if nx<0 or nx>=n or ny<0 or ny>=m:
      continue
    if graph[nx][ny]==0:
      queue.append((nx,ny))
      graph[nx][ny] = graph[x][y]+1

flag = False
for i in range(n):
  for j in range(m):
    if graph[i][j]==0:
      flag=True

if flag:
  print(-1)
else:
  print(max(map(max,graph))-1)