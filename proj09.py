# Project 09 CSE 231
#
# Algorithm
#  def open_file(s)
#   continuously prompts for an indian food file until successful
#   returns the file pointer when successful
#  def build_dictionary(fp)
#   takes the file pointer and creates a dictionary
#       uses region -> state -> food_name -> [{ingredients}, diet, (prep_time, cook_time), flavor]
#       returns the finished dictionary
#  def get_ingrediants(D, L)
#   takes a list of foods and looks through the dictionary for ingredients
#   creates a set of ingrediants and returns it
#  def get_useful_and_missing_ingredients(D, foods, pantry)
#   takes the list of foods and creates a list of ingredients using get_ingrediants
#   compares the pantry list to the ingredients list to find what can be used and what needs to be bought
#   returns the lists as a tuple
#  def get_list_of_foods(D, L)
#   uses the list of ingredients and creates a food list based off the dictionary
#   returns the list of foods sorted by cooking time then alphabetically
#  def get_food_by_preference(D, preferences)
#   loops through the dictionary extracting the food names that match all the preferences
#   returns a list of food names sorted alphabetically
#  def main()
#   prints the title and sets up a menu prompt
#   uses the different functions to display a result based on the prompt
#   reprompts until Q is entered and gives an ending message

import csv
from operator import itemgetter

def open_file(s):
    ''' Prompts for an indian food file and tries to open it. If fail then reprompt until successful.
        Returns the file pointer when successful.'''
    while 1 == True: #contiuous loop
        try:
            filename = input('Input a {} file: '.format(s)) #prompt for file name input
            file = open(filename) #opens file
            return file #return file when successful
            break #stops the loop
        except FileNotFoundError: #if not successful
            print('Invalid filename, please try again.') #error message
            continue #reprompt
            
def build_dictionary(fp):
    ''' Takes a filepointer and creates a dictionary based on {region : {state : {food_name : 
        [{ingredients}, diet, (prep_time, cook_time), flavor]}}}. Creates a dictionary where
        no regions and states are repeated. Returns the dictionary'''
    dict = {} #create a dictionary
    reader = csv.reader(fp, delimiter = ",") #read the file as a csv
    next(reader) #skip header
    for row in reader: #read each item in the list
        if "-1" in row: #if there is a "-1" data point then ignore
            continue
        else:
            food_name = row[0].strip() #food name in column 1
            ingredients = set(row[1].lower().strip().split(", ")) #ingredients in column 2
            diet = row[2].replace(" ","") #diet in column 3
            prep_time = int(row[3]) #prep time in column 4
            cook_time = int(row[4]) #cooking time in column 5
            flavor = row[5] #flavor in column 6
            state = row[7] #state in column 8
            region = row[8] #region in column 9
            if region not in dict: #if region isn't in dictionary then add it
                dict[region] = {state: {food_name : [ingredients, diet,
                (prep_time, cook_time), flavor]}}
            elif state not in dict[region]: #if the state isn't in dictionary then add it
                dict[region][state] = {food_name : [ingredients, diet,
                (prep_time, cook_time), flavor]}
            else: #if region + state in dictionary then add to the list
                dict[region][state][food_name] = [ingredients, diet,
                (prep_time, cook_time), flavor]
    return dict #return completed dictionary

def get_ingredients(D,L):
    ''' Takes a list of food and sorts through a dictionary to compile a list of ingredients needed to make
        all the food in the list. Create a set for ingredients. Loops through the dictionary and adds ingredients
        for each food into the set. Returns the set of ingredients needed. '''
    set_ingredi = set() #create a set for ingredients so duplicates are ignored
    for region in D: #loop through regions
        for state in D[region]: #loop through states
            for food in D[region][state]: #loop through food names
                if food in L: #if food is in list
                    data = D[region][state][food] #extract the data
                    ingredients = data[0] #ingredits is in index 0
                    set_ingredi.update(ingredients) #add ingredients to set
    return set_ingredi #return the set

def get_useful_and_missing_ingredients(D, foods, pantry):
    ''' Takes a list of foods and a list of pantry items and sorts through a dictionary to find what ingredients
        in the pantry can be used to make the food in the food list and also finds what ingredients are missing.
        Uses the food list to get a set of all the ingredients needed. Turns the pantry list into a set. Uses set
        methods to find the ingredients at hand that can be used and the ingredients that need to be bought. Returns
        a tuple of ingreidents have and ingreidents buy. '''
    ingredients = get_ingredients(D, foods) #gets a list of ingredients based off food list
    pantry = set(pantry) #turns the pantry list into a set
    have = ingredients & pantry #items in both ingredients and pantry
    buy = ingredients - pantry #missing items in pantry 
    ingredi_have = sorted(have) #sorted list of ingredients have
    ingredi_buy = sorted(buy) #sorted list of ingredients buy
    return ingredi_have, ingredi_buy #return as a tuple

def get_list_of_foods(D, L):
    ''' Takes a list of ingrediants in pantry and sorts through a dictionary to find all the foods that
        can be made with the ingredients at hand. Turns the list into a set and loops through the dictionary
        looking for foods that can be made with the ingredients in the pantry. Creates a list of tuples with
        food name and total cooking time. Sorts the list by name then time to create a list sorted alphabetically
        by the cooking time. Returns sorted list.'''
    list_food = []
    data_food = []
    pantry = set(L) #create a set of ingredients in pantry
    for region in D: #loops through regions
        for state in D[region]: #loops through states
            for food in D[region][state]: #loops through food names
                data = D[region][state][food] #extract data from dictionary
                total_time = sum(data[2]) #find the total cooking time
                ingredients = get_ingredients(D, food) #use function to get ingredients
                if ingredients.issubset(pantry): #if ingredients are in pantry
                    data_food.append([food, total_time]) #list of tuple(food, time)
    data_food_s = sorted(data_food, key = itemgetter(0)) #sort by name
    list_food_s = sorted(data_food_s, key = itemgetter(1)) #sort by time
    for item in list_food_s:
        list_food.append(item[0]) #remove the total time
    return list_food #return sorted food list
    
def get_food_by_preference(D, preferences):
    ''' Takes a list of preferences and sorts through a dictionary returning the food_names that meet
        all of the preferences. Loops through the regions, states, and food_names. Using those variables
        test if the diet and flavor match the preferences and append to food_list. Returns finished food
        list sorted alphabetically. '''
    p = preferences #assign preferences to a shorter variable
    food_list = [] #data is {region : {state : {food : [{ingredients}, diet, (prep, cook), flavor]}}
    for region in D: #loop through each region
        for state in D[region]: #loop through each state
            for food in D[region][state]: #loop through each food
                data = D[region][state][food] #take out the list of data
                if p[0] == None and p[1] == None and p[2] == None and p[3] == None: #[None, None, None, None]
                    food_list.append(food)
                elif p[0] == region and p[1] == None and p[2] == None and p[3] == None: #[i, None, None, None]
                    food_list.append(food)
                elif p[0] == region and p[1] == state and p[2] == None and p[3] == None: #[i, i, None, None]
                    food_list.append(food)
                elif p[0] == region and p[1] == None and p[2] == data[1] and p[3] == None: #[i, None, i, None]
                    food_list.append(food)
                elif p[0] == region and p[1] == None and p[2] == None and p[3] == data[3]: #[i, None, None, i]
                    food_list.append(food)
                elif p[0] == None and p[1] == state and p[2] == None and p[3] == None: #[None, i, None, None]
                    food_list.append(food)
                elif p[0] == None and p[1] == None and p[2] == data[1] and p[3] == None: #[None, None, i, None]
                    food_list.append(food)
                elif p[0] == None and p[1] == None and p[2] == None and p[3] == data[3]: #[None, None, None, i]
                    food_list.append(food)
                elif p[0] == None and p[1] == None and p[2] == data[1] and p[3] == data[3]: #[None, None, i, i]
                    food_list.append(food)
                elif p[0] == None and p[1] == state and p[2] == data[1] and p[3] == None: #[None, i, i, None]
                    food_list.append(food)
                elif p[0] == None and p[1] == state and p[2] == None and p[3] == data[3]: #[None, i, None, i]
                    food_list.append(food)
                elif p[0] == None and p[1] == state and p[2] == data[1] and p[3] == data[3]: #[None, i, i, i]
                    food_list.append(food)
                elif p[0] == region and p[1] == None and p[2] == data[1] and p[3] == data[3]: #[i, None, i, i]
                    food_list.append(food)
                elif p[0] == region and p[1] == state and p[2] == None and p[3] == data[3]: #[i, i, None, i]
                    food_list.append(food)
                elif p[0] == region and p[1] == state and p[2] == data[1] and p[3] == None: #[i, i, i, None]
                    food_list.append(food)
                elif p[0] == region and p[1] == state and p[2] == data[1] and p[3] == data[3]: #[i, i, i, i]
                    food_list.append(food)
    food_list_s = sorted(food_list) #sort alphabetically
    return food_list_s #return sorted list
    
def main():  
    print("Indian Foods & Ingredients.\n") #print title          
    MENU = '''
        A. Input various foods and get the ingredients needed to make them!
        B. Input various ingredients and get all the foods you can make with them!
        C. Input various foods and ingredients and get the useful and missing ingredients!
        D. Input various foods and preferences and get only the foods specified by your preference!
        Q. Quit
        : '''
    file = open_file("indian_food") #call open_file function
    D = build_dictionary(file) #build dict from file
    while 1 == True:
        choice = input(MENU).upper() #prompt for a choice
        if choice == "A": 
            foods = input('Enter foods, separated by commas: ').strip().replace(" ","").split(",") #create food list
            ingredients = get_ingredients(D, foods) #use fuction to get ingredients
            ingredients = sorted(ingredients) #sort the set of ingredients
            print('Ingredients: ') #print title
            for i, ingredi in enumerate(ingredients): #print ingredients with a ", " end and no end for last
                if i < len(ingredients) - 1:
                    print(ingredi, end = ", ")
                else:
                    print(ingredi)
        elif choice == "B":
            ingredients = input('Enter ingredients, separated by commas: ').strip().replace(" ","").split(",") #create list of ingredients
            foods = get_list_of_foods(D, ingredients) #use function to get food list
            print('Foods: ') #print title
            for i, food in enumerate(foods): #print foods with a ", " end and no end for last
                if i < len(foods) - 1:
                    print(food, end = ", ")
                else:
                    print(food)
        elif choice == "C":
            foods = input('Enter foods, separated by commas: ').strip().replace(" ","").split(",") #create lits of foods
            pantry = input('Enter ingredients, separated by commas: ').strip().replace(" ","").split(",") #create list of pantry
            ingredients = get_useful_and_missing_ingredients(D, foods, pantry) #use the function to get tuple of ingredients
            print('Useful Ingredients: ') #print title
            have = ingredients[0] #ingredients have + need in tuple index 0
            for i, item in enumerate(have): #print haves with a ", " end and no end for last
                if i < len(have) - 1:
                    print(item, end = ", ")
                else:
                    print(item)
            print('Missing Ingredients: ') #print title
            buy = ingredients[1] #ingredients need to buy in tuple index 1
            for i, item in enumerate(buy): #print buys with a ", " end and no end for last
                if i < len(buy) - 1:
                    print(item, end = ", ")
                else:
                    print(item)
        elif choice == "D":
            preferences = input('Enter preferences, separated by commas: ').strip().replace(" ","").split(",") #create a list of preferences
            foods = get_food_by_preference(D, preferences) #use function to get a list of food
            print('Preferred Food: ') #print title
            for i, item in enumerate(foods): #print foods with a ", " end and no end for last
                if i < len(foods) - 1:
                    print(item, end = ", ")
                else:
                    print(item) 
        elif choice == "Q": #input Q to stop
            break
        else:
            print("Invalid input. Please enter a valid input (A-D, Q)") #input error code
            continue
    print("Thanks for playing!") #ending message

if __name__ == '__main__':
    main()
