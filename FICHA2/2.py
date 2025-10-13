lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

sum_even = 0

for i in range(lower, upper + 1):
    if i % 2 == 0:
        sum_even += i

print(f"The sum of even numbers in the range = {sum_even}")
