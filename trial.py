import tensorflow as tf

x=tf.constant(5)
y=tf.constant(6)

with tf.Session as sess:
	sess.run(print(tf.mul(x,y)))
