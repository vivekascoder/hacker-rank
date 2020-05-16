"""
{ "1": 
    [(0, 0), (0, 1), (0, 2)]
    [        (1, 1)        ]
    [(2, 0), (2, 1), (2, 2)]
}
"""
import random
arr = []
for i in range(6):
    temp_arr = []
    for j in range(6):
        temp_arr.append(random.randint(-9, 9))
    arr.append(temp_arr)

arr_2 = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]

def houglassSum(arr):
    sum_of_watchglass = []
    for i in range(len(arr[0]) - 2):
        for j in range(len(arr[0]) - 2):
            temp_sum = 0
            for k in range(3):
                if k == 1:
                    temp_sum += arr[i + k][j + k]
                else:
                    temp_sum += arr[i + k][j] + arr[i + k][j + 1] + arr[i + k][j + 2]
            print(i, j, k, temp_sum)
            sum_of_watchglass.append(temp_sum)
    return max(sum_of_watchglass)


print(arr_2)

print(houglassSum(arr_2))

