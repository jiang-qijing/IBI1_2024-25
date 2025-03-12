# Define the variable 'weight' to represent the person's weight in kilograms
weight = 50

# Define the variable 'height' to represent the person's height in meters
height = 1.7

# Calculate the BMI (Body Mass Index) using the formula: weight (kg) divided by height (m) squared
BMI = weight / (height ** 2)

# Check the value of BMI and print the corresponding health status
if BMI > 30:  # If BMI is greater than 30, the person is considered obese
    print("obese")
elif BMI < 18.5:  # If BMI is less than 18.5, the person is considered underweight
    print("underweight")
else:  # If BMI is between 18.5 and 30, the person is considered to have a normal weight
    print("normal")
