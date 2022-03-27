##로직
- 모든 지점에대해 가능한 테크로미노를 만들고 최대 블록값을 계속해서 갱신하면됨
- 테트로미노는 한 블록에서 다양하게 생성되며, 또 각 블록마다 생성되므로 경우의 수가 많음
 => 한 탐색(가지) 중에 앞으로 수집될 블록이 모두 최대값이라고 해도 이전까지의 테트로미토 최대 블록값을 갱신하지 못한다면 중도 종료
- ㅗ모양을 별도의 처리해줘야 하므로 수집된블록이 2개일 때 다음 블록이 아닌 현재 블록에서 분기를 추가해주면 이를 반영할 수 있음

##쟁점사항
-bfs함수에서 분기의 예외처리
 => 현재 노드 반영 -> 다음 노드 탐색 -> 조건에 따라 분기


##배운점
-dfs의 방문처리 방법
1. dfs함수 밖에서 방문처리
2. dfs함수의 도입부에서 해당 지점 방문처리
3. dfs함수의 재귀부분에서 다음 지점 방문처리
- 이때 함수 2번과 3번을 둘다 해줄 경우 하나의 노드가 두번 이상 방문 처리 될 수 있음
- 가급적 시작 노드의 방문처리는 dfs함수 밖에서 선언, 이후 재귀적으로 다음 노드를 방문처리해주는 편이 우수함



n,m =map(int,input().split())
graph = []
for info in input().split("\n"):
    graph.append(list(map(int,info.split())))


def dfs(x,y,visited,count,total):
    global result

    #탐색횟수 꽉 차면 최대값 갱신 후 마무리
    if count == 4 :
        result = max(result, total ) # 해당 점에서 시작된 블록 합을 계산하고 가장 큰 값을 갱신
        return

    #조기 종료 조건 (한 탐색(가지)에서 앞으로 전체 최대 블록 값만을 담아도 최대치를 갱신하지 못하면 조기종료)
    if (total + max_value * (4-count)) < result : return

    #이동할 위치 탐색
    dxs,dys  = [0,0,1,-1] ,[1,-1,0,0]
    for dx,dy in zip(dxs,dys):
        nx,ny  = x + dx, y +dy
        if nx <0  or nx >= n or ny < 0 or ny >= m : continue
        if (nx,ny) not in visited : #한 탐색(가지)에서 방문한적이 없다면

            #분기 시작
            #블럭 두개 수집된 상황에서 제자리에서 분기를 해주면 ㅗ 모양 가능
            if count == 2 :
                visited.append((nx,ny)) #방문 처리 통해 한번 갔던 곳 탐색 하는 경우 없앰
                dfs(x,y,visited,count+1,total + graph[nx][ny])
                visited.remove((nx,ny)) #다시 방문에서 제거 해주며 다른 분기에서 이 블럭 탐색할 수 있게 해줌
            #블럭 수와 관계없는 분기
            visited.append((nx,ny))
            dfs(nx,ny,visited,count+1,total + graph[nx][ny])
            visited.remove((nx, ny))



##모든지점에서 반복
result = 0 #테크로미노에 의한 최대 값
max_value = max(map(max,graph)) # 그래프 안에서 최대 블록 값
for x in range(n):
    for y in range(m) :
        visited = []
        visited.append((x,y))
        dfs(x,y,visited,1,graph[x][y])

print(result)








