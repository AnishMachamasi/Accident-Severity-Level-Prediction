### Accident Severity Level Prediction

In this project, we will build a XGBoost model to predict the severity of an accident given various conditions.

### Running this project:
`python app.py`

### Dataset used:
https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents?utm_medium=social&utm_campaign=kaggle-dataset-share&utm_source=twitter 

### About Dataset

This is a countrywide car accident dataset, which covers 49 states of the USA. The accident data are collected from February 2016 to Dec 2021, using multiple APIs that provide streaming traffic incident (or event) data. These APIs broadcast traffic data captured by a variety of entities, such as the US and state departments of transportation, law enforcement agencies, traffic cameras, and traffic sensors within the road-networks. Currently, there are about 2.8 million accident records in this dataset. Check here to learn more about this dataset.

The dataset contains the following columns:

- ID: A unique identifier for each accident.
- Severity: The severity of the accident on a scale from 1 to 4, with 1 being the least severe and 4 being the most severe.
- Start_Time: The start time of the accident.
- End_Time: The end time of the accident, if available.
- Start_Lat: The latitude of the starting location of the accident.
- Start_Lng: The longitude of the starting location of the accident.
- End_Lat: The latitude of the ending location of the accident, if available.
- End_Lng: The longitude of the ending location of the accident, if available.
- Distance(mi): The length of the road affected by the accident, in miles.
- Description: A description of the accident.
- Number: The street number of the location of the accident, if available.
- Street: The name of the street of the location of the accident.
- Side: The side of the street (Right/Left) on which the accident occurred.
- City: The city in which the accident occurred.
- County: The county in which the accident occurred.
- State: The state in which the accident occurred.
- Zipcode: The zipcode in which the accident occurred.
- Country: The country in which the accident occurred (should be 'US' for all rows).
- Timezone: The timezone of the location of the accident.
- Airport_Code: The code of the nearest airport to the location of the accident.
- Weather_Timestamp: The time at which the weather conditions were observed.
- Temperature(F): The temperature at the time of the accident, in Fahrenheit.
- Wind_Chill(F): The wind chill at the time of the accident, in Fahrenheit.
- Humidity(%): The humidity at the time of the accident, as a percentage.
- Pressure(in): The air pressure at the time of the accident, in inches of mercury.
- Visibility(mi): The visibility at the time of the accident, in miles.
- Wind_Direction: The direction of the wind at the time of the accident.
- Wind_Speed(mph): The speed of the wind at the time of the accident, in miles per hour.
- Precipitation(in): The amount of precipitation at the time of the accident, in inches.
- Weather_Condition: A description of the weather conditions at the time of the accident.
- Amenity: A boolean indicating whether there was an amenity (e.g. a restaurant, gas station, or hospital) near the location of the accident.
- Bump: A boolean indicating whether there was a speed bump near the location of the accident.
- Crossing: A boolean indicating whether there was a crossing (e.g. a pedestrian or railroad crossing) near the location of the accident.
- Give_Way: A boolean indicating whether there was a give way sign near the location of the accident.
- Junction: A boolean indicating whether there was a junction (e.g. a intersection or roundabout) near the location of the accident.
- No_Exit: A boolean indicating whether there was a no exit sign near the location of the accident.
- Railway: A boolean indicating whether there was a railway near the location of the accident.
- Roundabout: A boolean indicating whether there was a roundabout near the location of the accident.
- Station: A boolean indicating whether there was a station (e.g. a bus or train station) near the location of the accident.
- Stop: A boolean indicating whether there was a stop sign near the location of the accident.
- Traffic_Calming: A boolean indicating whether there was traffic calming measures (e.g. speed humps or roundabouts) near the location of the accident.
- Traffic_Signal: A boolean indicating whether there was a traffic signal (e.g. a traffic light) near the location of the accident.
- Turning_Loop: A boolean indicating whether the location of the accident is at the end of a cul-de-sac or other turning loop.
- Sunrise_Sunset: A flag indicating whether the accident occurred during sunrise or sunset.
- Civil_Twilight: A flag indicating whether the accident occurred during civil twilight (the period after sunset or before sunrise when there is still some light in the sky).
- Nautical_Twilight: A flag indicating whether the accident occurred during nautical twilight (the period after civil twilight when the center of the sun is between 6 and 12 degrees below the horizon).
- Astronomical_Twilight: A flag indicating whether the accident occurred during astronomical twilight (the period after nautical twilight when the center of the sun is between 12 and 18 degrees below the horizon).

The dataset contains over 3 million records, with a mixture of numerical, categorical, and
datetime features. The severity column, which is the target variable, has four possible
values, and the dataset is imbalanced, with the majority of accidents classified as minor.


### demo:




https://user-images.githubusercontent.com/98002255/235290144-50c5b57f-3b1a-40f5-bc5a-88481bd5a68c.mp4

