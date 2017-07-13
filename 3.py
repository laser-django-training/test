import random

list1 = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
list2 = [random.randint(100000, 999999) for x in range(26)]

phonebook = {x:y for x,y in zip(list1, list2)}

letter = input("enter letter: ")
print(phonebook[letter.upper()])


