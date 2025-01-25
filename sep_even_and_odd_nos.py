#take numbers with space and convert into list

numbers=input("enter numbers separated by space: ").split()

#separating numbers

even_num=[int(num) for num in numbers if int(num)%2==0]
odd_num=[int(num) for num in numbers if int(num)%2!=0]
print("Even numbers are: ", even_num)
print("Odd numbers are: ", odd_num)
