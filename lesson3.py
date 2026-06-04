"""
Operators: 
    - Arithemtic (allow you ot perform mathematical operations)
    - comparison (reasoning)
    - Logic (reasoning)
    - assignment  (giving a variable new values)
    - bit wise operators (https://realpython.com/python-bitwise-operators/)
 
"""

# Arithmetic: *, +,-, /,//, **, % => operators

output = ""
num1 = 10 # operand
num2 = 11 # operand
output = num1 + num2 # addition
output = num1  - num2 # subraction
output = num1 * num2 # multiplication
output = num1 ** num1 # power 
output = num1 % num2 # modulus: returns the remainder
output = num1 / num2 # divison
output = num1 // num2 # floor divison - truncation

# comparison operators: basically does a compariosn and returns either true/ false => predicate
# ==, !=, >=, <=, !, <, >

firstName = "John"
lastName = "Doe"
output = firstName == lastName # equality sign
output = firstName != lastName # not equal sign 
number1 = 600
number2 = 300 
output = number1 < number2 # less than operator
output = number1 > number2 # greater than operator
output = number1 <= number2 # less than or equal to operator 
output = number1 >= number2 # greater than or equal to operator 

isLightOn = True 
output = not isLightOn # negation
 

# Boolean operators => and , or , not (ogten used when trying ot make decisions/ enable control flows)
# this is important when handling decisions within a system
firstName = "John"
lastName = "Doe" 
age = 20
dob = 1966
canVote = age>18
calculatedDob =2026 - 1966

# 'and' scenario applies a strict approach in comparisons i.e both cases must be true for the outcome to be true else false =>and is STRICT both must be true else false
output = canVote and (calculatedDob == age)

# 'or' scenario applies a not strict appraoch in the sense that atlast you must have one true for the outcome to be true
output = canVote or (calculatedDob == age) 

# 'not' it negates the outcome eg if outcome is to be True then outcome become False the opposite
output = not(canVote or (calculatedDob == age) )


# Arithmetic + asignemnt operartos: =, *=, +=,-=, /=,//=, **=, %= => assignemtn operatots operators
num1 = 10 # assignment operator equal sign
num2 = 11 # assignment operator equal sign
output = num1 + num2 # addition
num1 = num1 + num2
num1 += num2 # addition and assignment 
num1 -= num2 # subtraction and assignment
num1 *= num2 # subtraction and assignment
num1 *= 2
num1 = 3
num1 **= 2
num1 =12
num1 /= 2 # division retruns floating point number by default
num1 //= 2 # floating point number since the current value is still a floating point number 
num1 = int(num1)
# num1 //= 2 # floating point number since the current value is still a floating point number 
# num1 = 4
num1 = 11
num2 = 3
num1 %= num2 # gives us the remainder
output = num1


print("=======================================")
print(output)
print("=======================================")