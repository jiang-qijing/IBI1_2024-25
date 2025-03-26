# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
N=10000# Total population size
S=N-1# Initial number of susceptible individuals
I=1# Initial number of infected individuals
R=0# Initial number of recovered individuals
beta=0.3# Infection rate
gamma=0.05# Recovery rate

# Initialize lists to store the number of susceptible, infected, and recovered individuals over time
S_array=[S]
I_array=[I]
R_array=[R]

# Simulation loop
for t in range (1000):
    infection_probability=beta*(I/N)# Calculate the infection probability
    recovery_probability=gamma# Calculate the recovery probability
    new_infections=np.random.choice(range(2),S,p=[1-infection_probability,infection_probability]).sum() # Determine the number of new infections
    new_recoveries=np.random.choice(range(2),I,p=[1-recovery_probability,recovery_probability]).sum()# Determine the number of new recoveries
# Update the number of susceptible, infected, and recovered individuals
    S-=new_infections
    S=max(S,0)
    S_array.append(S)

    I+=new_infections-new_recoveries
    I=max(I,0)
    I_array.append(I)

    R+=new_recoveries
    R=max(R,0)
    R_array.append(R)
# Plotting
plt.figure(figsize=(6,4),dpi=150)
plt.plot(S_array,label='susceptible')
plt.plot(I_array,label='infected')
plt.plot(R_array,label='recovered')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend(loc='upper right')
plt.savefig('SIR_model.png')
plt.show()
