car = 192.0
bus = 105.0
neutral = 0.0
EV = 53
rail = 41.0
add = True
kmCarList = []
kmBusList = []
kmRailList = []
kmEVList = []
kmCarbonNullList = []
while add:
  choice = input("Do you want to add a log (Y/N): ")
  if choice == "N":
    print("Program exiting...")
    add = False
  else:
    date = input("Enter Date (YY/MM/DD): ")
    
    #input from user for kilometers in car
    kmCar = float(input("Kilometers in Car: "))
    kmCarList.append(kmCar)
    sKmCarList = sum(kmCarList)
    #input from user for kilometers in Bus
    kmBus = float(input("Kilometers in Bus: "))
    kmBusList.append(kmBus)
    sKmBusList = sum(kmBusList)
    #input from user for kilometers in Rail
    kmRail = float(input("Kilometers in Rail: "))
    kmRailList.append(kmRail)
    sKmRailList = sum(kmRailList)
    #input from user for kilometers in EV
    kmEV = float(input("Kilometers in Electric Vehicle: "))
    kmEVList.append(kmEV)
    sKmEVList = sum(kmEVList)
    #input from user for kilometers in Carbon Neutral
    kmCarbonNull = float(input("Kilometers in Biking/Walking/Running: "))
    kmCarbonNullList.append(kmCarbonNull)
    sKmCarbonNullList = sum(kmCarbonNullList)
    
    #If all modes of travel km is 0 then this will run.
    if kmCar == kmBus == kmRail == kmCarbonNull == kmEV == 0:
      print("Have some walk... Please...")
      exit()
    #Calculating total distance traveled
    #Theorically if distance is traveled by only car

    totalDis = kmCar + kmBus + kmRail + kmEV + kmCarbonNull
    
    totalDisList = sKmCarList + sKmBusList + sKmRailList + sKmCarbonNullList + sKmEVList
    #Calculating total CO2 if in car
    totalCO2 = totalDis * car
    
    totalCO2List = totalDisList * car
  
    #Calculating actual CO2 in all modes of transport plus car
    #actualCO2 is the users CO2 emmision
    actualCO2 = (car * kmCar) + (bus * kmBus) + (rail * kmRail) + (
        neutral * kmCarbonNull) + (EV * kmEV)
    
    actualCO2List1 = car*sKmCarList + bus*sKmBusList + rail*sKmRailList
    actualCO2List2 = neutral*sKmCarbonNullList + EV*sKmEVList
    actualCO2List = actualCO2List1 + actualCO2List2
    #result of efficency by percentage
    result = round(100 - (actualCO2 / totalCO2 * 100), 1)
    resultList = round(100 - (actualCO2List / totalCO2List * 100), 1)
    #If you are 100% efficent then prints 'you are carbon neutral!
    #Congrats! If not then it shows the percentage
    
    print("On ", date, " You are ",
          result,
          "% more efficent than just using car to travel!",
          sep="")
    
    print("You are in total ",
          resultList,
          "% more efficent than just using car to travel!",
          sep="")
  
    #Grams of CO2 emmision saved in actual compared to all car in the total CO2
    savedCO2 = int(totalCO2 - actualCO2)
    savedCO2List = int(totalCO2List - actualCO2List)
    print("You saved:", savedCO2, "grams of CO2!")

    print("You saved:", savedCO2List, "grams of CO2 in total!")