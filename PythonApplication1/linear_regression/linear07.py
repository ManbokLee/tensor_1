import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

num_potint = 1000
vectors_set = []
for i in range(num_potint):
    x1 = np.random.normal(0.0, 0.55)
    y1 = x1 * 0.1 + 0.3 + np.random.normal(0.0,0.03)
    vectors_set.append([x1, y1])

    x_data = [v[0] for v in vectors_set]
    y_data = [v[1] for v in vectors_set]

W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1])) # zeros 는 내열 내부를 0으로 초기화하라
y = W * x_data + b
loss = tf.reduce_mean(tf.square(y - y_data)) # 경사하강법

optimizer = tf.train.GradientDescentOptimizer(0.5) # 0.5 는 학습 속도
train = optimizer.minimize(loss)

init = tf.global_variables_initializer() 

sess = tf.Session()
sess.run(init)

plt.xlabel('x')
plt.ylabel('y')

for i in range(8):
    sess.run(train)
    print(sess.run(W), sess.run(b))
    plt.plot(x_data, y_data, 'ro')
    plt.plot(x_data, sess.run(W) * x_data + sess.run(b))
    #plt.xlabel('x')
    #plt.ylabel('y')
    plt.show(block=False)
    plt.pause(0.5)
plt.show()

"""
    학습속도 (leaning rate)
    텐서플로가 각 반복 때 마다 얼마나 크게 이동할 것인가를 제어함
"""