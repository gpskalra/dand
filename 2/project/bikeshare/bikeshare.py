# Logging
DEBUG = True
def log(x):
    if DEBUG:
        print(x)

## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'
months = ['january', 'february', 'march', 'april', 'may', 'june']


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Test Inputs used: (This should ideally be in test code along with their expected
    outputs! I am doing some MANUAL UNIT TESTING !!)
    Chicago
    NewYork
    Washington
    asdfasdfasdf
    new york city
    ""
    "    "
    NEW YORK

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    log('get_city(): User entered : ' + city)
    files = {'chicago':chicago, 'new york':new_york_city, 'washington':washington}
    while city.lower() not in files:
        city = input('\nYou have entered an invalid city name.\n'
                     'Please enter one of the following:\n'
                     'Chicago\n'
                     'New York\n'
                     'Washington\n\n'
                     'Note that case does not matter but spaces do, so\n'
                     'NewYork is an invalid input and\n'
                     'WaSHiNgtOn is a valid input.\n'
                     'Lets try again.\n'
                     'Would you like to see data for Chicago, New York, or Washington?\n')
        log('get_city(): User entered : ' + city)
    return files[city.lower()]

def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Test Inputs used:
    day
    month
    none
    asdfasdfasdf
    mnth1
    ""
    "    "
    DAy
    nil
    January

    Args:
        none.
    Returns:
        (str) time period filter chosen by user: "day", "month" or "none"
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    log('get_time_period(): User entered : ' + time_period)
    time_periods = ['day', 'month', 'none']
    while time_period.lower() not in time_periods:
        time_period = input('\nYou have entered an invalid time period.\n'
                     'Please enter one of the following:\n'
                     'day\n'
                     'month\n'
                     'none\n\n'
                     'Note that case does not matter, so\n'
                     'DAY is a valid input and so are\n'
                     'day and DaY.\n'
                     'Lets try again.\n'
                     'Would you like to filter the data by month, day, or not at'
                     ' all? Type "none" for no time filter.\n')
        log('get_time_period(): User entered : ' + time_period)
    return time_period.lower()


def get_month():
    '''Asks the user for a month and returns the specified month.

    Test user inputs; Return value:

    january; january
    february; february
    march; march
    april; april
    may; may
    june; june
    jan, feb, mar, apr, may; may
    1, 2, 3, 4, 5, 6, JAN, JANuary; january

    Args:
        none.
    Returns:
        (str) Month chosen by user.
              One of "january", "february", "march", "april", "may", and "june".
    '''
    month = input('\nWhich month? January, February, March, April, May, or June?\n')
    log("get_month(): User entered : " + month)
    while month.lower() not in months:
        month = input('\n This is an invalid input.\n'
                      'Please enter a valid month name:\n'
                      'Which month? January, February, March, April, May, or June?\n')
        log("get_month(): User entered : " + month)
    return month.lower()

def get_day():
    '''Asks the user for a day and returns the specified day.

    Test user inputs; Return value:

    mon, MON, monday, MONDAY, 1; 1
    tues, TUES, tuesday, TUESDAY, 2; 2
    wed, WED, wednesday, WEDNESDAY, 3; 3
    thurs, THURS, thursday, THURSDAY, 4; 4
    fri, FRI, friday, FRIDAY, 5; 5
    sat, SAT, saturday, SATURDAY, 6; 6
    sun, SUN, sunday, SUNDAY, 7; 7
    8, -1, 13, hello, none, nil, 1; 1

    Args:
        none.
    Returns:
        (int) Day of the week. 1 represents Monday, 2 Tuesday, ..., 7 Sunday.
    '''
    day = input('\nWhich day? Please type your response as an integer.\n'
                'Enter 1 for Monday, 2 for Tuesday, ..., 7 for Sunday.\n')
    # TODO: Complete this function


def popular_month(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?
    '''
    # TODO: complete function


def popular_day(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    # TODO: complete function


def popular_hour(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular hour of day for start time?
    '''
    # TODO: complete function


def trip_duration(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    '''
    # TODO: complete function


def popular_stations(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular start station and most popular end station?
    '''
    # TODO: complete function


def popular_trip(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
    '''
    # TODO: complete function


def users(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    '''
    # TODO: complete function


def gender(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    '''
    # TODO: complete function


def birth_years(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    '''
    # TODO: complete function


def display_data():
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    # TODO: handle raw input and complete function


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()
    log('statistics(): get_city() returned ' + city)

    # Filter by time period (month, day, none)
    time_period = get_time_period()
    log('statistics(): get_time_period() returned ' + time_period)

    if time_period == 'month':
        month = get_month()
        log('statistics(): get_month() returned ' + month)
    if time_period == 'day':
        day = get_day()
        log('statistics(): get_day() returned ' + day)

    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()

        #TODO: call popular_month function and print the results

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()

        # TODO: call popular_day function and print the results

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    start_time = time.time()

    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    # TODO: call gender function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    # TODO: call birth_years function and print the results

    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data()

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()
