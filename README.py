# Kockice
import numpy as np
import matplotlib.pyplot as plt
import random

list_rand = []
for i in range (0,1000):
    a=random.randint(1,6)
    b=random.randint(1,6)
    c=a+b
    list_rand.append(c)
    
list_rand2 = []
for i in range (0,1000):
    a=random.randint(1,6)
    b=random.randint(1,6)
    c=random.randint(1,6)
    d=a+b+c
    list_rand2.append(d)
    
values, counts = np.unique(list_rand, return_counts=True) 
plt.plot (values, counts, color='r', label='2')
values, counts = np.unique(list_rand2, return_counts=True) 
plt.plot (values, counts, color='b', label='3')
plt.legend()
