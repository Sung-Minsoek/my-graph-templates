import pandas as pd
import matplotlib.pyplot as plt

# Parameters
FILE = "temp-line-graph-data.xlsx"
TITLE = "Test"
X = "Round"
Y = "Dynamic Layout Score"

# Font template
font = {
    'family': 'serif',
    'color': 'b',
    'weight': 'bold',
    'size': 14        
}

x = [1, 2, 3, 4]
minX = 0
maxX = 20

y = [1, 4, 9, 16]
minY = 0
maxY = 20

axis_boundary = [minX, maxX, minY, maxY]

# Import Data with Pandas
data = pd.read_excel(FILE)

x = data[X]
y = data[Y]

# Data
plt.plot(x, y)                  # Insert a data to plot.

# Axis
#plt.axis(axis_boundary)         # Set a total Axis boundary.
plt.xlabel(X, fontdict=font)       # Set lable of Axis.
plt.ylabel(Y, fontdict=font)
plt.grid()

# Save to pdf
#plt.savefig(TITLE+".pdf", format="pdf")

plt.show()
