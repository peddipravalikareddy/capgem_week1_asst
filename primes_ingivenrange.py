#check if number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Get input from the user
start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))

for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")
