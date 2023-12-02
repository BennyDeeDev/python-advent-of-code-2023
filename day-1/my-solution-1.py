sum_array = []
sum = 0

with open('./day-1/input.txt', 'r') as file:
    for line in file:
        split_list = list(line)
        num_list = []
        for s in split_list:
            if s.isdigit():
                num_list.append(s)

        if len(num_list) == 1:
            firstNum = num_list[0]
            sum_array.append(f"{firstNum}{firstNum}")
        elif len(num_list) > 1:
            firstNum = num_list[0]
            lastNum = num_list[-1]
            sum_array.append(f"{firstNum}{lastNum}")

for s in sum_array:
    sum = int(sum) + int(s) 

print("The Solution sum_array is", sum_array)
print("The Solution sum is", sum)
