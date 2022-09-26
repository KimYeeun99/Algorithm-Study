import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 로봇 청소기가 있는 칸의 좌표 = (r,c)
# 로봇 청소기가 바라보는 방향 = d ->0: 북, 1: 동, 2:남, 3: 서
r, c, d = map(int, input().split())

floor = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

#북, 동, 남, 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
  global d
  d -= 1
  if d==-1:
    d = 3

visited[r][c] = 1
cnt = 1
turn_time=0

while True:
  turn_left()
  nx = r+dx[d]
  ny = c+dy[d]

  if visited[nx][ny] == 0 and floor[nx][ny] == 0: # 이동을 했는데, 방문하지 않았거나, 빈 공간인 경우
    visited[nx][ny] = 1
    r = nx
    c = ny
    cnt+=1
    turn_time = 0
    continue
  else:
    turn_time+=1
    if turn_time==4:
      nx = r-dx[d]
      ny = c-dy[d]
      if floor[nx][ny]==0:
        r = nx
        c = ny
      else:
        break
      turn_time=0
print(cnt)