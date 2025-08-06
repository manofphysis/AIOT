# NumPy 기초 정리

## 1. 배열 생성

``` python
import numpy as np

a = np.array([1, 2, 3])          # 1차원 배열
b = np.array([[1, 2], [3, 4]])   # 2차원 배열
```

## 2. 배열 생성 함수들

``` python
np.arange(0, 10, 2)              # [0 2 4 6 8]
np.zeros((2, 3))                 # 0으로 채워진 2x3 배열
np.ones((2, 3))                  # 1로 채워진 2x3 배열
np.eye(3)                        # 3x3 단위행렬
np.linspace(0, 1, 5)             # 0에서 1까지 5개 균등 분할
```

## 3. 배열 연산

``` python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b, a - b, a * b, a / b       # 요소별 연산
a < 2                            # 불리언 배열
```

## 4. 랜덤 숫자 생성

``` python
np.random.seed(0)
np.random.randint(1, 100, size=10)
np.random.randint(1, 100, size=(2, 3))
np.random.normal(loc=0, scale=1, size=10)
```

## 5. 그래프 시각화 (matplotlib 활용)

``` python
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("사인 곡선")
plt.show()
```

## 6. 2차 방정식의 근 구하기

``` python
a = 1
b = -3
c = 2

D = b**2 - 4*a*c
x1 = (-b + np.sqrt(D)) / (2*a)
x2 = (-b - np.sqrt(D)) / (2*a)
print(x1, x2)
```
