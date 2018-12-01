import tensorflow as tf

def variable_summary(var):
    with tf.name_scope("summ"):
        mean = tf.reduce_mean(var)
        tf.summary.scalar('mean', mean)
        with tf.name_scope("test_1"):
            test1 = tf.sqrt(tf.reduce_mean(tf.square(var - mean)))
        tf.summary.scalar('test_1',test_1)
        tf.summary.scalar('max', tf.reduce_max(var))
        tf.summary.scalar('min', tf.reduce_min(var))
        tf.summary.histogram('histogram', var)


def nn_layer(input_tensor, input_dimm, output_dimm, layer_name, act = tf.nn.relu):
    with tf.name_scope(layer_name):
        with tf.name_scope('weights'):
            weight = weight_variable([input_dimm, output_dimm])
            variable_summaries(biases)



