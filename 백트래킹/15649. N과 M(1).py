n, m = map(int, input().split())
tmp = []

def dfs(level):
  if level == m:
    print(' '.join(map(str, tmp)))
    return

  for i in range(1, n+1):
    if i not in tmp:
      tmp.append(i)
      dfs(level+1)
      tmp.pop()
      
dfs(0)