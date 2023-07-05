import time
import pandas as pd

city_name_data = {
    "chicago": ("chicago.csv", "Chicago"),
    "newyorkcity": ("new_york_city.csv", "New York City"),
    "washington": ("washington.csv", "Washington"),
}

month_name = [
    "all",
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
]

day_name = [
    "all",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print(
        "Hello! Let's explore some US bikeshare data! You should select the city, month period and day of week.\n"
    )

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = get_city_input()

    # get user input for month (all, january, february, ... , june)
    month = get_month_input()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = get_day_input()

    print("-" * 40)
    return city, month, day


def get_city_input():
    """
    Asks the user to enter the city name.

    Returns:
        (str) city - Name of the city to analyze
    """
    while True:
        city = (
            input(
                "Enter the city name you want to choose to begin the analysis: Chicaco, New Your City or Washington: "
            )
            .replace(" ", "")
            .lower()
        )
        if city in city_name_data:
            return city
        else:
            print("\nInvalid city name, please choose a valid city. \n")


def get_month_input():
    """
    Asks the user to enter the month name.

    Returns:
        (str) month - Name of the month to filter by, or "all" to apply no month filter
    """
    while True:
        month = (
            input(
                "\nEnter the month name you want to choose to analyze or enter all to choose all the months: "
            )
            .replace(" ", "")
            .lower()
        )
        if month in month_name:
            return month.capitalize()
        else:
            print("\nInvalid month name, please choose a valid month. \n")


def get_day_input():
    """
    Asks the user to enter the day of the week.

    Returns:
        (str) day - Name of the day of the week to filter by, or "all" to apply no day filter
    """
    while True:
        day = (
            input(
                "\nEnter the day of week you want to choose to analyze or enter all to choose all the days of week: "
            )
            .replace(" ", "")
            .lower()
        )
        if day in day_name:
            return day.capitalize()
        else:
            print("\nInvalid day of week, please choose a valid day of week. \n")


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
    # load city data file into dataframe
    df = pd.read_csv(city_name_data[city][0])

    # Convert Start Time to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    # Check if month is not all
    if month != "All":
        # Filter the dataframe by the month name of Start Time
        df = df[df["Start Time"].dt.month_name() == month]
    # Check if day is not all
    if day != "All":
        # Filter the dataframe by the day of week of Start Time
        df = df[df["Start Time"].dt.day_name() == day]
    # print("shape: {}".format(df.shape[0]))
    return df


def time_stats(df, month, day):
    """
    Displays statistics on the most frequent times of travel.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
        month - Name of the month to filter by, or "all" to apply no month filter
        day - Name of the day of the week to filter by, or "all" to apply no day filter
    """
    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # display the most common month
    if month != "All":
        print("The most common month is {}.\n".format(month))
    else:
        print("The most common month is {}.\n".format(
            most_common_month_name(df)))

    # display the most common day of week
    if day != "All":
        print("The most common day of week is {}.\n".format(day))
    else:
        print(
            "The most common day of week is {}.\n".format(
                most_common_day_of_week_name(df)
            )
        )

    # display the most common start hour
    print("The most common hour is {}.\n".format(most_common_hour(df)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def most_common_month_name(df):
    """
    Returns the most common month name.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day

    Returns:
        (str) - Name of the most common month
    """
    return df["Start Time"].dt.month_name().mode()[0]


def most_common_day_of_week_name(df):
    """
    Returns the most common day of the week name.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day

    Returns:
        (str) - Name of the most common day of the week
    """
    return df["Start Time"].dt.day_name().mode()[0]


def most_common_hour(df):
    """
    Returns the most common start hour.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day

    Returns:
        (int) - Most common start hour
    """
    return df["Start Time"].dt.hour.mode()[0]


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station_name = df["Start Station"].mode()[0]
    print(
        "The most common start station is {}.\n".format(
            most_common_start_station_name)
    )

    # display most commonly used end station
    most_common_end_station_name = df["End Station"].mode()[0]
    print("The most common end station is {}.\n".format(
        most_common_end_station_name))

    # display most frequent combination of start station and end station trip
    df["Start and End Station Combined"] = (
        df["Start Station"] + " to " + df["End Station"]
    )
    most_common_combined_start_end_station_name = df[
        "Start and End Station Combined"
    ].mode()[0]
    print(
        "The most common combination of start and end station is {}.\n".format(
            most_common_combined_start_end_station_name
        )
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # display total travel time
    print(
        "The total travel time is {} seconds.\n".format(
            total_travel_time_seconds(df))
    )

    # display mean travel time
    print("The mean travel time is {} seconds.\n".format(
        mean_travel_time_seconds(df)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def total_travel_time_seconds(df):
    """
    Calculates the total travel time in seconds.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day

    Returns:
        (int) - Total travel time in seconds
    """
    return df["Trip Duration"].sum()


def mean_travel_time_seconds(df):
    """
    Calculates the mean travel time in seconds.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day

    Returns:
        (int) - Mean travel time in seconds
    """
    return round(df["Trip Duration"].mean())


def user_stats(df, city):
    """
    Displays statistics on bikeshare users.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
        city - Name of the city being analyzed
    """
    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # Display counts of user types
    print("Count by User Types:\n")
    print(count_by_user_types(df))

    if "Gender" not in df.columns:
        print("\nWe do not have user gender data for {}.\n".format(
            city_name_data[city][1]))
    else:
        print("\nCount by User Gender:\n")
        print(count_by_user_gender(df))

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" not in df.columns:
        print(
            "\nWe do not have user year of birth data for {}.\n".format(
                city_name_data[city][1]
            )
        )
    else:
        print("\nYear birth analysis:\n")
        print("The first user year of birth is {}.\n".format(
            user_first_birth_year(df)))
        print("The last user year of birth is {}.\n".format(
            user_last_birth_year(df)))
        print(
            "The most common user year of birth is {}.\n".format(
                user_most_common_birth_year(df)
            )
        )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def count_by_user_types(df):
    """
    Returns the count of user types.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day

    Returns:
        (str) - Count of user types
    """
    return df["User Type"].value_counts().to_string()


def count_by_user_gender(df):
    """
    Returns the count of user genders.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day

    Returns:
        (str) - Count of user genders
    """
    return df["Gender"].fillna("Not Declared").value_counts().to_string()


def user_first_birth_year(df):
    """
    Returns the earliest user birth year.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day

    Returns:
        (float) - Earliest user birth year
    """
    return df["Birth Year"].min()


def user_last_birth_year(df):
    """
    Returns the most recent user birth year.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day

    Returns:
        (float) - Most recent user birth year
    """
    return df["Birth Year"].max()


def user_most_common_birth_year(df):
    """
    Returns the most common user birth year.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day

    Returns:
        (int) - Most common user birth year
    """
    return int(df["Birth Year"].mode()[0])


def raw_data(df):
    """
    Displays 5 lines of raw data upon user request.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    raw_data_init_row = 0
    df_total_rows = len(df)
    should_show_raw_data = get_5_lines_raw_data_input()
    should_show_more_raw_data = "no"
    no_more_rows_to_show = "\nWe do not have any more rows to show.\n"

    if should_show_raw_data == "yes":
        show_raw_data(df, raw_data_init_row)
        raw_data_init_row += 5

        if df_total_rows > raw_data_init_row:
            should_show_more_raw_data = get_show_more_raw_data_input()
        elif df_total_rows <= raw_data_init_row:
            print(no_more_rows_to_show)

        while should_show_more_raw_data == "yes" and (
            df_total_rows > raw_data_init_row
        ):
            show_raw_data(df, raw_data_init_row)
            raw_data_init_row += 5
            if df_total_rows > raw_data_init_row:
                should_show_more_raw_data = get_show_more_raw_data_input()
            else:
                print(no_more_rows_to_show)


def get_5_lines_raw_data_input():
    """
    Asks the user if they want to see 5 lines of raw data.

    Returns:
        (str) - User input: 'yes' or 'no'
    """
    while True:
        user_input = (
            input("\nDo you want to see the 5 lines of raw data, enter yes or no:")
            .replace(" ", "")
            .lower()
        )
        if user_input in ["yes", "no"]:
            return user_input
        else:
            print("\nInvalid input, please enter yes or no. \n")


def get_show_more_raw_data_input():
    """
    Asks the user if they want to see more lines of raw data.

    Returns:
        (str) - User input: 'yes' or 'no'
    """
    while True:
        user_input = (
            input("\nDo you want to see the next 5 lines of raw data, enter yes or no:")
            .replace(" ", "")
            .lower()
        )
        if user_input in ["yes", "no"]:
            return user_input
        else:
            print("\nInvalid input, please enter yes or no. \n")


def show_raw_data(df, raw_data_init_row):
    """
    Displays 5 lines of raw data from the specified row.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
        raw_data_init_row - Initial row number for displaying raw data
    """
    print(df[raw_data_init_row: raw_data_init_row + 5].to_string())


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        raw_data(df)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != "yes":
            break


if __name__ == "__main__":
    main()
