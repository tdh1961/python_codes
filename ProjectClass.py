#Write a code that will take a string from user , and display how many characters are in that string
"""
my_string = input("enter a string:  ")
l = len(my_string.strip())
print(f'The string entered is {l} characters')


#Write a code that will take a string from user and if the string has less than 4 charactars, it should display "invalid entry" and 
#if the characters number in the string is more that 4 , it should display "valid entry"

my_string = input('enter a string:  ')
l = len(my_string)
if l < 4:
    print('invalid entry')
else:
    print('valid entry') 

#Username and password of an application is admin. Write a code that takes two inputs from user username and password and tell the user
#"wrong username or password" if the username and password entered is not admin; and if it is admin and admin, it display "successfully login"    

a = input('Username: ')
b = input('Password: ')
if a == b ==  'admin':
    print('successfully login')
else:
    print('wrong username or password')

#Write a program to take users zip code and check if the input data was a digit number with 5 digits. 
#(a good zip code has 5 digits) if it is good , display "your entry is valid" if not , display "please enter a valid zip code"
    
zip_zip = input("enter you zip code: ")
digit = len(zip_zip)
print(digit)


if  digit == 5 and zip_zip.isdigit():

    print("valid entry")
else:
    print("please enter a valid entry")

"""
try:
    # Take two integers as input from the user
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

    # Calculate the sum of the two integers
    sum_of_integers = num1 + num2

    # Print the sum
    print("The sum of", num1, "and", num2, "is:", sum_of_integers)

except ValueError:
    print("Invalid input! Please enter integers only.")