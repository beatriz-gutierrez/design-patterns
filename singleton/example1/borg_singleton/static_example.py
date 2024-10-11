class Example():
    _temp = 10

ex1 = Example()
print(ex1._temp)

ex2 = Example()
print(ex2._temp)
ex2._temp = 20
print(Example._temp)
print(ex2._temp)
print(ex1._temp)
Example._temp = 30
print(ex2._temp)
print(Example._temp)
print(ex1._temp)
