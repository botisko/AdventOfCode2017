"""Advent of Code 2017 - Day 3: Spiral Memory - Part I"""

#import sys

def main():
    """Calculate the path"""
    pathSize = 0

    # Define the ways
    wayUp = [1, 4]
    wayDn = [1, 8]
    wayLeft = [1, 6]
    wayRight = [1, 2]

    # Define destination interval
    # maxDest = 320000
    # minDest = 0

    # Define initial step size
    step = 62

    # Calculate the value in chosen way step size away
    chosenWay = wayUp # wayDn wayLeft wayRight

    #print("Check:",wayRight[0])

    n = 1
    stepSize = chosenWay[1] - chosenWay[0]
    pathSize = chosenWay[1]
    print("Step:0, Value:",pathSize)
    while n < step:
        stepSize += 8*(n-1)
        pathSize += stepSize + 8
        print("Step:",n,"Size:",stepSize,"Value:",pathSize)
        n += 1

    print("Path size:",pathSize)

    print(pow(2,3))

if __name__ == '__main__':
    main()
