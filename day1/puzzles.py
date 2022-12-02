#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
 @Author: Mayara Ferreira
 @Github: @mayaracsferreira

Advent of Code 2022
Day 1 puzzle
--------------------
Puzzle 1:
1# read input values 
2# separate and convert calories carried per elf
3# sum total amount of calories per elf
4# get most high calorie value

Puzzle 2:
5# get top three calories sum carried by elves
'''

INPUT_VALUES_FILE = 'input.txt'

def read_file(filename: str):
    file = open(filename)
    try:
        return file.read()
    except Exception as e:
        print("Unable to open file {filename}. {exception}".format(filename = filename, exception=str(e)))
    finally:
        file.close()
 
def list_convert_calories_per_elf(calories_list: list[str]):
    elvesCaloriesList = []
    for calories in calories_list:
        # 2# separate and convert calories carried per elf
        caloriesPerElf = [int(calorie) for calorie in calories.split("\n")]
        elvesCaloriesList.append(caloriesPerElf)
    return elvesCaloriesList
    
def list_sum_calories_per_elf(calories_elves_list: list):
    sum_calories_per_elf_list = [sum(elvesCalories) for elvesCalories in calories_elves_list]
    sum_calories_per_elf_list.sort(reverse=True)
    return sum_calories_per_elf_list

try:
    # 1# read input values    
    input_calories_list = read_file(INPUT_VALUES_FILE).split("\n\n")
    # 2# separate and convert calories carried per elf
    calories_per_elf_list = list_convert_calories_per_elf(input_calories_list)
    # 3# sum total amount of calories per elf
    total_calorie_amount_per_elf_list = list_sum_calories_per_elf(calories_per_elf_list) 
    # 4# get most high calorie value
    puzzle1_answer = max(total_calorie_amount_per_elf_list)
    # 5# get top three calories sum carried by elves
    puzzle2_answer = sum(total_calorie_amount_per_elf_list[:3])
finally:        
    print("Puzzle 1: How many total Calories is that Elf carrying? " + str(puzzle1_answer))
    print("Puzzle 2:  How many Calories are those Elves carrying in total? " + str(puzzle2_answer) )