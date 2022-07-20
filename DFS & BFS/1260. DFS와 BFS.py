from collections import deque

# 1) 모든 정점을 방문하는 주요한 문제 -> BFS, DFS 사용 가능
# 2) 경로의 특징을 둬야하는 문제 -> DFS 사용 (BFS는 경로의 특징을 가지지 못함)
# ex) 각 정점에 숫자가 적혀있고 a부터 b까지 가는 경로를 구하는데 경로에 같은 숫자가 있으면 안 된다는 문제
# 3) 최단거리 구해야하는 문제 -> BFS가 유리 (ex. 미로찾기)

'''
깊이 우선 탐색(Depth-First-Search)
- 최대한 깊이 내려간 뒤, 더이상 깊이 갈 곳이 없을 경우 옆으로 이동
- 현재 정점에서 갈 수 있는 점들까지 들어가면서 탐색
- Stack 또는 재귀함수를 사용하여 구현
'''
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    graph[v].sort()
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

'''
너비 우선 탐색(Breadth-First-Search)
- 최대한 넓게 이동한 다음, 더 이상 갈 곳이 없을 경우 아래로 이동
- 현재 정점에 연결된 가까운 점들부터 탐색
- Queue 이용하여 구현
'''
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        graph[v].sort()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False]*(n+1)
dfs(graph, v, visited)
print() #줄바꿈을 하기 위해 사용

visited = [False]*(n+1)
bfs(graph, v, visited)
