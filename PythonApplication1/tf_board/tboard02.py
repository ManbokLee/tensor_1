import tensorflow as tf

X = tf.placeholder(tf.float32, name='X')
Y = tf.placeholder(tf.float32, name='Y')

add = tf.add(X, Y)
mul = tf.multiply(X, Y)

# step1 node 의 선택
add_hist = tf.summary.scalar('add_scalar', add) # return 이 단일 (scalar)
mul_hist = tf.summary.scalar('mul_scalar', mul)

# step2 summary 로 데이터 통합
merged =tf.summary.merge_all() # 두개의 동작을 통합함

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer()) # 변수 초기화

    # step3 writer 생성
    writer = tf.summary.FileWriter("./logs/add", sess.graph)

    for i in range(100):
        # step4 노드 추가
        summary = sess.run(merged, {X:i*1.0, Y: 2.0})
        print(sess.run(add, {X:i*1.0, Y: 2.0}))
        print(sess.run(mul, {X:i*1.0, Y: 2.0}))
        writer.add_summary(summary, i)

# step5 콘솔에서 명령실행 -> 텐서보드 실행



