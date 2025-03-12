#Method1
# Using a for loop to calculate the sum of the first 10 natural numbers
# The formula used here is the sum of an arithmetic sequence: (n * (n + 1)) / 2
for i in range(1, 11):  # Loop from 1 to 10 (inclusive)
    print((1 + i) * i / 2)  # Calculate and print the sum of the first i natural numbers


#Method2
# Initialization of variables
i = 0  # Counter variable
n = 10  # Number of terms in the sequence
a1 = 1  # First term of the arithmetic sequence
d = 1  # Common difference of the arithmetic sequence
sum_sequence = 0  # Variable to store the sum of the sequence

# Using a while loop to calculate the sum of the first n terms of the arithmetic sequence
while True:
    i += 1  # Increment the counter
    current_term = a1 + (i - 1) * d  # Calculate the current term using the formula: a1 + (i-1)*d
    sum_sequence += current_term  # Add the current term to the sum

    # Using an f-string to format the output
    # f-string allows embedding expressions inside string literals, using curly braces {}
    print(f'The number is {i}, the current term is {current_term}, the sum of sequence is {sum_sequence}.')

    if i >= n:  # Check if the number of terms has reached the desired count
        break  # Exit the loop if the condition is met
