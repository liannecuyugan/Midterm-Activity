my_list = []

# Write your code here
for i in range(1, 10):
    my_list.append(i)

print("Original list:", my_list)
print("Length of list:", len(my_list))

y = 1
for x in range(len(my_list)):
    if x < len(my_list):
        if my_list[x] == y:
            # my_list.remove(my_list[x])
            del my_list[x]
        else:
            y = y + 1
    else:
        break

print("The list with unique elements only.")
print(my_list)