##로직
- 사방향으로 이동 후 제거하는 함수 생성
- 큐 구조를 이용해 빈칸이 아닌 값을 수집하고 뿌림
- 이 때 큐에서 빼낸 값과 큐의 첫번째 값이 같다면 두 값을 합쳐서 뿌리는 방식으로, 합치기를 실행

##쟁점
- 블럭당 합치기는 한번만 가능함
 => 큐에서 뺄때부터 값을 더함으로 이를 해결

##배운점
- 조합 : 순서 상관 없음
- 순열 : 순서 상관 있음
- 중복 순열 및 중복 조합 : 조합과 순열의 원소 중 복원추출을 허용할 경우
- 이때 itertools보다는 백트래킹 방식으로 구현하는 것이 좋음

from collections import deque
from itertools import product

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
direc = [0, 1, 2, 3]  # 왼 위 오 아


# 이동 후 제거
def move_del(graph, d):
    temp = [[0] * n for _ in range(n)]
    if d == 0:  # 왼쪽
        for i in range(n):
            # 수집
            q = deque()
            for j in range(n):
                if graph[i][j] != 0:
                    q.append(graph[i][j])
            # 뿌리기
            j = 0
            while q:
                col = q.popleft()
                if q != deque() and col == q[0]:  # 나오려는 두 값이 다르다면 애초에 합해서 나오기
                    col += q.popleft()
                temp[i][j] = col
                j += 1

    elif d == 1:  # 위쪽
        for j in range(n):
            # 수집
            q = deque()
            for i in range(n):
                if graph[i][j] != 0:
                    q.append(graph[i][j])
            # 뿌리기
            i = 0
            while q:
                col = q.popleft()
                if q != deque() and col == q[0]:  # 나오려는 두 값이 다르다면 애초에 합해서 나오기
                    col += q.popleft()
                temp[i][j] = col
                i += 1

    elif d == 2:  # 오른쪽
        for i in range(n):
            # 수집
            q = deque()
            for j in range(n - 1, -1, -1):
                if graph[i][j] != 0:
                    q.append(graph[i][j])
            # 뿌리기
            j = n - 1
            while q:
                col = q.popleft()
                if q != deque() and col == q[0]:  # 나오려는 두 값이 다르다면 애초에 합해서 나오기
                    col += q.popleft()
                temp[i][j] = col
                j -= 1
    else:  # 아래쪽
        for j in range(n):
            # 수집
            q = deque()
            for i in range(n - 1, -1, -1):
                if graph[i][j] != 0:
                    q.append(graph[i][j])
            # 뿌리기
            i = n - 1
            while q:
                col = q.popleft()
                if q != deque() and col == q[0]:  # 나오려는 두 값이 다르다면 애초에 합해서 나오기
                    col += q.popleft()
                temp[i][j] = col
                i -= 1
    return temp


# 최대값 찾기
def search_max(graph):
    return max(map(max, graph))


# 모든 경우의 수 / 최대 1024/ 중복을 허용한 순열
max_block = 0
for info in product(direc,direc,direc,direc,direc):
    temp = graph #원본을 유지하기 위해 temp에 저장
    for d in info:
        temp = move_del(temp,d)

    # 최대값 찾기
    max_block = max(max_block, search_max(temp))
print(max_block)






