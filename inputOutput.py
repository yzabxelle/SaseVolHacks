import csv

class inputOutput():
    # Asks for User Input & Organizes them into data
    def askForInput(dataSet):
        while True:
            list = []

            # Asks for transportation type
            transportationType = input("Enter transportation type: ")

            # Asks for distance traveled & metrics
            distance = input("Enter travel distance: ")
            distanceType = input("Enter travel distance: ")

            # Asks for Start Time & End Time
            startTime = input("Enter Start Time: ")
            endTime = input("Enter End Time: ")

            # Asks for date in YY/MM/DD
            date = input("Enter Date (YY/MM/DD): ")

            # Makes a list of data
            for i in range(6):
                list.append(transportationType)
                list.append(distance)
                list.append(distanceType)
                list.append(startTime)
                list.append(endTime)
                list.append(date)
            
            # Logs list to dataSet
            dataSet.append(list)
            
            # Asks User if there's additional data
            if (input("Is there additional data? (Y/N): ") == "N"):
                break

    # Makes an excel file & Stores data
    def organizeExcel(dataSet):
        file = open("dataLog.csv", "w")

        writer = csv.writer(file)

        # Writes to excel file from dataSet
        for row in dataSet:
            print(row)
            writer.writerow(row)

        file.close("dataLog.csv")

    """
    def main():
        dataSet = []
        inputOutput.askForInput(dataSet)
        inputOutput.organizeExcel(dataSet)
    """