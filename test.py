#         # data = {"data": "Hello World"}
#         # val = pd.Series(res).to_json(orient='values')
#         # scaler = StandardScaler()
#         # x = scaler.fit_transform(res)

#         # x = pd.DataFrame(x.reshape(2, -1))
#         # val = pd.DataFrame(x).to_json(orient='split')



#         # working code

#         from flask import Flask, jsonify, request
# import os
# import numpy as np
# import pandas as pd
# import librosa 
# from sklearn.preprocessing import StandardScaler, OneHotEncoder
# from sklearn.metrics import confusion_matrix, classification_report
# from sklearn.model_selection import train_test_split
# import tensorflow as tf
# import json


# model = tf.keras.models.load_model('C:/Users/shehr/OneDrive/Documents/chalega/model/FINAL VSA/FINAL VSA/gfgModel.h5')

# def noise(data):
#     noise_amp = 0.04*np.random.uniform()*np.amax(data)
#     data = data + noise_amp*np.random.normal(size=data.shape[0])
#     return data

# def stretch(data, rate=0.70):
#     return librosa.effects.time_stretch(data, rate)

# def shift(data):
#     shift_range = int(np.random.uniform(low=-5, high = 5)*1000)
#     return np.roll(data, shift_range)

# def pitch(data, sampling_rate, pitch_factor=0.8):
#     return librosa.effects.pitch_shift(data, sampling_rate, pitch_factor)

# def higher_speed(data, speed_factor = 1.25):
#     return librosa.effects.time_stretch(data, speed_factor)

# def lower_speed(data, speed_factor = 0.75):
#     return librosa.effects.time_stretch(data, speed_factor)

# def extract_features(data):
#     result = np.array([])
#     mfccs = librosa.feature.mfcc(y=data, sr=22050, n_mfcc=58)
#     mfccs_processed = np.mean(mfccs.T, axis=0)
#     result = np.array(mfccs_processed)

#     return result

# def get_features(path):
#     # duration and offset are used to take care of the no audio in start and the ending of each audio files as seen above.
#     data, sample_rate = librosa.load(path, duration=3, offset=0.5, res_type='kaiser_fast') 
    
#     #without augmentation
#     res1 = extract_features(data)
#     result = np.array(res1)
    
#     #noised
#     noise_data = noise(data)
#     res2 = extract_features(noise_data)
#     result = np.vstack((result, res2)) # stacking vertically
    
#     #stretched
#     stretch_data = stretch(data)
#     res3 = extract_features(stretch_data)
#     result = np.vstack((result, res3))
    
#     #shifted
#     shift_data = shift(data)
#     res4 = extract_features(shift_data)
#     result = np.vstack((result, res4))
    
#     #pitched
#     pitch_data = pitch(data, sample_rate)
#     res5 = extract_features(pitch_data)
#     result = np.vstack((result, res5)) 
    
#     #speed up
#     higher_speed_data = higher_speed(data)
#     res6 = extract_features(higher_speed_data)
#     result = np.vstack((result, res6))
    
#     #speed down
#     lower_speed_data = higher_speed(data)
#     res7 = extract_features(lower_speed_data)
#     result = np.vstack((result, res7))
    
#     return result

# app = Flask(__name__)


# @app.route('/hello', methods=['GET'])
# # @app.route('/')
# def hello_world():
#     if (request.method == 'GET'):
#         audioURL = 'C://Users//shehr//Music//a_126.wav'
#         data, sample_rate = librosa.load(audioURL, duration=3, offset=0.5, res_type='kaiser_fast') 
#         res = get_features(audioURL)

#         x = np.expand_dims(res, axis=2)

#         pred_test = model.predict(x)
#         pred_arr = pred_test.tolist()
#         json_str = json.dumps(pred_arr)
#         # encoder = OneHotEncoder()
#         # y_pred = encoder.inverse_transform(pred_test)


#         # val = pd.Series(y_pred.flatten()).to_json(orient='values')
#         return json_str
        



# if __name__ == '__main__':
#     app.run(debug=True,port=8080)

"""
CODE DATED 16 JULY 2020 WORKING MODEL
from flask import Flask, jsonify, request, render_template
import os
import numpy as np
import pandas as pd
import librosa 
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
import tensorflow as tf
import json


model = tf.keras.models.load_model('C:/Users/shehr/OneDrive/Documents/chalega/model/FINAL VSA/FINAL VSA/gfgModel.h5')

def noise(data):
    noise_amp = 0.04*np.random.uniform()*np.amax(data)
    data = data + noise_amp*np.random.normal(size=data.shape[0])
    return data

def stretch(data, rate=0.70):
    return librosa.effects.time_stretch(data, rate)

def shift(data):
    shift_range = int(np.random.uniform(low=-5, high = 5)*1000)
    return np.roll(data, shift_range)

def pitch(data, sampling_rate, pitch_factor=0.8):
    return librosa.effects.pitch_shift(data, sampling_rate, pitch_factor)

def higher_speed(data, speed_factor = 1.25):
    return librosa.effects.time_stretch(data, speed_factor)

def lower_speed(data, speed_factor = 0.75):
    return librosa.effects.time_stretch(data, speed_factor)

def extract_features(data):
    result = np.array([])
    mfccs = librosa.feature.mfcc(y=data, sr=22050, n_mfcc=58)
    mfccs_processed = np.mean(mfccs.T, axis=0)
    result = np.array(mfccs_processed)

    return result

def get_features(path):
    # duration and offset are used to take care of the no audio in start and the ending of each audio files as seen above.
    data, sample_rate = librosa.load(path, duration=3, offset=0.5, res_type='kaiser_fast') 
    
    #without augmentation
    res1 = extract_features(data)
    result = np.array(res1)
    
    #noised
    noise_data = noise(data)
    res2 = extract_features(noise_data)
    result = np.vstack((result, res2)) # stacking vertically
    
    #stretched
    stretch_data = stretch(data)
    res3 = extract_features(stretch_data)
    result = np.vstack((result, res3))
    
    #shifted
    shift_data = shift(data)
    res4 = extract_features(shift_data)
    result = np.vstack((result, res4))
    
    #pitched
    pitch_data = pitch(data, sample_rate)
    res5 = extract_features(pitch_data)
    result = np.vstack((result, res5)) 
    
    #speed up
    higher_speed_data = higher_speed(data)
    res6 = extract_features(higher_speed_data)
    result = np.vstack((result, res6))
    
    #speed down
    lower_speed_data = higher_speed(data)
    res7 = extract_features(lower_speed_data)
    result = np.vstack((result, res7))
    
    return result

app = Flask(__name__)


# @app.route('/hello', methods =["POST"])
# @app.route('/')
# def my_form():
#     return render_template('home.html')
@app.route('/', methods=['GET'])
def hello_world():
    if (request.method == 'GET'):
        audioURL = 'C:/Users/shehr/Music/t1.wav'
        data, sample_rate = librosa.load(audioURL, duration=3, offset=0.5, res_type='kaiser_fast') 
        res = get_features(audioURL)
        scaler = StandardScaler()
        test1 = scaler.fit_transform(res)

        x = np.expand_dims(test1, axis=2)



        pred_test = model.predict(x)
        pred_arr = pred_test.tolist()
        json_str = json.dumps(pred_arr)
        encoder = OneHotEncoder()
        # y_pred = encoder.inverse_transform(pred_test)
        arr=[]
        for i in range(len(pred_test)):
            if pred_test[i][0] > pred_test[0][1]:
                arr.append('angry')
            else:
                arr.append('mix')


        # val = pd.Series(y_pred.flatten()).to_json(orient='values')
        return jsonify(arr)




if __name__ == '__main__':
    app.run(debug=True,port=8080)
"""