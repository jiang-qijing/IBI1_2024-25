# Define variable 'a' with a value of 15
a = 15

# Define variable 'b' with a value of 75
b = 75

# Calculate the sum of 'a' and 'b' and store it in 'c'
c = a + b

# Define variable 'd' with a value of 90
d = 90

# Define variable 'e' with a value of 5
e = 5

# Calculate the sum of 'd' and 'e' and store it in 'f'
f = d + e

# Compare the values of 'c' and 'f'
if c < f:  # Check if 'c' is less than 'f'
    print("walk to the bus stop and take the bus directly to their office is quicker")
else:  # If 'c' is not less than 'f'
    print("drive to a nearby car park and then walk the final stage is quicker")


#Answer:walk to the bus stop and take the bus directly to their office is quicker


# Create two Boolean variables X and Y
X = True   # X is initialized to True
Y = False  # Y is initialized to False

# Create a new variable W which represents the Boolean expression 'both X and Y'
W = X and Y  # W will be True only if both X and Y are True

# Print the value of W
print(f"W: {W}")
# X | Y | W (X and Y)
# -------------------
# T | T | T
# T | F | F
# F | T | F
# F | F | F
