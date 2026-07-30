import pandas as pd

# Load the dataset
data = pd.read_csv("workload_data.csv")

# Initialize hypothesis
hypothesis = None

print("Training Process:\n")

for i, row in data.iterrows():
    # Consider only positive examples
    if row["High-Performance Edge"] == "Yes":

        # Remove target column
        instance = row[:-1].tolist()

        # Initialize with first positive example
        if hypothesis is None:
            hypothesis = instance

        # Generalize hypothesis
        else:
            for j in range(len(hypothesis)):
                if hypothesis[j] != instance[j]:
                    hypothesis[j] = "?"

        print(f"After processing row {i+1}:")
        print(hypothesis)
        print()

print("Final Specific Hypothesis:")
print(hypothesis)