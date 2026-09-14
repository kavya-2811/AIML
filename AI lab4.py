import pandas as pd

# Display all columns without truncation
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Load the dataset
data = pd.read_csv(r"C:\Users\kavya\Downloads\workload_data.csv")

# Remove any unwanted empty columns (if present)
data = data.loc[:, ~data.columns.str.contains("^Unnamed")]

print("Training Dataset:\n")
print(data.to_string(index=False))

# Initialize the most specific hypothesis
hypothesis = ['0'] * (len(data.columns) - 1)

print("\nInitial Hypothesis:")
print(hypothesis)

# Apply Find-S Algorithm
for index, row in data.iterrows():

    print(f"\nProcessing Row {index + 1}:")
    print(row.to_list())

    # Consider only positive examples
    if row["High-Performance Edge"] == "Yes":

        # First positive example initializes the hypothesis
        if hypothesis[0] == '0':
            hypothesis = list(row.iloc[:-1])

        else:
            # Generalize attributes where values differ
            for i in range(len(hypothesis)):
                if hypothesis[i] != row.iloc[i]:
                    hypothesis[i] = '?'

    print("Current Hypothesis:", hypothesis)

print("\nFinal Specific Hypothesis:")
print(hypothesis)
