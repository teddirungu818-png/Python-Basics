"""
    Control flows: 
        - if ... else
        - if ... elif...else
        - match
        - ternary operator ( {True} if condition else {False})
        - for loop
        - while loop 
    - Functions:
        - parameterized
        - non-parameterized
        - anonymous function (lambda functions)
"""

# if else
start = 0 
stop = 100
rest = 50

"""
- Key word => if
- condition => start < stop
"""
output = "" # global variable 

start += 102 # this is the same as start = start + 2
if start < stop:
    output = start
    start +=1
else: 
    output = "not equal to start" 


start = 10
stop = 110
rest = 60

start = 60
start = 111

if start < stop and start < rest: 
    output = start
    start +=1
elif start == rest:
    output = "Resting Phase"
else:
    output = "stop running"


# color_a = "white"
# color_b = "blue"
# color_c = "green"
# color_d = "red"

color_a = "red"
color_b = "green"
color_c = "white"
color_d = "white"

#  logical operators => and, or, not
output = (color_a == color_b)

output = (color_a == color_b) and (color_c == color_d) # and states that both scenarios must be staisfied for this to be True
output = (color_a == color_b) or (color_c == color_d) # or states that atleast one must be satisfied(True) to beTrue
output = not ((color_a == color_b) or (color_c == color_d)) # not implies negation

color = "yellow"

match color:
    case 'green':
        output ="Color is indeed GREEN"
    case 'red':
        ouput = "Color is RED"
    case 'black':
        ouput = "Color is RED"
    case 'gold':
        ouput = "Color is RED"
    case _: # default outcome
        output = "Color not found in Nations Flag!" 


x = 11
#scenario 1
if x == 10:
    output = "ten"
else:
    output = "not TEN"

output = "ten" if x == 10 else  "NOT ten" # scenario 2


"""
functions: 
This is a collection of statetments that achieve a specific goal i.e login, format text or convert to number
    - non-parameterized
    - parameterized
    - anonymous

Note: Should be single purposed not multi (BEST Practice)

"""

userOne = "John Doe"
userTwo = "Johanna Does"
userThree = "Does Johanna"
userFour = "Michael Schumar"

#  bad approach as it repeats code
print(userOne.upper())
print(len(userOne))
print(f"username: __{userOne[0:4]}__")

print(userTwo.upper())
print(len(userTwo))
print(f"username: __{userTwo[0:4]}__")

print(userThree.upper())
print(len(userThree))
print(f"username: __{userThree[0:4]}__")

print(userFour.upper())
print(len(userFour))
print(f"username: __{userFour[0:4]}__")

#  parametrized function: (takes up parameters), enable customization
def formatUserName(username):
    print(username.upper())
    print(len(username))
    print(f"username: __{username[0:4]}__")

#  good approach embracing functions henc has a single point of failure
formatUserName(userOne)
formatUserName(userTwo)
formatUserName(userThree)
formatUserName(userFour)

#  non- parameterized functions
#  defined a function
def greetings():
    print("Welcome ot Deepseek LAB!")

#  we call the function in order to use it
greetings()

#  anonymous function =>  it does not need an explicit implementation or rather a function definiton

x = lambda y: y + 10 # an anoymous function

uppercase = lambda text: text.upper() # scenario one 

# scenario two
def uppercaseTwo(text): 
    return text.upper() # the return statement aids in returning and outocme of the function logic

def formatUserName(username):
    print(username.upper())
    print(len(username))
    print(f"username: __{username[0:4]}__")

formatNewUser = lambda name: formatUserName(name)

output = x(10)
output = uppercase("welcome to the deepseek LAB 2026")
output = uppercaseTwo("welcome to the deepseek LAB 2026 awesome!")
output = formatNewUser("John Michael Schumarker II")

print("========================================")
print(output)
print("========================================")