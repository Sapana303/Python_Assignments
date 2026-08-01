# Question 1: Invert a Dictionary
# Problem:
# Given a dictionary where all values are unique, 
# return a new dictionary where the keys and values are swapped.

# Input: {"a": 1, "b": 2, "c": 3}
# Output: {1: "a", 2: "b", 3: "c"}

# Question 2: Filter Dictionary by Value
# Problem:
# Given a dictionary of product names and their prices, 
# return a new dictionary containing only the products 
# with a price greater than a given threshold.

# Input: products = {"pen": 8, "cup": 35, "bag": 2, "box": 70}
# threshold = 15
# Output: {"cup": 35, "box": 70}

# Question 3 (Basic-Medium): Count Vowels and Consonants
# Problem:
# Given a string, return a dictionary with two keys,
# "vowels" and "consonants", showing the count of each in 
# the string. Ignore spaces, digits, and punctuation. 
# Treat the input as lowercase letters only.

# Input: "hello world"
# Output: {"vowels": 3, "consonants": 7}


# Question 4: Find All Keys with Maximum Value
# Problem:
# Given a dictionary of item names and their quantities, 
# return a list of all item names that have the highest quantity.
# If there's a tie, include all of them (sorted alphabetically).

# Input: {"marker": 90, "pen": 10, "box": 90,  "sharpener": 5}
# Output: ["box", "marker"]

# Question 5: Sum of Values in a Dictionary
# Problem:
# Given a dictionary of expenses (category → amount), 
# return the total sum of all amounts.

# Input: {"food": 200, "rent": 1000, "household": 150, "others": 300}
# Output: 1650

# Question 6 : Common Keys Between Two Dictionaries
# Problem:
# Given two dictionaries,
# return a sorted list of keys that exist in both dictionaries.

# Input: dict1 = {"a": 1, "b": 2, "c": 3}
#        dict2 = {"b": 5, "c": 6, "d": 7}
# Output: ["b", "c"]




# 1
# Invert a dictionary in Python means to swap its keys and values.
# like {key:value} to {value:key}
n = int(input())
dict = {}
for i in range(1,n+1):
    dict[i] = input()

print(*dict.items())
inv_dict = {}
for key, value in dict.items():
    inv_dict[value] = key

print(*inv_dict.items())

# dict items= (1, 'sanu') (2, 'sanu') (3, 'kanu') (4, 'kanu')
# inv_dict items= ('sanu', 2) ('kanu', 4)
# ** inverse dict took only unique values and their last key as value in inverse dict


# 2
# filter dictionary by value
n = int(input("Enter no of products:"))

dict = {}
for _ in range(n):
    details = input().split()
    # when we have long name of product like input -> Apple iphone 13 pro max 45000 then we have two extract whole except the last price
    product = ' '.join(details[:-1]) # join all the words except the last one for product name
    price = int(details[-1])
    # product = details[0] #if only two words in input like "Apple" 45000 then we ca extract like this using 0, 1 index
    # price = int(details[1])
    #print(product,price)
    dict[product] = price

print(dict) # print dictionary
# print(*dict.items()) # print dict items in tuple format
# for product, price in dict.items(): # will iterate through all the items in dictionary and unpack them into product and price variables
#     print(f"{product} : {price}")

# creating new dictionary with only those products whose price is greater than threshold
# new_dict = {}
threshold = int(input("Enter threshold: "))
# for product, price in dict.items():
#     if price > threshold:
#         new_dict[product] = price

# print(*new_dict.items())

# updating the existing dictionay only keeping items above threshold
for product, price in dict.items():
    if price <= threshold:
        del dict[product]

print(*dict.items())


# 3. 
# counting vowels and cosonants in a string and storing in dictionary
s = input("string:")
s = s.lower()
# removing punctuations
for char in s:
    if char in "!@#$%^&*()-+":
        s = s.replace(char, "")

dict = {}
vow_count = 0
cons_count = 0
for ch in s:
    if ch in "aeiou":
        vow_count += 1
    elif ch.isalpha(): # check if character is alphabet if we direct use else the will count spaces also in consonants
        cons_count += 1

dict["vowels"] = vow_count
dict["consonants"] = cons_count
print(*dict.items())

# Using dictionary directly
dict_cnt = {"Vowels": 0, "Consonants": 0}
for ch in s:
    if ch.isalpha():
        if ch in "aeiou":
            dict_cnt["Vowels"] += 1
        else:
            dict_cnt["Consonants"] += 1

print(*dict_cnt.items())

# using defaultdict 
from collections import defaultdict
dict_cnt = defaultdict(int)

vowels = "aeiou"

for ch in s:
    if ch.isalpha():
        if ch in vowels:
            dict_cnt["Vowels"] += 1
        else:
            dict_cnt["Consonants"] += 1

print(*dict_cnt.items())


# 4.
# find all keys with maximum value
from numpy import sort
item = {
    "marker" : 90,
    "pen" : 10,
    "box" : 90,
    "sharpner" : 5,
    "eraser": 90
}

# item = {
#     "marker" : 90,
#     "Pen" : 10,
#     "box" : 90,
#     "sharpner" : 5,
#     "Eraser": 90   # Eraser is capital so it will come first in sorted order
# }

max_values = max(item.values())# max() return the maximum value from the values of dictionary
l = []
for key, value in item.items():
    if value == max_values:
        l.append(key)
print(l)
l.sort() 
print(l)


## 5.
## sum of values in dictionary
item = {
    "food" : 100,
    "drink" : 2000,
    "rent": 6500,
    "transport" : 3000
}

print(sum(item.values()))

# total = 0
# for value in item.values():
#     total += value
# print(total)


## 6.
## common keys beween two dictionaries
dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {'b':4, 'c':5, 'd':6}
l = []

for key in dict1.keys():
    if key in dict2.keys():
        l.append(key)
l.sort()
print(l)
print(*l)