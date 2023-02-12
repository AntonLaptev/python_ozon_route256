from collections import Counter


def is_contiguous(map_, n, m):
    for color, count_ in color_count.items():
        visited = [[False for _ in range(m)] for _ in range(n)]
        sdc = 0
        for i in range(n):
            if sdc == 1:
                break
            for j in range(m):
                if map_[i][j] == color:
                    sdc = 1
                    visited1 = [map_[i][j]]
                    line = [[i, j]]
                    visited[i][j] = True
                    break

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or visited[i][j] or map_[i][j] != color:
                return
            line.append([i, j])
            visited[i][j] = True
            visited1.append(map_[i][j])
        while line:
            i, j = line.pop(0)
            if map_[i][j] != '.' and map_[i][j] == color:
                dfs(i-1, j-1)
                dfs(i, j-2)
                dfs(i+1, j-1)
                dfs(i-1, j+1)
                dfs(i, j+2)
                dfs(i+1, j+1)
        if len(visited1) != count_:
            return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    map_ = [input() for _ in range(n)]
    map1_ = []
    for i in range(n):
        map1_ += map_[i]
    color_count = dict(Counter(map1_))
    del color_count['.']
    print(is_contiguous(map_, n, m))
