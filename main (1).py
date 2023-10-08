#CO2 calculations math part

#intialized the values for car, bus, rail, and carbon neutral of transport
#Grams of carbon diocide per passenger kilometer
car = 192.0
bus = 105.0
neutral = 0.0
rail = 41.0

#input from user for kilometers in car
kmCar = float(input("Kilometers in Car: "))

#input from user for kilometers in Bus
kmBus = float(input("Kilometers in Bus: "))

#input from user for kilometers in Rail
kmRail = float(input("Kilometers in Rail: "))

#input from user for kilometers in Carbon Neutral
kmCarbonNull = float(input("Kilometers in Biking/Walking/Running: "))

if kmCar == kmBus == kmRail == kmCarbonNull == 0:
  print("Have some walk... Please...")
  exit()
#Calculating total distance traveled
#Theorically if distance is traveled by only car
totalDis = kmCar + kmBus + kmRail + kmCarbonNull

#Calculating total CO2 if in car
totalCO2 = totalDis * car

#Calculating actual CO2 in all modes of transport plus car
#actualCO2 is the users CO2 emmision
actualCO2 = (car * kmCar) + (bus * kmBus) + (rail * kmRail) + (neutral * kmCarbonNull)

#result of efficency by percentage
result = round(100 - actualCO2 / totalCO2 * 100, 1)

#If you are 100% efficent then prints 'you are carbon neutral!
#Congrats! If not then it shows the percentage
if result == 100:
  print("You are carbon neutral! Congrats!")
else:
  print("You are ", result, "% more efficent than just using car to travel!", sep = "")

#Grams of CO2 emmision saved in actual compared to all car in the total CO2
savedCO2 = round((totalCO2 - actualCO2), 1)
print("You saved:", savedCO2, "grams of CO2")