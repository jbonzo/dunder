

class Dunder(object):
    def __init__(self, phrase):
        self.phrase = phrase

    def __str__(self):
        return "This Dunder's phrase is {phrase}" \
        .format(phrase=self.phrase)

    def __len__(self):
        return len(self.phrase)

    def __add__(self, other):
        return Dunder(self.phrase + other.phrase)


























class ConfusedPerson(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.self_worth = age % len(name)






















class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class ConfusedPerson(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.self_worth = age % len(name)

class ConfidentPerson(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.self_worth = age + len(name)

