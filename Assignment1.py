import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr']
searches = [60, 65, 70, 75]
direct = [80, 85, 90, 82]
social = [70, 75, 80, 60]

x = np.arange(len(months))
width = 0.25

# Plot
fig, ax = plt.subplots()
ax.bar(x - width, searches, width, label='Searches', color='blue')
ax.bar(x, direct, width, label='Direct', color='orange')
ax.bar(x + width, social, width, label='Social Media', color='yellow')

# Labels and Title
ax.set_ylabel('Visitors')
ax.set_xlabel('Months')
ax.set_title('Visitors by Web Traffic Sources')
ax.set_xticks(x)
ax.set_xticklabels(months)
ax.legend()

plt.tight_layout()
plt.show()