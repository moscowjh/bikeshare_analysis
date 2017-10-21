## import all necessary packages and functions.
import csv # read and write csv files
from datetime import datetime # operations to parse dates
from pprint import pprint # use to print data structures like dictionaries in
                          # a nicer way than the base print function.
# filename = './data/NYC-CitiBike-2016.csv'
def print_first_point(filename):
    """
    This function prints and returns the first data point (second row) from
    a csv file that includes a header row.
    """
    # print city name for reference
    city = filename.split('-')[0].split('/')[-1]
    print('\nCity: {}'.format(city))    
    
    with open(filename, 'r') as f_in:
        ## TODO: Use the csv library to set up a DictReader object. ##
        ## see https://docs.python.org/3/library/csv.html           ##
        trip_reader = csv.DictReader(f_in)
        ## TODO: Use a function on the DictReader object to read the     ##
        ## first trip from the data file and store it in a variable.     ##
        ## see https://docs.python.org/3/library/csv.html#reader-objects ##
        rows = list(trip_reader)
        first_trip = rows[0]
        # print(first_trip)

        ## TODO: Use the pprint library to print the first trip. ##
        ## see https://docs.python.org/3/library/pprint.html     ##
        pprint(first_trip)

    # output city name and first trip for later testing
    return (city, first_trip)

# list of files for each city
data_files = ['./data/NYC-CitiBike-2016.csv',
              './data/Chicago-Divvy-2016.csv',
              './data/Washington-CapitalBikeshare-2016.csv',]

# print the first trip from each file, store in dictionary
example_trips = {}
for data_file in data_files:
    city, first_trip = print_first_point(data_file)
    example_trips[city] = first_trip

# print(filename)
# print_first_point('./data/NYC-CitiBike-2016.csv')
datum = example_trips[city]
def duration_in_mins(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the trip duration in units of minutes.
    
    Remember that Washington is in terms of milliseconds while Chicago and NYC
    are in terms of seconds. 
    
    HINT: The csv module reads in all of the data as strings, including numeric
    values. You will need a function to convert the strings into an appropriate
    numeric type when making your transformations.
    see https://docs.python.org/3/library/functions.html
    """
    duration = 0
    if city=='NYC' or city=='Chicago':
        duration = float(datum['tripduration'])/60
    else:
        duration = float(datum['Duration (ms)'])/60000
    return duration
    print(duration)

print(duration_in_mins(example_trips['NYC'],'NYC'))
print(duration_in_mins(example_trips['Chicago'],'Chicago'))
print(duration_in_mins(example_trips['Washington'],'Washington'))

def time_of_trip(datum,city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the month, hour, and day of the week in
    which the trip was made.
    
    Remember that NYC includes seconds, while Washington and Chicago do not.
    
    HINT: You should use the datetime module to parse the original date
    strings into a format that is useful for extracting the desired information.
    see https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    """
    if city == 'NYC':
        # print('Yo mama')
        str_n = datetime.strptime(datum['starttime'], '%m/%d/%Y %H:%M:%S')
        # print (str_n)
        hour = str_n.hour
        day_of_week = str_n.strftime('%A')
        month = str_n.month
        # print(month, hour, day_of_week)
    if city == 'Chicago':
        # print('Let\'s play two!')
        str_c = datetime.strptime(datum['starttime'], '%m/%d/%Y %H:%M')
        # print(str_c)
        hour = str_c.hour
        day_of_week = str_c.strftime('%A')
        month = str_c.month
        # print(month, hour, day_of_week)
    if city == 'Washington':
        # print('Sonny Jurgenson')
        str_w = datetime.strptime(datum['Start date'], '%m/%d/%Y %H:%M')
        # print(str_w)
        hour = str_w.hour
        day_of_week = str_w.strftime('%A')
        month = str_w.month
        # print(month, hour, day_of_week)
        
    return (month, hour, day_of_week)

time_of_trip (example_trips['NYC'],'NYC')
time_of_trip (example_trips['Chicago'],'Chicago')
time_of_trip (example_trips['Washington'],'Washington')

def type_of_user(datum, city):
    user_type = ''
    if city =='NYC' or city =='Chicago':
        user_type = (str(datum['usertype']))
        return user_type
    else:
        user_type = (str(datum['Member Type']))
        if user_type == 'Registered':
            user_type = 'Subscriber'
        else:
            user_type = 'Customer'
    return user_type
    # print(user_type)

print (type_of_user(example_trips['NYC'],'NYC'))
print (type_of_user(example_trips['Chicago'],'Chicago'))
print (type_of_user(example_trips['Washington'],'Washington'))

def condense_data(in_file, out_file, city):
    """
    This function takes full data from the specified input file
    and writes the condensed data to a specified output file. The city
    argument determines how the input file will be parsed.
    
    HINT: See the cell below to see how the arguments are structured!
    """
    
    with open(out_file, 'w') as f_out, open(in_file, 'r') as f_in:
        # set up csv DictWriter object - writer requires column names for the
        # first row as the "fieldnames" argument
        out_colnames = ['duration', 'month', 'hour', 'day_of_week', 'user_type']        
        trip_writer = csv.DictWriter(f_out, fieldnames = out_colnames)
        trip_writer.writeheader()
        
        ## TODO: set up csv DictReader object ##
        trip_reader = csv.DictReader(f_in)
        rows = list(trip_reader)
        # collect data from and process each row
        for row in rows:
            # set up a dictionary to hold the values for the cleaned and trimmed
            # data point
            new_point = {}
        
            ## TODO: use the helper functions to get the cleaned data from  ##
            ## the original data dictionaries.                              ##
            ## Note that the keys for the new_point dictionary should match ##
            ## the column names set in the DictWriter object above.         ##
            new_point['duration'] = duration_in_mins(row, city)
            new_point['month'] = time_of_trip(row,city)[0]
            new_point['hour'] = time_of_trip(row,city)[1]
            new_point['day_of_week'] = time_of_trip(row,city)[2]
            new_point['user_type'] = type_of_user(row, city)

            ## TODO: write the processed information to the output file.     ##
            ## see https://docs.python.org/3/library/csv.html#writer-objects ##
            trip_writer.writerow(new_point)


# Run this cell to check your work
city_info = {'Washington': {'in_file': './data/Washington-CapitalBikeshare-2016.csv',
                           'out_file': './data/Washington-2016-Summary.csv'},
             'Chicago': {'in_file': './data/Chicago-Divvy-2016.csv',
                         'out_file': './data/Chicago-2016-Summary.csv'},
             'NYC': {'in_file': './data/NYC-CitiBike-2016.csv',
                     'out_file': './data/NYC-2016-Summary.csv'}}

for city, filenames in city_info.items():
    condense_data(filenames['in_file'], filenames['out_file'], city)
    print_first_point(filenames['out_file'])
