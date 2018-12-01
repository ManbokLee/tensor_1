# *********************************
# -- 텐서는 세션 내부에서 연산한다
# *********************************

import tensorflow as tf

a = tf.constant(5.0, name = "a")
b = tf.constant(10.0, name = "b") # =  tf.constant([10.0], name = "b")


# 세션안에서 모든연산이 실행됨
with tf.Session() as sess:
    print("a = ", sess.run(a))
    print("b = ", sess.run(b))
