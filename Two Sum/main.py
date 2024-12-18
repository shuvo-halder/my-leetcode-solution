import os, sys
from typing import List, Tuple

# nums = [2,7,11,15], target = 9

# not work in single target

nums = [2,7,11,15,0]
target = 15


class Main:
    def sumTwo(nums, target):
        numToIndexMap = {}
        
        for num1_index, num1 in enumerate(nums):
            num2 = target - num1

            try:
                num2_index = numToIndexMap[num2]
            except KeyError:
                numToIndexMap[num1] = num1_index
            else:
                sortedValue = tuple(sorted([num1_index, num2_index]))
                print(sortedValue)
                return sortedValue
            
    
    if __name__ == '__main__':
        sumTwo(nums , target)

