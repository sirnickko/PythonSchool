import matplotlib.pyplot as plt

X1 = ["BSE","BBIT", "BSCIT", "BCS", "BCM"]
Y1= [200, 400, 250, 180, 180]
plt.bar(X1, Y1, label="students", color='y')
plt.plot()
plt.xlabel("COURSE")
plt.ylabel("NUMBER OF STUDENTS")
plt.title("INTAKE AS PER THE COURSES")
plt.grid(True)
plt.legend()
plt.show()