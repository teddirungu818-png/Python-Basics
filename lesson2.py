"""
Rational:   
    - we are dealing a program that is meant to run inside a machine
    - data is transformed in machine code and stored or logic enacted on it
    - different data types occupy different spaces in memory (memory is limited)
    - we have two core types of variables:
        - local (restarined in a particular section)
        - global (can be accesed throughout the entire program)
    
DATA TYPES: 
- Text (strings)
- Numbers(Integer, Float, complex)
- Lists (set, array, tuple, dictionary) # basic data structures
"""

# Strings 
"""
- collections of characters wrapped inside either single quotes or double quotes
- a string is but an array/ collection/ list of character => you can access each element
- they stem from the class str() implies  <class 'str'>
- each and evry class contains its own methods(function that resides inside a class)
- We can slice strings into sections, slicing => think of a rectangular cake that is compsed of more than one 
flavor your favorite flavor is at the center, you will slice and pick only your favorite part
"""

userName = "John Doe" # string defined with double quotes
lastName = 'Lenny Lonovo' # string defined with single quotes

output ="" # global variable

output = type(userName) # redefining the value of output and getting the data type of userName
output = type(lastName)
output = userName # redefining the variable userName
userName = "WonderLand"
output = userName # redefining the variable userName

# accesing elements in a string
userName = "Wikipedia" # has element inside it the elements are characters eg 'W', 'i', 'k', 'i'
# an index is a positional integer that start from 0 - n-1, n being the size of that list
output = len(userName) # returns the size of the word
output = userName[1] 
output = userName[-1] 
userName = "Wikipedia-"# a space is also regarded as a character use this for ref: https://www.asciitable.com/
output = len(userName) # returns the size of the word
output = userName[-10]
output = userName[3:] # slicing start at position 3 till the end
output = userName[3: 6] # slicing starts from positoin 3 and ends at position 5 which is 6-1
output = userName[3: 8] # slicing starts from positoin 3 and ends at position 7 which is 7-1 
output = userName[3: 8: 2] # slicing starts from positoin 3 and ends at position 7 which is 7-1 and with a step of 2

output = userName[3: 8: 2].upper() # we are using a string method called upper() => converts to uppercase
output = output.lower()

output = userName.find('-') # searches for a particur character
output = userName.count('i')  # brings the number of occurences of a character i

#note: A string character is immutable
# userName[0] = 'Q' # this evokes an error since strings are immutable

# when performing a search process in a string it is fastest to search using index as opposed to looping through it
userName = "Webopedia"
wikiText = "Wikipedia[e] is a free online encyclopedia written and maintained by a community of volunteers, known as Wikipedians, through open collaboration and the wiki software MediaWiki. Founded by Jimmy Wales and Larry Sanger in 2001, Wikipedia has been hosted since 2003 by the Wikimedia Foundation, an American nonprofit organization funded mainly by donations from readers.[1] Wikipedia is the largest and most read reference work in history.[2][3]"
# for i in wikiText:
#     print(i)

# output = wikiText[0]

pageName ="Wikipedia"
output = pageName[3:8:3]
wikiText = """
Wikipedia[e] is a free online encyclopedia written
 and maintained by a community of volunteers, 
 known as Wikipedians, through open collaboration and
  the wiki software MediaWiki. Founded by Jimmy Wales and 
  Larry Sanger in 2001, Wikipedia has been hosted since 2003 
  by the Wikimedia Foundation, an American nonprofit organization 
  funded mainly by donations from readers.[1] Wikipedia is the largest and most read reference work in history.[2][3]
"""
output = wikiText

pageName = "Youtube"
output = pageName[-2]

statement = 'The puppy is John\'s' # SyntaxError: unterminated string literal (detected at line 99), the remedy is to add an excae character before the 2nd quotation mark
statement = "The puppy is John's" # this is another rememdey => preferred
statement = "The puppy \n \bis \bJohn's"
output = statement

# Numbers(Integer, Float, complex)
"""
- Integers are whole numbers  that span from 0 to +ve infinity and  0 to -ve infinity
- Integers stem from athe int() class: <class 'int'>
- can be subjected to mathematical computations
"""

age = 10

output = type(age) # getting the data type

age = age + 1 # summation
age += 1 
output = age 

output = type(age) # getting the data type
age = str(age) # casting the integer value of age into a string
output = type(age) # getting the data type
age = int(age) # cast bck to int
output = age
output = type(age) # getting the data type


"""
- Float are fractions/ numbers with decimals 
- the more the decimal points the more the better accuracy eg location info eg latitude and longitude => if you 37.56(ambigous) and 37.567890 (more accurate)
- Float stems from the float() class: <class 'float'>
- can be subjected to mathematical computations
"""


weight = 20.75
output =type(weight)
output = int(weight) # perfoms a truncation of the data 
output = float(200) # converted into a floating point data type
"""
- Complex number are often encounted in mathematical situations / approximations => computation technics or numerical analysis
- Complex data types stem from the complex() class:  <class 'complex'>
"""

output = complex(2)
output = 200j # the character j represents complex
output = type(output)


print("=====================================")
print(output)
print("=====================================")

 

"""
Summary: 
    - Python is an object oriented programming language, imlying that when we create variables we are basically creating instances of things
"""