# This program use the data in pump_data.txt to compile a report of pump
# operation and power use. The short_data.txt file contains just one hour's
# worth of data from the pump

# Constant definition:
# 1 hour equals to 60 minutes, 1 day equals to 24 hours
# pump produces two gallons of water per minute when it's running
# pump should be expected to draw about 1000 watts a minute when it's running
# the lowest running watt should be 800 based on the data in pump_data.txt
# based on the data in file, when watt reach to 500, it is ready to run
# divide the Watt minutes value by 1000 to turn the Watts into Kilowatts
# our report will include how long it took to consume 5 gallons and 100 gallons
MINUTE_HOUR_CONVERSION = 60
HOUR_DAY_CONVERSION = 24
PER_MINUTE_GALLON = 2
PER_MINUTE_WATT = 1000
KWH_CONVER_WATT = 1000

RUNNING_WATT = 500

FIVE_GALLON = 5
ONE_HUNDRED_GALLON = 100


# prompt the user to input a file name, if it is valid, open the file and
# execute the functions below it. If it is not valid, give the user a message
# that he cannot open it
def main():
    file_name = input("Enter the file name: ")
    try:
        data_file = open(file_name, "r")
    except:
        print("Unable to open {}".format(file_name))
        return

    report(data_file)


# convert minute-by-minute power consumption data in file into integer and
# store the data into a list
def data_storage(data_file):
    data_list = []
    for num in data_file.readlines():
        data_list.append(int(num))

    return data_list


def report(data_file):
    data = data_storage(data_file)
    total_minute = len(data)
    total_minute_power = sum(data)

    # Report the duration of the data file in both hours and days
    total_hour = total_minute / MINUTE_HOUR_CONVERSION
    day_num = total_hour / HOUR_DAY_CONVERSION

    print("Data covers a total of {} hours".format(total_hour))
    print("(That's {} days)".format(day_num))

    # How long the pump runs and what is the total_watt it produces
    running_time = 0
    total_watt = 0
    for watt in data:
        if watt > RUNNING_WATT:
            running_time += 1
            total_watt += watt

    gallon_amount = running_time * PER_MINUTE_GALLON
    gallon_day = gallon_amount / total_hour * HOUR_DAY_CONVERSION
    kilowatts = (total_minute_power / KWH_CONVER_WATT) / MINUTE_HOUR_CONVERSION

    # Report both the total number of gallons produced
    # and the average daily consumption.
    print("\nPump was running for", running_time, "minutes",
          "producing",  gallon_amount, "gallons")
    print("(That's {} gallons per day)".format(gallon_day))

    # Report the total power used by the pump
    print("\nPump required a total of", total_minute_power,
          "watt minutes of power")
    print("That's {} kWh".format(kilowatts))

    # Print how long it took to consume 5 gallons and 100 gallons
    five_gallon_minutes = 0

    for i in range(len(data)):
        if data[i] >= RUNNING_WATT:
            five_gallon_minutes += 1
            if five_gallon_minutes >= FIVE_GALLON / PER_MINUTE_GALLON:
                print("\nIt took", i+1, "minutes of data to reach",
                      FIVE_GALLON, "gallons.")
                break

    hundred_gallon_minutes = 0
    for j in range(len(data)):
        if data[j] >= RUNNING_WATT:
            hundred_gallon_minutes += 1
            if hundred_gallon_minutes >= (ONE_HUNDRED_GALLON /
                                          PER_MINUTE_GALLON):
                print("It took", j+1, "minutes of data to reach",
                      ONE_HUNDRED_GALLON, "gallons.\n")
                break
    else:
        print("It took", -1, "minutes of data to reach", ONE_HUNDRED_GALLON,
              "gallons.\n")

    # check the data in the data list, when the pump runs for at least
    # 120 minutes in a row, report when the long run started and
    # how long it lasted.
    new_list = []
    for i in range(len(data)):
        while data[i] >= RUNNING_WATT:
            new_list.append(data[i])
            break

        else:
            if len(new_list) >= 120:
                print(len(new_list), "minute run started at",
                      i-len(new_list)+1)
            new_list = []

main()
