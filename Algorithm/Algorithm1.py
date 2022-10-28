import random
import time

from numpy import number

startTime1 = time.time()

numbers = []

for i in range(100000):
    a = random.randint(1, 100000)
    while a in numbers:
        a = random.randint(1, 100000)
    numbers.append(a)


def serch_list(a, x):
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            return i
    return (-1)


print(serch_list(numbers, 5687))
print("선형 탐색 알고리즘 실행 완료! {0}".format(time.time()-startTime1))


startTime2 = time.time()
sorted_numbers = sorted(numbers)


def binary_serch(a, x):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


print(binary_serch(sorted_numbers, 5687))
print("이분 탐색 알고리즘 실행 완료! {0}".format(time.time()-startTime2))
