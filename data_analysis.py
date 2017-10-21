## import all necessary packages and functions.
import csv # read and write csv files
from datetime import datetime # operations to parse dates
from pprint import pprint # use to print data structures like dictionaries in
                          # a nicer way than the base print function.

def number_of_trips(filename):
    """
    This function reads in a file with trip data and reports the number of
    trips made by subscribers, customers, and total overall.
    """
    with open(filename, 'r') as f_in:
        # set up csv reader object
        reader = csv.DictReader(f_in)
        
        # initialize count variables
        n_subscribers = 0
        n_customers = 0
        
        # tally up ride types
        for row in reader:
            if row['user_type'] == 'Subscriber':
                n_subscribers += 1
            elif row['user_type'] == 'Customer':
                n_customers += 1

        # print city name for reference
        city = filename.split('-')[0].split('/')[-1]
        print('\nCity: {}'.format(city))    


        # compute total number of rides, proportions for question 4a
        n_total = n_subscribers + n_customers
        prop1 = n_subscribers/n_total
        print ('Proportion of subscriber trips/total trips is '+"{:.1%}".format(prop1))
        prop2 = n_customers/n_total
        print ('Proportion of short-term user trips/total trips is '+"{:.1%}".format(prop2))
        
        # return tallies as  tuple
        print ('(subscriber trips, short-term customer trips, total trips)')
        return (n_subscribers, n_customers, n_total)
        
        
## Modify this and the previous cell to answer Question 4a. Remember to run ##
## the function on the cleaned data files you created from Question 3.      ##

data_file = './data/NYC-2016-Summary.csv'
print(number_of_trips(data_file))

data_file = './data/Chicago-2016-Summary.csv'
print(number_of_trips(data_file))

data_file = './data/Washington-2016-Summary.csv'
print(number_of_trips(data_file))

data_file = './examples/BayArea-Y3-Summary.csv'
print(number_of_trips(data_file))

def average_trip_length (filename):
    """
    This function takes a file with a city's trip data and computes the average
    trip duration for that city.
    """
    # set up csv reader object   
    with open(filename, 'r') as f_in:
        reader = csv.DictReader(f_in)
        # initialize variables to total minutes and count trips
        total = 0
        count = 0
        # total minutes of all rides
        for row in reader:
            total += float(row['duration'])
    # count the number of rides
    with open (filename, 'r') as f_out:
        count = sum(1 for line in f_out) - 1 

        # print city name for reference
        city = filename.split('-')[0].split('/')[-1]
        print('\nCity: {}'.format(city))    
           
        # print (total)
        print ('Total number of trips is ' + str(count))
        # compute average and return average ride duration (rounded to 1 decimal)
        average = total/count
        return 'Average trip length for ' + city + ' is ' + str(round(average,1)) + ' minutes.'
        

data_file = './data/Chicago-2016-Summary.csv'
print(average_trip_length(data_file))

data_file = './data/NYC-2016-Summary.csv'
print(average_trip_length(data_file))

data_file = './data/Washington-2016-Summary.csv'
print(average_trip_length(data_file))

# data_file = './examples/BayArea-Y3-Summary.csv'
# print(average_trip_length(data_file))

def proportion_longer_trips(filename):
    """
    This function takes a file with a city's trip data and computes the proportion
    of trips over 40 minutes for that city.
    """
    # initialize variable to count total rides
    total_rides = 0
    # count total rides (reusing code from average_trip_length)
    with open (filename, 'r') as f_out:
        total_rides = sum(1 for line in f_out) - 1
    # print (total_rides)
    # initialize variable to count longer rides (>30 mins)
    long_rides = 0
    # set up csv reader object   
    with open(filename, 'r') as f_in:
        reader = csv.DictReader(f_in)
        # count rides of duration > 30 mins
        for row in reader:
            if float(row['duration']) > 30:
                long_rides += 1
        # print (long_rides)
        
    # print city name for reference
    city = filename.split('-')[0].split('/')[-1]
    print('\nCity: {}'.format(city))
    
    # Compute proportion of long rides and print as percentage (rounded to 1 decimal)
    prop_long_rides = long_rides/total_rides
    return 'Proportion of 30+ minute rides for ' + city + ' is ' +"{:.1%}".format(prop_long_rides)
    
data_file = './data/Chicago-2016-Summary.csv'
print(proportion_longer_trips(data_file))

data_file = './data/NYC-2016-Summary.csv'
print(proportion_longer_trips(data_file))

data_file = './data/Washington-2016-Summary.csv'
print(proportion_longer_trips(data_file))

def subscribers_v_customers(filename):
    """
    This function takes a file with a city's trip data, computes length of trip per
    customer type, and comparest the two
    """
    with open(filename, 'r') as f_in:
        # set up csv reader object
        reader = csv.DictReader(f_in)

        # initialize subscriber variables
        subscriber_count = 0
        subscriber_total = 0
        # initialize customer variables
        customer_count = 0
        customer_total = 0
        
        # computes average length of trip per customer type
        for row in reader:
            if row['user_type'] == 'Subscriber':
                subscriber_count += 1
                subscriber_total+= float(row['duration'])
            elif row['user_type'] == 'Customer':
                customer_count += 1
                customer_total += float(row['duration'])               
        subs_avg = subscriber_total/subscriber_count
        cust_avg = customer_total/customer_count
        
    # print city name for reference
    city = filename.split('-')[0].split('/')[-1]
    print('\nCity: {}'.format(city))
    # print short-term customer and subscribers average trip per ride
    print('Shorter term customers average ' + str(round(cust_avg,1)) +' minutes per ride.')
    print('Subscribers average ' +str(round(subs_avg,1)) +' minutes per ride.')
    
data_file = './examples/BayArea-Y3-Summary.csv'
subscribers_v_customers(data_file)

data_file = './data/Chicago-2016-Summary.csv'
subscribers_v_customers(data_file)

data_file = './data/NYC-2016-Summary.csv'
subscribers_v_customers(data_file)

data_file = './data/Washington-2016-Summary.csv'
subscribers_v_customers(data_file)




