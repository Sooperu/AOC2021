import json
from typing import List

#Imports a method that pulls the text data from the AOC site
import shared
org_list = shared.get_day(2021, 2)
#print(json.dumps(org_list))


direction = ''
movement = ''
x_coor = 0
y_coor = 0
def y_movement(direction: str, move: int)-> int:
    """Adjust the y_coor based on the description of the movement and the 
    amount. """
    if direction == 'up':
        return -abs(move)
    elif direction == 'down':
        return move
    else:
        raise Exception()
#Part 1
for i in org_list:
    direction, movement = i.split(' ')
    if direction == 'forward': #checks to see if the movement is horizontal
        x_coor += int(movement)
    elif direction == 'up' or direction == 'down':
        y_coor += y_movement(direction, int(movement))
    else:
        raise Exception()
product = x_coor * y_coor
print(f'My final horizontal position is {x_coor} and vertical position is {y_coor}.')
print(f'The product of my two coordinates is {product}.')



new_direction = ''
new_movement = ''
new_x_coor = 0
new_y_coor = 0
aim_coor = 0
def aim_movement(direction: str, move: int)-> int:
    """Adjust the aim based on the description of the movement and the 
    amount. """
    if direction == 'up':
        return -abs(move)
    elif direction == 'down':
        return move
    else:
        raise Exception()

#Part 2
for i in org_list: 
    new_direction, new_movement = i.split(' ')
    if new_direction == 'forward': #checks to see if the movement is horizontal
        new_x_coor += int(new_movement)
        aim_change = int(new_movement) * aim_coor 
        new_y_coor += aim_change 
    elif new_direction == 'up' or new_direction == 'down':
        aim_coor += aim_movement(new_direction, int(new_movement))
    else:
        raise Exception()
    
new_product = new_x_coor * new_y_coor
print(f'The new product of our horizontal and depth is {new_product}.')