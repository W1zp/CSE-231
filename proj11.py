# Project 11 Cse 231
#
# Algorithm
#  class Matrix(object):
#   def __init__(self, num_rows, num_cols)
#       default values for both is 2
#       create an array = matrix with row and cols value
#       if rows or col is neg print error message
#   def __str__(self):
#       prints the matrix as a string formatted with brackets, indents, and spaces
#   def __repr__(self):
#       calls the __str___ function
#   def __getitem__(self, iijj):
#       takes the index or indexs iijj and returns the value at that position
#       checks if index is an int or tuple of ints
#       prints error if indexes are neg or out of range or non int
#   def __setitem__(self, iijj, value):
#       does the indexes check like in __getitem__
#       changes the value of the matrix according to the indexes
#   def __add__(self, B):
#       checks if B is matrix and if the rows and cols values match
#       returns the result of adding the two matrixes
#   def dot_product(self, L1, L2):
#       checks if the two lists have equal lengths
#       finds the result of multipling and adding each value according to index
#       returns the result
#   def __mul__(self, B):
#       checks if multiplying is possible - equal len + is matrix
#       creates two lists based on rows and cols
#       creates a result matrix of the dot products and returns it
#   def transpose(self):
#       flips the rows and cols
#   def __eq__(self, B):
#       checks if B is matrix and if the rows and cols value match
#       checks if each value is equal and returns True
#       else will return False
#   def __rmul__(self, i):
#       checks if i is an int
#       multiplies each value in the matrix by the i and returns the new matrix

'''
    Maxtrix class with different functions. Functions: print str, get_item,
    set_item, add, dot_product, multiply, transpose, equal, and int multiply.
'''

class Matrix(object):
    def __init__(self,num_rows = 2,num_cols = 2): #default values are 2
        '''
            Initializes num_rows, num_cols, and array. Default value of num_rows and num_cols is 2.
            Array is a list of lists that represent each row in the matrix. If any num_rows or num_cols
            values are negative give a ValueError.
        '''
        self.num_rows = num_rows #create the row variable
        self.num_cols = num_cols #create the cols variable
        self.array = [[0] * self.num_cols for i in range(self.num_rows)] #create matrix based on rows and cols
        if num_rows < 0 or num_cols < 0: #if row or cols value is negative print error
            raise ValueError("Matrix: Error, the dimensions must be positive integers!")

    def __str__(self):
        '''
            Prints the matrix as a string. String needs to start with a "[" and each row is printed as
            a list without any "," serperating the values, each row is in a new line with a space in front.
            Last row ends with a "]". 
        '''
        rows = [str(row).replace(",", "") for row in self.array] #remove the "," from each list with the list
        str_out = "[" + rows[0] + "\n " #first row starts with a "[" in front
        index = 1 #ignores first row
        for i in range(1, len(self.array) - 1): #prints each row after first except last
            str_out += rows[i] + "\n " #each row is on a new line with a space in front
            index += 1 #counter for last row
        str_out += rows[index] + "]" #last row ends with a "]"
        return str_out #prints the string

    def __repr__(self):
        '''
            Returns the same string as __str__ by calling the function.
        '''
        Matrix.__str__(self) #call the __str__ function
    
    def __getitem__(self, iijj):
        '''
            Gets a value from within a matrix. Checks if iijj is an int or a tuple of ints. If iijj is an int then
            print the entire row according to the index. If iijj is a tuple of ints then extract the two indexes
            and print the specific value according to the index. If iijj not int or tuple of ints print ValueError.
            if i or i and j are negative or out of range print IndexError.
        '''
        if type(iijj) is int: #checks if input is just an int
            i = iijj - 1 #extracts the row index
            if i < 0: #if index is negative print error
                raise IndexError("Matrix: Error, bad indexing!")
            return self.array[i] #returns the entire row
        if type(iijj) is tuple: #check if input is a tuple
            if type(iijj[0]) is not int or type(iijj[0]) is not int: #makes sure the tuple is of ints
                raise ValueError("Matrix: Error, the indices must be a positive integer or a tuple of integers!")
            i = iijj[0] - 1 #extracts the index for row
            j = iijj[1] - 1 #extracts the index for cols
            if i < 0 or j < 0: #if index is negative print error
                raise IndexError("Matrix: Error, bad indexing!")
            if i > self.num_rows or i > self.num_cols: #if index is out of range print error
                raise IndexError("Matrix: Error, index out of range!")
            return self.array[i][j] #return the specific value according to rows and cols index
        if type(iijj) is not int or type(iijj) is not tuple: #if input is neither a int or tuple print error
            raise ValueError("Matrix: Error, the indices must be a positive integer or a tuple of integers!")
    
    def __setitem__(self, iijj, value):
        '''
            Sets a certain value in the matrix according to the given indexes. Checks if value is an int or a float.
            Does the same tuple checks as __getitem__. If value is not int or float or iijj is not a tuple of ints
            then print ValueError. If indexes are negative or out of range print IndexError.
        '''
        if type(value) is not int and type(value) is not float: #checks if value is an int or a float
                raise ValueError("Matrix: Error, You can only assign a float or int to a matrix!")
        if type(iijj) is tuple: #if input is a tuple
            if type(iijj[0]) is not int or type(iijj[0]) is not int: #check if the tuple is of ints or float
                raise ValueError("Matrix: Error, the indices must be a tuple of integers!")
            i = iijj[0] - 1 #extracts the row index
            j = iijj[1] - 1 #extracts the cols index
            if i < 0 or j < 0: #if indexes are negative print error
                raise IndexError("Matrix: Error, bad indexing!")
            if i > self.num_rows or i > self.num_cols: #if indexes are out of range print error
                raise IndexError("Matrix: Error, index out of range!")
            self.array[i][j] = value #change the value in the specificed matrix location
        if type(iijj) is not tuple: #if input is not a tuple print error
            raise ValueError("Matrix: Error, the indices must be a tuple of integers!")

    def __add__(self,B):
        '''
            Adds two matrixes together. Checks if what is being added is a matrix and if the rows and cols
            match up. Creates a result matrix and updates it according to the addition. Returns the result
            matrix.
        '''
        if type(B) != Matrix: #checks if what is being added is a matrix
            raise ValueError("Matrix: Error, you can only add a matrix to another matrix!")
        if self.num_rows != B.num_rows or self.num_cols != B.num_cols: #checks if rows and cols match up
            raise ValueError("Matrix: Error, matrices dimensions must agree in addition!")
        else:
            result = Matrix(self.num_rows, self.num_cols) #creates a result matrix
            for i in range(len(self.array)): #for each row
                for j in range(len(self.array[0])): #for each cols
                    result.array[i][j] = self.array[i][j] + B.array[i][j] #add the values according to index
            return result #return the result matrix

    def dot_product(self,L1,L2):
        '''
            Returns the dot product of two lists. Checks if the list lengths are equal. Multiples each
            value according to index then adds up the results. Returns the result.
        '''
        if len(L1) != len(L2): #checks for equal length
            raise ValueError("Dot Product: must be same length")
        else:
            result = 0 #sets result variable
            for i in range(len(L1)): #reads each index
                result += (L1[i] * L2[i]) #multiplies according to index and adds up the results
        return result #return the resulting number

    def __mul__(self,B):
        '''
            Multiples two matrixes. Checks if what is being multipled is a matrix and has the correct rows
            and cols. Creates a result matrix and upates the matrix according to the dot_product of each
            rows and cols. Returns the result.
        '''
        if type(B) != Matrix: #checks if what is being multiples is a matrix
            raise ValueError("Matrix: Error, you can only multiply a matrix to another matrix!")
        if len(self.array[0]) != len(B.array): #checks if A.cols = B.rows
            raise ValueError("Matrix: Error, matrices dimensions must agree in multiplication!")
        else:
            result = Matrix(len(self.array), len(B.array[0])) #creates result matrix based off A.rows and B.cols
            for i in range(len(self.array)): #for each row
                for j in range(len(B.array[0])): #for each cols
                    L1 = [] #list 1 for dot product
                    L2 = [] #list 2 for dot product
                    for k in range(len(self.array[0])): #for the num of cols
                        L1.append(self.array[i][k]) #take each value in row
                        L2.append(B.array[k][j]) #take each value in cols
                    result.array[i][j] = Matrix.dot_product(self,L1,L2) #put dot prodcut according to index
        return result #return the resutling matrix

    def transpose(self):
        '''
            Flips the rows and cols of the matrix.
        '''
        result = Matrix(len(self.array[0]), len(self.array)) #creates result matrix
        for i in range(len(self.array)): #for each row
            for j in range(len(self.array[0])): #for each col
                result.array[j][i] = self.array[i][j] #flip the values
        return result #return the resulting matrix

    def __eq__(self,B):
        '''
            Checks if two matrixes are equal to each other. Checks for if what is being compared
            is a matrix and if the rows and cols match up. Returns True or False.
        '''
        if type(B) == Matrix: #check if comparison is a matrix
            if self.num_rows == B.num_rows and self.num_cols == B.num_cols: #checks if rows and cols value match
                for i in range(len(self.array)): #for each row
                    for j in range(len(self.array[0])): #for each col
                        if self.array[i][j] != B.array[i][j]: #return false if any aren't equal
                            return False
                return True #return true if it passes all tests
        return False #false if not compared to matrix or non-matching rows and cols values

    def __rmul__(self,i):
        '''
            Does a scalar multiplication of the matrix. Checks if what is being multipled is an int.
            Returns resulting matrix.
        '''
        if type(i) is not int: #checks if input is an int
            raise ValueError("Matrix Error: scaler must be an int.")
        else:
            result = Matrix(self.num_rows, self.num_cols) #creates result matrix
            for k in range(len(self.array)): #for each row
                for j in range(len(self.array[0])): #for each col
                    result.array[k][j] = self.array[k][j] * i #multiply the value by i
            return result #return the resulting matrix
        