import json
from typing import List

#Imports a method that pulls the text data from the AOC site
import shared
org_list = shared.get_day(2021, 3)
#print(json.dumps(org_list))

def zero_or_one(letter: str)-> bool:
    if letter == '1':
        return True
    else:
        return False
#Part 1
count_zero = 0
count_one = 0
gamma_rate = ''
ep_rate = ''
length = len(org_list[0])
for i in range(length):
    for j in org_list:
        if zero_or_one(j[i]):
            count_one += 1
        else:
            count_zero+= 1         
    if count_one > count_zero:
        gamma_rate += '1'
        ep_rate += '0'
    else:
        gamma_rate += '0'
        ep_rate += '1'
    count_zero = 0
    count_one = 0
print(int(gamma_rate, 2)*int(ep_rate, 2))