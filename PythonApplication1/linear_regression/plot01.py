import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = 'C:/Windows/Fonts/NanumGothic.ttf'
fontprop = fm.FontProperties(fname=font_path, size=16)
fontpropSm = fm.FontProperties(fname=font_path, size=10)

plt.style.use('ggplot')
mbr = ['김', '이', '박', '권', '신']
mbr_idx = range(len(mbr))
score = [100,80,60,50,30]
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.bar(mbr_idx, score, align='center', color='blue')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xticks(mbr_idx, mbr, rotation = 0, fontsize= 'small', fontproperties=fontpropSm) # rotation = 0 은 눈금레이블을 푸형으로 지정
plt.xlabel('학생이름', fontproperties=fontprop)
plt.ylabel('점수', fontproperties=fontprop)
plt.title('학생별 점수', fontproperties=fontprop)
plt.savefig('score.png', dpi=300, bbox_inches = 'tight') # dpi 는 해상도 , bbox_inches = 'tight' 는 그림의 여백을 제거
plt.show()







