# Project 04 CSE 231
#
# Function decode_char(ch,shift)
#   if ch is not a letter, return it
#   find index of ch, let's name it index
#   use index to find the decode index - use equation in project description
#   return that index
# Function get_shift(s,ignore)
#   find the most common char
#   if more than one go by alphabet
#   ignore the first ch and test the others
#   return int.ch
# Function output_plaintext(s,shift)
#   output the text using the shift
#   use decode_char to decode each letter
#   begin output with a blank line
#   display string
# Function main()
#   prompt for an input cipher-text string
#   get a key - decode_char
#   display the plaintext - output_plaintext
#   ask if readable
#       if not "no" print message
#       if "no" add the ch to the ignore string and go back to "get a key"

import string  #string for uppercase letters

def decode_char(ch,shift): #decode text function
    letters = string.ascii_uppercase
    if ch.isalpha(): #if/else for alphabet or other
        position = letters.find(ch) #encrypted position
        new_position = (position + shift) % 26 #decrypted position
        new_ch = letters[new_position] #decrypt character
        return new_ch 
    else:
        return ch
        
def get_shift(s,ignore): #function to find the shift
    letters = string.ascii_uppercase
    max_count = 0
    for index, ch in enumerate(letters): #ch in input
        if ch in ignore: #ignores certain chars
            continue
        else:
            count = s.count(ch) #most common char
            if count > max_count: #if bigger count
                max_count = count #replace count
                max_ch = ch #store the max count char
                shift = letters.index("E") - letters.index(ch) #find shift
    return shift, max_ch 
    
def output_plaintext(s,shift): #function to output the decoded text
    result = ""
    for ch in s: #decode each char in input
        result = result + decode_char(ch,shift) #decoded message
    return result
    
def main(): #main function
    print("Cracking a Caesar cypher.") #introduction/title
    s = input("\nInput cipherText: ").upper() #prompt for code input
    ignore = "" 
    key,ch = get_shift(s,ignore) #get the shift and max ch
    shift = key 
    ignore = ch #put max ch into ignore
    result = output_plaintext(s,shift) #get the result with the shift
    print("\n" + result) #print result
    again = input("\nIs the plaintext readable as English? (yes/no): ") #ask again?
    while again == "no": #if no then decrypt again
        shift, ch = get_shift(s,ignore) 
        ignore += ch
        result = output_plaintext(s,shift)
        print(result)
        again = input("\nIs the plaintext readable as English? (yes/no): ")
    else:
        print("\nDone.")

# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main()