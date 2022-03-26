##로직
- 방향 확인 -> 이동할 위치 탐색 -> 머리이동 -> 꼬리 빼기 유무 확인  반복
- 이동할 위치를 탐색할 때 벽이나 꼬리에 부딪히면 횟수 한칸 늘리고 끝내기
- 꼬리는 큐 구조를 이용해서 보관했다가 사과가 없는 곳을 지나갈때마다 큐에서 하나 씩 제거


from collections import deque
n = int(input())
k = int(input())
apple =[tuple(map(int,input().split())) for _ in range(k)]
l = int(input())
move = {}
for _ in range(l):
    second, direc = input().split()
    move[int(second)] = direc



#방향 확인 함수
def check_direc(d,count):
    if count not in move:  # 방향 변경이 없다면
        return d
    direc = move[count]
    if direc == "D": #방향이 D라면
        d = (d+1)%4
    elif direc =="L": #방향이 L이라면
        d = (d+3)%4
    return d

dx = [0,1,0,-1] #오,아,왼, 위
dy = [1,0,-1,0]
tail = deque()
x,y,d = 1,1,0
count = 0
while True:
    ##방향 설정
    d= check_direc(d,count)

    nx = x + dx[d]
    ny = y + dy[d]
    ##다음위치 탐색
    if nx < 1 or nx > n  or ny <1 or ny > n or (nx,ny) in tail :  #격자를 벗어나거나 꼬리에 부딪히면
        count += 1
        break
    ##머리를 꼬리에 추가
    tail.append((x,y))

    ##머리 이동
    x,y = nx,ny

    ##꼬리빼기 유무 결정(사과가 있으면 꼬리를 안뺌)
    if (x,y) in apple :
        apple.remove((x,y))
    else :
        tail.popleft()

    count+=1

print(count)

