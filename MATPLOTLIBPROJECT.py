import matplotlib.pyplot as plt
import numpy as np

# Sample data
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])
sales = np.array([10000, 12000, 8000, 15000, 9000, 11000])
expenses = np.array([8000, 9000, 10000, 11000, 12000, 13000])

# Plot the data
plt.plot(months, sales, label='Sales')
plt.plot(months, expenses, label='Expenses')

# Set the title and axis labels
plt.title('Sales and Expenses by Month')
plt.xlabel('Month')
plt.ylabel('Amount (USD)')

# Add a legend
plt.legend()

# Display the plot
plt.show()
