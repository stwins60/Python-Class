#ASSIGNMENT #4: YOU HAVE BEEN HIRED FINALLY BY THE 21 Century as a Senior Programmer and you've been tasked to help
#in revamping their credit rating system and loan issuing system. Just remember, your job is to make things happen.
#As a Sr. Developer in Python Programming, all the lights and attention are turned towards you and there is a job to be
#done to deliver this critical system on time.

#Your job is to design a simple program to allow the loan officer(s) to enter the customer particulars at the terminal and
#determine if a customer is credit worthy. 

#Based on their looan officer's entry, your system is required to get the best desired resired as shown below in the OUTPUT.

#Please design a program to do the input entry, do the desired calculations and come up with the needed requirements and output them as needed.
#Please consider all the needed variable. If you need to add any, please do add if need is there. Good luck.


#Enter the price of the House you wish to Buy
print("Enter the house price")
price = float(input())

#Enter the first name
print("Enter the first name")
first_name = input()

#Enter the last name
print("Enter the last name")
last_name = input()

fullname = first_name + " " + last_name

#Enter the email
print("Enter the email address")
email = input()

#Enter the phone number
print("Enter the phone number")
phone = input()

#Enter the mailing
print("Enter the mailing address")
address =input()

#Enter the mailing
print("Enter the City")
city = input()

#Enter the mailing
print("Enter the State")
state = input()

#Enter the mailing
print("Enter the zip code")
zipcode = input()

print("Enter your credit Score:")
CreditScore = int(input())

#Qualify for loans with the best interest rates
if 780 <= CreditScore <= 850:
    print ("Excellent Credit")
    downPayment = 0.10 * price
    print("Zero Down Payment")

# #Usually qualify for loans with the best interest rates
elif 740 <= CreditScore <= 779:
    print("Very Good")
    downPayment = 0.1 * price
    print("Downpayment: " + str(downPayment))

# #May face slightly higher loan Interest rates
elif CreditScore >= 720 and  739:
    print("Above Average")
    downPayment = 0.3 * price
    print("Downpayment: " + str(downPayment))
# #May qualify for most loans of higher interest rates
elif CreditScore >= 680 and 719:
    print("Average")
    downPayment = 0.6 * price
    print("Downpayment: " + str(downPayment))
# #May qualify for most loans at significant higher Interest rates
elif CreditScore >= 620 and 679:
    print("Below Average")
    downPayment = 0.18 * price
    print("Downpayment: " + str(downPayment))
# #Usually has some credit issues; will probably not qualify for most loans
elif CreditScore >= 580 and 619:
    print("Poor Credit Score")
    downPayment = 0.20 * price
    print("Downpayment: " + str(downPayment))
# #Facing extreme credit issue
elif CreditScore < 520:
    print("Poor Credit Score")
    downPayment = 0.25 * price
    print("Downpayment: " + str(downPayment))
else:
    print("invalid output")

print("---------------------------------------")

print("Fist name is : " + fullname)
print("Email: " + email)
print("Phone: " + phone)
print("Physical address: " + address)
print("City: " + city)
print("State: " + state)
print("Zipcode: " + zipcode)
print("Price of the house:",price)
print('Credit Score:', CreditScore)
print("---------------------------------------")