# Project 10 CSE 231
#
# Algorithm
#  def initialize()
#   creates 10 lists for each column and deals 5 cards to each
#   last 2 cards are added to the middle of cells list
#   returns tableau list, foundation list, and cells list
#  def display(tableau, foundation, cells)
#   displays the current state of the game
#   displays the tableau list in columns + foundation and cell list
#  def get_option()
#   prompts the user for an option input and returns error if wrong input
#  def validate_MTT
#   validates if card move between tableau is valid
#   returns a bool
#  def validate_MCT
#   validates if card move from cell to tableau is valid
#   returns a bool
#  def validate_MTC
#   validates if card move from tableau to cell is valid
#   returns a bool
#  def validate_MTF
#   validates if card move from tableau to foundation is valid
#   returns a bool
#  def validate_MCF
#   validates if card move from cell to foundation is valid
#   returns a bool
#  def move_MTT
#   card move between tableaus
#   returns a bool
#  def move_MCT
#   card move from cell to tableau
#   returns a bool
#  def move_MTC
#   card move from tableau to cell
#   returns a bool
#  def move_MTF
#   card move from tableau to foundation
#   returns a bool
#  def move_MCF
#   card move from cell to foundation
#   returns a bool
#  def check_for_win(foundation)
#   checks if the foundation lists are full
#   assumes list is in correct order and returns bool
#  def main()
#   prints header + initilizes the tableau, foundation, and cell
#   displays the game at start and prints menu
#   while loop
#       checks for win + if win then prints win message and restarts game
#       prompts for option input
#       if "R" then restart game
#       if "Q" then break the loop
#       if "H" then reprint the menu
#       if None then keep reloopping
#       if statements for each function
#           if function is true
#               check win if win then continue
#               else display the board
#           else print input error message
#   if loop break then print end message
#
# Solitaire: Seahaven

#DO NOT DELETE THESE LINES
import cards, random
random.seed(100) #random number generator will always generate 
                 #the same random number (needed to replicate tests)

MENU = '''     
Input options:
    MTT s d: Move card from end of Tableau column s to end of column d.
    MTC s d: Move card from end of Tableau column s to Cells d.
    MCT s d: Move card from Cells s to end of Tableau column d.
    MTF s d: Move card from end of Tableau column s to Foundation d.
    MCF s d: Move card from end of Cell s to Foundation d.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game       
'''

def initialize():
    '''
        Uses the imported card class to create a deck of cards. Shuffles the cards and creates a list for
        foundation, cells, and tableau. Tableau is a list of 10 lists each dealt 1 card in order. The last
        two cards in the deck is put in the middle of cells list. Returns tableau list, foundation list, and
        cells list.
    '''
    stock = cards.Deck() #grab deck of cards
    stock.shuffle() #shuffle deck of cards
    foundation = [[],[],[],[]] #4 lists - hearts, spades, diamonds, clubs
    cells = [None, None, None, None] #empty cells list
    tableau = [] #list for tableaus
    for i in range(10): #a list of 10 lists (columns)
        tableau.append([])
    for n in range(5): #for each of the 5 rows
        for i in range(10): #append 1 card at a time
            tableau[i].append(stock.deal())
    cells[1] = stock.deal() #last 2 cards put in cells
    cells[2] = stock.deal()
    return tableau, foundation, cells #return tableau, foundation, cells

def display(tableau, foundation, cells):
    '''Display the cell and foundation at the top.
       Display the tableau below.'''
       
    print("\n{:<11s}{:^16s}{:>10s}".format( "foundation","cell", "foundation"))
    print("{:>14s}{:>4s}{:>4s}{:>4s}".format( "1","2","3","4"))
    for i,f in enumerate(foundation):
        if f and (i == 0 or i == 1):
            print(f[-1],end=' ')  # print first card in stack(list) on foundation
        elif i == 0 or i == 1:
            print("{:4s}".format( " "),end='') # fill space where card would be so foundation gets printed in the right place
    print("{:3s}".format(' '),end='')
    for c in cells:
        if c:
            print(c,end=' ')  # print first card in stack(list) on foundation
        else:
            print("[  ]",end='') # fill space where card would be so foundation gets printed in the right place
    print("{:3s}".format(' '),end='')
    for i,f in enumerate(foundation):
        if f and (i == 2 or i == 3):
            print(f[-1],end=' ')  # print first card in stack(list) on foundation
        elif i == 2 or i == 3:
            print("{}{}".format( " ", " "),end='') # fill space where card would be so foundation gets printed in the right place
        
    print()
    print("\ntableau")
    print("   ",end=' ')
    for i in range(1,11):
        print("{:>2d} ".format(i),end=' ')
    print()
    # determine the number of rows in the longest column        
    max_col = max([len(i) for i in tableau])
    for row in range(max_col):
        print("{:>2d}".format(row+1),end=' ')
        for col in range(10):
            # check that a card exists before trying to print it
            if row < len(tableau[col]):
                print(tableau[col][row],end=' ')
            else:
                print("   ",end=' ')
        print()  # carriage return at the end of each row
    print()  # carriage return after printing the whole tableau
    
        
def validate_move_within_tableau(tableau,src_col,dst_col): #MTT s d, src_col = remove column, dst_col = place column
    '''
        Validates if the card moved between tableau is a king or in the same suit
        and 1 lower. Returns True or False (Bool).
        ! Empty tableau can only have a king moved to it
        ! Can only be moved if card is in same suit
        ! Moved card has to be 1 lower
    '''
    if len(tableau[src_col]) == 0: #no cards to be moved, empty list
        return False
    elif len(tableau[dst_col]) == 0: #if the move to column is empty
        if tableau[src_col][-1].rank() == 13: #if the card placed is a king
            return True
    elif tableau[src_col][-1].rank() == (tableau[dst_col][-1].rank() - 1): #placed card has to be 1 less
        if tableau[src_col][-1].suit() == tableau[dst_col][-1].suit(): #has to be same suit
            return True
    return False

def validate_move_cell_to_tableau(tableau,cells,cell_no,dst_col): #MCT s d, cell_no = cell num, dst_col = place column
    '''
        Validates if card in cell moved to tableau is in the same suit and 1
        lower. Returns True or False (Bool).
        ! Empty tableau can only have a king in it
        ! Can only be moved if card is in same suit
        ! Moved card has to be 1 lower
    '''
    if cells[cell_no] == None: #no cards to be moved, empty list
        return False
    elif len(tableau[dst_col]) == 0: #if tableau is empty
        if cells[cell_no].rank() == 13: #can only place a king card
            return True
    elif cells[cell_no].rank() == (tableau[dst_col][-1].rank() - 1): #card has to be 1 higher than in_card
        if cells[cell_no].suit() == tableau[dst_col][-1].suit(): #card has to be same suit as in_card
            return True
    return False

def validate_move_tableau_to_cell(tableau,cells,src_col,cell_no): #MTC s d, src_col = remove column, cell_no = cell num
    '''
        Validates if card moved from tableau to cell is valid and returns True
        or False (Bool).
        ! Cell has to be empty for move to be valid
    '''
    if len(tableau[src_col]) == 0: #no cards to be moved, empty list
        return False
    elif cells[cell_no] == None: #can only move card if cells slot is empty
        return True
    return False

def validate_move_tableau_to_foundation(tableau,foundation,src_col,found_no): #MCT s d, cell_no = cell num, dst_col = place column
    '''
        Validates if card moved from tableau to foundation is one higher and in
        the same suit. Returns True or False (Bool).
        ! Has to start with an Ace
        ! Goes up in order and has to be in the same suit
    '''
    if len(tableau[src_col]) == 0: #no cards to be moved, empty list
        return False
    elif len(foundation[found_no]) == 0: #if foundation list is empty
        if tableau[src_col][-1].rank() == 1: #first card has to be an ace
            return True
    elif (foundation[found_no][-1].rank() + 1) == tableau[src_col][-1].rank(): #card has to be 1 higher than in_card
        if foundation[found_no][-1].suit() == tableau[src_col][-1].suit(): #card has to be same suit as in_card
            return True
    return False

def validate_move_cell_to_foundation(cells,foundation,cell_no,found_no): #MCF s d, cell_no = cell num, found_no = found num
    '''
        Validates if card moved from cell to foundation is one above and in the
        same suit. Returns True or False (Bool).
        ! Has to start with an Ace
        ! Goes up in order and has to be in the same suit
    '''
    if cell_no > 4 or cell_no < -4: #a list of 4 cards, index can't be greater than 4 or less than -4
        return False
    elif cells[cell_no] == None: #no cards to be moved, empty list
        return False
    elif len(foundation[found_no]) == 0: #if foundation list is empty
        if cells[cell_no].rank() == 1: #first card has to be an ace
            return True
    elif (foundation[found_no][-1].rank() + 1) == cells[cell_no].rank(): #card has to be 1 higher than in_card
        if foundation[found_no][-1].suit() == cells[cell_no].suit(): #card has to be same suit as in_card
            return True
    return False
    
def move_within_tableau(tableau,src_col,dst_col): #MTT s d, src_col = remove column, dst_col = place column
    '''
        Moves cards between tableau columns. Calls validate function to test
        if move is allowed. Returns True after moving the card or False if the
        move is not valid.
    '''
    if validate_move_within_tableau(tableau, src_col, dst_col) == True: #if valid is true
        card = tableau[src_col].pop(-1) #take out the card
        tableau[dst_col].append(card) #put the card in new tableau
        return True
    return False

def move_tableau_to_cell(tableau,cells,src_col,cell_no): #MTC s d, src_col = remove column, cell_no = cell num
    '''
        Moves card from tableau column to cell. Calls validate function to test
        if move is allowed. Returns True if successful and False if the move is 
        not valid.
    '''
    if validate_move_tableau_to_cell(tableau, cells, src_col, cell_no) == True: #if valid is true
        card = tableau[src_col].pop(-1) #takes last card in column
        cells[cell_no] = card #puts the card in cells slot
        return True
    return False
        
def move_cell_to_tableau(tableau,cells,cell_no,dst_col): #MCT s d, cell_no = cell num, dst_col = place column
    '''
        Moves card from cell to tableau. Calls validate function to test if move
        is allowed. Returns True if successful or False if move is not valid.
    '''
    if validate_move_cell_to_tableau(tableau, cells, cell_no, dst_col) == True: #if valid is true
        card = cells[cell_no] #take the card out
        cells[cell_no] = None #replace the card with None
        tableau[dst_col].append(card) #put the card in tableau
        return True
    return False

def move_cell_to_foundation(cells,foundation,cell_no,found_no): #MCF s d, cell_no = cell num, found_no = found num
    '''
        Moves card from cell to foundation. Calls validate function to test if 
        move is valid. Returns True after moving the card or False if move is
        not valid.
    '''
    if validate_move_cell_to_foundation(cells, foundation, cell_no, found_no) == True: #if valid is true
        card = cells[cell_no] #take the card out
        cells[cell_no] = None #replace the card with None
        foundation[found_no].append(card) #put the card in foundation list
        return True
    return False
            
def move_tableau_to_foundation(tableau,foundation,src_col,found_no): #MTF s d, src_col = remove column, found_no = found num
    '''
        Moves card from tableau to foundation. Calls the validate function to test
        if the move is valid. Returns True after moving the card or False if the
        move is invalid.
    '''
    if validate_move_tableau_to_foundation(tableau, foundation, src_col, found_no) == True: #if valid is true
        card = tableau[src_col].pop(-1) #takes last card in column
        foundation[found_no].append(card) #puts the card in the foundation list
        return True
    return False
                    
def check_for_win(foundation):
    '''
        Checks if each foundation is filled up to king with their respective suits.
        Returns True for completion or False if not completed.
    '''
    if len(foundation[0]) == 13 and len(foundation[1]) == 13 and len(foundation[2]) == 13 and len(foundation[3]) == 13:
        return True #if all lists are full and correct
    return False

def get_option():
    '''Prompt the user for an option and check that the input has the 
       form requested in the menu, printing an error message, if not.
       Return:
    MTT s d: Move card from end of Tableau column s to end of column d.
    MTC s d: Move card from end of Tableau column s to Cells d.
    MCT s d: Move card from Cells s to end of Tableau column d.
    MTF s d: Move card from end of Tableau column s to Foundation d.
    MCF s d: Move card from Cells s to Foundation d.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game        
    '''
    option = input( "\nInput an option (MTT,MTC,MCT,MTF,MCF,R,H,Q): " )
    option_list = option.strip().split()
    
    opt_char = option_list[0][0].upper()
    
    if opt_char in 'RHQ' and len(option_list) == 1:  # correct format
        return [opt_char]

    if opt_char == 'M' and len(option_list) == 3 and option_list[1].isdigit() \
        and option_list[2].isdigit():
        opt_str = option_list[0]
        if opt_str in ['MTT','MTC','MCT','MTF','MCF']:
            return [opt_str,int(option_list[1]),int(option_list[2])]

    print("Error in option:", option)
    return None   # none of the above
 
def main():
    print("\nWelcome to Seahaven Solitaire.\n") #header
    tableau, foundation, cells = initialize() #initialize tableau list, foundation list, and cells list
    display(tableau, foundation, cells) #display the start of the board
    print(MENU) #print options menu
    while 1 == True: #while loop
        check_for_win(foundation) #checks for win condition
        if check_for_win(foundation) == True: #if won
            print("You won!") #print winning message
            display(tableau, foundation, cells) #display the winning board
            print("\n- - - - New Game. - - - -") #print header
            tableau, foundation, cells = initialize() #reinitialize new lists
            display(tableau, foundation, cells) #display the new game board
            print(MENU) #print menu
            continue #keep relooping
        option = get_option() #prompt for an option input
        if option == None: #wrong input then keep relooping
            continue
        if option == ["R"]: #if input is R
            tableau, foundation, cells = initialize() #reset the lists
            display(tableau, foundation, cells) #display the new game board
            print(MENU) #print the menu
            continue #keep relooping
        elif option == ["Q"]: #if input is Q
            break #stop the looping
        elif option == ["H"]: #if input is H
            print(MENU) #reprint the menu
        elif option[0] == "MTT": #if MTT is inputted
            if move_within_tableau(tableau, option[1] - 1, option[2] - 1) == True: #run the function
                if check_for_win(foundation) == True: #if win then go back to top of loop
                    continue
                else:
                    display(tableau, foundation, cells) #if not then display current board
            else: #if function error then print error message
                print("Error in move: {:s} , {:d} , {:d}".format(option[0], option[1], option[2]))
        elif option[0] == "MTC": #if MTC is inputted
            if move_tableau_to_cell(tableau, cells, option[1] - 1, option[2] - 1) == True: #run the function
                if check_for_win(foundation) == True: #if win then go back to top of loop
                    continue
                else:
                    display(tableau, foundation, cells) #if not then display current board
            else: #if function error then print error message
                print("Error in move: {:s} , {:d} , {:d}".format(option[0], option[1], option[2]))
        elif option[0] == "MCT": #if MCT is inputted
            if move_cell_to_tableau(tableau, cells, option[1] - 1, option[2] - 1) == True: #run the function
                if check_for_win(foundation) == True: #if win then go back to top of loop
                    continue
                else:
                    display(tableau, foundation, cells) #if not then display current board
            else: #if function error then print error message
                print("Error in move: {:s} , {:d} , {:d}".format(option[0], option[1], option[2]))
        elif option[0] == "MTF": #if MTF is inputted
            if move_tableau_to_foundation(tableau, foundation, option[1] - 1, option[2] - 1) == True: #run the function
                if check_for_win(foundation) == True: #if win then go back to top of loop
                    continue
                else:
                    display(tableau, foundation, cells) #if not then display current board
            else: #if function error then print error message
                print("Error in move: {:s} , {:d} , {:d}".format(option[0], option[1], option[2]))
        elif option[0] == "MCF": #if MCF is inputted
            if move_cell_to_foundation(cells, foundation, option[1] - 1, option[2] - 1) == True: #run the function
                if check_for_win(foundation) == True: #if win then go back to top of loop
                    continue
                else:
                    display(tableau, foundation, cells) #if not then display current board
            else: #if function error then print error message
                print("Error in move: {:s} , {:d} , {:d}".format(option[0], option[1], option[2]))
    print("Thank you for playing.") #Endding message

if __name__ == '__main__':
    main()