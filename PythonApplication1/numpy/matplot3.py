
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = 'C:/Windows/Fonts/NanumGothic.ttf'
fontprop = fm.FontProperties(fname=font_path, size=16)

mu, sigma = 0.5, 0.1
s = np.random.normal(mu, sigma, 1000)
# mu 평균, sigma 표준편차

count, bins, ignored = plt.hist(s, 20, normed=True)

plt.title('정규분포', fontproperties=fontprop)
plt.plot(bins, 1/(sigma * np.sqrt(2*np.pi)) * np.exp( - (bins - mu)**2 / (2*sigma**2)), linewidth=3, color='y')
plt.show()