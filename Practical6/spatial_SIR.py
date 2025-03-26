#For each time step t from 0 to num_time_steps:
    #1. Create a temporary array new_population with the same size as the population to store the updated status.
    #2. Traverse each location in the population (i, j):
        #a. If (i, j) is infected (population[i, j] == 1) :
            #- Change the position to convalescent with probability gamma (new_population[i, j] = 2).
            #- Otherwise, remain infected (new_population[i, j] = 1).
            #- Find 8 neighbors of the location (up, down, left, right and diagonal).
            #- For each neighbor (ni, nj):
                #- Check whether the neighbor is within the grid range.
                #- If the neighbors are susceptible (population[ni, nj] == 0) :
                    #- Turn neighbors into infected persons with probability beta (new_population[ni, nj] = 1).
        #b. If (i, j) is susceptible or recovered, copy the status directly to new_population.
    #3. Update population = new_population.   
    #4. Add a title to display the current time step.
    #5. Display the heat map.

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Initialize parameters
population_size = (100, 100)
beta = 0.3# Infection probability
gamma = 0.05# Recovery rate
num_time_steps = 100# Number of time steps

# Initialize the population, all susceptible
population = np.zeros(population_size, dtype=int)

# Randomly select an initial infection point
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1# Set this point to infected

# Simulation process
for t in range(num_time_steps):
    new_population = population.copy()
    
# Walk through each location
    for i in range(population_size[0]):
        for j in range(population_size[1]):
            if population[i, j] == 1:# The current location is infected
# Check for recovery
                if np.random.rand() < gamma:
                    new_population[i, j] = 2# Become a recovered person
                else:
# Infect neighbors
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            if di == 0 and dj == 0:
                                continue# Skip itself
                            ni, nj = i + di, j + dj
                            if 0 <= ni < population_size[0] and 0 <= nj < population_size[1]:
                                if population[ni, nj] == 0:# Neighbors are susceptible
                                    if np.random.rand() < beta:
                                        new_population[ni, nj] = 1# Infect neighbors
    population = new_population# Update the population
    
# Ploting
    if t==10 or t==50 or t==99:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.colorbar(ticks=[0, 1, 2], label='State')
        plt.title(f'Time Step {t}')
plt.show()
