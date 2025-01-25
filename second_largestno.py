
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

numbers.sort(reverse=True)

second_lar = numbers[1]

print("The 2nd largest number is:", second_lar)

