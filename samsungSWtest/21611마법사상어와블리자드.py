'''
pypy3
117388kb
240ms
'''

'''
로직
- 달팽이 그림을 1차원 배열로 풀어서 문제를 품 -> 1차원 배열로 풀었을 때 이후 모든 연산이 더 쉬우므로
- 블리자드 함수 + 폭발함수 + 구슬 증식함수와 앞으로 당기는 함수를 만듬
- 블리자드 함수는 그리드 상에서 터지는 부분의 번호를 찾고 1차원리스트의 값을 0으로 바꿔주는 역할
- 폭발함수는 연속된 값을 찾고(two point) 제거 + 앞으로 당김
- 구슬증식함수는 연속된 값을 찾고 갯수 + 번호를 임시 배열에 저장. 중복 서칭 방지를 위해 연속된 값을 0으로 변경시켜줌

쟁점 
- 폭발함수에서 더 이상 없앨 구슬이 없을 경우를 결정하기 위해 폭발이 일어날때마다 카운트하고, 폭발 없으면 중지시킴

배운점
- 달팽이를 1차원 배열로 푸는것이 더 쉬움.
 => 필요에 의해 달팽이 위치에 맞는 번호를 찾는 것이 더 쉽다
- two point를 활용해 연속된 값을 찾을 수 있음
'''


from copy import deepcopy
n,m = map(int,input().split())
#graph = [list(map(int,input().split())) for _ in range(n)]
'''
orders = []
for _ in range(m) : 
    _d , _s  = map(int,input().split())
    orders.append((_d-1,_s))
'''


graph = []
for info in input().split("\n"):
    graph.append(list(map(int,info.split())))
orders = []
for info in input().split("\n"):
    _d,_s = map(int, info.split())
    orders.append((_d-1,_s))

'''달팽이 그리드 생성'''
temp = [[0 for _ in range(n)] for _ in range(n)] #블리자드때 위치 -> 리스트 인덱스 찾기 위함
dx = [0, 1, 0, -1]  # 좌 하 우 상
dy = [-1, 0, 1, 0]
balls = [] #구슬을 1차원 배열로 정렬

sx, sy = n // 2, n // 2
for level in range(1, n // 2 + 1):
    # 좌로 한번
    nx, ny = sx + dx[0], sy + dy[0]
    temp[nx][ny] = temp[sx][sy] + 1
    balls.append(graph[nx][ny]) #리스트로 추가
    sx, sy = nx, ny

    # 아래로 2level - 1
    for _ in range(2 * level - 1):
        nx, ny = sx + dx[1], sy + dy[1]
        temp[nx][ny] = temp[sx][sy] + 1
        balls.append(graph[nx][ny])  # 리스트로 추가
        sx, sy = nx, ny

    # 우상좌 2level번
    for i in [2, 3, 0]:
        for _ in range(2 * level):
            nx, ny = sx + dx[i], sy + dy[i]
            temp[nx][ny] = temp[sx][sy] + 1
            balls.append(graph[nx][ny])  # 리스트로 추가
            sx, sy = nx, ny

if balls == [ 0 for _ in range(n**2 - 1)] :
    balls = []

'''그리드 위치에 따른 번호 찾기'''
def search_num(x,y):
    return temp[x][y] - 1


'''블리자드 함수
input = 주문
참조 = lst, 위치 차즌ㄴ 함수, 앞으로 당기는 함수
output = 주문 후 lst
주문 -> 얼음깨기 -> 앞으로 당기기
'''
def blizzard(d,s):
    global lst
    bdx = [-1,1,0,0] #상하좌우
    bdy = [0,0,-1,1]

    #얼음깨기
    for i in range(1,s+1):
        nx = n//2 + bdx[d]* i
        ny = n//2 + bdy[d]* i
        idx = search_num(nx, ny)
        if len(lst) > idx :
            lst[idx] = 0

    #앞으로 당기기
    lst= compress(lst)


'''구슬 폭발 함수
연속된 구슬 갯수를 파악하고 4개 이상이면 모두 0으로 바꿈, 이때 값에 따라서 answer출력
'''
def boom():
    global lst,answer
    if lst == [] :
        return

    while True :
        cnt = 0
        for i in range(len(lst) - 1):
            if lst[i] == 0: continue
            # 연속된 구술
            j = i + 1
            while j < len(lst):
                if lst[i] == lst[j]:
                    j += 1
                else:
                    break
            # 연속된 구슬이 4개 이상일 경우 제거
            if j - i >= 4:
                answer[lst[i] - 1] += (j - i)
                lst[i:j] = [0 for _ in range(j - i)]
                cnt += 1

        lst = compress(lst)
        if cnt == 0 : break #변화가 없으면 끝

'''앞으로 당기는 함수'''
def compress(lst):
    if lst == [] :
        return []
    last = 0
    for i in range(len(lst)) :
        if lst[i] != 0 :
            lst[last] = lst[i]
            last += 1
    return lst[:last]

'''구슬 증식시키는 함수'''
def add_balls():
    global lst
    if lst == [] : return
    temp_lst = []
    for i in range(len(lst)):
        if lst[i] == 0: continue
        # 연속된 구술
        j = i + 1
        while j < len(lst):
            if lst[i] == lst[j]:
                j += 1
            else:
                break
        value = lst[i]
        #증식
        lst[i:j] = [0 for _ in range(j - i)]
        temp_lst +=[j-i,value]

    #자르기
    lst = temp_lst
    if len(lst) > n**2 -1  :
        lst = lst[: n**2 -1]


'''프로세스
마법 -> 구슬 폭발 -> 증식
'''

answer = [0 for _ in range(3)]
lst = compress(balls)
for d,s in orders :
    blizzard(d, s)
    boom()
    add_balls()


print(answer[0] + 2 * answer[1] + 3* answer[2])



