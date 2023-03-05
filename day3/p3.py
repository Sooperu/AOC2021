import json
from typing import List

#Imports a method that pulls the text data from the AOC site
import shared
org_list = shared.get_day(2021, 3)
#print(json.dumps(org_list))

def zero_or_one(letter: str)-> bool:
    '''Function to check if the string is 1 or not.
    '''
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

#Part 2
def find_most_common_bit(text: List[str])-> str:
    '''Function that compares the specific index of a string in a list, and then 
    takes count of it and returns a string combination of the most common bit.'''
    length = len(text[0])
    count_one, count_zero = 0, 0
    temp = ''
    for i in range(length):
        for j in text:
            if zero_or_one(j[i]):
                count_one += 1
            else:
                count_zero+= 1
        if count_one >= count_zero:
            temp += '1'
        else:
            temp += '0'
        count_one, count_zero = 0,0
    return temp

def find_least_common_bit(text: List[str])-> str:
    '''Function that compares the specific index of a string in a list, and then 
    takes count of it and returns a string combination of the least common bit.'''
    length = len(text[0])
    count_one, count_zero = 0, 0
    temp = ''
    for i in range(length):
        for j in text:
            if zero_or_one(j[i]):
                count_one += 1
            else:
                count_zero+= 1
        if count_one >= count_zero:
            temp += '0'
        else:
            temp += '1'
        count_one, count_zero = 0,0
    return temp

def delete_most_common_bit(text: List[str], index: int)-> List[str]:
    '''Function that uses the other function called, to find parse the list of strings and
    deletes the ones that has the same bit in the specific index.'''
    common = find_most_common_bit(text)
    text = list(text)
    del_list = []
    for i in text:
        if i[index] != common[index]:
            del_list.append(i)
        else:
            continue
    for line_to_delete in del_list:
        place = text.index(line_to_delete)
        del text[place]
    return text

def delete_least_common_bit(text: List[str], index: int)-> List[str]:
    '''Function that uses the other function called, to find parse the list of strings and
    deletes the ones that has the same bit in the specific index.'''
    common = find_least_common_bit(text)
    text = list(text)
    del_list = []
    for i in text:
        if i[index] != common[index]:
            del_list.append(i)
        else:
            continue
    for line_to_delete in del_list:
        place = text.index(line_to_delete)
        del text[place]
    return text

otwo_list = org_list
index = 0
while len(otwo_list) > 1:
    otwo_list = delete_most_common_bit(otwo_list, index)
    index += 1

cotwo_list = org_list
index = 0
while len(cotwo_list) > 1:
    cotwo_list = delete_least_common_bit(cotwo_list, index)
    index += 1
print(int(otwo_list[0], 2) * int(cotwo_list[0], 2))