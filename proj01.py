# Project #1 CSE 231
# 
# Algorithm
#  promtp for a rod input
#  convert to float number
#   convert to meters
#   convert to feet
#   convert to miles
#   convert to furlongs
#   convert to minutes
#    display all values

num_rods = input('Input rods: ') # ask for rod input
num_rods = float(num_rods) # convert to float number


num_meters = num_rods * 5.0292 # multiply rods by 5.0292
num_feet = num_meters / 0.3048 # divide meters by 0.3048
num_miles = num_meters / 1609.34 # divide meters by 1609.34
num_furlongs = num_rods / 40 # divide rods by 40
num_time = num_miles * 60 / 3.1 # divide mile by 3.1 for hours then multiply 60 

print('You input', num_rods,'rods.') # print number of rods
print('\nConversions') # make spacing and label for conversions
print('Meters:',round(num_meters, 3)) # print conversions and round to 3
print('Feet: ',round(num_feet, 3))
print('Miles:',round(num_miles, 3))
print('Furlongs:',round(num_furlongs, 3))
print('Minutes to walk',num_rods,'rods:',round(num_time,3))
