n = int(input("Enter the number: "))
reverse = input("Reverse pattern? (yes/no): ").lower() == 'yes'

for i in range(n, 0, -1) if reverse else range(1, n + 1):
    print('*' * i)
