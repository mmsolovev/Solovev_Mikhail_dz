import sys

nums = sys.argv[1:]
with open('bakery.csv', encoding='utf-8') as file:
    if len(nums) > 1:
        index1 = int(nums[0])
        index2 = int(nums[1])
    elif len(nums) == 0:
        index1 = 0
        index2 = sum(1 for line in file)
        file.seek(0)
    else:
        index1 = int(nums[0])
        index2 = sum(1 for line in file)
        file.seek(0)

    for index, line in enumerate(file):
        if index1 <= index + 1 <= index2:
            print(line.strip())
