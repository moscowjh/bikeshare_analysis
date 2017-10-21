## import all necessary packages and functions.
import csv # read and write csv files
from datetime import datetime # operations to parse dates
from pprint import pprint # use to print data structures like dictionaries in
                          # a nicer way than the base print function.
import matplotlib.pyplot as plt

# this is a 'magic word' that allows for plots to be displayed
# inline with the notebook. If you want to know more, see:
# http://ipython.readthedocs.io/en/stable/interactive/magics.html
# %matplotlib inline 

# example histogram, data taken from bay area sample
"""data = [ 7.65,  8.92,  7.42,  5.50, 16.17,  4.20,  8.98,  9.62, 11.48, 14.33,
        19.02, 21.53,  3.90,  7.97,  2.62,  2.67,  3.08, 14.40, 12.90,  7.83,
        25.12,  8.30,  4.93, 12.43, 10.60,  6.17, 10.88,  4.78, 15.15,  3.53,
         9.43, 13.32, 11.72,  9.85,  5.22, 15.10,  3.95,  3.17,  8.78,  1.88,
         4.55, 12.68, 12.38,  9.78,  7.63,  6.45, 17.38, 11.90, 11.52,  8.63,]
plt.hist(data)
plt.title('Distribution of Trip Durations')
plt.xlabel('Duration (m)')
plt.show()
"""
# use filename variable to store data file for Washington DC
filename = './data/Washington-2016-Summary.csv'
# set up csv reader object   
with open(filename, 'r') as f_in:
    reader = csv.DictReader(f_in)
# create list for trip data
    data = list(reader)
# print first row of dictionary as test
    # print (data[1])
# initialize empty list for trip duration data points
#    trips = []
# iterate through data dictionary creating list of trip durations
#   for row in data:
#       trips.append(float(row['duration']))

"""
plot histogram for all riders using code from example histogram
plt.hist(trips, bins = 'auto')
plt.title('Distribution of Trip Durations (WashDC Bikeshare)')
plt.xlabel('Duration (m)')
plt.ylabel('Number of Trips')
plt.axis([0, 60, 0, 3000])
plt.show()
"""

# initialize empty list for trip duration data points
subscriber_trips = []
customer_trips = []
# iterate through data dictionary creating list of trip durations for respective user types 
for row in data:
    if row['user_type'] == 'Subscriber':
        subscriber_trips.append(float(row['duration']))
    if row['user_type'] == 'Customer':
        customer_trips.append(float(row['duration']))
# print(subscriber_trips[:5])
# print(customer_trips[:5])
          
# plot histogram for WashDC Bikeshare - Longterm Subscribers
plt.hist(subscriber_trips, bins = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75])
plt.title('Distribution of Bikeshare Trip Durations (WashDC Subscribers)')
plt.xlabel('Duration (m)')
plt.ylabel('Number of Trips')
plt.axis([0, 75, 0, 20000])
plt.show()

# plot histogram for WashDC Bikeshare - Short-Term Customers
plt.hist(customer_trips, bins = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75])
plt.title('Distribution of Bikeshare Trip Durations (WashDC Short-Term Customers)')
plt.xlabel('Duration (m)')
plt.ylabel('Number of Trips')
plt.axis([0, 75, 0, 20000])
plt.show()

