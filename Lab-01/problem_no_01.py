# Find the smallest number in a list using a loop
n = int(input("Enter the number of value in list : "))

n_list = []

for i in range(n) :
    value = int(input(f"Enter the value no {i+1} : "))
    n_list.append(value)

# find the small value.
small = n_list[0]
for i in range(n) :
    if small > n_list[i] :
        small = n_list[i]

print("The small number is : " + str(small)); 