

"""

Filename: Spike_and_burst_of_neuron_different_parameters.py
Name: Khang Ly 
Date: February 29th, 2024
Description:
    Create a map for different scenario of spiking and bursting of the neuron, 
    with different value of a, o, and u
        In this script, o = 0.2 and u = 0.01

"""


import matplotlib.pyplot as plt 

# Set the value of parameters a, sigma (o), and meu (u) 
a = 3.5
o = 0.2
u = 0.01
 

X = []
Y = []

# Give x and y a value as the initial conditions

x = -1.2
y = -3.9

# Define a function to represent f(x,y)

def nonlinear_function(a,x,y):
    if x <= 0:
        return (a / (1-x)) + y
    elif x < (a+y):
        return (a+y)
    else:
        return -1 
   
# Create a for loop to get rid of the transient

for n in range(10000):      
    print(n,x,y)
    x1 = nonlinear_function(a, x, y)
    y1 = y - u*(x+1) + (u*o)
    
    x = x1
    y = y1
    
# Create another for loop to plot the map without the transient

for n in range(10000):
    print(n,x,y)
    x1 = nonlinear_function(a, x, y)
    y1 = y - u*(x+1) + (u*o)
    
    X.append(x1)
    Y.append(y1)
    
    x = x1
    y = y1

# Plot the map

#plt.plot(X,Y,marker='.')
#plt.scatter(0,0)
fig, (ax1) = plt.subplots(1, 1, figsize=(16, 9))
                               #sharex=True)
ax1.plot(X,Y)#',k', alpha=.25)

plt.plot(x, y1, label='o = 0.2, u = 0.01')  # Label for the first line

# Increase the size of tick labels on both x and y axes
plt.xticks(fontsize=25)  # Adjust the fontsize as needed
plt.yticks(fontsize=25)  # Adjust the fontsize as needed

# Adding labels and title
plt.xlabel('x', fontsize=25)  # Adjust the fontsize as needed
plt.ylabel('y', fontsize=25)  # Adjust the fontsize as needed
plt.title('Loop with o = 0.2 & u = 0.01', fontsize=30)  # Adjust the fontsize as needed

plt.legend(fontsize = 25) # Adjust the fontsize as needed 



