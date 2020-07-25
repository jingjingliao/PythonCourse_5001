def main():
    age = int(input("Please enter your age: "))
    restHR = int(input("Please enter your resting heart rate: "))

    print("=======================================")

    max_heart_rate = 208 - 0.7 * age
    reserve_rate = max_heart_rate - restHR

    print("Your heart rate reserve is: {} bpm".format(reserve_rate))

    print("Here is a breakdown of your training zones:")

    # Zone 1 (50-60%)
    # Zone 2 (60-70%)
    # Zone 3 (70-80%)
    # Zone 4 (80-93%)
    # Zone 5 (93-100%)
    # Zone_rate = rest_heart_rate + reserve * X%

    zone1_lowest_bgm = restHR + reserve_rate * 0.5
    zone1_highest_bgm = restHR + reserve_rate * 0.6
    zone2_highest_bgm = restHR + reserve_rate * 0.7
    zone3_highest_bgm = restHR + reserve_rate * 0.8
    zone4_highest_bgm = restHR + reserve_rate * 0.93
    zone5_highest_bgm = restHR + reserve_rate * 1.0

    # The zones are measured to two decimal places.
    # The lowest value for a given zone should be 0.01 greater than the highest
    # value for the previous zone.

    print("Zone 1:", round(zone1_lowest_bgm, 2), "to", round(zone1_highest_bgm, 2), "bpm")
    print("Zone 2:", round(zone1_highest_bgm + 0.01, 2), "to", round(zone2_highest_bgm, 2), "bpm")
    print("Zone 3:", round(zone2_highest_bgm + 0.01, 2), "to", round(zone3_highest_bgm, 2), "bpm")
    print("Zone 4:", round(zone3_highest_bgm + 0.01, 2), "to", round(zone4_highest_bgm, 2), "bpm")
    print("Zone 5:", round(zone4_highest_bgm + 0.01, 2), "to", round(zone5_highest_bgm, 2), "bpm")


main()
