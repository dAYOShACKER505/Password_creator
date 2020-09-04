
# Author =dAYOShACKER 
# VERSION = 1.0 




import os
import random
import string
from termcolor import colored

# to clear the screen
os.system("clear")

# input
input(colored("Press enter to continue", "green"))

# to clear the screen
os.system("clear")

print("\n")

print("\t\t    #DevilanD")

# logo


print(colored("{__       {__      {_       {__     {__      {_       {__   {__        {_       {__","red"))      
print(colored("{_ {__   {___     {_ __     {__     {__     {_ __     {__  {__        {_ __     {__","yellow"))     
print(colored("{__ {__ { {__    {_  {__    {__     {__    {_  {__    {__ {__        {_  {__    {__","green"))     
print(colored("{__  {__  {__   {__   {__   {______ {__   {__   {__   {_ {_         {__   {__   {__","red"))     
print(colored("{__   {_  {__  {______ {__  {__     {__  {______ {__  {__  {__     {______ {__  {__","yellow"))      
print(colored("{__       {__ {__       {__ {__     {__ {__       {__ {__   {__   {__       {__ {__","green"))      
print(colored("{__       {__{__         {__{__     {__{__         {__{__     {__{__         {__{________","red"))
                                                                                         
print(colored("\t\t\t Created by DayosHACKER", "yellow"))
print(colored("\t\t\t\t (DEVILAND)", "green"))
print(colored("Mahakal is a strong password creator tool made by dAYOShACKER","red"))
print("\n")



print(colored("*************************************************************************", "red"))

print(colored("\n\nSELECT A OPTION", "yellow"))


# user options

print(colored(" [ 1 ] Easy", "yellow"))
print(colored(" [ 2 ] Medium", "yellow"))
print(colored(" [ 3 ] Hard", "yellow"))
print(colored(" [ 9 ] Exit\n", "yellow"))


#user input
user_ch = int(input(colored("Enter your choice:\nDevil_> ", "cyan")))




# if user's choice is 2, then
if user_ch == 1:
	
	#charcters
	char = []
	char.extend(list(string.ascii_letters))
	
	random.shuffle(char)
	
	# password length
	plen = int(input(colored("\nEnter your password length: \nDevil_> ", "blue")))
	
	# logic
	passwrd = "".join(char[0:plen])
	
	# printing password
	print("Your password is: ", "".join(passwrd))
	
	# to save the password
	sav = input(colored("\nDo you want to save your password (y/n) : \nDevil_> ", "magenta"))
	
	
	# if user don't save the password
	if sav == "n" or sav == "N":
		print(colored("\ngood - luck\n\n", "red"))
	
	# if user save password	
	elif sav == "y" or sav == "Y":
		
		# asking for password name
		name = input(colored("\nName your password: \nAD4rSH_> ","red"))
		
		# to save the password
		dict = {name:passwrd}
		
		# file handling
		f = open("easy.txt", "a")
		f.write(str(dict))
		f.write("\n")
		f.close
		
		# sucessful message
		print(colored("\nSucessfully added.....................\n\n", "blue"))

	# else statement
	else:
		print(colored("\nPlease enter a valid value!!!\n\n", "red"))




# if user's choice is 3, then
elif user_ch == 2:
	
	#charcters
	char = []
	char.extend(list(string.ascii_letters))
	char.extend(list(string.digits))
	
	random.shuffle(char)
	
	# password length
	plen = int(input(colored("\nEnter your password length: \nAD4rSH_> ", "blue")))
	
	# logic
	passwrd = "".join(char[0:plen])
	
	# printing password
	print("Your password is: ", "".join(passwrd))
	
	# to save the password
	sav = input(colored("\nDo you want to save your password (y/n) : \nAD4rSH_> ", "magenta"))
	
	
	# if user don't save the password
	if sav == "n" or sav == "N":
		print(colored("\nBye - Bye\n\n", "red"))
	
	# if user save password	
	elif sav == "y" or sav == "Y":
		
		# asking for password name
		name = input(colored("\nName your password: \nAD4rSH_> ","red"))
		
		# to save the password
		dict = {name:passwrd}
		
		# file handling
		f = open("medium.txt", "a")
		f.write(str(dict))
		f.write("\n")
		f.close
		
		# sucessful message
		print(colored("\nSucessfully added.....................\n\n", "blue"))

	# else statement
	else:
		print(colored("\nPlease enter a valid value!!!\n\n", "red"))




# if user's choice is 5, then
elif user_ch == 3:
	
	#charcters
	char = []
	char.extend(list(string.ascii_letters))
	char.extend(list(string.digits))
	char.extend(list(string.hexdigits))
	char.extend(list(string.punctuation))
	
	
	random.shuffle(char)
	
	# password length
	plen = int(input(colored("\nEnter your password length: \nAD4rSH_> ", "blue")))
	
	# logic
	passwrd = "".join(char[0:plen])
	
	# printing password
	print("Your password is: ", "".join(passwrd))
	
	# to save the password
	sav = input(colored("\nDo you want to save your password (y/n) : \nAD4rSH_> ", "magenta"))
	
	
	# if user don't save the password
	if sav == "n" or sav == "N":
		print(colored("\ngood - luck\n\n", "red"))
	
	# if user save password	
	elif sav == "y" or sav == "Y":
		
		# asking for password name
		name = input(colored("\nName your password: \nDevil_> ","red"))
		
		# to save the password
		dict = {name:passwrd}
m		# file handling
		f = open("hard.txt", "a")
		f.write(str(dict))
		f.write("\n")
		f.close
		
		# sucessful message
		print(colored("\nSucessfully added.....................\n\n", "blue"))

	# else statement
	else:
		print(colored("\nPlease enter a valid value!!!\n\n", "red"))




elif user_ch == 9:
	print(colored("\nAlways Be Strong!!!\n", "red"))		
						
else:
	print(colored("Please enter a valid value", "red"))
	
					


