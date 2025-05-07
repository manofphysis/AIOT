
# 🐍 파이썬(Python) 기본 문법 요약

파이썬은 문법이 간결하고 직관적이어서 초보자도 쉽게 배울 수 있는 프로그래밍 언어입니다.

---

## 1. 변수와 자료형

```python
x = 10         # 정수형
pi = 3.14      # 실수형
name = "Tom"   # 문자열
is_ok = True   # 불리언 (참/거짓)
```

---

## 2. 자료형 출력 및 형 변환

```python
print(type(x))         # 자료형 출력
print(int(3.9))        # 정수형으로 변환: 3
print(float(5))        # 실수형으로 변환: 5.0
print(str(10))         # 문자열로 변환: "10"
```

---

## 3. 연산자

```python
# 산술 연산자
a + b     # 더하기
a - b     # 빼기
a * b     # 곱하기
a / b     # 나누기
a % b     # 나머지
a ** b    # 거듭제곱
a // b    # 몫

# 비교 연산자
==, !=, >, <, >=, <=

# 논리 연산자
and, or, not
```

---

## 4. 조건문 (if)

```python
age = 20

if age >= 18:
    print("성인입니다.")
elif age >= 13:
    print("청소년입니다.")
else:
    print("어린이입니다.")
```

---

## 5. 반복문 (for, while)

```python
# for 문
for i in range(5):
    print(i)    # 0부터 4까지 출력

# while 문
count = 0
while count < 5:
    print(count)
    count += 1
```

---

## 6. 리스트, 튜플, 딕셔너리

```python
# 리스트 (수정 가능)
fruits = ["apple", "banana", "cherry"]
print(fruits[0])      # apple
fruits.append("grape")

# 튜플 (수정 불가능)
point = (3, 4)

# 딕셔너리 (key-value)
person = {"name": "Tom", "age": 21}
print(person["name"])
```

---

## 7. 함수 정의

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

---

## 8. 입력과 출력

```python
name = input("이름을 입력하세요: ")
print("안녕하세요,", name)
```

---

## 9. 예외 처리

```python
try:
    num = int(input("숫자를 입력하세요: "))
    print(10 / num)
except ValueError:
    print("숫자가 아닙니다.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
```

---

## 10. 파일 입출력

```python
# 쓰기
with open("example.txt", "w") as f:
    f.write("Hello, world!")

# 읽기
with open("example.txt", "r") as f:
    content = f.read()
    print(content)
```

---

## ✅ 마무리

파이썬은 배우기 쉽고 활용도 높은 언어입니다. 기초 문법을 잘 익힌 후에는 다양한 실습을 통해 자신만의 프로젝트를 만들어보세요!

