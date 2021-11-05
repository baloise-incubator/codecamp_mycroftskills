import numpy as np
import tensorflow as tf

def resize_with_pad(image, label):
    i = image
    i = tf.cast(i, tf.float32)
    i = tf.image.resize_with_pad(i, 150, 150)
    return (i, label)

class image_classifier:
    def classify_image(self):
        model = tf.keras.models.load_model('./my_model.h5')
        model.summary()
        img = tf.keras.utils.load_img(
            #"../tensorflow_detection/code/07.jpg"
            "../tensorflow_detection/verify2.jpg"
        )
        image_resized, label = resize_with_pad(img, 1)
        image_resized = tf.image.rgb_to_grayscale(image_resized)
        tf.keras.utils.save_img('test.jpg', image_resized)
        img_array = tf.keras.utils.img_to_array(image_resized)
        img_array = tf.expand_dims(img_array, 0) # Create a batch
        prediction = model.predict(img_array)
        print(prediction)
        score = tf.nn.softmax(prediction[0])
        print(score)
        max_score = np.argmax(score)
        print(max_score)
        percent = 100 * np.max(score)
        print(percent)


if __name__=='__main__':
    classifier = image_classifier()
    classifier.classify_image()