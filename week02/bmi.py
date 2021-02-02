# This program calculates a person's BMI based on their inputs
# Written by Sheila Bambrick
# Take inputs from user (weight and height)

height = float(input("enter height in cms:"))
weight = float(input("enter weight in kg:"))

# The formula for calculating BMI is 
bmi = weight/((height/100)*(height/100))

# BMI calculation
print ("Your BMI is:", round(bmi,2))

