# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:58:17 2024

@author: Zoujiw
"""

from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import numpy as np
from tensorflow.keras.layers import Dropout
import sklearn.metrics
from pandas import read_csv
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.utils import plot_model

# Load data
file = read_csv("C:/Users/zoujiw/Desktop/field measurement data/0615-0915 final data processing/Forest_training.csv")
target = "rsds"   #predition target, ta,rh,dpT,ws,gws,wd,rsds(air temperature,relative humidity,dew point temperature,wind speed,gust wind speed,wind direction,solar radiation)
file = file.dropna(how='all')

df = file[["Temp","Rel_H", "Wind Dir","Wind Spd","Solar Radiation", target]]


# Assume df is already loaded and contains the relevant columns
features = ["Temp","Rel_H", "Wind Dir","Wind Spd","Solar Radiation"]


def create_sequences(data, target, time_steps=1):
    X, y = [], []
    for i in range(len(data) - time_steps):
        v = data.iloc[i:(i + time_steps)].values
        X.append(v)
        y.append(target.iloc[i + time_steps])
    return np.array(X), np.array(y)

# Prepare the sequence data
time_steps = 24  # Example window size
X, y = create_sequences(df[features], df[target], time_steps)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=200)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train.reshape(-1, X_train.shape[2])).reshape(X_train.shape)
X_test_scaled = scaler.transform(X_test.reshape(-1, X_test.shape[2])).reshape(X_test.shape)

# Define the LSTM model
model = Sequential()
model.add(LSTM(50, input_shape=(X_train_scaled.shape[1], X_train_scaled.shape[2]), return_sequences=True))
model.add(Dropout(0.2))  # Dropout 20% of the nodes
model.add(LSTM(40))
model.add(Dropout(0.2))  # Dropout 20% of the nodes
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_absolute_error', metrics=['mae'])

# Train the model
history = model.fit(X_train_scaled, y_train, epochs=1000, batch_size=32, validation_split=0.2)

# Evaluate the model
model.evaluate(X_test_scaled, y_test)


import numpy as np
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Assuming 'model' is your trained LSTM model and 'history' is the output of model.fit()

# Predicting training and testing sets
train_predictions = model.predict(X_train_scaled)
test_predictions = model.predict(X_test_scaled)

# Calculating R-squared values for the training and testing sets
r2_train = r2_score(y_train, train_predictions)
r2_test = r2_score(y_test, test_predictions)

# Printing R-squared values
print("Training R_square: ", r2_train)
print("Validation R_square: ", r2_test)

# Evaluate model on test set
test_loss, test_accuracy = model.evaluate(X_test_scaled, y_test)
print("Test_loss: ", test_loss)
print("Test_MAE: ", test_accuracy)

# Plotting the training and validation loss over epochs
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(loss) + 1)

plt.figure(figsize=(14, 5))

# Plotting training and validation loss
plt.subplot(1, 2, 1)
plt.plot(epochs, loss, 'y', label='Training loss')
plt.plot(epochs, val_loss, 'r', label='Validation loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

# Plotting training and validation MAE
plt.subplot(1, 2, 2)
mae = history.history['mae']
val_mae = history.history['val_mae']
plt.plot(epochs, mae, 'y', label='Training MAE')
plt.plot(epochs, val_mae, 'r', label='Validation MAE')
plt.title('Training and Validation MAE')
plt.xlabel('Epochs')
plt.ylabel('MAE')
plt.legend()

plt.tight_layout()
plt.show()

