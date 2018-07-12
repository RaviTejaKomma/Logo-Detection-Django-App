import numpy as np
from keras.preprocessing import image
from LogoClassification import settings as sett


def predict_image(path):
    test_image = image.load_img(path, target_size=(64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)

    with sett.graph.as_default():
        result = sett.model.predict(test_image)

    if result[0][0] == 0:
       prediction = 'Image contains Apple Logo'
    else:
       prediction = 'Image does not contain Apple Logo'
    return prediction


def load_and_predict(filepath):
    return predict_image(filepath)
