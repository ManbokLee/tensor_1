import tensorflow as tf

tf.set_random_seed(777) # 랜덤값이 저장되는 공간 선언

# trainable 한 variable 이다.
x_train = [1,2,3,4,5,6,7,8,9]
y_train = [1,2,3,4,5,6,7,8,9]
#x_train = [1,2,3]
#y_train = [1,2,3]

# random_normal : 평균값에 근사한 랜덤값
W = tf.Variable(tf.random_normal([1]), name='weight') # 가중치
b = tf.Variable(tf.random_normal([1]), name='bias') # 편차의 시작값 
# [1] => 랭크가 1인 배열 (1차원)
# 탠서가 사용하는 variable 이다.


# ************************************************************************
# 가설
hypothesis = x_train * W + b 
# hypothesis 는 x_train 에 의해서 결정될 것이다.
# hypothesis 는 하나이고 x_train은 다수의 데이터를 뜻하고 위 식에서 x_train 은 독릭된 별개의 데이터(독립변수)이고 hypothsis 는 x_train 에 의해 결정되는 종속변수이다.
cost = tf.reduce_mean(tf.square(hypothesis - y_train))

# 비용함수의 최소화 minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)
# train 은 노드가 되고 이것을 실행해야 한다.
# ************************************************************************

sess = tf.Session()
sess.run(tf.global_variables_initializer()) # Variable 초기화

# 학습시킨다 -> training
# 최적화를 학습시킨다 -> learn best fit W:[1], b:[0]
for step in range(2001):
    sess.run(train)
    if step % 20 == 0:
        print(step,'/', sess.run(cost),'/', sess.run(W),'/', sess.run(b))

# 트레이닝을 실행하면 코스트, 하이퍼시스의 W와 b 값을 추출할 수 있다.
# W=1 이 되고, b=0 이 되면 학습이 잘 된 것이다. 라고 정의 
print(sess.run(W),'/', sess.run(b))


