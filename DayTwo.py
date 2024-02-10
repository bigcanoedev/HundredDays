#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill_amount = int(input("What was the total of your bill?"))

tip_percentage = int(input("How much would you like to tip? \n 12 \n 15 \n 20 \n"))

number_of_people = int(input("How many people split the bill? "))

indiviual_cost = ( bill_amount / number_of_people ) * (1 + (tip_percentage / 100))

print("Each person will pay: {:.2f}".format( indiviual_cost ))

