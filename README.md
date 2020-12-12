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


<b>Data Analysis & Insights</b>
![Location](https://user-images.githubusercontent.com/75762359/101990056-7150ef80-3c72-11eb-9495-b3b69db3e678.png)

![Temperature](https://user-images.githubusercontent.com/75762359/101990021-36e75280-3c72-11eb-9255-7dec201af5b9.png)

![Weather Factor](https://user-images.githubusercontent.com/75762359/101989926-92fda700-3c71-11eb-9612-e428bb9dffe1.png)

![Time](https://user-images.githubusercontent.com/75762359/101990132-e8868380-3c72-11eb-81a5-43314e6d5fc5.png)

WE first focus the chance that driver can be paid by cash.

The changce of cash payment in Manhattan is 0.3552647403799782
And following is the top 10 zone to get paid by cash in Manhattan:
East Harlem North       0.606004
Central Harlem North    0.605387
Highbridge Park         0.600000
Manhattanville          0.574264
Hamilton Heights        0.569968
Marble Hill             0.560000
Central Harlem          0.539134
Chinatown               0.485114
East Harlem South       0.484915
Morningside Heights     0.484615

The changce of cash payment in Bronx is 0.5647916192211342
And following is the top 10 zone to get paid by cash in Bronx:
Fordham South                       0.807018
Mott Haven/Port Morris              0.712150
Bronx Park                          0.700000
Melrose South                       0.692308
West Concourse                      0.680251
Bedford Park                        0.676768
Highbridge                          0.655629
East Concourse/Concourse Village    0.621875
Morrisania/Melrose                  0.616766
Mount Hope                          0.608696

The changce of cash payment in Queens is 0.605137766728817
And following is the top 10 zone to get paid by cash in Queens:
Forest Park/Highland Park           1.000000
Saint Michaels Cemetery/Woodside    0.941176
Long Island City/Hunters Point      0.896220
Woodside                            0.803235
Astoria Park                        0.750000
Long Island City/Queens Plaza       0.741784
Sunnyside                           0.716279
Astoria                             0.714286
Elmhurst                            0.701220
Old Astoria                         0.693506

The changce of cash payment in Brooklyn is 0.3998106284767428
And following is the top 10 zone to get paid by cash in Brooklyn:
Marine Park/Floyd Bennett Field    0.666667
Brighton Beach                     0.650000
Manhattan Beach                    0.592593
Carroll Gardens                    0.588889
Williamsburg (South Side)          0.568000
Fort Greene                        0.538647
Greenpoint                         0.523256
Bushwick South                     0.506383
Ocean Parkway South                0.500000
Clinton Hill                       0.495327

The changce of cash payment in Staten_Island is 0.4880952380952381
And following is the top 10 zone to get paid by cash in Staten_Island:
West Brighton                  1.000000
Stapleton                      1.000000
South Beach/Dongan Hills       1.000000
Oakwood                        1.000000
Heartland Village/Todt Hill    1.000000
Great Kills                    1.000000
Westerleigh                    0.800000
Arrochar/Fort Wadsworth        0.500000
Charleston/Tottenville         0.470588
New Dorp/Midland Beach         0.375000

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


