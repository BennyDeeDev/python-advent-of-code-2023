sum_array = []
sum = 0

string_numbers = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}

with open('./day-1/input.txt', 'r') as file:
    for line in file:
        split_list = list(line.strip())
        num_list = []

        for i in range(len(split_list)):
            c = split_list[i]

            if c.isdigit():
                num_list.append(c)                
            else:
                j = i
                for j in range(len(split_list)):
                    strNumber = string_numbers.get(''.join(split_list[i:j+1]))
                    if strNumber is not None:
                        num_list.append(str(strNumber))   
                        i = j   
                        break
            
        if len(num_list) == 1:
            firstNum = num_list[0]
            sum_array.append(f"{firstNum}{firstNum}")
        elif len(num_list) > 1:
            firstNum = num_list[0]
            lastNum = num_list[-1]
            sum_array.append(f"{firstNum}{lastNum}")

for c in sum_array:
    sum = int(sum) + int(c) 

print("The Solution sum_array is", sum_array)
print("The Solution sum is", sum)
