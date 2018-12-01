#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = 'C:/Windows/Fonts/NanumGothic.ttf'
fontprop = fm.FontProperties(fname=font_path, size=16)

x = np.arange(0,3 * np.pi, 0.1)
y = np.sin(x)

plt.title('사인 웨이브 폼', fontproperties=fontprop)

plt.plot(x,y)
plt.show()