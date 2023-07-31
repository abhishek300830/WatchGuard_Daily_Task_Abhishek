from collections import Counter

device_temperatures = [13.5, 14.0, 15,6, 14.0, 14.0, 15.8]

temperature_counter = Counter(device_temperatures)
print(temperature_counter)
print(temperature_counter[14.0])