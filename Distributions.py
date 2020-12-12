import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
df=pd.read_csv('nyccleaned.csv')
df=df[df['trip_distance']>0]  # Factor out 0 mils travel
sns.distplot(df['passenger_count'],kde=False)  #Distribution of Passenger count per ride
plt.title('Passenger Count Distribution')
plt.show()
def timezone(x):
    if x>=datetime.time(5, 0, 1) and x <=datetime.time(8, 0, 0):
        return 'Morning'
    if x>=datetime.time(8, 0, 1) and x <=datetime.time(11, 0, 0):
        return 'Rushhour'
    elif x>=datetime.time(11, 0, 1) and x <=datetime.time(13, 0, 0):
        return 'Lunch'
    elif x>=datetime.time(13, 0, 1) and x <=datetime.time(17, 0, 0):
        return 'Afternoon'
    elif x>=datetime.time(17, 0, 1) and x <=datetime.time(19, 0, 0):
        return 'After_Work'
    elif x>=datetime.time(19, 0, 1) and x <=datetime.time(22, 0, 0):
        return 'Evening'
    elif x>=datetime.time(22, 0, 1) and x <=datetime.time(1, 0, 0):
        return 'Late Evening'
    elif x>=datetime.time(1, 0, 1) or x <=datetime.time(5, 0, 0):
        return 'MidNight'
def distance(x):
    if x>0 and x<=1:
        return 'Short'
    if x>1 and x<=5:
        return 'Regular'
    if x>5 and x<=10:
        return 'Middle'
    if x>10:
        return "Long"
def rain(x):
    if x==0 or x=='T':
        return "No Rain"
    if x>0 and x<0.1:
        return 'Light Rain'
    if x>=0.1 and x<0.3:
        return 'Moderate Rain'
    if x>0.3:
        return 'Heavy Rain'
def temp(x):
    if x<=50:
        return "Cold"
    if x>50 and x<=65:
        return 'Cool'
    if x>65 and x<77:
        return 'Warm'
    if x>=77:
        return 'Hot'
df['Pickup Time Period']=df['TripStart'].apply(lambda x:timezone(datetime.datetime.strptime(str(x), "%m/%d/%Y %H:%M").time()))
fig,axis=plt.subplots(figsize=(10,8))
sns.countplot(x='Pickup Time Period',data=df)       #Group travel count by time of the day
plt.title('The Distribution of Number of Pickups On Each Part of The Day')
plt.xticks()
plt.show()
df['Distance Type']=df['trip_distance'].apply(lambda x:distance(x))   #Group distance into separate categories
fig,axis=plt.subplots()
sns.countplot(x='Distance Type',data=df)
plt.title('The Distribution of Distance')
plt.show()
df['tip_rate']=(df['tip_amount'])/(df['trip_distance'])        #Relation between tip and distance
tip_distance=df.groupby(['Distance Type'])['tip_rate'].mean()
b=tip_distance.plot(figsize=(15,5))
b.set_ylabel('Tip/Distance Correlation Coefficient')
plt.show()
tip_period=df.groupby(['Pickup Time Period'])['tip_rate'].mean()
tip_period.plot(figsize=(15,5))
plt.show()
df_location=df[(df['PickupBorough']!='Unknown')&(df['PickupBorough']!='EWR')]    #Factored out Newwark and NV, only 5 Boroughs left
tip_location=df_location.groupby(['PickupBorough'])['tip_rate'].mean()
a=tip_location.plot(figsize=(15,5))
a.set_ylabel('Tip/Distance Correlation Coefficient')
plt.show()
df['weather']=df['Precipitation'].apply(lambda x:rain(x))
tip_weather=df.groupby(['weather'])['tip_rate'].mean()
c=tip_weather.plot(figsize=(15,5))
c.set_ylabel('Tip/rain Correlation Coefficient')
plt.show()
df['temperature']=df['Avg Temp'].apply(lambda x:temp(x))
distance_temperature=df.groupby(['temperature'])['trip_distance'].mean()
d=distance_temperature.plot(figsize=(15,5))
d.set_ylabel('Average Miles/Temperature Correlation Coefficient')
plt.show()
tip_temperature=df.groupby(['temperature'])['tip_rate'].mean()
e=tip_temperature.plot(figsize=(15,5))
e.set_ylabel('Average Miles/Temperature Correlation Coefficient')
plt.show()
