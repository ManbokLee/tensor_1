import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = 'C:/Windows/Fonts/NanumGothic.ttf'
fontprop = fm.FontProperties(fname=font_path, size=16)

tf.set_random_seed(777)

X = [1,2,3]
Y = [1,2,3]

W = tf.placeholder(tf.float32)
hypothesis = X * W # bios 생략 ... weight 만 관계된 차트 보기 위함

cost = tf.reduce_mean(tf.square(hypothesis - Y))
#optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
#train = optimizer.minimize(cost)

sess = tf.Session()
W_history = []
cost_history = []

for i in range(-20, 50):
    curr_W = i*0.1
    corr_cost = sess.run(cost,{W:curr_W})
    W_history.append(curr_W)
    cost_history.append(corr_cost)

# 차트 확인
plt.title('가중치 차트', fontproperties=fontprop)
plt.plot(W_history, cost_history)
plt.show()

