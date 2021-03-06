"""
Problem #18
---------------
By starting at the top of the triangle in INPUT1 and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23. That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle in INPUT2:
NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

***NOT COMPLETE, UNDER CONSTRUCTION***
"""
import io

def generateList(filepath: str):
    nums = []
    with open(filepath,'r') as fp:
        # Read a new line & strip it of its endline character
        line = fp.readline().strip()
        while line:
            # Start with the line in the form of a string (e.g. '4 6')
            # Transform it into a list of smaller strings (e.g. ['4', '6']) using line.split()
            # Transform it into a list of integers (e.g. [4, 6]) using list(map())
            line = list(map(int,line.split())) 
            # Add the new line of numbers to nums
            nums.append(line)
            # Read new line. If it's empty, the loop will stop.
            line = fp.readline().strip()
    fp.close()
    return nums

def maxPathSumBruteForce(nums: list):
    # Brute force method
    # I think I need to use a binary tree.......
    sums = []
    numrows = len(nums)
    numpaths = 2 ** (numrows - 1)
    starter_path = [0 for i in range(0,numrows)]
    print(starter_path)
    # print(nums)
    # print(numrows)
    # print(numpaths)
    # path_index = []
    # path_values = []
    # for i in range(0,numrows):
    #     path_index.append(i)
    #     path_values.append(nums[i][i])
    # print(path_index)
    # print(path_values)
    # paths = []
    # for path in numpaths:
    #     paths.append([0])
    # for row in range(0,numrows):
    #     print(paths)
    #     print(paths[0])
    #     new_el = paths.append(0)
    #     print(new_el)
    #     new_paths.append(new_el)
    #     paths = new_paths
    #     # Define the new path using tuples
    #     path = ()
    #     # Generate the sum for the path and add it to the list of sums
    #     # Go on to the next path
    #     i+=1
    # return max(sums)

def maxPathSumClever(nums: list):
    # Clever method
    pass

input = generateList('PE\p018_input2.txt')
print(maxPathSumBruteForce(input))
