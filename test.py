import sys
sys.setrecursionlimit(10000)

def dfs(x, y, field, visited):
    stack = [(x, y)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 방향
    while stack:
        cx, cy = stack.pop()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(field) and 0 <= ny < len(field[0]) and not visited[nx][ny] and field[nx][ny] == 1:
                visited[nx][ny] = True
                stack.append((nx, ny))

def solve():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []

    for _ in range(T):
        M = int(data[idx])
        N = int(data[idx + 1])
        K = int(data[idx + 2])
        idx += 3

        field = [[0] * M for _ in range(N)]
        visited = [[False] * M for _ in range(N)]

        for _ in range(K):
            x = int(data[idx])
            y = int(data[idx + 1])
            idx += 2
            field[y][x] = 1

        count = 0
        for i in range(N):
            for j in range(M):
                if field[i][j] == 1 and not visited[i][j]:
                    visited[i][j] = True
                    dfs(i, j, field, visited)
                    count += 1

        results.append(count)

    for result in results:
        print(result)

solve()