# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Initialize parameters
beta=0.3# Infection probability
gamma=0.05# Recovery probability
vaccination_rate=0.2# Proportion of the population that is vaccinated

# Make array of all susceptible population
population=np.zeros((100,100))

# Randomly select an initial infection point
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1# Set this point to infected

# Vaccinate a proportion of the population
num_vaccinated=int(vaccination_rate*10000)
vaccinated_indices=np.random.choice(np.arange(10000),num_vaccinated,replace=False)
for index in vaccinated_indices:
    i,j=divmod(index,(100,100)[1])
    population[i,j]=3# Assign vaccinated state

# Simulation loop
for t in range(100):
    new_population=population.copy()
    for i in range((100,100)[0]):
        for j in range((100,100)[1]):
            if population[i,j]==1:# If the individual is infected
                if np.random.rand()<gamma:# Check if the individual recovers
                    new_population[i,j]=2
                else:
                    for di in [-1,0,1]:# Check all neighbors
                        for dj in [-1,0,1]:
                            if di==0 and dj==0:# Skip the individual itself
                                continue
                            ni,nj=i+di,j+dj
                            if 0<=ni<(100,100)[0] and 0<=nj<(100,100)[1]:# Check bounds
                                if population[ni,nj]==0:# If the neighbor is susceptible
                                    if np.random.rand()<beta:# Check if the neighbor gets infected
                                        new_population[ni,nj]=1
    population=new_population# Update the population

# Plotting
    if t==10 or t==50 or t==99:
        plt.figure(figsize=(6,4),dpi=150)
        plt.imshow(population,cmap='viridis',interpolation='nearest')
        plt.colorbar(ticks=[0,1,2,3],label='State',boundaries=[-0.5,0.5,1.5,2.5,3.5])
        plt.title(f'Time Step {t}')
        plt.show()
