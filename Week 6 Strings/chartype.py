char = input("Enter a character: ")
if ord("z") >= ord(char) >= ord("a"):
    print("{} is a lower case letter.".format(char))
elif ord("Z") >= ord(char) >= ord("A"):
    print("{} is an upper case letter.".format(char))
elif ord("9") >= ord(char) >= ord("0"):
    print("{} is a digit.".format(char))
else:
    print("{} is a non-alphanumeric character.".format(char))