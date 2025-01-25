name=input()

Sub_1=int(input("Enter the marks in subject 1 : "))
Sub_2=int(input("Enter the marks in subject 2 : "))
Sub_3=int(input("Enter the marks in subject 3 : "))
Sub_4=int(input("Enter the marks in subject 4 : "))
Sub_5=int(input("Enter the marks in subject 5 : "))

Total_marks=Sub_1+Sub_2+Sub_3+Sub_4+Sub_5
print("Your Total marks are : ",Total_marks)
Percentage=(Total_marks/500)*100
print("Your Percentage is : ",Percentage)

if(Total_marks>=(80/100)*500):
    print("Grade A")

elif(Total_marks<=(80/100)*500 and Total_marks>=(60/100)*500):
    print("Grade B")

elif(Total_marks<=(60/100)*500 and Total_marks>=(40/100)*500):
    print("Grade C")
    
else:
    print("fail")



