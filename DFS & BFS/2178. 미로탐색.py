from collections import deque

n, m = map(int, input().split())

graph = [ list(map(int, input())) for _ in range(n) ]

def bfs(x, y):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  
  #Queue 생성
  queue = deque()
  queue.append((x,y))
  
  while queue:
    x, y = queue.popleft()
  
    #4가지 방향으로 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
  
      #위치가 벗어나서는 안됨
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      
      #벽이므로 진행 불가
      if graph[nx][ny] == 0:
        continue
  
      #벽이 아니므로 이동
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  return graph[n-1][m-1]

print(bfs(0,0))