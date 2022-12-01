#import tensorflow as tf
import tensorflow.compat.v1 as tf # DBG
tf.disable_v2_behavior() # DBG

class Randomer(object):
    stddev = None

    @staticmethod
    def random_normal(wshape):
        return tf.random.normal(wshape, stddev=Randomer.stddev) # DBG

    @staticmethod
    def set_stddev(sd):
        Randomer.stddev = sd