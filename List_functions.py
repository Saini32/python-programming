# Define a list
st = [13, 22, 8, 27, 11]

# Sort in descending order
st.sort(reverse=True)
print("Sorted list (in Descending):", st)

# Count occurrences of a value
print("st.count(21):", st.count(21))  # Count occurrences of 21

# Length of the list
print("len(st):", len(st))

# Minimum and maximum values in the list
print("min(st):", min(st))
print("max(st):", max(st))

# Insert an element at a specific index
st.insert(2, -1)
print("After inserting -1 at index 2:", st)

# Append an element to the end of the list
st.append(4)
print("After appending 4:", st)

# Index of a specific value
if 8 in st:
    print("Index of 8:", st.index(8))
else:
    print("8 is not in the list.")

# Remove an element from the list
if 8 in st:
    st.remove(8)
    print("After removing 8:", st)
else:
    print("8 is not in the list, cannot remove.")

# Reverse the list
st.reverse()
print("After reversing the list:", st)

# Sort the list in ascending order
st.sort()
print("Sorted list (in Ascending):", st)

# Pop the last element
popped_value = st.pop()
print("After popping the last element:", st)
print("Popped value:", popped_value)

# Clear the list
st.clear()
print("After clearing the list:", st)
