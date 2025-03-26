# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Define vaccination rates
V_rate=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
# Total population
N=10000
# Used to store the number of infected persons at each vaccination rate
I_data=[]

# SIR Model parameters
beta=0.3# Infection rate
gamma=0.05# Recovery rate

# Simulate SIR Dynamics for each vaccine coverage rate
for v in V_rate:
    V=int(N*v)# Number of people vaccinated
    S=N-1-V# Number of susceptible persons
    S=max(S,0)# Make sure S is not negative
    I=1# Number of initial infected persons
    R=0# Number of recovered persons

# The initialization array is used to store changes in S, I, and R
    S_array=[S]
    I_array=[I]
    R_array=[R]
# Simulate 1000 time steps
    for t in range (1000):
        infection_probability=beta*(I/N)# Infection probability
        recovery_probability=gamma# recovery probability
# Randomly determine the number of new infections
        new_infections=np.random.choice(range(2),S,p=[1-infection_probability,infection_probability]).sum()
# Randomly determine the number of new recoveries
        new_recoveries=np.random.choice(range(2),I,p=[1-recovery_probability,recovery_probability]).sum()
# Update the values of S, I, and R
        S-=new_infections
        S=max(S,0)
        S_array.append(S)

        I+=new_infections-new_recoveries
        I=max(I,0)
        I_array.append(I)

        R+=new_recoveries
        R=max(R,0)
        R_array.append(R)
# Add the number of infected people at current vaccination rates to I_data
    I_data.append(I_array)
# loting
plt.figure(figsize=(6,4),dpi=150)
colors = cm.viridis(np.linspace(0, 1, len(V_rate)))# Dynamic color mapping
for i, rate in enumerate(V_rate):
    plt.plot(I_data[i], color=colors[i], label=f'{int(rate*100)}%')# Use dynamic colors
    plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.legend(loc='upper right')
plt.savefig('SIR_model_with_different_vaccination_rates.png')
plt.show()
