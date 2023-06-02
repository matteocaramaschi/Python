#miles and kilometers

#KM and MILES
print("Kilometers and Miles conversion")
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#USD and EUR
print("EUR - USD conversion")
usd = 12.25
eur = 7.38

usd_to_eur = usd * 0.93
eur_to_usd = eur / 0.93

print(usd, "usd is", round(usd_to_eur, 3), "us dollars")
print(eur, "eur is", round(eur_to_usd, 3), "euros")

#Celsius and Fahrenheit
print("Celsius - Fahrenheit conversion")
celsius = 27.7
fahrenheit = 392.4

cel_to_fahr = celsius * 33.8
fahr_to_cel = fahrenheit / 33.8

print(celsius, "celsius is", round(cel_to_fahr), "fahrenheit")
print(fahrenheit, "fahrenheit is", round(fahr_to_cel, 1), "celsius")

#End time after duration
print("Time calculation")
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

if hour >= 0 and hour <= 24 and mins >= 0 and mins <= 60:
	endHours = (hour + ((mins + dura) // 60) ) % 24
	endMins = (mins + dura) % 60

	print(endHours, ":", endMins)
else:
	print("Hour or minute not in a correct format.")