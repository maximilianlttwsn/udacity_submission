import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    valid_cities = ["chicago", "new york city", "washington"]

    city = "block"

    while city not in valid_cities:
        city = input("For which City would you like to see the data. Data is available for Chicago, New York City, Washington: ").lower()
        if city not in valid_cities:
            print("Sorry, {} is not a valid input. Please enter Chicago, New York City or Washington".format(city))
        else:
            print("Okay, we will show you the data for {}".format(city.title()))
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    valid_months = ["all", "january", "february", "march","april","may","june"]

    month = "block"

    while month not in valid_months:
        month = input("For which month would you like to see the data? Enter a month or all ").lower()
        if month not in valid_months:
            print("Sorry, {} is not a valid input. Please enter a correct day".format(month))
        else:
            print("Okay, we will show you the data for {}".format(month))
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    valid_days = ["all", "monday", "tuesday", "wednesday","thursday","friday","saturday","sunday"]

    day = "block"

    while day not in valid_days:
        day = input("For which day would you like to see the data? Enter a day or all ").lower()
        if day not in valid_days:
            print("Sorry, {} is not a valid input. Please enter a correct day.".format(day))
        else:
            print("Okay, we will show you the data for {}".format(day))
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
   # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    common_month = df['month'].mode()[0]

    print('\nMost common month:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]

    print('\nMost common day:', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]

    print('\nMost common start hour:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    print('\nMost common Start Station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    print('\nMost common End Station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_combination = (df['Start Station']+ " and " + df['End Station']).mode()[0]
    print('\nMost common combination:', common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = (df['Trip Duration']).sum()
    print('\nTotal Travel Time in seconds:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = (df['Trip Duration']).mean()
    print('\nMean Travel Time in seconds:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\n", user_types)

    # TO DO: Display counts of gender
    if city == "washington":
        print("Gender statistics not available for Washington")
    else:
        user_gender = df['Gender'].value_counts()
        print("\n",user_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if city == "washington":
        print("Birthday statistics not available for Washington")
    else:
        recent_year_of_birth = int(df['Birth Year'].min())
        print("\nMost recent year of birth:", recent_year_of_birth)

        earliest_year_of_birth = int(df['Birth Year'].max())
        print("\nEarliest year of birth:", earliest_year_of_birth)

        common_year_of_birth = int(df['Birth Year'].mode()[0])
        print("\nMost common year of birth:", common_year_of_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):

    """  Asks user if he wants to see raw data at the end of the process. Repeats until answer =! yes """

    linecount = 1

    while True:
        want_raw = input("If you would like to see 5 lines of raw data, please answer yes or no").lower()
        if want_raw == 'yes':
            print(df[linecount:(linecount+5)])
            linecount = linecount + 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Thank you for using the application")
            break


if __name__ == "__main__":
	main()
