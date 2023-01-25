from keras.preprocessing.image import ImageDataGenerator
from tensorflow import keras


class Classification:
######## CLASSIFICATION #########
    def __init__(self):
        pass

    def classify(self, file_path: str):
        #print(file_path)
        model = keras.models.load_model('checkpoints/checkpoint-07-0.91.hdf5')
        test_datagen = ImageDataGenerator(rescale=1./255)
        test_generator = test_datagen.flow_from_directory(
            directory=file_path,
            target_size=(300, 300),
            batch_size=1,
            class_mode=None,
            shuffle=False,
            seed=12
        )

        y_class = model.predict(test_generator)
        return y_class
