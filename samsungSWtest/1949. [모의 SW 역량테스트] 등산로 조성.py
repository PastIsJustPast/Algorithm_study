# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.
# dfs 높은곳에서 시작
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(sx, sy, visited, cnt):
    global max_cnt
    visited[sx][sy] = True
    for i in range(4):
        nx, ny = sx + dx[i], sy + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
        if graph[nx][ny] < graph[sx][sy]:  # 더 작으면 이동
            dfs(nx, ny, visited, cnt + 1)

    # 만약 더이상 갈 곳 없다면
    if max_cnt < cnt: max_cnt = cnt
    return

T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    # 최대값
    max_num = 0
    lst = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == max_num:
                lst.append((i, j))
            elif graph[i][j] > max_num:
                max_num = graph[i][j]
                lst = [(i, j)]

    max_cnt = 1
    for i in range(n):
        for j in range(n):
            for z in range(1, k + 1):
                if graph[i][j] < z: continue
                graph[i][j] -= z  # 깍고
                for sx, sy in lst:
                    visited = [[False for _ in range(n)] for _ in range(n)]
                    dfs(sx, sy, visited, 1)
                graph[i][j] += z

    print("#{} {}".format(test_case, max_cnt))
