from vector import Vector

def printall():
    print("===== v1 =====")
    print("Values = ",v1.values)
    print("Shape = ",v1.shape)
    print()
    print("===== v2 =====")
    print("Values = ",v2.values)
    print("Shape = ",v2.shape)
    print()

print("===== v1 and v2 created =====")

v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[0.5], [1.5], [2.5], [3.5]])

v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = Vector([[0.5, 1.5, 2.5, 3.5]])

print("===== __STR__ =====")
print(v1)
print(v2)

print("== v1 + v2 ==")
print(v1 + v2)
print()

print("== v1 - v2 ==")
print(v1 - v2)
print()

print("== v1.dot(v2) ==")
print(v1.dot(v2))
print()

print("== v1 * 5 ==")
print(v1 * 5)
print()

print("== 5 * v1 ==")
print(5 * v1)
print()

print("== v1 / 2 ==")
print(v1 / 2)
print()

print("== 2 / v1 ==")
print(2 / v1)
print() 

print("== v1.T() ==")
print(v1.T()) 

printall()
