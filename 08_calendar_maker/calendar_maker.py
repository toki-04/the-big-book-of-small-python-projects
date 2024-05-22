import datetime

# Set up the constants:
DAYS: tuple[str] = (
    "Sunday", "Monday", "Tuesday",
    "Wednesday", "Thursday", "Friday",
    "Saturday",
)

MONTHS: tuple[str] = (
    "January", "February", "March",
    "April", "May", "June",
    "July", "August", "September",
    "October", "November", "December",
)


while True: # Loop to get a year from the user.
    print("Enter the year for the calendar:")
    response: int = input("> ")

    if response.isdecimal() and int(response) > 0:
        response = int(response)
        year = response
        break

    print("Please enter a numeric year, like 2023.")

while True: # Loop to get a month from the user.
    print("Enter the month for the calendar, 1-12:")
    response: int = input("> ")

    if not response.isdecimal():
        print("Please enter a numeric month, like 3 for March.")
        continue

    month = int(response)

    if 1 <= month <= 12:
        break

    print("Please enter a number from 1 to 12.")


def get_calendar_for(year:int, month:int):
    cal_text: str = "" # cal_text will contain the string of our calendar.

    # Put the month and year at the top of the calenda:
    cal_text += (' ' * 34) + MONTHS[month - 1] + " " + str(year) + "\n"

    # Add the days of the week labels to the calendar:
    cal_text += "...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n"

    # The horizontal line string that seperate weeks:
    week_seperator: str = ("+----------" * 7) + "+\n"

    # The blank rows have ten spaces in between the | day seperators:
    blank_row: str = ("|          " * 7) + "|\n"

    # Get the first date in the month. (The datetime module handles all
    # the complicated calendar stuff for us here.

    current_date = datetime.date(year, month, 1)

    # Roll back current_date until it is Sunday. (weekday() returns 6
    # for Sunday, not 0.

    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)

    while True: # Loop over each week in the month.
        cal_text += week_seperator

        # day_number_row is the row with the day number labels:
        day_number_row: str = ""
        for i in range(7):
            day_number_label = str(current_date.day).rjust(2)
            day_number_row += "|" + day_number_label + (' ' * 8)
            current_date += datetime.timedelta(days=1) # Go to next day.

        day_number_row += "|\n" # Add the vertical line after Saturday.

        # Add the day number row and 3 blank rows to the calendar text.
        cal_text += day_number_row

        for i in range(3): # (!) Try changing the 4 to a 5 or 10.
            cal_text += blank_row

        # Check if we're done with the month:
        if current_date.month != month:
            break

    # Add the horizontal line at the very bottom of the calendar.
    cal_text += week_seperator
    return cal_text


cal_text = get_calendar_for(year, month)
print(cal_text) # Display the calendar.

# Save the calendar to a text file:
calendar_file_name: str = f"calendar_{year}_{month}.txt"
with open(calendar_file_name, "w") as file_obj:
    file_obj.write(cal_text)

print("Saved to "+ calendar_file_name)



            














