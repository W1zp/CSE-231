# Project 08 CSE 231
# 
# Algorithm
# Function plot_regression(x,y)
#   plots the regression line between 2 variables
# Function plot(region_states)
#   plots the data and regression line between 2 of the data
# Function open_file(s)
#   prompt for file type depending on s
#   returns the file
# Function read_icnome_file(fp)
#   read the income file as a csv
#   skip 4 lines
#   create a dictionary of {state: [region, income]}
#   return the dictionary
# Function read_gdp_file(fp, D)
#   read the gdp file as a csv
#   skip 6 lines
#   extract the gpd data and append it to previous Dictionary
#   return the new dictionary
# Function read_pop_file(fp, D)
#   read pop file as csv
#   skip 1 line
#   extract the population data and append it to previous Dictionary
#   return the new dictionary
# Function get_min_max(D, region)
#   if region is not in list then return none
#   if region is "all" then find data for all states in STATES
#   if data has region then find data for the specific states
#   sort by max income then extract min and max
#   sort by max gdp then extract min and max
#   return max + min income and max + min gdp
# Function get_region_states(D, region)
#   if region not in Region list then return none
#   if region in region list
#       if region is "all" then extract the data for all states
#       else extract the data for certain states in a region
#   sort the data alphabetically according to state
#   return the sorted data
# Function display_region(D, region)
#   if region not in region list return none
#   if region is "all" then print all header
#   else print the header for specific region
#   if region in region list:
#       get_max_min and print the formatted data
#       get_region_states and print the formatted data
# Function main()
#   open up an income, gdp, and population file
#   read the files
#   create a loop
#       ask for region input using given prompt
#           if region is "q" then break loop
#           if region is in prompt1 then display the data according to region
#               prompt for plot if yes then plot

import csv, pylab
from operator import itemgetter

REGION_LIST = ['Far West','Great Lakes','Mideast','New England','Plains','Rocky Mountain','Southeast','Southwest','all']
STATES = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','District of Columbia','Florida','Georgia','Hawaii',
'Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri',
'Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania',
'Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']

PROMPT1 = "\nSpecify a region from this list or 'q' to quit -- \nFar West,Great Lakes,Mideast,New England,Plains,Rocky Mountain,Southeast,Southwest,all: "

def plot_regression(x,y):
    '''
        This function plots the regression line between 2 variables. 
        This function is provided in the skeleton code.
        
        Parameters:            
            x: a list that includes the values for the first variable
            y: a list that includes the values for the second variable
                                
        Returns: None
    '''
    #set the size of the plot
    pylab.rcParams['figure.figsize'] = 6.4, 4.8
    xarr = pylab.array(x) #numpy array
    yarr = pylab.array(y) #numpy arry
    #fit a line, only takes numpy arrays
    m,b = pylab.polyfit(xarr,yarr, deg = 1) 
    #plotting the regression line
    pylab.plot(xarr,m*xarr + b, '-') 

def plot(region_states):
    '''
        This function plots the data (GDP, population, Income, GDP per capita, and
        Income per capita) for the selected region. It also plots the regression
        line between 2 of the data. This function is provided in the skeleton code.
        
        Parameters:            
            region_states (list of tuples): list of tuples of data for states 
            in the specified region (state, population, GDP, income, 
                                    GDP per capita, and income per capita)
                                
        Returns: None
    '''
    
    VALUES_LIST = ['Pop', 'GDP', 'PI', 'GDPp', 'PIp']
    VALUES_NAMES = ['Population(m)','GDP(m)','Income(m)','GDP per capita','Income per capita']
    PROMPT2 = "Specify x and y values, space separated from Pop, GDP, PI, GDPp, PIp: "
    
    # prompt for which values to plot
    while True:
        x_name, y_name = input(PROMPT2).strip().split()
        if x_name.lower() in [s.lower() for s in VALUES_LIST] \
           and y_name.lower() in [s.lower() for s in VALUES_LIST]:
               break
        else:
            print("Error in selection. Please try again.")
            
    x_index = VALUES_LIST.index(x_name)
    y_index = VALUES_LIST.index(y_name)
    #print("indices:",x_name,":",x_index," ; ", y_name, ":",y_index)

    # +1 accounts for skipping state name in list
    x = [state[x_index+1] for state in region_states]
    y = [state[y_index+1] for state in region_states]
    state_names = [state[0] for state in region_states]
    
    # get full names
    x_name = VALUES_NAMES[x_index]
    y_name = VALUES_NAMES[y_index]

    # Set the labels and titles of the plot
    pylab.title(x_name + " vs. " + y_name)   #title

    pylab.xlabel(x_name)   #label x axis
    pylab.ylabel(y_name)   #label y axis
    
    #plot the scatter plot   
    pylab.scatter(x,y)
    for i, txt in enumerate(state_names): 
        pylab.annotate(txt, (x[i],y[i]))
    
    #plot the regression line between x and y
    plot_regression(x,y)
    
    #save and show the graph
    pylab.savefig("plot.png",dpi = 100)  
    pylab.show()      
    
def open_file(s):
    '''Opens a file for reading. Depending on what s is, the prompt text is different.
        if there is an error then continue to prompt.'''
    while 1 == True: #continuous loop
        if s == "income":
            file = input('Input a {} file: '.format(s)) #income text
        elif s == "GDP":
            file = input('Input a {} file: '.format(s)) #gdp text
        elif s == "population":
            file = input('Input a {} file: '.format(s)) #population text
        try:
            fp = open(file) #try to open the file
            return fp #return if successful
            break #break the loop after opening file
        except FileNotFoundError: #if file error
            print('Invalid filename, please try again.') #error statement
            continue #continue loop

def read_income_file(fp):
    '''Reads the income file as a csv. Skips 5 heading lines. Reads the data and takes
        the first column as states, if region then skip, and extracts the income from
        column 7, removing the , and converting to int. Adds data into a dictionary with
        key = state and values = [region, income]. Returns the dictionary'''
    dict = {} #create a dictionary
    reader = csv.reader(fp, delimiter = ",") #read income file as csv
    for i in range(5): #skip first 5 lines
        next(reader)
    for row in reader: #reads each row
        state = row[0].strip() #extracts the state name
        if state not in STATES: #if region then skip
            region = row[0].strip() #region isn't updated until another one shows up
            continue
        else:
            income = int(row[6].replace(",", "")) #extract income data and format
            dict[state] = [region, income] #key = state and value = [region,income]
    return dict #return the dictionary

def read_gdp_file(fp,D):
    '''Reads the GDP file as a csv. Skips 6 heading lines. Reads the data and extracts the
        first column as states, if column is region then skip. Extract the gdp data and format
        add the gdp into the dictionary according to the state. Return the updated dictionary'''
    dict_gdp = D #income dictionary
    reader = csv.reader(fp, delimiter = ",") #read gdp file as csv
    for i in range(6): #skip the first 6 lines
        next(reader)
    for row in reader: #reach each row
        state = row[0].strip() #extract the state
        if state in REGION_LIST: #if region then skip
            continue
        else: 
            GDP = int(row[7].replace(",", "")) #extract the gdp data and format
            dict_gdp[state].append(GDP) #add the gdp data into dictionary according to state
    return dict_gdp #return the updated dictionary

def read_pop_file(fp,D):
    '''Reads the pop file as a csv. Skips the first line. Reads the data and extracts the second
        column as states. Extract the population data and divide it by 1 mil to get it in the
        millions then round to 2 decimal places. Add the population data into the dictionary
        according to state. Return the updated dictionary'''
    dict_pop = D #gdp dictionary
    reader = csv.reader(fp, delimiter = ",") #read pop file as csv
    next(reader) #skip 1 line
    for row in reader: #read each row
        state = row[1].strip() #extract the state from column 2
        if state in STATES: #if state is in state list
            population = int(row[2].strip()) #extract the population from column 3
            population = round(population / 1000000, 2) #divide by 1 mil to get it in millions
            dict_pop[state].append(population) #add the population according to state
    return dict_pop #return the updated list

def get_min_max(D,region):
    '''Takes the region and finds the data in the format [state, income per capita, GDP per capita].
        income per capita is income / pop and gdp per capita is gdp / population.
        Return nothing is region is not in region list. If region is all then return the data for all
        states. Else return the data for states within a certain region. Sort the data according to the
        income capita and extract the max and min. Sort the data according to the gdp capita and extract
        the max and min. Return the max and mins as 4 tuples.'''
    data = [] #create a data list
    if region not in REGION_LIST: #if region not in list then return none
        return
    elif region == "all": #if region is all
        for state in STATES: #for each state
            income_capita = int(round(D[state][1] / D[state][3])) #calculate income
            GDP_capita = int(round(D[state][2] / D[state][3])) #calculate gdp
            data += [(state, income_capita, GDP_capita)] #format the data and add to list
    else:
        for state in STATES: #for each state
            if D[state][0] == region: #if region is region
                income_capita = int(round(D[state][1] / D[state][3])) #calculate the income
                GDP_capita = int(round(D[state][2] / D[state][3])) #calculate the gdp
                data += [(state, income_capita, GDP_capita)] #format the data and add to list
    data_sort_income = sorted(data, key = itemgetter(1)) #sort by income capita
    income_max = data_sort_income[-1] #get max
    income_min = data_sort_income[0] #get min
    data_sort_GDP = sorted(data_sort_income, key = itemgetter(2)) #sort by gdp capita
    GDP_max = data_sort_GDP[-1] #get max
    GDP_min = data_sort_GDP[0] #get min
    list_sort = income_min, income_max, GDP_min, GDP_max #set up the data
    return list_sort #return as 4 tuples

def get_region_states(D,region):
    '''Takes the region and finds all the states within that region. the data is formatted as [state, population,
        GDP, income, gdp capita, income capita]. If region is not in list then return none. if region is all then
        find the income and gdp capita, if sate is District of Columbia then shorten to DC. Format the data into a
        tuple and add to the list. If region specific then find all states with region data and format the data into
        a tuple and add to the list. Sort the data list in alphabetical order according to the state.
        Return the data list.'''
    data = [] #create a data list
    if region not in REGION_LIST: #if not in region list then skip
        return
    if region in REGION_LIST: #if it is in region list
        if region == "all": #if region is all
            for state in STATES: #fpr each state
                income_capita = int(round(D[state][1] / D[state][3])) #calculate income
                GDP_capita = int(round(D[state][2] / D[state][3])) #calculate gdp
                if state == "District of Columbia": #if district of columbia
                    state_abv = "DC" #shorten to DC
                    data += [(state_abv, D[state][3], D[state][2], D[state][1], GDP_capita, income_capita)] #format data and add to list
                else:
                    data += [(state, D[state][3], D[state][2], D[state][1], GDP_capita, income_capita)] #add data into list
        else: 
            for state in STATES: #for each state 
                if D[state][0] == region: #if region is in data
                    income_capita = int(round(D[state][1] / D[state][3])) #calculate income
                    GDP_capita = int(round(D[state][2] / D[state][3])) #calculate gdp
                    if state == "District of Columbia": #if district of columbia
                        state_abv = "DC" #shorten to DC
                        data += [(state_abv, D[state][3], D[state][2], D[state][1], GDP_capita, income_capita)] #format data and add to list
                    else:
                        data += [(state, D[state][3], D[state][2], D[state][1], GDP_capita, income_capita)] #add data into list
    data_sort_state = sorted(data, key = itemgetter(0)) #sort the data alphabetically according to state
    return data_sort_state #return sorted list

def display_region(D, region):
    '''Takes the region and displays the formatted data. If region is not in region list then return None. If region is all
        print all heading else print specific region heading. if region is in the region list then find max_min and print
        the max gdp, min gdp, max income, and min income. Then find region_states and print each state + data.'''
    if region not in REGION_LIST: #if not in list then return None
       return
    if region == "all": #if region is all
        print("\nData for the all regions:") #print all heading
    else:
        print("\nData for the {:s} region:".format(region)) #print specific region heading
    if region in REGION_LIST: #if region in list
        max_min = get_min_max(D, region) #find the max_min
        print("\n{:s} has the highest GDP per capita at ${:,d} ".format(max_min[3][0], max_min[3][2])) #print max gdp
        print("{:s} has the lowest GDP per capita at ${:,d} ".format(max_min[2][0], max_min[2][2])) #print min gdp
        print("\n{:s} has the highest Income per capita at ${:,d} ".format(max_min[1][0], max_min[1][1])) #print max income
        print("{:s} has the lowest Income per capita at ${:,d} ".format(max_min[0][0], max_min[0][1])) #print min income
        region_states = get_region_states(D, region) #find the region_states
        print("\nData for all states in the {:s} region:".format(region)) #print region heading
        print("\n{:15s}{:>13s}{:>10s}{:>12s}{:>18s}{:>20s}".format('State','Population(m)','GDP(m)','Income(m)','GDP per capita','Income per capita')) #print headers
        for row in region_states: #for each row in list
            print("{:15s}{:>13,.2f}{:10,d}{:12,d}{:18,d}{:20,d}".format(row[0], row[1], row[2], row[3], row[4], row[5])) #print each data point

def main():
    '''Opens an income, gdp, and population file. Reads them using the specific file functions. Create a loop for
        prompting for region input. If region is q or Q then break loop. If region input is in the list then display
        data according to the region input. Prompt for plot if plot is yes exactly then plot else no. Else continue
        to continue the loop after 1 run through.'''
    ifile = open_file("income") #open an income file
    gfile = open_file("GDP") #open a gdp file
    pfile = open_file("population") #open a population file
    income_file = read_income_file(ifile) #read the income file
    GDP_file = read_gdp_file(gfile, income_file) #read the gdp file
    D = read_pop_file(pfile, GDP_file) #read the population file
    while 1 == True: #create a loop
        region = input(PROMPT1)
        if region == "q" and "Q":
            break #break loop when q or Q is entered
        elif region in REGION_LIST: #if region is in list
            display_region(D, region) #display the data according to region
            plot_prompt = input("\nDo you want to create a plot? ").lower()
            if plot_prompt == "yes": #if plot prompt yes
                region_states = get_region_states(D, region) #get the region_states
                plot(region_states) #plot the region_states
        else:
            continue #continue the loop

if __name__ == '__main__':
    main()
    
