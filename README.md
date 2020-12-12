![1](https://user-images.githubusercontent.com/16584326/101976413-0e7c3b80-3c13-11eb-87c8-513934739789.jpg)


Due to current the Corona Virus,the taxi market has been decimated as New york was the one of the earliest hit by the virus.

As shown in the graph below, during the month of March you see a great decline as month goes by.

![taxi_rate](https://user-images.githubusercontent.com/16584326/101976845-5309d600-3c17-11eb-88a6-a46fecaa9a0a.png)

<b>Introduction & Objectives</b>

Our mission today is to help the struggle taxi driver earn the most amount of money in the quickly and most efficent.

<b>Data Set</b>

Yellow taxi Data & 2020
https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page

Pickup/dropoff location data
https://data.cityofnewyork.us/Transportation/NYC-Taxi-Zones/d3c5-ddgc

Weather data 
https://www.noaa.gov/weather 

<b>Data Collection & Joining</b>

We ran a python script that allow use to combine the three data sources above into on major one.

It first used numeral location from in the pickup and drop off location and converted it to the name using the Pickup/dropoff location data.

Based on the date, we use link the temperture of each date to the table.

<b>Data Cleaning</b>

NYC Taxi Data from https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
Data-mined weather data from https://www.noaa.gov/weather 
Merged all data sources with pandas 
Transposed numeric locations to location names
Created new columns for durations and times
Removed invalid data

<b>Libraries Used</b>
1. Pandas
2. Numpy
3. Seaborn
4. SKLearn
5. StreamLit


<b>Data Analysis</b>


<b>Insights</b>


<b>Feature Engineering & Selection</b>
For the feature engineering, we created various date time fields to analyze the data on various levels of granularity, create calculated fields such as tips/mile, make new categorical features from continous data, etc.

At the end of this process, we have a total of 48 features.

In order to select the most important features for machine learning model, we used our domain knowledge to select 8 features. 
The final features selected are:['passenger_count','trip_distance','payment_type','TripStart_dayofweek', 'TripStart_hourofday','PickupBorough','DropoffBorough','Avg Temp']


<b>Model Building</b>
For creating the machine learning model, we selected a simple Linear regression from the SKLearn library.
For data preprocessing, we used various pipelines and column transformers to create the data flow.
After training the model, the evaluation metrics we used was RootMeanSquaredError and R2 score which was at 2.07 and 80 respectively.

Having trained the model, we used a pickle file to dump the model and used StreamLit framework to create a UI where users can enter their data to get a fare prediction for their taxi ride. Kindly refer to the TaxiApp.py script for the code.

<b>Conclusion</b>
Overall, our data analysis has shown that if a taxi driver wants to make the most cash and tips, he/she must do the following:
1. Drive in Brooklyn
2. Drive when the temperature is below 55-60
3. Drive post lunch between 15:00-17:00
4. Drive especially if it is raining


