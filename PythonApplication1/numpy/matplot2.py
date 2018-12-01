import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


font_path = 'C:/Windows/Fonts/NanumGothic.ttf'
fontprop = fm.FontProperties(fname=font_path, size=16)

x = np.arange(0,10)
y = x^2

z = np.arange(0,10)
q = x**2

plt.title('그래프 그리기', fontproperties=fontprop)
plt.xlabel('시간', fontproperties=fontprop)
plt.ylabel('거리', fontproperties=fontprop)
plt.plot(x,y, 'r') # 라인 색갈
plt.plot(z,q, '>') # 라인타입 꺽은선

plt.show()
