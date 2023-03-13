from sys import argv

joinedstr = ""

#Joining all argvs in a string using " " as separator
for str in argv[1:]:

    joinedstr = " ".join([joinedstr, str])

#Inverting the string
invertedstr = joinedstr[::-1]

#Swapping lower and upper case
swappedstr = invertedstr.swapcase()

print(swappedstr)

