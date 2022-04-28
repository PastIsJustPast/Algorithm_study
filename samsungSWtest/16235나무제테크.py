'''
43퍼에서 시간초과
'''

'''
배운점 : 
- 작은 값을 추출할 때 힙큐를 반복적으로 사용하는 것 보다 sort후 순서대로 출력하는게 더 빠름
- 제한시간 짧고, 삭제 후 추가가 많은 문제에서는 정렬을 최소화 하는 것이 관건.
- pop과 슬라이싱 활용하면 더 빠름
'''
n,m,k = map(int,input().split())
k = 5
food = [list(map(int,input().split())) for _ in range(n)]
trees = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    _x, _y, _z = map(int, input().split())
    trees[_x-1][_y-1].append(_z)


trees = [[[], [], [], [], []], [[3], [], [], [], []], [[], [3], [], [], []], [[], [], [], [], []], [[], [], [], [], []]]


'''봄 여름 가을 겨울
input :  
참조 : 나무, 현재 양분, 
output : 변경 후 나무 및 양분
'''
direc = [(0,1),(0,-1),(1,1),(1,-1),(1,0),(-1,0),(-1,1),(-1,-1)]
def ssfw():
    global maps, trees
    '''봄'''
    #양분먹이고, 부족하면 제거
    die = []
    growth = [] #증식할 나무
    
    for x in range(n):
        for y in range(n):
            for idx in range(len(trees[x][y])) :

                z = trees[x][y][idx] #x,y에 있는 idx번째 나무
                
                if maps[x][y] >= z : #양분을 먹을 수 있으면
                    maps[x][y] -= z
                    z += 1
                    trees[x][y][idx] =  z #크기 증가
                    if z % 5 == 0 :
                        growth.append((z,x,y))
                else :
                    die.append((z,x,y,idx))

    '''여름'''    #양분 및 나무 초기화
    if die != []:
        for z,x,y,idx in die:
            del trees[x][y][idx]
            if z >= 2:
                maps[x][y] += z//2

    '''가을'''
    if growth != []:
        for z, x, y in growth:
            for dx, dy in direc:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                trees[nx][ny] = [1] + trees[nx][ny]

    '''겨울'''
    maps = [[maps[i][j] + food[i][j] for j in range(n)] for i in range(n)]

trees
maps = [[5 for _ in range(n)] for _ in range(n)] #잔여 양분
for _ in range(k):
    ssfw()

count = 0
for i in range(n):
    for j in range(n) :
        count += len(trees[i][j])
print(count)


