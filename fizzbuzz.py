#Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number, and 
# for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
mylist=[]
for number in range(1,101):
    if(number%3==0 and number%5==0):
        print("FizzBuzz")   
    elif (number%3==0):
        print("fizz")
    elif(number%5==0):
        print("buzz")
  
    else:
        print(number)     
        