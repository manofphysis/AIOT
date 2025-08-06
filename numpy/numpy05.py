import numpy as np
# 0부터 10 미만까지 1씩 증가하는 배열 생성
arr1 = np.arange(0, 10, 1)
print("arr1:", arr1)
# 5부터 20 미만까지 3씩 증가하는 배열 생성
arr2 = np.arange(5, 20, 3)
print("arr2:", arr2)
# 0부터 1까지 0.2씩 증가하는 배열 생성 (실수도 가능)
arr3 = np.arange(0, 1, 0.2)
print("arr3:", arr3)
# 단일 인자 사용 (0부터 5 미만까지 1씩 증가)
arr4 = np.arange(5)
print("arr4:", arr4)