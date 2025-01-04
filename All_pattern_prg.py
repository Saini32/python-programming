# Pattern 1
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# Pattern 2
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# Output:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# Pattern 3
for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
# Output:
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

# Pattern 4
for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()
# Output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# Pattern 5
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()
# Output:
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

# Pattern 6
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
for i in range(4, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# Pattern 7
for i in range(1, 6):
    for j in range(5, i - 1, -1):
        print(j, end=" ")
    print()
# Output:
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

# Pattern 8 (same as Pattern 6)
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
for i in range(4, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# Pattern 9
for i in range(1, 6):
    for j in range(5, i - 1, -1):
        print(i, end=" ")
    print()
# Output:
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

# Pattern 10
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
# Output:
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

