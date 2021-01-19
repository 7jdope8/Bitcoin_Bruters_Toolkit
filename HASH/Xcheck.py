# Psuedo Code:
# open my found addresses,txt (as a tuple?)
# open the blockchain addresses,csv (as a tuple?)
# compare list a to list b looking for a match
# if a match is found, find the address from addr_priv and print it to freemoney.txt
#.. Question is how to do this fast?

file = open("test1.csv", "r")
lineB = file.read().splitlines()
file.close()
print(lineB)

"""

file = open("addresses.txt", "r")
lineA = file.read().splitlines()
file.close()
print(lineA)
"""







"""
import csv
import sys

#input number you want to search
number = raw_input('Enter number to find\n')

#read csv, and split on "," the line
csv_file = csv.reader(open('test.csv', "r"), delimiter=",")

#loop through the csv list
for row in csv_file:
    #if current rows 2nd value is equal to input, print that row
    if number == row[1]:
         print (row)

"""