
my_list = []
print("1. Empty list created:", my_list)

# 1. Append the items to my_list variable:
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("2. After appending elements:", my_list)

# 2. Insert the value 15 at the second position in the list
my_list.insert(1, 15)  # Inserts 15 at index 1 (second position)
print("3. After inserting 15 at second position:", my_list)

# 3. Extend my_list on another list:
my_list.extend([50, 60, 70])
print("4. After extending with [50, 60, 70]:", my_list)

# 4. Remove the last element from my_list
last_element = my_list.pop()  # Remove and return the last element
print(f"5. Removed the last element: {last_element}")
print("   Updated list:", my_list)

# 5. Sort my_list in ascending order
my_list.sort()
print("6. After sorting in ascending order:", my_list)

# 6. Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print(f"7. Index of value 30 in my_list: {index_of_30}")

# Print the final list
print("\nFinal my_list:", my_list)