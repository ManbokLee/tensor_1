import tensorflow as tf

node1 = tf.constant(3.0, tf.float32, name='A')
node2 = tf.constant(4.0, name='B')
node3 = tf.add(node1, node2)

# 노드상태의 값을 출력
print("node1: ", node1,"/node2: ", node2)
print("node3: ", node3)

sess = tf.Session()
# 텐서가 계산한 값을 출력 
print(sess.run([node1, node2]))
print(sess.run(node3))



a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
addr_node = a + b

print(a,'/',b)
print(addr_node)

print(sess.run(addr_node, feed_dict={a:3,b:4.5}))
print(sess.run(addr_node,{a:[1,3],b:[2,4]}))



x_train = [1,2,3]
y_train = [1,2,3]

w = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = x_train * w + b

cost = tf.reduce_mean(tf.square(hypothesis - y_train))

print(cost)
print(sess.run(tf.random_normal([1])))
# sess.run(tf.global_variables_initializer())
sess.run(w.initializer)
sess.run(b.initializer)
print(sess.run(cost))



