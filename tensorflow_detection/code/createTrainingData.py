from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import tensorflow as tf

def resize_with_pad(image, label):
    i = image
    i = tf.cast(i, tf.float32)
    i = tf.image.resize_with_pad(i, 150, 150)
    i = tf.keras.applications.mobilenet_v2.preprocess_input(i)
    return (i, label)

if __name__=='__main__':
    datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

    img = load_img('../code/07.jpg')
    img, lb = resize_with_pad(img, 0)# this is a PIL image
    image_resized = tf.image.rgb_to_grayscale(img)
    x = img_to_array(image_resized)  # this is a Numpy array with shape (3, 150, 150)
    x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

    # the .flow() command below generates batches of randomly transformed images
    # and saves the results to the `preview/` directory
    i = 0
    for batch in datagen.flow(x, batch_size=10,
                              save_to_dir='../images_for_training/berkay', save_prefix='', save_format='jpeg'):
        i += 1
        if i > 200:
            break  # otherwise the generator would loop indefinitely