BASE = 32
CONVERSION = 5/9

highest_temp = 77
lowest_temp = 53
difference_temp = highest_temp - lowest_temp

print("""The difference between the highest and the lowest
temperature values predicted for the 10 day forecast
is""", difference_temp, "°F")

temp_at_noon = [66, 69, 66, 64, 60, 60, 59, 60, 62, 63]
average_temp = sum(temp_at_noon)/len(temp_at_noon)

print("""The average temperature at noon predicted
for the 10 day forecast is""", average_temp, "°F")


def converter(fahrenheit):
    celsius = (fahrenheit - BASE) * CONVERSION
    return celsius
highest_celsius_temp = converter(highest_temp)

print("""The highest temperature predicted for the 10 day forecast,
onverted from Fahrenheit to Celsius is""", highest_celsius_temp, "°C")
