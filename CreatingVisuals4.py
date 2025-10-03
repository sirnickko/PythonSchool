import matplotlib.pyplot as plt

labels = 'A', 'B', 'C'
sections = [56, 66, 24]
colors = ['c', 'g', 'y']
plt.pie(sections, labels=labels, colors=colors,startangle=90,explode = (0, 0.1, 0),autopct = '%1.2f%%')
plt.title('GRADES FOR DATA SCIENCE')
plt.show()