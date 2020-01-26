"""
Python script to check validity of credit card numbers
"""

import sys
import re
import datetime

def sum_digits(digit):
    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)
        return sum

# Use Luhn's algorithm here to check a valid dard number
def validate(cc_num):
    # reverse the credit card number
    cc_num = str(cc_num)
    cc_num = cc_num[::-1]
    # convert to integer list
    cc_num = [int(x) for x in cc_num]
    # double every second digit
    doubled_second_digit_list = list()
    digits = list(enumerate(cc_num, start=1))
    for index, digit in digits:
        if index % 2 == 0:
            doubled_second_digit_list.append(digit * 2)
        else:
            doubled_second_digit_list.append(digit)

    # add the digits if any number is more than 9
    doubled_second_digit_list = [sum_digits(x) for x in doubled_second_digit_list]
    # sum all digits
    sum_of_digits = sum(doubled_second_digit_list)
    # return True or False
    return sum_of_digits % 10 == 0


def validate_date(expiry_date):
    try:
    # if 1:
        expiry_date = datetime.datetime.strptime(expiry_date,'%Y/%m/%d')
        # Make sure end date is >= start date
        start_date = datetime.datetime.today()
        # print(start_date)
        # print(expiry_date)
        # Check the expiry date input must be greater than or equal to the current dates
        if expiry_date >= start_date:
            print("correct date")
        else:
            print("Expiry date cannot be less than current date")
            return False
        return True
    #Raise exception if the provided input is not in require date format
    except ValueError:
    # else:
        print("Incorrect date format, should be YYYY-MM-DD")
        return False


def validate_cvv(card_cvv):
    try:
    # if 1:
        if(int(card_cvv)):
            #check the length of cvv number
            if len(str(card_cvv)) == 3:
                # print("ok")
                return True
            else:
                # print("owkdodo")
                return False
                # return True
    #Raise exception when cvv cannot be converted to int
    except:
    # else:
        print("CVV must be 3 digit numeric number.")
        return False

def validate_name(card_owner_name):
    try:
        if card_owner_name.isalpha():
            # print("ok")
            return True
        else:
            # print("not ok")
            return False
    except:
        # print("not ok")
        return False
#
# if __name__ == "__main__":
#     card_number = input("Enter the card number: ")
#     while validate(card_number) != True:
#         print("Your card number is invalid!")
#         card_number = input("Enter the card number,enter q to exit.")
#         if card_number=='q':
#             continue
#         else:
#             print(validate(card_number))
#
#     card_owner_name = input("Enter Owner Name: ")
#     print(validate_name(card_owner_name))
#
#     expiry_date = str(input("Please provide Expiry Date of card: "))
#     print(validate_date(expiry_date))
#     while validate_date(expiry_date) == False:
#         expiry_date = str(input("Please provide Expiry Date of card: "))
#         print(validate_date(expiry_date))
#
#     card_cvv = str(input("Enter CVV: "))
#     print(validate_cvv(card_cvv))
#     while(validate_cvv(card_cvv)==False):
#         card_cvv = str(input("Enter CVV: "))
#         print(validate_cvv(card_cvv))

