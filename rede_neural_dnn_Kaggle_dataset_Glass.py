import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical, normalize
from sklearn.model_selection import train_test_split

df_train = pd.read_csv('../input/glass.csv')
X_train = df_train.drop('Type', axis = 1)
y_train = df_train['Type']



glass_classes = y_train.unique()
values = y_train.value_counts()
plt.bar(glass_classes, values)
plt.title('Train set')
plt.xlabel('Glass Classes')
plt.ylabel('Examples count')
plt.show()

X_train = df_train.values
X_train = normalize(X_train)
y_train = to_categorical(y_train)
y_train.shape
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size = 0.2)
X_val, X_test, y_val, y_test = train_test_split(X_val, y_val, test_size = 0.5)



model = tf.keras.models.Sequential([
       
    tf.keras.layers.Dense(256, input_shape=(9,), activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.3),
    
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.3),
    
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.5),
            
    tf.keras.layers.Dense(7, activation='softmax')
])



model.compile(loss='categorical_crossentropy',optimizer=Adam(0.0001),metrics=['acc'])
history = model.fit(X_train, y_train,
                    epochs=150,
                    validation_data=(X_val, y_val),
                    verbose=2,
                   )

plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()