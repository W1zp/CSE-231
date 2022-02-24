# Project 06 CSE 231
#
# Algorithm
# Function open_file()
#   while function to loop until successful
#       try prompt for read file and try to open
#           return the file if successful
#       except print error and reprompt
# Function get_county_state(s)
#   split the string input at the ","
#   strip any leading or ending spaces
#   assign the first variable as county
#   assign the second variable as state
#   return the county and state
# Function handle_commas(s)
#   replace "," with ""
#   turn the string into an integer
#   return that integer
# Function read_file(fp)
#   read the file as a csv divided by a ,: create a list of tuples
#   remove the header in the file
#   for each row in the file
#       use get_county_state to extract the county and state from the 2nd colum
#       extract the string from the 11th column to get the income
#           use handle_commas to remove the commas + turn into int 
#       if the income is blank
#           skip that state
#       else add data into a new list
#           format the data as (state,county,income)
#   sort the data in decreasing order according to the income
#   return the sorted list
# Function state_average_income(state, master_list)
#   for row in master_list
#       if state is the state in row
#           add income to total and add 1 to count
#   if the total is 0 then return None since no data
#   else calculate the average
#       return the average rounded to 2 decimal places
# Function top_counties_by_income(master_list)
#   return the first 10 tuples in the master_list
# Function bottom_counties_by_income(master_list)
#   return the last 10 tuples in the master_list
# Function top_states_by_income(master_list)
#   create a list of state + states that have been calculated
#   for row in master_list
#       state = first part
#       average = state_average_income(state, master_list)
#       if state is in finished states
#           continue loop
#       else add the data into list
#           data is formatted as (state, average)
#       add the state into finished states list
#   sort the list according to the average in decreasing order
#   return the first 10 of the list
# Function bottom_states_by_income(master_list)
#   create a list of state + states that have been calculated
#   for row in master_list
#       state = first part
#       average = state_average_income(state, master_list)
#       if state is in finished states
#           continue loop
#       else add the data into list
#           data is formatted as (state, average)
#       add the state into finished states list
#   sort the list according to the average in decreasing order
#   get the last 10 if the list
#   return the list according to the average in increasing order
# Function counties_in_state(state,master_list)
#   for row in master_list
#       if the row has the state
#           add the county + income to the list
#   sort the counties in alphabetical order and return the list
# Function display_options()
#   displays the options menu
# Function main()
#   print title
#   use open_file() to get a read file then use read_file(fp) to read it
#   create a loop
#       use display_options() to show menu then prompt for an input
#       if input is "1":
#           get the state_average_income and print it
#       elif input is "2":
#           get the top_counties_by_income and print it
#       elif input is "3":
#           get the bottom_counties_by_income and print it
#       elif input is "4":
#           get the top_states_by_income and print it
#       elif input is "5":
#           get the bottom_states_by_income and print it
#       elif input is "6":
#           get the counties_in_state and print it
#       elif input is "q":
#           break the loop
#       else print error and loop

import csv #import all the functions we need
from operator import itemgetter

STATES = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"] #all the recorded states

def open_file():
    """Opens a file for reading. Continuously prompts for a file name until a file
        that can be read is inputted. Returns the file"""
    while 1 == True: #continuous loop
        try:
            file_in = input('Input a file: ') #prompt for a file name
            fp = open(file_in) #try to open file
            return fp #if it works then return the file
            break #loop breaker
        except FileNotFoundError: #if it doesn't work print error and loop
            print('Invalid filename, please try again.')
            continue

def get_county_state(s):
    """Takes a string and splits it into two parts from the "," then returns the
        first part as the county and the second as the state"""
    line = s.split(",") #split at the ","
    county = line[0].strip() #remove any leading or ending spaces
    state = line[1].strip()
    return county,state #return the outcomes
    

def handle_commas(s): #remove commas + spaces and convert
    '''Takes in a string s, removes commas from s and converts to int'''
    s = s.replace(",","") #replace the commas
    if s == "": #if there is no string return None
        return
    else:
        str_in = int(s) #convert the string to int
        return str_in
    
def read_file(fp):
    """Reads the file as a csv: makes the data into a list of tuples seperated by
        a ",". It skips any data with no median_income listed, removes the heading,
        removes any commas in income data, and sorted through descreasing income
        After formatting, it returns the list"""
    list_tuple = [] #set up the list
    reader = csv.reader(fp, delimiter = ",") #read the file as tuples in a list
    header = next(reader, None) #remove the header
    for row in reader: #read each tuple
        county, state = get_county_state(row[1]) #seperate the county and state string
        median_income = handle_commas(row[10]) #extract and format the income
        if median_income == None: #skip if there is no income value
            continue
        else:
            data = [(state, county, median_income)] #format the data
            list_tuple += data #add the data into the list
    list_tuple = sorted(list_tuple, key = itemgetter(2), reverse = True) #format the list
    return list_tuple

def state_average_income(state, master_list):
    """Calcualtes the average income of the states by taking the total of the counties
        in the state and dividing by the number of counties. Returns the calculation."""
    total = 0
    count = 0
    for row in master_list: #read each tuple
        if state == row[0]: #if the state is in the tuple 
            total += row[2] #add the income to a total count
            count += 1 #number of counties
    if total == 0: #if there is no data then return None
        return
    else:
        average = float(total / count) #calculate the average
        average = round(average, 2) #round to 2 decimal places
        return average

def top_counties_by_income(master_list):
    """Lists the top 10 counties based on income"""
    top_counties = master_list[:10] #first 10
    return top_counties

def bottom_counties_by_income(master_list):
    """lists the bottom 10 counties based on income"""
    bottom_counties = master_list[-10:] #last 10
    return bottom_counties

def top_states_by_income(master_list):
    """Lists the top 10 states based on income in a descreasing order"""
    list_states = [] #set up both lists
    states_fin = ""
    for row in master_list: #read each tuple
        state = row[0] #state the first in the tuple
        average = state_average_income(state, master_list) #find the average
        if state in states_fin: #skip any states already calculated
            continue
        else:
            data = [(state, average)] #set up the data
            list_states += data #add the data into the list
        states_fin = states_fin + "," + row[0] #add state to finished list
    top_states = sorted(list_states, key = itemgetter(1), reverse = True) #format the list in decreasing order
    top_states_sort = top_states[:10] #first 10
    return top_states_sort

def bottom_states_by_income(master_list):
    """Lists the bottom 10 states based on income in an ascending order"""
    list_states = [] #set up both lists
    states_fin = ""
    for row in master_list: #read each tuple
        state = row[0] #state the first in the tuple
        average = state_average_income(state, master_list) #calculate the average
        if state in states_fin: #skip any states already calcualted
            continue
        else:
            data = [(state, average)] #set up the data
            list_states += data #add the data into the list
        states_fin = states_fin + "," + row[0] #add state to finished list
    bottom_states = sorted(list_states, key = itemgetter(1), reverse = True) #income descending order 
    bot_states_des = bottom_states[-10:] #last 10
    bot_states_sort = sorted(bot_states_des, key = itemgetter(1)) #income ascending order
    return bot_states_sort
    
def counties_in_state(state, master_list):
    """Lists the counties in a state"""
    list_counties = [] #set up list
    for row in master_list: #read each tuple
        if row[0] == state: #if state in tuple
            counties = [(row[1], row[2])] #get the county + income
            list_counties += counties #add to the list
    county_state = sorted(list_counties, key = itemgetter(0)) #sort county alphabetically 
    return county_state

def display_options(): #displays the menu
    """
    DO NOT CHANGE
    Display menu of options for program
    """
    OPTIONS = """\nMenu
    1: Average median household income in a state
    2: Highest median household income counties
    3: Lowest median household income counties
    4: Highest average median household income states
    5: Lowest average median household income states
    6: List counties' median household income in a state\n"""
    print(OPTIONS)

def main(): #main function to run everything
    print("\nMedian Income Data") #title
    data = open_file() #prompts for a read file
    data_in = read_file(data) #read the file as a csv
    while 1 == True: #continuous loop
        display_options() #display the menu
        a = input('Choose an option, q to quit: ') #prompt for an input
        if a == "1":
            while 1 == True:
                state = input('Please enter a 2-letter state code: ') #prompt for a state
                if state in STATES: #check if in valid states list
                    average = state_average_income(state, data_in) #find average 
                    print('\nAverage median income in {:2s}: ${:<10,.2f}'.format(state, average)) #print average
                    break
                else:
                    print('Please input a valid state') #error and reprompt
                    continue
        elif a == "2":
            print('\nTop 10 Counties by Median Household Income (2018)') #heading
            print('{:<10}{:<30s}{:10s}'.format('State', 'County', 'Median Household Income')) #titles
            list_top = top_counties_by_income(data_in) #find top 10
            for row in list_top: #for each tuple print according to format
                print('{:<10}{:<30s}${:<10,d}'.format(row[0], row[1], row[2]))
        elif a == "3":
            print('\nBottom 10 Counties by Median Household Income (2018)') #heading
            print('{:<10}{:<30s}{:<10s}'.format('State', 'County', 'Median Household Income')) #title
            list_bottom = bottom_counties_by_income(data_in) #find bottom 10
            for row in list_bottom: #for each tuple print according to format
                print('{:<10}{:<30s}${:<10,d}'.format(row[0], row[1], row[2]))
        elif a == "4":
            print('\nTop 10 States by Average Median Household Income (2018)') #heading
            print('{:<10}{:<10s}'.format('State', 'Median Household Income')) #title
            list_top = top_states_by_income(data_in) #find top 10
            for row in list_top: #for each tuple print according to format
                print('{:<10}${:<10,.2f}'.format(row[0], row[1]))
        elif a == "5":
            print('\nBottom 10 States by Average Median Household Income (2018)') #heading
            print('{:<10}{:<10s}'.format('State', 'Median Household Income')) #title
            list_bottom = bottom_states_by_income(data_in) #find bottom 10
            for row in list_bottom: #for each tuple print according to format
                print('{:<10}${:<10,.2f}'.format(row[0], row[1]))
        elif a == "6":
            while 1 == True:
                state = input('Please enter a 2-letter state code: ') #promtp for a state
                if state in STATES: #check if valid state
                    count = len(counties_in_state(state, data_in)) #count how many counties
                    countstates = counties_in_state(state, data_in) #get list of counties
                    if count == 0: #0 counties
                        print('\nThere are 0 counties in {}'.format(state))
                        break
                    else: 
                        print('\nThere are {} counties in {}:'.format(count, state)) #print count
                        print('{:<30s}{:<10}'.format('County', 'Median Household Income')) #title
                        for row in countstates: #for each tuple print according to format
                            print('{:<30s}${:<10,d}'.format(row[0], row[1]))
                        break
                else:
                    print('Please enter a 2-letter state code: ') #reprompt
                    continue
        elif a == "q": #stop the loop if input is q
            break
        else: #any other input give error and reprompt
            print('Invalid choice, please try again')
            continue

if __name__ == '__main__': #runs the main function
    main()
