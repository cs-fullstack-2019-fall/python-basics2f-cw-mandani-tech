# # Python Basics: Math and String Formatting
#
# ### Problem 1:
# Write some Python code that has three variables called ```greeting```, ```my_name```, and ```my_age```.
# Intialize each of the 3 variables with an appropriate value, then print out the example below using the 3 variables
# and two different approaches for formatting Strings.
#
# 1) Using concatenation and the ```+``` and 2) Using an ```f-string```. Sample output:
#
# ```
# YOUR_GREETING_VARIABLE YOUR_NAME_VARIABLE!!! I hear that you are YOUR_MY_AGE_VARIABLE today!
# ```
# greeting="Hello !!"
# my_name="Hamida"
# my_age="31"
#
# complete_string= (greeting + " " + my_name + "!!!" + "I hear that you are " + my_age + " today!")
# print(complete_string)
#
# complete_string_f_string= f'{greeting} {my_name} !!! I hear that you are {my_age} today !'
# print(complete_string_f_string)


# ### Problem 2:
# Write some Python code that asks the user for a secret password. Create a loop that quits with the user's quit word.
# If the user doesn't enter that word, ask them to guess again.
#
secret_password= input("Enter a secret password: ")
guess_password= input("Guess the secret password: ")
while(guess_password != 'q' and secret_password != guess_password):
    guess_password= input("Wrong !! Enter the secret password: ")
print("You got it !")

#

# ### Problem 3:
# Write some Python code using ```f-strings``` that prints 0 to 50 three times in a row (vertically).
# ```
# 1 1 1
# 2 2 2
# 3 3 3
# 4 4 4
# 5 5 5
# .
# .
# .
# ```
for column in range (0,51):
    number_col = f'  {column}   {column}   {column}'
    print(number_col)


# ### Problem 4:
# Write some Python code that create a random number and stores it in a variable. Ask the user to guess the random number.
# Keep letting the user guess until they get it right, then quit.
import random
random_number= random.randint(1,10)
print(random_number)
guess_number =input("Guess the random number: ")
while(guess_number!= 'q' and int(guess_number)!= random_number):
    guess_number =input("Try again Guess the random number: ")




#
# ### Challenge
# Write some Python code to ask the user to create a number for the computer to guess between 1 - 10000.
# Write the code so that the computer guesses random numbers between 1 - 10000 and
# will keep guessing until the computer guesses the number correctly.
# Once the computer guesses the random number, alert the user with an alert box that
# displays how many guesses it took to guess the random number.
import random
user_number= random.randint(1,100000)
random_number=0
while(random_number!= user_number):
    random_number= random.randint(1,100000)
    if(random_number== user_number):
        print(random_number)
