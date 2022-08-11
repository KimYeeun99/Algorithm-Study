from collections import deque

def bfs(n):
  global visited
  queue =deque([n])

  while queue:
    n = queue.popleft()
    if n==k:
      return visited[n]
    for i in (n+1, n-1, n*2):
      if i<0 or i>=100001:
        continue
      if visited[i]==0:
        visited[i]=visited[n]+1
        queue.append(i)
      

n, k = map(int, input().split())

visited = [0 for _ in range(100001)]
print(bfs(n))