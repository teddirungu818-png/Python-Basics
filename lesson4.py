"""
Lists:
    - data structure (how do i store items in an efficient(time & space) manner?)
    - Types:
        - tuples
        - dictionary
        - array/ lists
        - set 
    - each data type has its respective methods 

"""
output ="" # global variable
"""
Array: 
    - can be composed of different data types
    - enclosed in a square bracket []
    - each item is accessed via an index
    - class type is a list: <class 'list'>
    - lists are mutable in nature
"""

# array
# fruits = ['apple', 'mango', 'pineapple', 1,2,3,4] # not best practice to have multiple data types
fruits = ['apple', 'mango', 'pineapple', 'oranges', 'banana', 'coconut','avocado','tomatoe','dragon fruit', 'kiwi','watermelon','pawpaw', 'lime']
output = fruits

# methods
fruits.pop() # remove last item
fruits.sort() # sorts in ascending
fruits.remove("pawpaw") # removing targeted item from the list 
fruits.append("sweet bananas")#adds an item to the end of the list
fruits.insert(0, "grapes") # adds an item at a specific position in
fruits.sort() # sorts in ascending

# loop (used to iterate through lists)
# for fruit in fruits:
#     print(fruit)

output = output[3] # accessing via index

output = fruits 
output = type(output)
fruits[0] = "Green Apples" # lists are mutable in nature

output = fruits

"""
Tuple: 
    - can be composed of different data types
    - enclosed in a parentheses ()
    - class type: <class 'tuple'>
    - immutable in nature (cannot update them)
"""

clouds = ('nimbus', 'cirrus', 'cumulus', 'startus')

output = clouds
output = type(clouds)
# clouds[0]='NIMBUS' # TypeError: 'tuple' object does not support item assignment => immutability
output = clouds[0].upper()

output = clouds.index('cumulus') # index of the item


"""
Set: 
    - composed of unique items
    - enclosed in a curly braces {}
    - you can perform set operations on them (union, intersection, difference,disjoint etc.)
    - class type: <class 'set'> 
    - methods: (https://www.w3schools.com/python/python_ref_set.asp)
"""
uniqueNumbers = {1,11,0,0,0,1,2,3,4,5,6,7,7,7,7,8,8,8,9,9,9,9,10,10,10}
output = uniqueNumbers # set only returns unique items in an organized manner (not in the order they were added)
output = type(uniqueNumbers)
fruits = {'apple', 'apple', 'apple', 'mango','mango','mango','mango','mango', 'pineapple',  'pineapple',  'pineapple',  'pineapple', 'oranges', 'banana',}
output = fruits

"""
Dictionary:
     - composed of key value pairs
     - key is often in string form nad can be numbers as well
     - enclosed in a curly braces {}
     - class type: <class 'dict'>
     - we use keys to access values
     - methods: (https://www.w3schools.com/python/python_ref_dictionary.asp)

    """
Student = {
    "name": "Tedd Irungu",
    "age": 18,
    "course": "AI for Software Developers"
}

output = Student
output = Student.get("age")
output = Student.clear()
examiner = ("Tedd Irungu", "John Doe", "Jane Doe")

output = "Tedd Irungu" in examiner # membership operator => checks if an item is in a list and returns either true or false






print("=======================================")
print(output)
print("=======================================")