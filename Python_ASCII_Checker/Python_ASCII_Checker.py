# ASCII Value Checker

char = input("Enter a single character: ")

if len(char) == 1:
    print(f"The ASCII value of '{char}' is {ord(char)}")
else:
    print("Please enter exactly one character.")