import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False  # 마이너스(-) 깨짐 방지

# 데이터 준비
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 그래프 그리기
plt.plot(x, y, marker='o')
plt.title('간단한 선 그래프')
plt.xlabel('X축')
plt.ylabel('Y축')
plt.grid(True)
plt.show()
