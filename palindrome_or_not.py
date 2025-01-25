def is_palindrome(value):
    # Converting to string to handle both numbers and strings
    value_str = str(value)
    return value_str == value_str[::-1]

while True:
    value = input("Enter a string or number (or 'exit' to quit): ")
    
    if value == 'exit':
        break
    
    if value == value[::-1]:
        print("Palindrome!")
    else:
        print("Not a palindrome!")
