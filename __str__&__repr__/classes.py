class Parent(object):
    def __init__(self, name, age, children=None):
        self.name = name
        self.age = age
        if children:
            self.children = children
        else:
            self.children = []

    def __str__(self):
        return "Parent: %s" % self.name

    def __repr__(self):
        return "Parent (name: {name}, age: {age}, children: {children})".format(
            name=self.name, age=self.age, children=self.children
        )
