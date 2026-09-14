import math

# Training dataset
data = [
    {"Day": "D1", "Outlook": "Sunny", "Temperature": "Hot", "Humidity": "High", "Wind": "Weak", "Play Tennis": "No"},
    {"Day": "D2", "Outlook": "Sunny", "Temperature": "Hot", "Humidity": "High", "Wind": "Strong", "Play Tennis": "No"},
    {"Day": "D3", "Outlook": "Overcast", "Temperature": "Hot", "Humidity": "High", "Wind": "Weak", "Play Tennis": "Yes"},
    {"Day": "D4", "Outlook": "Rain", "Temperature": "Mild", "Humidity": "High", "Wind": "Weak", "Play Tennis": "Yes"},
    {"Day": "D5", "Outlook": "Rain", "Temperature": "Cool", "Humidity": "Normal", "Wind": "Weak", "Play Tennis": "Yes"},
    {"Day": "D6", "Outlook": "Rain", "Temperature": "Cool", "Humidity": "Normal", "Wind": "Strong", "Play Tennis": "No"},
    {"Day": "D7", "Outlook": "Overcast", "Temperature": "Cool", "Humidity": "Normal", "Wind": "Strong", "Play Tennis": "Yes"},
    {"Day": "D8", "Outlook": "Sunny", "Temperature": "Mild", "Humidity": "High", "Wind": "Weak", "Play Tennis": "No"},
    {"Day": "D9", "Outlook": "Sunny", "Temperature": "Cool", "Humidity": "Normal", "Wind": "Weak", "Play Tennis": "Yes"},
    {"Day": "D10", "Outlook": "Rain", "Temperature": "Mild", "Humidity": "Normal", "Wind": "Weak", "Play Tennis": "Yes"},
    {"Day": "D11", "Outlook": "Sunny", "Temperature": "Mild", "Humidity": "Normal", "Wind": "Strong", "Play Tennis": "Yes"},
    {"Day": "D12", "Outlook": "Overcast", "Temperature": "Mild", "Humidity": "High", "Wind": "Strong", "Play Tennis": "Yes"},
    {"Day": "D13", "Outlook": "Overcast", "Temperature": "Hot", "Humidity": "Normal", "Wind": "Weak", "Play Tennis": "Yes"},
    {"Day": "D14", "Outlook": "Rain", "Temperature": "Mild", "Humidity": "High", "Wind": "Strong", "Play Tennis": "No"}
]

target = "Play Tennis"
attributes = ["Outlook", "Temperature", "Humidity", "Wind"]


# Calculate entropy
def entropy(rows):
    total = len(rows)

    if total == 0:
        return 0

    counts = {}

    for row in rows:
        label = row[target]
        counts[label] = counts.get(label, 0) + 1

    result = 0

    for count in counts.values():
        probability = count / total
        result -= probability * math.log2(probability)

    return result


# Calculate information gain
def information_gain(rows, attribute):
    total_entropy = entropy(rows)
    total = len(rows)

    values = set(row[attribute] for row in rows)

    weighted_entropy = 0

    for value in values:
        subset = [row for row in rows if row[attribute] == value]
        weighted_entropy += (len(subset) / total) * entropy(subset)

    return total_entropy - weighted_entropy


# Build the ID3 decision tree
def id3(rows, remaining_attributes):
    labels = [row[target] for row in rows]

    # If all records belong to one class
    if len(set(labels)) == 1:
        return labels[0]

    # If no attributes remain, return the majority class
    if not remaining_attributes:
        return max(set(labels), key=labels.count)

    # Select the attribute with highest information gain
    best_attribute = max(
        remaining_attributes,
        key=lambda attribute: information_gain(rows, attribute)
    )

    tree = {best_attribute: {}}

    values = set(row[best_attribute] for row in rows)

    for value in values:
        subset = [
            row for row in rows
            if row[best_attribute] == value
        ]

        new_attributes = [
            attribute for attribute in remaining_attributes
            if attribute != best_attribute
        ]

        tree[best_attribute][value] = id3(subset, new_attributes)

    return tree


# Print the decision tree neatly
def print_tree(tree, indent=""):
    if not isinstance(tree, dict):
        print(indent + "→ " + tree)
        return

    attribute = next(iter(tree))
    print(indent + attribute + "?")

    for value, subtree in tree[attribute].items():
        print(indent + "├── " + value)
        print_tree(subtree, indent + "│   ")


# Main program
print("ENTROPY OF COMPLETE DATASET:")
print(f"{entropy(data):.3f}")

print("\nINFORMATION GAIN:")
for attribute in attributes:
    gain = information_gain(data, attribute)
    print(f"{attribute}: {gain:.3f}")

tree = id3(data, attributes)

print("\nFINAL ID3 DECISION TREE:")
print_tree(tree)