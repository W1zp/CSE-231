# Project #2 CSE 231
# 
# Algorithm
#  import math functions
#  print directions and greeting
#  prompt for continuation
#  while function for continuation
#   prompt for customer code
#   if statement for non-recongnized codes
#   prompt for amount of rental days
#   prompt for odometer start reading
#   prompt for odometer end reading
#   if statement for smaller end reading calculation
#   else statement for mileage calculation
#   if Budget plan conversions
#   if Daily plan conversions
#   if Weekly plan conversions
#   Calculate bill
#   print all values
#   prompt for continuation
#  print thank you message

import math #Math functions ex: math.ceil
print("\nWelcome to car rentals. ") #Beginning greeting and directions
print("\nAt the prompts, please enter the following: ")
print("\tCustomer's classification code (a character: BDW) ")
print("\tNumber of days the vehicle was rented (int)")
print("\tOdometer reading at the start of the rental period (int)")
print("\tOdometer reading at the end of the rental period (int)")
Continue = input("\nWould you like to continue (Y/N)? ") #prompt for continuation
while Continue == "Y": #While statement for when continue is Y
    Code = input("\nCustomer code (BDW): ") #Ask for what plan
    if Code != "B" and Code != "D" and Code != "W": #Error when code isn't a recognized code
        while Code != "B" and Code != "D" and Code != "W":
            Code = input("\n\t*** Invalid customer code. Try again. ***\n\nCustomer code (BDW): ")
    Days = int(input("\nNumber of days: ")) #Ask for number of rental days
    Mile_start = int(input("Odometer reading at the start: ")) #Odometer start reading
    Mile_end = int(input("Odometer reading at the end:  ")) #Odometer end reading
    
    if Mile_end < Mile_start: #if statenent if end is smaller than start
        Miles = ((1000000 + Mile_end) - Mile_start)/10 #Mile calculation for end < start
    else:
        Miles = (Mile_end - Mile_start) / 10 #Mile calculation for end > start

    if Code == 'B': #Budget plan
        Base = 40 * Days #$40.00 per day
        Mileage = 0.25 * Miles #$0.25 per mile
    
    if Code == 'D': #Daily plan
        Base = 60 * Days #$60.00 per day
        if (Miles / Days) <= 100: #if under 100 mi/day no charge
            Mileage = 0
        else:
            Mileage = 0.25 * (Miles - (100 * Days)) #each mi over 100 mi/day

    if Code == 'W': #Weekly plan
        Base = 190 * math.ceil(Days/7) #$190 per week (round up)
        if (Miles / math.ceil(Days/7)) <= 900: #if <= $900 then no charge
            Mileage = 0
        elif 900 < (Miles/ math.ceil(Days/7)) <= 1500: #if 900 < x <= 1500 then $100 per week
            Mileage = 100 * math.ceil(Days/7)
        else: #if 1500 < x then $200 per week + $0.25 per mile over 1500 per week
            Mileage = (200 * math.ceil(Days/7)) + (0.25 * (Miles - (1500 * math.ceil(Days/7)))) 
            
    Bill = float(Mileage + Base) #Bill calculation
    print("\nCustomer summary:") #Customer summary with all values printed
    print('\tclassification code:', Code)
    print('\trental period (days):', Days)
    print('\todometer reading at start:', Mile_start)
    print('\todometer reading at end: ', Mile_end)
    print('\tnumber of miles driven: ', Miles)
    print('\tamount due: $', Bill)
    Continue = input("\nWould you like to continue (Y/N)? ") #Continuation prompt
print("Thank you for your loyalty.") #End thank you after code termination