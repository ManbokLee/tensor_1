import tensorflow as tf

a = tf.placeholder("float")
b = tf.placeholder("float")

c= tf.multiply(a, b)

sess = tf.Session()


print(sess.run(c, feed_dict={a:3, b:3}))


