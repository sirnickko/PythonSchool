import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y1 = [2,4,6,8,10,12,14,16]
y2 = [2,1,6,20,14,13,15,18]

plt.plot(x,y1, label = "SEMESTER 1")
plt.plot(x,y2, label = "SEMESTER 2")
plt.plot()

plt.xlabel('X-AXIS')
plt.ylabel('Y-AXIS')
plt.title('DISTRIBUTION PER SEMESTER')
plt.legend()
plt.show()
