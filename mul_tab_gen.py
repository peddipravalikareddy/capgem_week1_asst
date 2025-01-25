def main():

    number=int(input("Enter a number to display it multiplication table: "))

    for n  in range(1,11):

        print(f"{number} * {n} = {int(number)*n}")  
main()