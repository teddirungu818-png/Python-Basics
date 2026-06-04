"""
Control flows:
    -for loop
    -while loop
    
Funtions:
    -parametrized
    -non-parametrized
    -anonymous functions (lambda functions)
"""

# loops = > running iteration

fruits = ['apple', 'mango', 'pineapple', 'oranges', 'banana', 'coconut','avocado','tomatoe','dragon fruit', 'kiwi','watermelon','pawpaw', 'lime']

# for loop
for fruit in fruits:
    print(fruit.upper())
    pass # used as a placeholder when you have not implemented the logic yet but you want to avoid an error

fruits_two = fruits.copy()
while (len(fruits_two) <= len(fruits)):
    print(fruits)
    print(fruits_two)
    fruits_two.append("guavas")
    print(fruits_two)