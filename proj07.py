# Project 07 CSE 231
# 
# Algorithm
# Function do_plot(x_vals, y_vals, year)
#   provided in the project folder - plots the bottom 40 in the data
# Function open_file()
#   prompts for a year input
#   uses year to open up text file
#   ask again if there is no text file or wrong input
#   returns file and year
# Function handle_commas(s, T)
#   replace "," with ""
#   return integer or float depending on T
# Function read_file(fp)
#   remove the header and title
#   format the data as a list of ((float, float), int, int, float, float, float)
#   return the list
# Function get_range(data_list, percent)
#   Find data for when the percent is >= input percent
#   return the data set as ((column 0, column 2), column 5, column 7)
# Function get_percent(data_list, income)
#   Find data for percent for a certain income
#   return the data set as ((column 0, column 2), column 5)
# Function find_average(data_list)
#   denominator = column 4 in the last data line
#   numerator = add up all the column 6s
#   return the average after calculating and rounding to 2
# Function find_median(data_list)
#   use get_range(data, 50) to find the median
#   return the income value
# Function def main()
#   open file + print year
#   read file and assign to variable
#   print average income + median income using find_average and find_median
#   prompt for plotting
#       if yes x_vals = column 0s and y_vals = column 5s
#       print(do_plot(x_vals, y_vals, year))
#   prompt for range, percent, or nothing - looped
#       if r ask for percent input
#           use get_range(data, percent) to get range
#           print range + percent
#       if p ask for income input
#           use get_percent(data, salary) to get percent
#           print income + percent
#       if nothing then stop the loop
#       anything else continues the loop prompt

import pylab #for plot

def do_plot(x_vals,y_vals,year):
    '''Plot x_vals vs. y_vals where each is a list of numbers of the same length.'''
    pylab.xlabel('')   # Label for X-axis
    pylab.ylabel('')   # Label for Y-axis
    pylab.title("Cumulative Percent for Income in "+\
                str(year))# Title for graph (what is written on top)
    pylab.plot(x_vals,y_vals)    # draws the plot (including labels and title)
    pylab.rcParams['figure.figsize'] = 6.4, 4.8 #  Set the size of the plot
    pylab.savefig("plot.png",dpi = 100)  # save the plot with a specified resolution
    pylab.show()   # displays the plot
    
def open_file():
    '''Opens the text file with the yearly data'''
    while 1 == True: #loop
        try:
            year = int(input("Enter a year where 1990 <= year <= 2019: ")) #year input
            if 1990 <= year <= 2019:
                try:
                    filename = "year" + str(year) + ".txt" #yearXXXX.txt
                    fp = open(filename) #opens the file
                    return fp, year #return file and year
                    break
                except FileNotFoundError:
                    print("Error in file name:",filename," Please try again.") #file error
                    continue
            else:
                print("Error in year. Please try again.") #year isn't in range
                continue
        except:
            print("Error in year. Please try again.") #not a number
            continue

def handle_commas(s,T): #remove commas + spaces and convert
    '''Takes in a string s and a string T, removes commas from s and converts to int or float depending
        on T input, if either does not work return None'''
    s = s.replace(",","") #replace the commas
    if T == "int": #if code int
        try:
            s = int(s)
            return s #int conversion
        except:
            return #return nothing if can't be turned int
    elif T == "float":
        try:
            s = float(s)
            return s #float conversion
        except:
            return #return nothing if can't be turned float
    else:
        return #return nothing for all else 

def read_file(fp):
    '''Reads and formats the data into a list of tuples'''
    f = "float"
    i = "int"
    list_data = []
    header = fp.readline() #skips the first two lines
    title = fp.readline()
    for line in fp:
        data = line.split() #splits the lines for formatting
        tup = (((handle_commas(data[0], f), handle_commas(data[2], f)), handle_commas(data[3], i), handle_commas(data[4], i),
                handle_commas(data[5], f), handle_commas(data[6], f), handle_commas(data[7], f))) #use handle_commmas to format
        list_data.append(tup) #add formated tuple to list
    return list_data #return list of tuples        
        
def get_range(data_list, percent):
    '''Gets the range according to the percent'''
    for line in data_list:
        if line[3] >= percent: #find when the percent is greater than input percent
            data_range = (line[0], line[3], line[5]) #Column 0, 2, 5, and 7 
            break
    return data_range #return formatted data

def get_percent(data_list, salary):
    '''Gets the percent according to the salary'''
    for line in data_list:
        if line[0][0] == salary: #find when the starting salary is input salary
            data_range = (line[0], line[3]) #Column 0, 2, and 5
            break
    return data_range #return formatted data

def find_average(data_list):
    '''Finds the average of all the incomes'''
    total_earners = 0
    total_value = 0
    for line in data_list:
        if line[0][1] == None: #when at the last line of data
            total_earners = line[2] #denominator 
        total_value += line[4] #numerator added up
    average = round(total_value / total_earners, 2) #calculate the average and round
    return average #return the average

def find_median(data_list):
    '''Find the median of the data'''
    median = get_range(data_list, 50) #find the income at 50%
    return median[2] #return the income value
    
def main():
    fp, year = open_file() #get the file + year 
    print("For the year {:4d}:".format(year)) #print the year
    data = read_file(fp) #read + format data
    average = find_average(data) #find the average
    print("The average income was ${:<13,.2f}".format(average)) #print average
    median = find_median(data) #find the median
    print("The median income was ${:<13,.2f}".format(median)) #print the median
    plot = input("Do you want to plot the data (yes/no): ") #prompt for plot
    if plot == "yes": #if answered yes to plot
        x_vals = []
        y_vals = []
        count = 0
        for line in data:
            x_vals.append(line[0][0]) #x_vals is column 0s
            y_vals.append(line[3]) #y_vals is column 5s
            count += 1 
            if count == 40: #bottom 40
                break
        print(do_plot(x_vals, y_vals, year)) #print plot
    while 1 == True: #choice loop
        choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ") #choice prompt
        try:
            if choice == "r": #when choice is range
                while 1 == True:
                    percent = int(input("Enter a percent: ")) #percent prompt
                    try:
                        r = get_range(data, percent) #get the range according to the percent
                        print("{:4.2f}% of incomes are below ${:<13,.2f}.".format(percent, r[0][0])) #print range + percent
                        break
                    except:
                        print("Error in percent. Please try again") #percent error
                        continue
            if choice == "p":
                while 1 == True:
                    income = int(input("Enter an income: ")) #income prompt
                    try:
                        p = get_percent(data, income) #get the percent according to the income
                        print("An income of ${:<13,.2f} is in the top {:4.2f}% of incomes.".format(income, p[1])) #print income + percent
                        break
                    except:
                        print("Error: income must be positive") #income error
                        continue
            if choice == "": #stops if input is nothing
                break
        except:
            print("Error in selection.") #choice error
            continue

if __name__ == '__main__':
    main()