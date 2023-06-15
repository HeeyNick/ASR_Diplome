from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd
import os
import librosa
import librosa.display
import numpy as np
# import IPython.display as ipd
from tqdm import tqdm
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_io as tfio
import subprocess

def change_format():
    subprocess.call(['ffmpeg', '-i', 'saved/file.wav',
                'saved/audio.wav'])

def predict():
    #/home/nick/Рабочий стол/1/ASR_Diplome/saved_models/audio_classification.hdf5
    #ASR_Diplome/saved_models/audio_classification.hdf5
    model = load_model('audio_classification.hdf5')

    extracted_features_df = pd.read_csv('my_data.csv')
    y = np.array(extracted_features_df['class'].tolist())

    labelencoder=LabelEncoder()
    y = to_categorical(labelencoder.fit_transform(y))




    file_name = 'saved/audio.wav'
    audio_data, sample_rate = librosa.core.load(file_name)
    mfccs_features = librosa.feature.mfcc(y=audio_data, sr=16000, n_mfcc=40)
    mfccs_scaled_features = np.mean(mfccs_features.T,axis=0)
    mfccs_scaled_features=mfccs_scaled_features.reshape(1,-1)
    predicted_label=model.predict(mfccs_scaled_features)
    classes_x=np.argmax(predicted_label,axis=1)
    prediction_class = labelencoder.inverse_transform(classes_x)
    return (prediction_class[0])

def clear():
    os.remove('saved/audio.wav')
