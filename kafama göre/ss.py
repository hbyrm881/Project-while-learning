class person:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, age: {self.age}"

flag = True
while flag:
    value_name = input("Name: ")
    value_age = input("Age: ")
    p2 = person(value_name,value_age)
    print(p2)
    flag = False

p1 = person("Hasan",18)
print (f"Name: {p1.name},age: {p1.age}")