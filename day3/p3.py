import json
from typing import List

#Imports a method that pulls the text data from the AOC site
import shared
org_list = shared.get_day(2021, 2)
print(json.dumps(org_list))