# Import the `pandas` module as "pd"
import pandas as pd

# Read in `road-accidents.csv`
car_acc = pd.read_csv('road-accidents.csv', comment='#', sep='|')

# Save the number of rows columns as a tuple
rows_and_cols = car_acc.shape
print('There are {} rows and {} columns.\n'.format(rows_and_cols[0], rows_and_cols[1]))

# Generate an overview of the DataFrame
car_acc_information = car_acc.info()
print(car_acc_information)

# Display the last five rows of the DataFrame
car_acc.tail()

print(car_acc)

# import seaborn and make plots appear inline
import seaborn as sns
#matplotlib inline

# import seaborn and make plots appear inline
import seaborn as sns
import matplotlib.pyplot as plt
#matplotlib inline

# Compute the summary statistics of all columns in the `car_acc` DataFrame
sum_stat_car = car_acc.describe()
print(sum_stat_car)

# Create a pairwise scatter plot to explore the data
sns.pairplot(sum_stat_car, height=0.5)
plt.show()

# Compute the correlation coefficent for all column pairs
corr_columns = car_acc.corr()
print(corr_columns)

