#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: November 2019
# This program outputs all integers from 1000 to 2000


def main():
    # this program outputs all integers from 1000 to 2000

    # process & output
    for counter in range(1000, 2001):
        print(counter, end=" ")
        if counter % 5 == 4:
            print(" ")


if __name__ == "__main__":
    main()
