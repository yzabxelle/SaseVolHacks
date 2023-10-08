# SaseVolHacks
#intialized the values for car, bus, rail, and carbon neutral 
# of transport*/
car = 0.192
bus = 0.105
neutral = 0.0
rail = 0.041

#input from user for kilometers in car
kmCar = float(input("Kilometers in Car: "))

#input from user for kilometers in Bus
kmBus = float(input("Kilometers in Bus: "))

#input from user for kilometers in Rail
kmRail = float(input("Kilometers in Rail: "))

#input from user for kilometers in Carbon Neutral
kmCarbonNull = float(input("Kilometers in Biking/Walking/Running: "))

#Calculating total distance traveled
totalDis = kmCar + kmBus + kmRail + kmCarbonNull

#Calculating total CO2 if in car
totalCO2 = totalDis * car

#Calculating actual CO2 in all modes of transport plus car
actualCO2 = (car * kmCar)+(bus * kmBus)+(rail * kmRail)+(neutral * kmCarbonNull)

#More efficent by percentage

result = 100 - (round((float(actualCO2) / float(totalCO2)), 2) * 100)

#If you are 100% efficent then prints 'you are carbon neutral! 
#Congrats! If not then it shows the percentage
if result == 100: 
  print("You are carbon neutral! Congrats!")
else: 
  print("You are", result, "% more efficent than just using car to travel!")

#Grams of CO2 eliminated in acutal compared to completely car in the total distance
savedCO2 = totalCO2 - actualCO2
