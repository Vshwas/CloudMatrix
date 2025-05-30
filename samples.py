# Example-1
# print("hello world")

#example-2
# print("hello world"/n)------ This code will be exceuted in next line.

#Example-3
#varaiable
#We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. Write 3 lines of code to switch the contents of the variables. You are not allowed to type the words "milk" or "juice". You are only allowed to use variables to solve this exercise. 
#glass1 = "milk"
#glass2 = "juice"
#temp = glass1  
#glass1 = glass2  
#glass2 = temp  
#print("glass1 contains:\n" + glass1)
#print("glass2 contains:\n" + glass2)

#Example-4
#print("welcome to the band")
#city = input("which city u grew up in ?:" "\n")
#pet = input("name of your pets:" "\n") 
#print("your band name would be:"  + city +  "" + pet )
#exa,ple-5
#print("welcome to the tip calacalate!""\n")
#bill = float(input("what was the total bill?""\n"))
#tip = int(input("what is per of the tip? 10 12 15""\n"))
#people = int(input("how many people to split the bill""\n"))
#tip_as_percent = tip /100
#total_tip_amount = bill * tip_as_percent
#total_bill = bill +total_tip_amount
#bill_per_person = total_bill / people
#final_amount = round(bill_per_person, 2 )
#print(f"each person should pay:  {final_amount}")
#Example-6
#print("welcome to the pizza page""\n")
#size = input("what is the size of pizza""\n")
#pepperoni = input("do you want pepperoni on your pizzer Y or N""\n")
#extra_cheese = input("do you want cheese Y or N""\n")
#bill = 0
#if size == "s":
    bill +=15
elif size == "m":
    bill +=20
elif size == "l":
    bill +=25
else:
    print("you type the wrong size of pizza ! try one more time""\n")
if pepperoni == "y":
    if size == "s":
        bill +=2
    else:
         bill +=3
if extra_cheese == "Y":
    bill +=1

print(f"your final bill is : ${bill}. ")
example -7 the program have a logicall condition
print("welcome to rollercoaster!""\n")
height = int(input("what is you height in cm ?""\n"))

if height >=120:
    print("you are in""\n")
    age = int(input("what is ur age""\n"))
    if age < 12:
        bill = 5
        print("child ticket is 5 $")
    elif age <=18:
        bill = 7
        print(" youth ticket is 7 $")
    elif age >= 45 and age <=55:
        bill =0
        print (" the ticket is on us ! you can travell free")
        
    else:
        bill = 12
        print("adult ticket is 12$")
    
    wants_photo = input("do you want photo Y OR N""\n")
    if wants_photo =="y":
        bill +=3
        print(f"your final bill is $$$:{bill}""\n")

