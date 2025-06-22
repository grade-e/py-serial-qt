class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        return f"Hello, my name is {self.name}."

    def have_birthday(self):
        self.age += 1
        return self.age