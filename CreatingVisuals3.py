# importing the necessary libraries and modules
import matplotlib.pyplot as plt
import numpy as np
# creating the data values for the vertical y and horisontal x axis
x = np.array(["BSE","BBIT", "BSCIT", "BCS", "BCM"])
y = np.array([200, 400, 250, 180, 180])
# using the pyplot.bar funtion
plt.bar(x,y)
plt.plot()
plt.xlabel("COURSE")
plt.ylabel("NUMBER OF STUDENTS")
plt.title("INTAKE AS PER THE COURSES")
# to show our graph
plt.show()