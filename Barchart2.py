import matplotlib.pyplot as plt

x = ["MAT","ENG","KIS","SCI","SOC"]
y = [67,88,24,94,56]

plt.bar(x,y, label = "grades", color = "green")
plt.plot()

plt.xlabel('SUBJECTS')
plt.ylabel('GRADES')

plt.title('Grades vs Subject')
plt.grid(True)
plt.legend()
plt.show()