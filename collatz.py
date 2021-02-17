# Program that asks the user to input any positive integer
# If it is even, divide it by two
# If it is odd, multiply it by three and add one
# Author: Sheila Bambrick
# The program will end if the current value is one
# Reference 

number = int(input('Enter a number:'))  

while number > 1:  
    if number % 2 == 0:  
        number  = number / 2 
        print(number)  
    else:  
        number = number * 3 + 1  
        print(number)

