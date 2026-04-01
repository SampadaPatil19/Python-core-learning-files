import datetime

now = datetime.datetime.now()
print("Current date and time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# Formatting date and time

formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_date)

# Creating a specific date
specific_date = datetime.datetime(2003, 7, 19, 22, 10, 0)
print("Specific date and time:", specific_date)

# Calculating difference between two dates
date1 = datetime.datetime(2022, 1, 1)
date2 = datetime.datetime(2023, 1, 10)

difference = date2 - date1
print("Difference between dates:", difference)
print("Days difference:", difference.days)
print("Days difference:", difference.days)

# strptime 
date_string = "2022-11-23 13:45:36"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed date and time:", parsed_date)


# strftime
current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%A, %d %B %Y %I:%M:%S %p") 
# %A - weekdayname, %d - day, %B - month name, %Y - year, %I - hour(12hr), %M - minute, %S - seconds, %p - AM/PM
print("Formatted current time:", formatted_time)

# Adding days to current date
days_to_add = 10
new_date = now + datetime.timedelta(days=days_to_add)
print(f"Date after adding {days_to_add} days:", new_date)
