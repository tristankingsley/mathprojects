# This function starts by making sure that 0! returns as 1.
# It then sets another number equal to our parameter.
# It then multiplies our returned value by decreasing increments
# of our input to return a factorial.
def factorial(n):
    if n == 0:
        n = 1

    m = n
    while n > 1:
        n = n - 1
        m = m * n

    return m


# This function calculates the numerator and the denominator of the
# formula for combinations using our factorial function.
# It then returns the quotient of the two.
def choose(n, k):
    num = factorial(n)
    denom = factorial(n-k) * factorial(k)
    return num/denom


# This function runs the choose function and multiplies it by k! in order
# to follow the permutation formula.
def perm(n, k):
    return choose(n, k) * factorial(k)

# This function initially takes both elements of the lists and assigns them
# to new lists. It then calculates the absolute value of the x and y distances.
# Finally, it uses the choose function with n being the total distances and k being
# the x distance.
def lat_two(cord):
    cord1 = cord[0]
    cord2 = cord[1]

    xdist = abs(cord1[0] - cord2[0])
    ydist = abs(cord1[1] - cord2[1])

    return choose(xdist+ydist, xdist)


# This function makes two lists; one list containing the first and second coordinates,
# the second being composed of the second and third coordinates. Then it uses
# the lat_two function on both lists and returns the product of running both functions.
def lat_three(cord):
    list1 = []
    list2 = []

    list1.append(cord[0])
    list1.append(cord[1])

    list2.append(cord[1])
    list2.append(cord[2])

    return lat_two(list1) * lat_two(list2)


print(factorial(0))
print(choose(20, 12))
print(perm(5, 4))
print(lat_two([[5, 3], [0, 0]]))
print(lat_three([[2, 5], [3, 5], [5, 5]]))
