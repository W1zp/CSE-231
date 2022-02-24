# Project 03 CSE 231
#
# Algorithm
#   print calculator heading
#   set retry to yes
#   while statement for yes to retry
#       ask for level input and change input to lower case
#       while statement if not an acceptable level
#           print "Invalid input. Try again."
#           ask for input again
#   if level is junior or senior
#       ask for which college
#       if college does not match
#           set college as none
#       else james madison college = "no"
#       if college is none
#           ask if in jmc
#           if jmc is not yes
#               college is none
#   if level is freshman or sophomore
#       ask if in college of engineering
#       if coe is yes
#           college = engineering
#           jmc = no
#       if coe is anything else
#           ask for jmc
#           if jmc is anything other than yes
#               college = none
#   ask for credit input
#   if credit is not a digit and is = 0
#       print error message and ask again
#   else if is digit and not equal to 0
#       change credit to int
#       while credit <= 0
#           display error and ask again
#       change credit to int
#   Residency cost for freshmans and engineering/business freshman
#   Residency cost for sophomores and engineering/business sophomores
#   Residency cost for juniors and seniors
#   Residency cost for engineering/business juniors and seniors
#   Special cost for engineering students (all levels)
#   Special cost for business students (junior and senior)
#   Special cost for health or sciences students (junior and senior)
#   Special cost for students with no college affliation
#   Student costs for >= 6 credits
#       if in jmc $7.5 more
#   Student costs if < 6 credits
#       if in jmc $7.5 more
#   calculate tuition = resident + special + student
#   print tuition with $ + , for thousands + 2 decimal places for cents
#   ask if user wants to retry 


print("2021 MSU Undergraduate Tuition Calculator.\n") #heading
retry = "yes" #retry to yes
while retry == "yes": #set up a continuous statement
    level = input("Enter Level as freshman, sophomore, junior, senior: ").lower() #ask for level
    while level != "freshman" and level != "sophomore" and level != "junior" and level != "senior": #if not any ask again
        print("Invalid input. Try again.")
        level = input("Enter Level as freshman, sophomore, junior, senior: ").lower()

    if level == "junior" or level == "senior": #Ask for college if a junior or senior
        college = input("Enter college as business, engineering, health, sciences, or none: ").lower()
        if college != "business" and college != "engineering" and college != "health" and college != "sciences":
            college = "none"
        else:
            jmc = "no"
        if college == "none": #if not in any college ask for jmc
            jmc = input("Are you in the James Madison College (yes/no): ")
            if jmc != "yes":
                college = "none"

    if level == "freshman" or level == "sophomore": #ask if in coe or jmc if freshman or sophomore
        coe = input("Are you admitted to the College of Engineering (yes/no): ")
        if coe == "yes":
            college = "engineering"
            jmc = "no"
        if coe != "yes":
            jmc = input("Are you in the James Madison College (yes/no): ")
            if jmc != "yes":
                college = "none"

    credit = input("Credits: ") #ask for amount of credits
    if credit.isdigit() != True or credit == "0":
        while credit.isdigit() != True or credit == "0":
            print("Invalid input. Try again.")
            credit = input("Credits: ")
        credit = int(credit)
        while credit <= 0:
            print("Invalid input. Try again.")
            credit = input("Credits: ")
        credit = int(credit)
    else:
        credit = int(credit)
        while credit <= 0:
            print("Invalid input. Try again.")
            credit = input("Credits: ")
        credit = int(credit)

    #base resident cost freshman - engineering and business is the same
    if level == "freshman" and (college == "none" or college == "business" or college == "engineering"):
        if credit <= 11:
            resident = credit * 482
        if 12 <= credit <= 18:
            resident = 7230
        if credit > 18:
            resident = 7230 + 482 * (credit - 18)

    #base resident cost sophomore - engineering and business is the same
    if level == "sophomore" and (college == "none" or college == "business" or college == "engineering"):
        if credit <= 11:
            resident = credit * 494
        if 12 <= credit <= 18:
            resident = 7410
        if credit > 18:
            resident = 7410 + 494 * (credit - 18)

    #base resident cost junior and senior
    if (level == "junior" or level == "senior") and college == "none":
        if credit <= 11:
            resident = credit * 555
        if 12 <= credit <= 18:
            resident = 8325
        if credit > 18:
            resident = 8325 + 555 * (credit - 18)
        
    #college of engienering and business costs resident - freshman and sophomore are same as base resident
    if (level == "junior" or level == "senior") and (college == "business" or college == "engineering"):
        if credit <= 11:
            resident = credit * 573
        if 12 <= credit <= 18:
            resident = 8595
        if credit > 18:
            resident = 8598 + 573 * (credit - 18)
        
    #special costs for engineering students
    if college == "engineering":
        if credit <= 4:
            special = 402
        else:
            special = 670
            
    #special costs for business
    if (level == "junior" or level == "senior") and college == "business":
        if credit <= 4:
            special = 113
        else:
            special = 226
        
    #special costs for health and sciences
    if (level == "junior" or level == "senior") and (college == "health" or college == "sciences"):
        if credit <= 4:
            special = 50
        else:
            special = 100

    #special costs for no college
    if college == "none":
        special = 0
        
    #student costs
    if credit >= 6:
        student = 21 + 3 + 5
        if jmc == "yes":
            student += 7.5
    else:
        student = 21 + 3
        if jmc == "yes":
            student += 7.5
    
    tuition = resident + special + student #tuition calculation and print
    print("Tuition is ${:,.2f}.".format(tuition))
    retry = input("Do you want to do another calculation (yes/no): ").lower()



















