import math
import os
import random
import re
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..','..')))
from utils.data_reader import read_txt_file


'''
arr1 = [1,2,2,4]
arr2 = [1,3,9,9,27,81]
arr3 = [1,5,5,25,125]
'''
def countTriplets(arr, r):
    seconds = {}
    thirds = {}
    count = 0

    for i in arr:
        
        if i in thirds.keys():
            count += thirds[i]

        if i in seconds.keys():
            if i * r in thirds:
                thirds[i * r] += seconds[i]
            else:
                thirds[i * r] = seconds[i]

        if i * r in seconds.keys():
            seconds[i * r] += 1
        else:
            seconds[i * r] = 1

    return count


if __name__ == '__main__':
    def printer(test_case,arr,r,expected_output):
        res = countTriplets(arr, r)
        print(f"Output:{res} \nExpected output:{expected_output}\n")
        assert res == expected_output , f"Expected output: {expected_output}, Your output: {res}"
        print(f"Test {test_case} passed")
        
    data_file_path = os.path.join(os.path.dirname(__file__), 'data.txt')
    nr = read_txt_file(data_file_path)
    
    '''Case 1'''
    print("\n----Case 1----\n")
    n = int(nr[0].replace('\n','').split()[0])
    r = int(nr[0].replace('\n','').split()[1])
    arr = list(map(int,nr[1].split()))
    
    printer(test_case=1,arr=arr,r=r,expected_output=2)
    
    '''Case 2'''
    print("\n----Case 2----\n")
    n = int(nr[2].replace('\n','').split()[0])
    r = int(nr[2].replace('\n','').split()[1])
    arr = list(map(int,nr[3].split()))
    
    printer(test_case=2,arr=arr,r=r,expected_output=6)

    '''Case 3'''
    print("\n----Case 3----\n")
    n = int(nr[4].replace('\n','').split()[0])
    r = int(nr[4].replace('\n','').split()[1])
    arr = list(map(int,nr[5].split()))
    
    printer(test_case=3,arr=arr,r=r,expected_output=4)
    
    print("\nCONGRATULATIONS ALL TEST PASSED")