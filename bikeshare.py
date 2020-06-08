import time
import pandas as pd


wrong_input = "Wrong input. Please, try again !!"
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nEnter the name of the city:\n- Chicago\n- New York\n- Washington\n").lower()
        if city in ['chicago', 'new york', 'washington']:
            break
        else:
            print(wrong_input)

    # get user input for month (all, january, february, ... , june)
    while True :
        month = input("\nEnter the name of the month:\nJanuary\nFebruary\nMarch\nApril\nMay\nJune\nto filter by, or \"all\" to apply for no month filter:\n").lower()
        if month in ["january", "february", "march", "april", "may", "june", "july", "all"]:
            break
        else:
            print(wrong_input)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        day = input("\nEnter the name of the day of the week\nMonday\nTuesday\nWednesday\nThursday\nFriday\nSaturday\nSunday\nto filter by, or \"all\" to apply for no day filter\n").lower()
        if day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]:
            break
        else:
            print(wrong_input)


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
    file_name = CITY_DATA[city]
    print ("Accessing data from: " + file_name)
    df = pd.read_csv(file_name)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # filter by month if applicable
    if month != 'all':
        # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month

        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        df['day_of_week'] = df['Start Time'].dt.day_name()

        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['month']=df['Start Time'].dt.month
    print('Most common month is:\t\t',df['month'].mode()[0])


    # display the most common day of week
    df['day']=df['Start Time'].dt.day_name()
    print('Most common day of week is:\t',df['day'].mode()[0])


    # display the most common start hour
    df['start_hour']=df['Start Time'].dt.hour
    print('Most common start hour is:\t',df['start_hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most commonly used start station is:\t",df["Start Station"].mode()[0])


    # display most commonly used end station
    print("Most commonly used end station is:\t",df["End Station"].mode()[0])
     


    # display most frequent combination of start station and end station trip
    combine_stations = df['Start Station'] + "/" + df['End Station']
    common_station = combine_stations.value_counts().idxmax()
    print('Most frequent used combinations are:\n\t{} \n\tto\n\t{}'.format(common_station.split('/')[0], common_station.split('/')[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time is:\t',round(df['Trip Duration'].sum()/60),'\tMinutes')

    # display mean travel time
    print('Mean travel time is:\t',round(df['Trip Duration'].mean()/60),'\tMinutes')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of user types is:\n',df['User Type'].value_counts())


    # Display counts of gender
    if 'Gender' in df.columns:
        print('Counts of gender is:\n',df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Earliest year of birth is:\t',int(df['Birth Year'].min()))
        print('Most recent year of birth is:\t',int(df['Birth Year'].max()))
        print('Most common year of birth is:\t',int(df['Birth Year'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def more_data(df):
    user_input = input('Would you like to see 5 more raw data? Enter yes or no.\n')
    number = 0

    while True :
        if user_input.lower() != 'no':
            print(df.iloc[number : number + 5])
            number += 5
            user_input = input('Would you like to see 5 more raw data? Enter yes or no.\n')
        else:
            break 
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        more_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
