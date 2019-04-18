# This function takes the range of the list inputted
# and assigns it to its own dictionary. It then makes a set of the range
# and assigns it to another dictionary. Lastly, it returns a boolean comparing
# the dictionaries lengths. If our function is one to one, then both dictionaries
# will have the same length.
def is_injective(list1):
    rang = (list1.values())
    comp = []

    for element in rang:
        if element not in comp:
            comp.append(element)

    return len(comp) == len(list1)

# This function takes a list representing a function with the domain
# as its ______ and its range as its dictionary values
# It appends all values in the codomain that aren't in the range
# and adds them to a new dictionary
# Finally, it returns true if no values were appended onto that list,
# meaning there were no values in our codomain not in the range

def is_surjective(list1, codo):
    rang = (list1.values())
    comp = []

    for value in codo:
        if value not in rang:
            comp.append(value)

    return len(comp) == 0

# A function is bijective if it is surjective and injective
# This function makes use of my other functions and just runs
# the input through both and returns a clause boolean

def is_bijective(list1, codo):
    return is_injective(list1) and is_surjective(list1, codo)


test = {0: 8, 1: 10, 2: 12, 3: 11}
codomain = [8, 10, 11, 12]

print(is_injective(test))
print(is_surjective(test, codomain))
print(is_bijective(test, codomain))
