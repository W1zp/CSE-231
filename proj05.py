# Project 05 CSE 231
#
# Algorithm
# Function open_file(ch)
#   if ch is "w" prompt for writing file name
#       open file for writing
#   else prompt for a file to read
#       try reading file
#       except ask for another file
# Function handle_commas(s,T)
#   remove commas from the s
#   make T a lowercase str
#   if T is int
#       try s = int(s) + return s
#       except return None
#   elif T is float
#       try s = float(s) + return s
#       except return None
#   else return None
# Function process_line(line)
#   strip the spaces + split the line
#   extract the country name
#   remove commas from deaths and turn into int
#   remove commas from population and turn into float
#   return country, deaths, and population
# Function main()
#   use open_file(ch) to get read file
#   use open_file(ch) to make write file
#   print the two headers into data_out and data_in
#   for line in data_in loop
#       process_line(line) to get country + population + deaths
#       if country in G20
#           calculate death rate
#           if rate > US_rate add to list_high
#           print the country, deaths, population, and rate into data_in and data_out
#       print countries with rate bigger than USA test
#       print list_high 

G20 = "Argentina, Australia, Brazil, Canada, China, France, Germany, India, Indonesia, Italy, Japan, South Korea, Mexico, Russia, Saudi Arabia, South Africa, Turkey, United Kingdom, USA, European Union"
US_RATE = 1277.10

def open_file(ch): #file opener
    '''Takes in ch and if ch is "w" then prompt for writing file name until valid and returns it
        else if not "w" then prompt for reading file name until valid and returns it'''
    if ch == "w": #checking for file mode
        while 1 == True: #loop statement
            try:
                file_out = input("Enter a file name for writing: ") #ask for write file name
                data_out = open(file_out, "w") #create a write file
                return data_out #return the write file
                break
            except IOError:
                print("Error opening file.") #write file error
                continue
    else:
        while 1 == True:
            try:
                file_in = input("Enter a file name for reading: ") #ask for input file name
                data_in = open(file_in) #open input file
                return data_in #return the input file
                break
            except IOError:
                print("Error opening file.") #input file error
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

def process_line(line): #extract info from each line
    '''Takes a line and extracts the country name, the amount of deaths, and the population number.
        Then uses handle_commas(s,T) to format it.'''
    i = "int"
    f = "float"
    line = line.strip() #remove spaces at end and beginning
    country = line[0:25].strip() #get the country name
    d = line[25:35].strip() #get the deaths
    deaths = handle_commas(d,i) #format the deaths
    p = line[55:].strip() #get the population
    population = handle_commas(p,f) #format the population
    return country, deaths, population #return everything

def main():
    read = "r"
    write = "w"
    list_high = [] 
    data_in = open_file(read) #get the input file
    heading = data_in.readline() #skip the heading in data_in
    data_out = open_file(write) #get the writing file
    print("{:<20s}{:>10s}{:>14s}{:>14s}".format("Country","Deaths","Population","Death Rate")) #heading for data_in
    print("{:<20s}{:>10s}{:>14s}{:>14s}".format("","","Millions","per Million"))
    print("{:<20s}{:>10s}{:>14s}{:>14s}".format("Country","Deaths","Population","Death Rate"),file = data_out) #heading for data_out
    print("{:<20s}{:>10s}{:>14s}{:>14s}".format("","","Millions","per Million"),file = data_out)
    for line in data_in: #reach each line in data_in
        country,deaths,population = process_line(line) #process each data point
        if country in G20: #only get data for countries in list
            rate = deaths / population #rate calculation
            if rate > US_RATE and country != "USA": #if rate is higher than USA
                list_high.append(country) #add each country into the list_high
            print("{:<20s}{:>10,d}{:>14,.2f}{:>14,.2f}".format(country,deaths,population,rate)) #results for data_in
            print("{:<20s}{:>10,d}{:>14,.2f}{:>14,.2f}".format(country,deaths,population,rate),file = data_out) #results for data_out
    print("\nCountries with higher death rates than USA per million.") #higher rate text
    print(", ".join(list_high)) #print the list_high
    data_in.close() #close each file
    data_out.close()

# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main()