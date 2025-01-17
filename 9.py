import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x, y, label='선 그래프', color='b', marker='o')
plt.title('선 그래프 예제')
plt.xlabel('x 값')
plt.ylabel('y 값')
plt.legend()
plt.show()

import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 30]
plt.bar(categories, values, color='orange')
plt.title('막대 그래프 예제')
plt.xlabel('카테고리')
plt.ylabel('값')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)
plt.hist(data, bins=30, color='green', edgecolor='black')
plt.title('히스토그램 예제')
plt.xlabel('값')
plt.ylabel('빈도')
plt.show()

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.scatter(x, y, color='red', label='산점도')
plt.title('산점도 예제')
plt.xlabel('x 값')
plt.ylabel('y 값')
plt.legend()
plt.show()

import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('파이 차트 예제')
plt.show()

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 9, 16, 25]
plt.subplot(2, 1, 1)
plt.plot(x, y1, label='선 그래프 1')
plt.title('서브플롯 1: 선 그래프')
plt.subplot(2, 1, 2)
plt.plot(x, y2, label='선 그래프 2', color='orange')
plt.title('서브플롯 2: 선 그래프')
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title('스타일 변경된 선 그래프')
plt.xlabel('x 값')
plt.ylabel('sin(x)')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 10, 100)
y = np.log(x)
plt.plot(x, y)
plt.xscale('log')
plt.title('로그 스케일 선 그래프')
plt.xlabel('x 값 (로그 스케일)')
plt.ylabel('log(x)')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 10)
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.title('히트맵 예제')
plt.colorbar()
plt.show()