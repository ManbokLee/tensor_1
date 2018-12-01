# *******************************
# 텐서는 3개의 파라미터를 갖는다.
# *******************************
'''
Arithmetic operations : add, subtract, multiply, ...
Matrix operations : matmul, matrix_inverse, ...
Control flow operations : tuple, group, …
Logical operations : logical_and, logical_not, …
Comparison operations : equal, less, not_equal, …
Debugging operations : is_finite, is_inf, ...

'''

import tensorflow as tf

x = tf.constant([[1,2]])
print(x)
# Tensor("Const:0", shape=(1, 2), dtype=int32)
# Tensor(랭크, 쉐입, 데이터타입)

# 랭크(Rank) : 텐서의 차원(dimenstion) 을 의미합니다.
# 랭크가 0 이라면 스칼라 1이라면 벡터 2라면 행렬 3이상이면 텐서 라고 부릅니다. 

# 쉐입은 행 n * 열 n2 

# 타입은 정수

# 텐서는 그래프 생성, 그래프 실행 두가지 과정을 거친다.
# 컴퓨터공학에서는 그래프를 노드 와 엣지로 이뤄진 자료구조로 정의한다.
# 텐서플로는 노드에 연산(Op), 변수(Var), 상수(Const) 등을 정의하고,
# 노드들간의 연결인 엣지를 통해 실제 텐서를 주고 받으며 계산을 실행함

node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0) # 암묵적으로 tf.float32 로 선언됨
print(node1)
print(node2)
node3 = node1 + node2
print(node3)
# node1 = tf.constant(3.0, dtype=tf.float32)
node4 = node3 + node1
print(node4)

node5 = node4 - node2
print(node5)

node6 = tf.constant(2, tf.int32)
print(node6)

node7 = node6 + tf.cast(node5, tf.int32)
print(node7)

node8 = tf.cast(node1 + node2, tf.int32)
print(node8)

node9 = node1 + node2 - node3
print(node9)

node10 = node1 - node2 + node3
print(node10)