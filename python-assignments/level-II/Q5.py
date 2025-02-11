"""
5. You are developing a program that analyzes weather data. Write
a Python function that takes a list of temperature readings for a
specific location and determines the average temperature, highest
temperature, and lowest temperature.
Input: temperature_readings = [25, 28, 21, 24, 27]
Output:
Average Temperature: 25.0
Highest Temperature: 28
Lowest Temperature: 21
"""

def details(temps):
    max_temp = float("-inf")
    min_temp = float("inf")
    total = 0
    for temp in temps:
        if temp > max_temp:
            max_temp = temp
        if temp < min_temp:
            min_temp = temp
        total += temp
    average = total / len(temps)
    return max_temp, min_temp, average

temps = list(map(int, input("Enter temperatures (space seperated): ").split()))
max_temp, min_temp, average = details(temps)
print("Average Temperature: ", average)
print("Highest Temperature: ", max_temp)
print("Lowest Temperature: ", min_temp)

