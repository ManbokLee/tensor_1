#*********
# 텐서보드
#*********
import tensorflow as tf
import matplotlib.pyplot as plt

a = tf.constant(20, name='cons_a')
b = tf.constant(30, name='cons_b')

y = tf.Variable(a + b + 7, name='var_y')
init = tf.global_variables_initializer()

# 세션을 초기화 하는 순간 변수에 값이 지정된다
# 데이터를 가지고 학습을 시켜서 적정한 값을 찾는다


# 그래프 관련 정보를 기본 디렉토리 하위에 logs 폴더에 저장한다.
with tf.Session() as sess:
    sess.run(init)
    text = sess.run(y)
    print(text)
    writer = tf.summary.FileWriter('C:/Users/ezen/Documents/tensorflow/studio/PythonApplication1/PythonApplication1/tf_board/logs', sess.graph)
    summary = tf.Summary()
    writer.add_summary(summary, 100)
    writer.close()




