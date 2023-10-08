import csv

class Gamification():
    # Calculates User XP
    def calculateXP():
        file = open('dataLog.csv')

        reader = csv.reader(file)

        # Reads from excel file to calculate XP
        for row in reader:
            #Grams of CO2 emmision saved in actual compared to all car in the total CO2
            #savedCO2 math in 'Math branch'
            savedCO2 = int(totalCO2 - actualCO2)
            totalXP = savedCO2

        file.close('dataLog.csv')
        return totalXP

    # Calculates User level
    def calculateLevel(totalXP):
        level = 0
        totalXP = totalXP
        threshold = 1000

        # Levels up until XP cannot reach newly calculated threshold
        while (totalXP >= threshold)
            totalXP -= threshold
            level += 1
            threshold = round(threshold * 1.15)
        
        return level
    

    # Unlocks reward if satisfactory level is reached
    def unlockReward(totalXP, rewardLVL):
        return (totalXP >= rewardLVL)
    
    """
    def main():
        Gamification.calculateLevel(calculateXP())
        Gamification.unlockReward(rewardLVL, calculateXP()) # rewardLVL depends on collectible
    """
