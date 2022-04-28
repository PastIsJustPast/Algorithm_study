T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    max_num = nums[-1]
    temp = 0
    cnt = 0
    total = 0
    for i in nums[:len(nums) - 1][::-1]:
        if i > max_num:  # 새 고점이다?
            total += ((max_num * cnt) - temp)
            max_num = i
            temp = 0
            cnt = 0
        elif i == max_num:
            continue
        else:
            temp += i
            cnt += 1
    if temp > 0:
        total += (max_num * cnt - temp)

    print("#{} {}".format(test_case, total))