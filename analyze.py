import numpy as np
import matplotlib.pyplot as plt
import math

file_name = input('data file?')
data = np.load(file_name,allow_pickle=True)
x = []
y = []
fin_x = []
fin_y = []
counter = int(input('intervals?'))
for i in range(len(data)):
    x.append(data[i][0])
    y.append(data[i][1]+200)
    if (i+1) % counter == 0:
        last_x = np.mean(x)
        last_y = np.mean(y)
        x = []
        y = []
        fin_x.append(last_x)
        fin_y.append(last_y)
        plt.scatter(last_x,last_y)
        
plt.show()
np.save('x_values',fin_x)
np.save('y_values',fin_y)
