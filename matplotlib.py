
import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]

pop = [2.519, 3.692, 5.263, 6.972]

# Line Plot
plt.plot(year,pop)

# Scatter Plot
plt.scatter(year,pop)

# Convert Axis-X to Logarithmic
plt.convertx('log')
  
  
# Display the plot
  plt.show()
  
