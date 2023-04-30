from flask import Flask, render_template, request
import pickle
import csv
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import category_encoders as ce

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Load the model
    filename = 'xgboost_final_model.sav'
    model = pickle.load(open(filename, 'rb'))

    # Get the input values from the form
    if 'OtherCity' in request.form and request.form['OtherCity']:
        City = request.form['OtherCity']
    else:
        City = request.form['City']
        
    Distance = float(request.form['Distance'])
    Month = int(request.form['Month'])
    Precipitation = float(request.form['Precipitation'])
    Crossing = True if request.form.get('Crossing') == 'on' else False
    Traffic_Signal = True if request.form.get('Traffic_Signal') == 'on' else False
    Start_Lng = float(request.form['Start_Lng'])
    Start_Lat = float(request.form['Start_Lat'])
    Junction = True if request.form.get('Junction') == 'on' else False
    Stop = True if request.form.get('Stop') == 'on' else False
    Hour = int(request.form['Hour'])
    Pressure = float(request.form['Pressure'])
    Weekday = int(request.form['Weekday'])
    Station = True if request.form.get('Station') == 'on' else False
    Weather_Condition = request.form['Weather_Condition']
    Amenity = True if request.form.get('Amenity') == 'on' else False
    Humidity = int(request.form['Humidity'])
    
    data_dict = [{'City':City,
              'Distance(mi)':Distance,
              'Month':Month,
              'Precipitation(in)':Precipitation,
              'Crossing':Crossing,
              'Traffic_Signal': Traffic_Signal,
              'Start_Lng':Start_Lng,
              'Start_Lat':Start_Lat,
              'Junction':Junction,
              'Stop': Stop,
              'Hour':Hour,
              'Pressure(in)': Pressure,
              'Weekday': Weekday,
              'Station': Station,
              'Weather_Condition': Weather_Condition,
              'Amenity': Amenity,
              'Humidity(%)': Humidity}]

    df = pd.DataFrame(data_dict)
    
    # List of weather conditions
    weather_conditions = ['Clear', 'Cloudy', 'Fog', 'Hail', 'Rain', 'Sand', 'Smoke', 'Snow', 'Thunderstorm', 'Windy']

    # Append columns with initial value of 0
    for condition in weather_conditions:
        df[f'Weather_Condition_{condition}'] = 0

    cities = ['City_0', 'City_1', 'City_2', 'City_3', 'City_4', 'City_5', 'City_6', 'City_7', 'City_8', 'City_9', 'City_10', 'City_11', 'City_12']

    # Append the city names as columns with initial value 0
    for city in cities:
        df[city] = 0
        
    # Set value of 1 in the 'Weather_Condition_{condition}' column if 'Weather_Condition' matches the condition
    for condition in weather_conditions:
        if df['Weather_Condition'].values[0] == condition:
            df[f'Weather_Condition_{condition}'] = 1

    df = df.drop('Weather_Condition', axis=1)
    
    rus_dfp = pd.read_csv('rus_df2.csv')

    rus_dfp1 =  rus_dfp.loc[:,['City', 'Distance(mi)', 'Month', 'Precipitation(in)', 'Crossing', 'Traffic_Signal', 'Start_Lng', 'Start_Lat', 'Junction', 'Stop', 'Hour', 'Pressure(in)','Weekday', 'Station', 'Weather_Condition', 'Amenity', 'Humidity(%)', 'Severity']
    ]

    scaler2 = MinMaxScaler()
    features = ['Distance(mi)','Humidity(%)','Pressure(in)','Precipitation(in)','Start_Lng','Start_Lat', 'Month','Weekday','Hour']
    rus_dfp1[features] = scaler2.fit_transform(rus_dfp1[features])

    categorical_features = set(["City", "Weather_Condition"])
    for cat in categorical_features:
        rus_dfp1[cat] = rus_dfp1[cat].astype("category")

    rus_dfp1 = rus_dfp1.replace([True, False], [1, 0])

    binary_encoder = ce.binary.BinaryEncoder()
    city_binary_enc = binary_encoder.fit_transform(rus_dfp1["City"])
    input_city = df.loc[0, 'City']
    # Find the row in the DataFrame containing the desired city name
    city_row = rus_dfp1.loc[rus_dfp1['City'] == input_city].iloc[0]

    # Encode the city name using the binary encoder
    city_encoded = binary_encoder.transform(pd.DataFrame({'City': [city_row['City']]})).iloc[0]

    df.loc[0, 'City_0':'City_12'] = city_encoded
    df = df.drop('City', axis=1)



    severity = model.predict(df)
    prediction = severity[0]
    
    print(prediction)
    return render_template('home.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
