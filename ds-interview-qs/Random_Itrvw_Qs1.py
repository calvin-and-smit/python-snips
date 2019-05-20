"""
Write a program that squares an integer and prints the result.
Input:Your program should read lines from standard input. 
Each line will contain a positive integer.Output:For each line of input, print to 
standard output the square of the number. Print out each result on a new line.
"""
import sys
for line in sys.stdin:
    print(int(line)**2)
