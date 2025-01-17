import math
import os
import random
import re
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..','..')))
from utils.data_reader import read_txt_file


def freqQuery(queries):
    data = {}
    res = []
    for q in queries:
        if q[0] ==1:
            if q[1] in data: 
                data[q[1]] += 1
            else:
                data[q[1]] = 1
        elif q[0] ==2:
            if q[1] in data:
                data[q[1]] -= 1
                if data[q[1]] == 0:
                    del data[q[1]]
        elif q[0] == 3:
            if q[1] in data.values():
                res.append(1)
            else:
                res.append(0)
    return res


if __name__ == '__main__':
    data_file_path = os.path.join(os.path.dirname(__file__), 'data.txt')
    file = read_txt_file(data_file_path)
    
    def exercise(file):
        exercises = {}
        current_exercise = None
        data = []
        
        i = 1
        for line in file:
            line = line.strip()
            if line.isdigit():
                if current_exercise is not None:
                    exercises[current_exercise] = data
                current_exercise = i
                i+=1
                data = []
            else:
                pair = tuple(map(int, line.split()))
                data.append(pair)
        if current_exercise is not None:
            exercises[current_exercise] = data
            
        return exercises
    
    
    def printer(test_case,queries,expected_output):
        res = freqQuery(queries)
        print(f"Output:{res} \nExpected output:{expected_output}\n")
        assert res == expected_output , f"Expected output: {expected_output}, Your output: {res}"
        print(f"Test {test_case} passed")
    
    
    test_cases = exercise(file)
        
    '''Case 1'''
    print("\n----Case 1----\n")
    queries = test_cases[1]
    expected_output = [0,1]
    
    printer(test_case=1,queries=queries,expected_output=expected_output)
    
    '''Case 2'''
    print("\n----Case 2----\n")
    queries = test_cases[2]
    expected_output = [0,1]
    printer(test_case=2,queries=queries,expected_output=expected_output)
    
    '''Case 3'''
    print("\n----Case 3----\n")
    queries = test_cases[3]
    expected_output = [0,1,1]
    printer(test_case=3,queries=queries,expected_output=expected_output)
    
    print("\nCONGRATULATIONS ALL TEST PASSED")