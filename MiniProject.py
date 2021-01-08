#Task: Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.  Hint: how does an even / odd number react differently when divided by 2?

#Bonus:
#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).  If check divides evenly into num, tell that to the user.  If not, print a different appropriate message.
#Write a custom function for finding whether the number is even or odd and call it in your main program code.



num = int(input('Please enter a number: '))

if num % 2 == 0:
  print('This is an even number!')
else:
  print('This is an odd number!')

Custom Function

def find(num):
   if num%2 == 0:
        num = 'even'

   else:
        num = 'odd'
  
    
   return num 


num = int(input('Please enter a number: '))
check = int(input('Please enter a second number: '))


if num % 4 == 0:
    print('The number you input is a multiple of 4')
elif num % 2 ==0:
    print('This is an even number.')
else:
    print('This is an odd number.')

if num % check == 0:
 
  print('This number could be divided evenly into the other number.')
else:
 
  print('This number could not be divided evenly into the second number.')

