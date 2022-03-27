n = int(input())
a = list(map(int,input().split()))
b,c = map(int, input().split())

##
count = 0
for number in a :
    #총감독관부터 무조건 한 명 배치함
    if number <= b : #총감독관 한명으로 될경우 끝냄
        count +=1
        continue
    else :  # 총감독관 한명으로 안될 경우 부감독 고려
        count +=1
        number -=b

        #부감독관 인원수 고려
        if number % c == 0 : #딱 나누어 떨어지면
            count += number//c
        else : #나누어 떨어지지 않는다면
            count += (number//c) +1


print(count)