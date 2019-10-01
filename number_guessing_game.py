#!/usr/bin/env python3

# Created by : Mariam Hemdan
# Created on : September 2019
# This module contains check the right guessing number


import constants


def main():
    # This function check the right gusseing number

    # input
    number_guessing_game = int(input("Enter a number from 0 to 9: "))
    print("")

    # process
    if number_guessing_game == constants.NUMBER_GUESSING_GAME:
        # output
        print("you get it right!")
    if number_guessing_game != constants.NUMBER_GUESSING_GAME:
        # output
        print("you are wrong")


if __name__ == '__main__':
    main()
