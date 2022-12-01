'''
Advent of Code 2022
Day 1 puzzle
Author: Mayara Ferreira
1# read input values 
2# separate calories carried per elf
3# separate and convert calories per elf
4# sum total amount of calories per elf
5# Print answer
'''

# 1# read input values 
file = open('input.txt')
elvesCalories = []
try:
    # 2# separate calories carried per elf
    elves = file.read().split("\n\n")
    for elf in elves:        
        # 3# separate and convert calories per elf
        caloryNumber = [int(calory) for calory in elf.split("\n")]
        # 4# sum total amount of calories per elf
        totalCalories = sum(caloryNumber)
        elvesCalories.append(totalCalories)
finally: 
    # 5# Print answer
    print("Total calories carried: " + str(max(elvesCalories)))
    print("Carried by the elf in position: " + str(elvesCalories.index(max(elvesCalories)) +1) )    
    file.close()