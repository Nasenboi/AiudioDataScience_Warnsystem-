import tensorflow as tf

print("Num GPUs available", len(tf.config.experimental.list_physical_devices("GPU")))