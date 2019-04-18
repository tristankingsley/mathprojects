# This function returns a sequence with c elements, starting with a
# increasing at increments of b

def arith(a, b, c):
    seq = []
    while c > 0:
        seq.append(a)
        a = a + b
        c = c - 1

    return seq

# This function returns a sequence with c elements, starting with a
# increasing at multiples of b

def geo(a, b, c):
    seq = []
    while c > 0:
        seq.append(a)
        a = a * b
        c = c - 1

    return seq

# This function returns a 10 element sequence starting with c and d
# and continuing by multiplying and adding previous elements

def recur(a, b, c, d):
    seq = []
    seq.append(c)
    seq.append(d)
    j = 2

    while j < 10:
        i = a*seq[j-1] + b*seq[j-2]
        seq.append(i)
        j = j + 1

    return seq

# This function returns a list containing differences within
# a sequence
def difference(seq):
    dif = []
    j = len(seq) - 1
    while j > 0:
        l = seq[j] - seq[j - 1]
        if l not in dif:
            dif.append(l)
        j = j - 1
    return dif

# This function checks to see if the first differences of a function
# are constant

def delta_one(seq):

    dif = difference(seq)

    return len(dif) == 1

# This function checks to see if the second differences of a function
# are constant

def delta_two(seq):
    fdif = difference(seq)
    sdif = difference(fdif)

    return len(sdif) == 1 or len(fdif) == 1

# This function checks to see if the third differences of a function
# are constant

def delta_three(seq):
    fdif = difference(seq)
    sdif = difference(fdif)
    tdif = difference(sdif)

    return len(tdif) == 1 or len(sdif) == 1 or len(fdif) == 1


print(delta_one([1, 3, 5, 7, 9, 11, 13]))
print(delta_one([1,4,9,16,25,36,49,64]))
print(delta_one([0,4,18,48,100,180]))

print(delta_two([1, 3, 5, 7, 9, 11, 13]))
print(delta_two([1,4,9,16,25,36,49,64]))
print(delta_two([0,4,18,48,100,180]))

print(delta_three([1, 3, 5, 7, 9, 11, 13]))
print(delta_three([1,4,9,16,25,36,49,64]))
print(delta_three([0,4,18,48,100,180]))