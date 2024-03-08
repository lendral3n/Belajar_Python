class MyClass:
    x = 5
    
p1 = MyClass()
print(p1.x)

# Fungsi __init__()
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person("jon", 27)
print(p1.name)
print(p1.age)

# Fungsi __str__()
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def __str__(self):
      return f"{self.name}({self.age})"

p1 = Person("johnsn", 99)
print(p1)

# Metode Objek
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name + "saya berumur " + str(self.age))

p1 = Person("John", 36)
p1.myfunc()