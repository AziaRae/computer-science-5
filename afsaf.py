num = int(input("Enter a non-negative integer: "))
original_num = num

sum_of_digits = 0
for digit in str(num):
    sum_of_digits += int(digit)

while sum_of_digits >= 10:
    num = sum_of_digits
    sum_of_digits = 0
    for digit in str(num):
        sum_of_digits += int(digit)    

print(f"The digital root of {original_num} is {sum_of_digits}")