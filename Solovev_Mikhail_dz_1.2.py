cube_list = []
number = -1
while number < 1000:
    number += 2
    cube_number = number ** 3
    cube_list.append(cube_number)
print(cube_list)

answer = 0
for nums in cube_list:
    num_sum = 0
    for numeral in str(nums):
        num_sum += int(numeral)
    if num_sum % 7 == 0:
        answer += nums
    else:
        continue
print(answer)

answer2 = 0
for nums in cube_list:
    nums += 17
    num_sum = 0
    for numeral in str(nums):
        num_sum += int(numeral)
    if num_sum % 7 == 0:
        answer2 += nums
    else:
        continue
print(answer2)
