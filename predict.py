from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import scipy.integrate
result = scipy.integrate.quad(
  lambda x: scipy.special.jv(2.5, x),
  0,
  4.5
)


def get_predict():
    predict_image_dir = "static/images_predict"
    predict_image_generator_0_1 = ImageDataGenerator(rescale=1. / 255)
    model_load = keras.models.load_model("static/model/model_vgg.h5", compile=False)
    BATCH_SIZE = 100
    IMG_SHAPE = 150
    predict_data_gen = predict_image_generator_0_1.flow_from_directory(batch_size=BATCH_SIZE,
                                                                       directory=predict_image_dir,
                                                                       shuffle=False,
                                                                       target_size=(IMG_SHAPE, IMG_SHAPE))

    sample_training_images, sample_labels = next(predict_data_gen)
    predict = model_load.predict(sample_training_images)
    predict = 100 - predict * 100
    return predict



predict = get_predict()
print(predict)
