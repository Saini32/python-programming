# Define a list of names
Names = ["Tushar", "Sonali", "Yeshu", "Vedu"]

# Display list items
print("Display list items:")
for e in Names:
    print(e)

# Display list items with their index
print("\nDisplay list items and index:")
for i, e in enumerate(Names):
    print(i, e)

# Display list items using range
print("\nDisplay list items using range:")
for i in range(len(Names)):
    print(f"Index {i}: {Names[i]}")

# List sum and average
s = [11, 22, 33]  # Example numerical list
total = sum(s)  # Calculate the sum of the list
avg = float(total) / len(s)  # Calculate the average

print("\nList:", s)
print("Total of list elements:", total)
print("Average of list elements:", avg)

# Joining list items
print("\nList join() example:")
s2 = ", ".join(Names)  # Join list items into a single string separated by ", "
print(s2)
