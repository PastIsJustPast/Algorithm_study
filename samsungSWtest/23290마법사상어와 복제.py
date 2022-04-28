from copy import deepcopy
m,s = map(int,input().split())
fish_loc = []
for info in input().split("\n") :
    fish_loc.append(list(map(lambda x : int(x)-1,info.split())))
sx,sy = (map(lambda x : int(x)-1,input().split()))

'''로직
- 물고기 이동함수 + 상어이동함수 + 전체 과정 함수
- s번의 dfs가 수행되기 때문에 시간 문제 없음. 시뮬레이션만 잘하면 됨
- 물고기 위치 및 방향은 2차원 격자 리스트에 저장 fish[x][y] = [d]
- 냄새는 2차원 리스트에 스칼라로 저장. 새로 생기면 그냥 2추가

'''


'''물고기 이동함수
모든 물고기의 다음 이동 자리를 임시 temp에 포함
물고기 다음위치 탐색 -> 방향 설정 -> temp에 이동 -> 반복 -> fish에 저장
'''
direc = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)] #←, ↖, ↑, ↗, →, ↘, ↓, ↙
def move_fish():
    temp = [[[] for _ in range(4)] for _ in range(4)]
    for fx in range(4) :
        for fy in range(4) :
            if fish[fx][fy] != [] : #물고기가 있다면
                for d in fish[fx][fy]:
                    fd = d
                    #방향 설정
                    for _ in range(8):
                        dx,dy = direc[fd]
                        nx,ny = fx + dx , fy + dy
                        if nx < 0 or  nx >= 4 or ny < 0 or ny >= 4 or smell[nx][ny] > 0 or (nx,ny) == (sx,sy) :
                            fd = (fd + 7 ) % 8 #아니면 반시계
                        else : break
                    if d != fd : #방향이 바뀌면
                        #이동
                        temp[nx][ny].append(fd)
                    else :
                        temp[fx][fy].append(fd)
    return temp
'''상어이동
- dfs기반
- 이동거리가 3칸이면 그 때 까지 먹은 값 찾고  갱신, 갱신되면 이동 위치 + 냄새 갱신(이동경로는 필요없고 냄새로 대체)
- 이동가능한게 여러개면 사전위치대로 해야함
- 상어는 상 좌 하 우 우선탐색

output = 현재 시점에서 최대 먹이, 이동경로
'''
dx = [-1,0,1,0] #상좌하우
dy = [0,-1,0,1]
def move_shark(x,y,cnt,food,traj):
    global fish ,max_food,move_traj
    #갱신
    if cnt == 3 :
        #print(traj)
        if food > max_food : #사전순 정의
            max_food = food
            move_traj = traj
        return

    #처음 상어 위치
    visited[x][y] = True

    #다음 위치
    for i in range(4):
        nx,ny = x + dx[i],y+dy[i]
        if nx < 0 or  nx >= 4 or ny < 0 or ny >= 4 or visited[nx][ny] == True : continue

        traj = traj + [(nx,ny)]
        move_shark(nx,ny,cnt+1,food +len(fish[nx][ny]),traj) # 다음위치에 횟수 + 물고기수
        traj = traj[:len(traj)-1]
    return



sx,sy=3,1
'''프로세스'''
fish = [[[] for _ in range(4)] for _ in range(4)]
for fx, fy, fd in fish_loc:
    fish[fx][fy].append(fd)
smell = [[0 for _ in range(4)] for _ in range(4)]

for _ in range(s) :
    '''복제시전'''
    copy_fish = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if fish[i][j] != [] :
                copy_fish[i][j] = fish[i][j]

    '''물고기 이동'''
    fish = move_fish()

    '''상어이동 및 먹이'''
    visited = [[False for _ in range(4)] for _ in range(4)]
    move_traj = []
    max_food = 0
    move_shark(sx, sy, 0, len(fish[sx][sy]), [(sx, sy)])

    sx,sy = move_traj[3] #상어 위치 이동

    '''물고기 냄새 사라짐, 순서바꾸면 연산 쉬움'''
    for i in range(4):
        for j in range(4):
            if smell[i][j]> 0 :
                smell[i][j] -= 1

    '''물고기 냄새'''
    for i,j in move_traj:
        if fish[i][j] != [] : #물고기가 먹혔다면
            fish[i][j] = []
            smell[i][j] = 2


    '''복제'''
    for i in range(4):
        for j in range(4):
            if copy_fish[i][j] != [] : #복제된 물고기가 있다면
                fish[i][j] += copy_fish[i][j]


count = 0
for i in  range(4):
    for j in range(4):
        count +=len(fish[i][j])
print(count)