import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.preprocessing import image
import zipfile
import os
import pickle
from keras.models import model_from_json
from django.conf import settings
from django.conf import settings




def training():
      zip_ref = zipfile.ZipFile("datasets/17810_23812_bundle_archive.zip", 'r')
      zip_ref.extractall("datasets/tmp")
      zip_ref.close()

      train_datagen = ImageDataGenerator(rescale = 1./255,
                                        shear_range = 0.2,
                                        zoom_range = 0.2,
                                        horizontal_flip = True)
      training_set = train_datagen.flow_from_directory('datasets/tmp/chest_xray/train',
                                                      target_size = (64, 64),
                                                      batch_size = 32,
                                                      class_mode = 'binary')

      train_datagen = ImageDataGenerator(rescale = 1./255,
                                        shear_range = 0.2,
                                        zoom_range = 0.2,
                                        horizontal_flip = True)
      test_set = train_datagen.flow_from_directory('datasets/tmp/chest_xray/test',
                                                      target_size = (64, 64),
                                                      batch_size = 32,
                                                      class_mode = 'binary')




      DESIRED_ACCURACY = 0.95

      class myCallback(tf.keras.callbacks.Callback):
            def on_epoch_end(self, epoch, logs={}):
                  if(logs.get('acc')>DESIRED_ACCURACY):
                      print("\nReached 99.9% accuracy so cancelling training!")
                      self.model.stop_training = True
                
      callbacks = myCallback()

      cnn = tf.keras.models.Sequential()
      cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu', input_shape=[64, 64, 3]))
      cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
      cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu'))
      cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
      cnn.add(tf.keras.layers.Flatten())
      cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))
      cnn.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))
      cnn.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
      cnn.fit(x = training_set, validation_data = test_set, epochs = 15)

      # pkl_filename="pickle_model_pneumonia.pkl"
      # with open(pkl_filename,'wb') as file:
      #     pickle.dump(cnn,file)
      
      # serialize model to JSON
      model_json = cnn.to_json()
      with open("datasets/model.json", "w") as json_file:
            json_file.write(model_json)
      # serialize weights to HDF5
      cnn.save_weights("datasets/model.h5")
      print("Saved model to disk")


def pred1(ob): 
      name = ob.file.name
      fullpath = os.path.abspath(name)
      print(fullpath)

      test_image = image.load_img(fullpath, target_size = (64, 64 ))
      # test_image = image.load_img(os.path.join(os.path.abspath( (__file__)), lastimage), target_size = (64, 64))
      test_image = image.img_to_array(test_image)
      test_image = np.expand_dims(test_image, axis = 0)


      #  later...

      # load json and create model
      json_file = open('datasets/model.json', 'r')
      loaded_model_json = json_file.read()
      json_file.close()
      loaded_model = model_from_json(loaded_model_json)

      # load weights into new model
      loaded_model.load_weights("datasets/model.h5")
      print("Loaded model from disk")


      result = loaded_model.predict(test_image)
      print(result)
      print(result[0][0])
      # training_set.class_indices
      if result[0][0] == 1:
            prediction = 'You are suffering from pneumonia'
      else:
            prediction = "Your health is Normal"
      print(prediction)
      return prediction
     

if __name__=="__main__":
      # pred1()
    training()