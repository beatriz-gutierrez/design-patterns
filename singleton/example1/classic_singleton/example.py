from singleton import Singleton, Child

singleton1 = Singleton("aaa")
print(singleton1.value)

singleton2 = Singleton("bbb")
print(singleton2.value)
print(singleton1.value)

print(singleton1 is singleton2)

singleton1.value = "ccc"
print(singleton1.value)
print(singleton2.value)


child = Child()
print("Creating a child")
print(child is singleton1)
print(child.value)
print(singleton1.value)
print(singleton2.value)

child2 = Child("ddd")
print("Creating a child2")
print(child2.value)


print(child2 is singleton1)
