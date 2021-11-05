import pathlib

import tensorflow as tf
from keras_preprocessing.image import ImageDataGenerator


def resize_with_pad(image, label):
    i = image
    i = tf.cast(i, tf.float32)
    i = tf.image.resize_with_pad(i, 150, 150)
    i = tf.keras.applications.mobilenet_v2.preprocess_input(i)
    return (i, label)

if __name__=='__main__':

    data_dir = pathlib.Path('../images_for_training')

    train_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(150, 150),
        batch_size=5)

    val_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(150, 150),
        batch_size=5)

    class_names = train_ds.class_names
    print(str(class_names))

    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(150, 150)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(2, activation='softmax')
    ])

    model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

    train_datagen = ImageDataGenerator(
        shear_range=0.01,
        zoom_range=0.01,
        horizontal_flip=False)

    train_generator = train_datagen.flow_from_directory(
        '../images_for_training',  # this is the target directory
        target_size=(150, 150),
        color_mode="grayscale",
        batch_size=1,
        class_mode="categorical")

    test_datagen = ImageDataGenerator()

    valid_generator = test_datagen.flow_from_directory(
        '../images_for_training',
        target_size=(150, 150),
        color_mode="grayscale",
        batch_size=1,
        class_mode="categorical")

    reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.2,
                              patience=5, min_lr=0.0001)
    model.fit(train_generator,
              steps_per_epoch=5,
              epochs=5000,
              validation_data=valid_generator,
              validation_steps=10,
              callbacks=[reduce_lr])

    model.summary()
    model.save('my_model.h5')
    test_loss, test_acc = model.evaluate(train_generator, verbose=2)

    print('\nTest accuracy:', test_acc)