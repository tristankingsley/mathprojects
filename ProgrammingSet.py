# Author: Tristan Kingsley
# Description: Programming set 1. This set of functions takes in lists of numbers to
# make sets out of them, make unions of said sets, make intersections of said sets,
# and take symmetric differences of said sets.
# Professor: Taylor Short
# Discrete Structures of Computational Mathematics


# Declares set values.
n = [7, 8, 9, 9, 10, 'a', 'c']
m = [7, 8, 'a', 'b']


# This function takes in a list and adds the list's elements to a new list, keeping in mind not to add elements
# previously added to our new list. It then returns the new list, which has no duplicate elements.
def make_set(list):

    set1 = []

    for numbers in list:
        if numbers not in set1:
            set1.append(numbers)

    return set1


# This function takes two lists and adds all elements of the first list, while checking for duplicates, to a new list.
# It then does the same with the second list, still keeping in mind no duplicates, and returns a union of the two lists.
def union(list1, list2):

    union1 = []

    for numbers in list1:
        if numbers not in union1:
            union1.append(numbers)

    for numbers in list2:
        if numbers not in union1:
            union1.append(numbers)

    return union1


# This function takes two lists and only adds elements from list1 that are also in list2 to a new list. It then returns
# the new list which is an intersect of the 2 inputted.
def intersect(list1, list2):

    intersect1 = []

    for numbers in list1:
        if numbers in list2:
            if numbers not in intersect1:
                intersect1.append(numbers)

    return intersect1


# This function takes two lists and only adds elements that are in list1 that are not in list 2. It also checks for
# duplicate elements to make it a set.
def symmetric_diff(list1, list2):

    symdif = []

    for numbers in list1:
        if numbers not in list2:
            if numbers not in symdif:
                symdif.append(numbers)

    return symdif


# These statements invoke functions with the arguments set and prints them
print(make_set(n))
print(union(n, m))
print(intersect(n, m))
print(symmetric_diff(n, m))
