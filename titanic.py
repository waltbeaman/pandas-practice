import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('titanic.csv')


def print_stats():
    # Get the first 5 rows of the dataframe.
    first_five_rows = df.head()
    print(first_five_rows)

    # Count rows.
    row_count = df.shape[0]
    print("Row count: " + str(row_count))

    # Get a count of null values for each column.
    # count_nulls = df.isnull().sum()
    # print(count_nulls)


#############################
#      Clean the Data       #
#############################

# Drop the columns with null values.
# TODO: Should this be assigned to a conditional? (i.e. if nulls > 10% of total rows)
df = df.drop(['cabin', 'boat', 'body', 'home.dest'], axis=1)

# Drop rows with null values.
df = df.dropna()

# Print cleaned data to examine.
# print_stats()

#############################
# Exploratory Data Analysis #
#############################

# Use describe() to get a summary of the numerical data.
print(df.describe())

# Visualize the data.
sns.countplot(x='survived', data=df)
plt.title('Survival Count')
plt.show()

plt.hist(x='age', data=df, bins=20)
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Age Distribution')
plt.show()

plt.scatter(x='age', y='fare', data=df)
plt.xlabel('Age')
plt.ylabel('Fare')
plt.title('Age vs. Fare')
plt.show()


# Correlation matrix.
numeric_columns = df.select_dtypes(include=['int64', 'float64'])
corr_matrix = numeric_columns.corr()

# Heatmap.
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
