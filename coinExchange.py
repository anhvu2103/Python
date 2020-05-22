# Anh Vu
# Prof. Wright - Python Programming
# Assign 9
#Notes:
#I will be using mod to hold remainder when calculating.


def dollar_change(dollar):
    if dollar <= 0:
        print("Error, you have to put positive value")
    else:
        twenty = dollar // 20
        ten = (dollar % 20) // 10
        five = (dollar % 10) //5
        one = dollar % 5 // 1

        print("")
        print("exchanging...")
        print("")
        print("The number of twenty dollars: ", int(twenty))
        print("The number of ten dollars: ", int(ten))
        print("The number of five dollars: ", int(five))
        print("The number of one dollars: ", int(one))


def coin_change(decimal):
    if decimal == 0:
        print("0 quarter, 0 dime, 0 nickel, 0 penny")
    else:
        quarter = decimal//25
        dime = (decimal % 25)//10
        nickel = (decimal % 25 % 10)// 5
        penny = decimal % 25 % 10 % 5 // 1
        print("The number of quarters: ", int(quarter))
        print("The number of dimes: ", int(dime))
        print("The number of nickels: ", int(nickel))
        print("The number of pennies: ", int(penny))

print("Please enter the numbers of quarters you want to put in for exchange: ")
in_quarter = int(input())
quarter_toVal = in_quarter * 25
print("You have put in: ", quarter_toVal, " cent(s)")

print("Please enter the numbers of dimes you want to put in for exchange: ")
in_dime = int(input())
dime_toVal = in_dime * 10
print("You have put in: ", dime_toVal+quarter_toVal, " cent(s)")

print("Please enter the numbers of nickels you want to put in for exchange: ")
in_nickel = int(input())
nickel_toVal = in_nickel * 5
print("You have put in: ", nickel_toVal + quarter_toVal + dime_toVal, " cent(s)")

print("Please enter the numbers of pennies you want to put in for exchange: ")
in_penny = int(input())
penny_toVal = in_penny * 1
print("You have put in: ", penny_toVal + nickel_toVal + quarter_toVal + dime_toVal, " cent(s)")

dollar = (quarter_toVal + dime_toVal + nickel_toVal + penny_toVal)/100
print("The total is: ", '{:7,.2f}'.format(dollar), " dollars")
# print(dollar) //debugging from test
# print(int(dollar)) //debugging from test 
decimal1 = (dollar-int(dollar))*100
decimal = round(decimal1,2) #I have to do this as a solution in order to have a correct result
#if you go down and see the result from my test, i was off 1 penny and it was because the decimal
#doesn't stick with .12, it goes down to .11998000000002 and I don't know why so I used round as a solution
# print(decimal) //debugging from test

dollar_change(dollar)
coin_change(decimal)


#Test:
# Please enter the numbers of quarters you want to put in for exchange: 
# 30
# You have put in:  750  cent(s)
# Please enter the numbers of dimes you want to put in for exchange: 
# 15
# You have put in:  900  cent(s)
# Please enter the numbers of nickels you want to put in for exchange: 
# 12
# You have put in:  960  cent(s)
# Please enter the numbers of pennies you want to put in for exchange: 
# 152
# You have put in:  1112  cent(s)
# The total is:    11.12  dollars
# 11.12
# 11
# 11
# 
# exchanging...
# 
# The number of twenty dollars:  0
# The number of ten dollars:  1
# The number of five dollars:  0
# The number of one dollars:  1
# The number of quarters:  0
# The number of dimes:  1
# The number of nickels:  0
# The number of pennies:  1

        
    
