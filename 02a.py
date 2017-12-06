"""Advent of Code - Day 02 - Checksum - Part I"""

import sys

def main():
    """Open TXT input and count the checksum"""
    #f = open(sys.argv[1],"r")

    #line by line example http://stackabuse.com/read-a-file-line-by-line-in-python/

    #https://www.reddit.com/r/SWGalaxyOfHeroes/comments/7g51fy/swgoh_101_the_comprehensive_mod_guide/

    #pole = f.readline()

    with open(sys.argv[1]) as fp:
        for cnt, line in enumerate(fp):
            print("Line {}: {}".format(cnt, line))

    #print(len(pole))

    #print(pole)

    # totalSum = 0
    # n = 0
    #
    # # Run through the input and do the countning
    # while n < (len(pole)-2):
    #     if int(pole[n]) == int(pole[n+1]):
    #         totalSum = totalSum + int(pole[n])
    #
    #     # print("Index:",n,"Actual:",pole[n],"Next:",pole[n+1],"Actual sum:",totalSum)
    #     n = n+1;
    #
    # # Compare the 1st and last ("circle buffer")
    # if int(pole[0]) == int(pole[-2]):
    #     totalSum = totalSum + int(pole[0])
    #
    # print("The inverse captcha sum of the input is:",totalSum)

    #f.close()

if __name__ == '__main__':
    main()
