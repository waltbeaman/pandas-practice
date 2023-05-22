import pandas as pd

df = pd.read_csv('titanic.csv')


def print_stats():
    # Get the first 5 rows of the dataframe.
    first_five_rows = df.head()
    print(first_five_rows)

    # Count rows.
    row_count = df.shape[0]
    print("Row count: " + str(row_count))

    # Get a count of null values for each column.
    count_nulls = df.isnull().sum()
    print(count_nulls)


print_stats()

# Drop the columns with null values.
# TODO: Should this be assigned to a conditional? (i.e. if nulls > 10% of total rows)
df = df.drop(['cabin', 'boat', 'body', 'home.dest'], axis=1)

print_stats()

# Drop rows with null values.
df = df.dropna()

print_stats()
