# === LISTS ===

# 1. Create a list of 5 numbers
# 2. Access the first and last element
# 3. Access the last element using a negative index
# 4. Slice the middle 3 elements
# 5. Add a number to the end
# 6. Remove the first element
# 7. Iterate and print each element
# 8. Iterate with index
# 9. Reverse it
# 10. Check if a number is in it

list = [1,2,3,4,5,6,7]
# print(list[0], list[-1])  # first element

# middle = len(list) // 2
# print (list[middle - 1: middle + 2])

# list.append(8)
# print(list)
# list.remove(list[0])
# print(list)

# for i in list:
#     print(i)

# for i in range(len(list)):
#     print(list[i])


# index = len(list) - 1
# new_list = []
# while index >= 0:
#     new_list.append(list[index])
#     index -= 1
# print(new_list)

num = 3

if num in list:
    print("yes")