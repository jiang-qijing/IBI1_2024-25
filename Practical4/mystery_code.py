# What does this piece of code do?#
# Answer:Roll two dice until they have the same number of points, and record the number of attempts.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5（both inclusive)
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress = 0  # progress is used to record the number of attempts, initialized to 0
# This is an infinite loop because progress is always non-negative (it increments in each iteration without any decrement).
# It can also be written as `while True`.
while progress >= 0:
    progress += 1  # Increment the progress value by 1 in each iteration to record the current attempt number

    first_n = randint(1, 6)  # Generate a random number between 1 and 6 (inclusive) for the first die
    second_n = randint(1, 6)  # Generate a random number between 1 and 6 (inclusive) for the second die

    # Check if the numbers on both dice are the same
    if first_n == second_n:
        print(progress)  # Print the current attempt number (progress)
        break  # Exit the loop using `break`

