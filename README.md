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


Kindly refer to the powerpoint presentation for analysis.


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

Finding
Going into each section by borough by borough we find the following:


![Bronx count](https://user-images.githubusercontent.com/16584326/101990282-16b89300-3c74-11eb-88dd-38d252ff528b.png)


|PickupZone                       |  DropoffZone                      |   Count|
|---------------------------------|---------------------------------|------|     
|East Concourse/Concourse Village   |East Concourse/Concourse Village  |    71|

|West Concourse                   |West Concourse                   |     79|

|Melrose South                     |Melrose South                     |    87|

|Mott Haven/Port Morris             |Mott Haven/Port Morris           |    199|

|

Looking at the following,we see that if driver stay in these area they can monopolies the area and earn the most money by trip by increasing the frequence .

![bronx avg](https://user-images.githubusercontent.com/16584326/101990274-07394a00-3c74-11eb-8081-becdd1cc2d5e.png)


PickupZone                         DropoffZone                      
Mott Haven/Port Morris             Melrose South                         35
West Concourse                     Highbridge                            37
Mott Haven/Port Morris             East Tremont                          39
University Heights/Morris Heights  University Heights/Morris Heights     40
Melrose South                      Mott Haven/Port Morris                53
Highbridge                         Highbridge                            70
East Concourse/Concourse Village   East Concourse/Concourse Village      71
West Concourse                     West Concourse                        79
Melrose South                      Melrose South                         87
Mott Haven/Port Morris             Mott Haven/Port Morris               199
Name: RatecodeID, dtype: int64
                                                         
PickupZone                 DropoffZone                         total_amount  trip_distance        
Spuyten Duyvil/Kingsbridge City Island                           36.800000   12.700000  
Pelham Bay                 Spuyten Duyvil/Kingsbridge            43.550000   13.013333 
Van Cortlandt Park         Parkchester                           62.910000   13.040000
Spuyten Duyvil/Kingsbridge Pelham Bay                            42.383333   13.646667  
Eastchester                Kingsbridge Heights                   43.383333   13.956667  
                           Spuyten Duyvil/Kingsbridge            43.050000   14.200000 
Van Cortlandt Park         Pelham Parkway                        64.170000   14.500000
West Farms/Bronx River     Bronxdale                             54.300000   15.760000 
                           Spuyten Duyvil/Kingsbridge            59.850000   19.250000  
Bronxdale                  University Heights/Morris Heights      8.800000   23.430000

Compare to the other location,the average for these trip earned more for driving less by picking up on Van Cortlandt Park.

With this,we notice that Bronxdale to University Heights Morris Heights has a average cost of  8.800000  but has 
a distance of 23.40 miles making you believe that there this trip is low but if you refer to the pie chart you notice the it 
only 1.3% meaning the quantity of taxi taking that fare it low and this can be seem as an outliner.


![queen count](https://user-images.githubusercontent.com/16584326/101990385-c8f05a80-3c74-11eb-99b4-9ed2540a6585.png)


The following are the main ones  taxi driver should focus.The the interesting thing is that  LaGuardia Airport and JFk are the main one not from coming from other regions but to each other.
PickupZone                      DropoffZone                       count                      
Astoria                         Astoria                            514
JFK Airport                     JFK Airport                        691
Queensbridge/Ravenswood         Queensbridge/Ravenswood            927
Long Island City/Hunters Point  Long Island City/Hunters Point    1290


![queen avg](https://user-images.githubusercontent.com/16584326/101990391-d3125900-3c74-11eb-924e-3040541eba9d.png)

Taking trip from the top three earn you close to $100 for a about an hour ride.Jamaica Bay to Howard Beach should be avoided as the money earn is not worth for the amount of driving.
PickupZone                      DropoffZone              Total          trip 
Hammels/Arverne                Murray Hill-Queens        92.6900        23.536667 
Murray Hill-Queens             Hammels/Arverne           95.8400        25.810000
Sunnyside                      Far Rockaway              93.6400        26.070000
Jamaica Bay                    Howard Beach              78.0500        42.910000  


![brooklyn count](https://user-images.githubusercontent.com/16584326/101990439-0bb23280-3c75-11eb-956b-bc1e371b41fa.png)


The following are the main ones  taxi driver should focus.
PickupZone                      DropoffZone                       count 
Prospect-Lefferts Gardens       Prospect-Lefferts Gardens         81
Canarsie                        Canarsie                          90
Park Slope                      Park Slope                        91
 Crown Heights North         Crown Heights North                  131
Fort Greene                     Fort Greene                        148


![brooklyn avg](https://user-images.githubusercontent.com/16584326/101990456-153b9a80-3c75-11eb-803f-2e941de7da22.png)


The below trip is the winner among all the boroughs as trip. 110 for one trip and make up for the shorter manhattan trips.
PickupZone             DropoffZone              Total          trip 
Carroll Gardens         Canarsie               110.465000  24.110000


Below looks like a other outliner.The rate doesn't match the rest and it only 1.2% of the pie
PickupZone             DropoffZone              Total          trip 
Coney Island              Brooklyn Navy Yard      9.680000   23.090000

![Staten_Island count ](https://user-images.githubusercontent.com/16584326/101990604-c5a99e80-3c75-11eb-9ff9-0a0ac3190901.png)


Staten island should be avoided based on these number.

![Staten_Island avg](https://user-images.githubusercontent.com/16584326/101990630-ea9e1180-3c75-11eb-85ff-f00098bd7041.png)


The amount of request are low but if you are lucky you can grab 
shorter trip to earn what appears to be more then normal.



![manhattan count](https://user-images.githubusercontent.com/16584326/101990720-29cc6280-3c76-11eb-9375-35b66c8d5307.png)

PickupZone             DropoffZone          
Upper West Side North  Upper West Side North    3504
Yorkville West         Lenox Hill West          3539
Upper East Side North  East Harlem South        3707
Upper West Side South  Upper West Side North    3726
Upper East Side North  Upper East Side South    4006
Yorkville West         East Harlem South        4074
Upper East Side South  Upper East Side North    4477
Upper East Side North  Upper East Side North    4554
East Harlem South      East Harlem South        4729
                       East Harlem North        5307
                       
                       
![manhattan mean](https://user-images.githubusercontent.com/16584326/101990769-4bc5e500-3c76-11eb-854c-7ad9cb41fba2.png)

                                               
PickupZone               DropoffZone              total_amount      trip_distance                      
Financial District South Washington Heights North     50.065714      13.617143
Financial District North Inwood                       49.578750      13.850000
Midtown South            Marble Hill                  43.300000      13.850000
Washington Heights South Financial District North     45.836667      13.964333
Hudson Sq                Highbridge Park              48.300000      14.080000
Financial District South Inwood                       44.525000      14.150000
World Trade Center       Inwood                       52.560000      14.720000
Midtown East             Inwood Hill Park             51.300000      16.320000
Little Italy/NoLiTa      Inwood                       68.033333      17.010000
Inwood Hill Park         Union Sq                     86.300000      26.620000

Our original belief while doing this analysis  was that Mahattan would be the most overcharge but fell within range to the other borough without any major outliners.


<b>Conclusion</b>
Overall, our data analysis has shown that if a taxi driver wants to make the most cash and tips, he/she must do the following:
1. Drive in Brooklyn
2. Drive when the temperature is below 55-60
3. Drive post lunch between 15:00-17:00
4. Drive especially if it is raining


