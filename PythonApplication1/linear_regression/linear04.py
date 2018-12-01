import tensorflow as tf

# 모델의 파라미터 선언 
W = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)

# Model input and output
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

linear_model = x * W + b

# cost function
loss = tf.reduce_mean(tf.square(linear_model - y))

# 옵티마이저
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(loss)

# 트레이닝 테이터
x_train = [1,2,3,4]
y_train = [0,-1,-2,-3]


# 트레이닝 회전
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(1000):
    sess.run(train, {x:x_train, y:y_train})

# evaluate training accuarcy
curr_W, curr_b = sess.run([W, b])
print("W: %s b: %s " %(curr_W, curr_b))



