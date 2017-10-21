## import all necessary packages and functions.
import csv # read and write csv files
from datetime import datetime # operations to parse dates
from pprint import pprint # use to print data structures like dictionaries in
                          # a nicer way than the base print function.
import matplotlib.pyplot as plt
import numpy as np

# use filename variable to store data file for Washington DC
filename = './data/Washington-2016-Summary.csv'
# set up csv reader object   
with open(filename, 'r') as f_in:
    reader = csv.DictReader(f_in)
    # create list for trip data
    data = list(reader)

    # initialize count variables
    Q1_subscribers = 0
    Q1_customers = 0
    Q2_subscribers = 0
    Q2_customers = 0
    Q3_subscribers = 0
    Q3_customers = 0
    Q4_subscribers = 0
    Q4_customers = 0


# iterate through data to tally up ride types per quarter
    for row in data:
        if row['user_type'] == 'Subscriber' and int(row['month'])< 4:
            Q1_subscribers += 1
        elif row['user_type'] == 'Customer' and int(row['month'])< 4:
            Q1_customers += 1
        elif row['user_type'] == 'Subscriber' and 3 < int(row['month']) < 7:
            Q2_subscribers += 1
        elif row['user_type'] == 'Customer' and 3 < int(row['month']) < 7:
            Q2_customers += 1
        elif row['user_type'] == 'Subscriber' and 6 < int(row['month']) < 10:
            Q3_subscribers += 1
        elif row['user_type'] == 'Customer' and 6 < int(row['month']) < 10:
            Q3_customers += 1
        elif row['user_type'] == 'Subscriber' and 9 < int(row['month']) < 13:
            Q4_subscribers += 1
        elif row['user_type'] == 'Customer' and 9 < int(row['month']) < 13:
            Q4_customers += 1
        
    # sums for total rides in each quarter
    Q1_total = Q1_subscribers + Q1_customers
    Q2_total = Q2_subscribers + Q2_customers
    Q3_total = Q3_subscribers + Q3_customers
    Q4_total = Q4_subscribers + Q4_customers
    # print total and subtotal for rides per quarter
    print (Q1_total, Q1_subscribers, Q1_customers)
    print (Q2_total, Q2_subscribers, Q2_customers)
    print (Q3_total, Q3_subscribers, Q3_customers)
    print (Q4_total, Q4_subscribers, Q4_customers)
    print (str(Q1_total) + ' total rides in Jan-Mar, including '+ \
           str(Q1_subscribers) + ' by subscribers and ' + str(Q1_customers) + \
           ' by short-term customers.')
    print (str(Q2_total) + ' total rides in Apr-Jun, including '+ \
           str(Q2_subscribers) + ' by subscribers and ' + str(Q2_customers) + \
           ' by short-term customers.')
    print (str(Q3_total) + ' total rides in Jul-Sep, including '+ \
           str(Q3_subscribers) + ' by subscribers and ' + str(Q3_customers) + \
           ' by short-term customers.')
    print (str(Q4_total) + ' total rides in Oct-Jan, including '+ \
           str(Q4_subscribers) + ' by subscribers and ' + str(Q4_customers) + \
           ' by short-term customers.')
    # create tuple for consumption by matplotlib function
    subs_rides = (Q1_subscribers, Q2_subscribers, Q3_subscribers, Q4_subscribers)
    cust_rides = (Q1_customers, Q2_customers, Q3_customers, Q4_customers)
    # print(subs_rides)
    # print(cust_rides)
    # create stacked bar chart
    N = 4
    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, subs_rides, width)
    p2 = plt.bar(ind, cust_rides, width,bottom=subs_rides)

    plt.ylabel('# of Rides/Qtr')
    plt.title('Distribution of 2016 DC Bikeshare Rides Per Qtr')
    plt.xticks(ind, ('Q1', 'Q2', 'Q3', 'Q4'))
    plt.yticks(np.arange(0, 24000, 2000))
    plt.legend((p1[0], p2[0]), ('Subscribers', 'Short-Term Customers'))

    plt.show()
