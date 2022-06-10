import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.layers import GlobalAveragePooling2D
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.preprocessing.image import img_to_array, load_img, smart_resize


def predict_landmark(input_features): 

    model = tf.keras.models.load_model('model.h5')


    """
    predict NYC landmarks

    Args:
        arg1: explanation
    Returns:
        [ if an image is Empire State Building, MET museum, Brooklyn Bridge, MOMA, Statue of Liberty,
        911 Memorial. ]
    """

    return model.predict(input_features)