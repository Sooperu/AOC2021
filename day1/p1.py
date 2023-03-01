import json
from typing import List

#Imports a method that pulls the text data from the AOC site
import shared
org_list = shared.get_day(2021, 1)

#Function to compare two numbers, and see if its bigger
def is_it_big(original: int, new: int) -> bool:
    """Purpose of this function is to compare whether each number is going
    to be bigger than the previous one."""
    if new > original:
        return True
    else: 
        return False

#Part 1
count = 0
for index,i in enumerate(org_list[:-1]):
    if is_it_big(int(i), int(org_list[index+1])):
        count+= 1
print(count)


#Function to sum 3 numbers together
def sum_three(original: int, next_org:int, next_next_org: int)-> int:
    return sum((original, next_org, next_next_org))

#Part 2
new_count = 0
for index,i in enumerate(org_list[:-3]):
    cur_num = int(org_list[index])
    cur_numone = int(org_list[index+1])
    cur_numtwo = int(org_list[index+2])
    cur_numthree = int(org_list[index+3])
    if is_it_big(sum_three(cur_num,cur_numone,cur_numtwo), sum_three(cur_numone,cur_numtwo,cur_numthree)):
        new_count+= 1
print(new_count)