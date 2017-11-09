# What is `__str__` and `__repr__`
* both are dunder methods that reprensent an object in some way
* `__str__` is invoked by printing an object
* `__repr__` is invoked by `repr()` or by just referencing the object like so:

```python
In [1]: from classes import Adult

In [2]: p = Adult("rick", 21)

In [3]: p
Out[3]: Adult (name: rick, age: 21, children: [])

In [4]: print(p)
Adult: rick 
```

# `__str__` is used for informal representation
Here is a class definition for some class called Adult

```python
class Adult(object):
    def __init__(self, name, age, children=None):
        self.name = name
        self.age = age
        if children:
            self.children = children
        else:
            self.children = []

    def __str__(self):
        return "Parent: %s" % self.name

```
 * Adult has three attributes `name`, `age`, and `children`.
 * `__str__` prints the class name and the `name` attribute
 * informal, minimal, descriptive

# `__repr__` for formal representation

```python
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
```
* This representation is more comprehensive


# Other notes

## when `__str__` is undefined, `__repr__` is called

```python
In [30]: class fanboy(object):
         def __init__(self, tv):
             self.tv = tv
         def __repr__(self):
             return "fanboy(tv='{tv}')".format(tv=self.tv)    

In [31]: r = fanboy("30 Rock")

In [32]: print(r)
fanboy(tv='30 Rock')
```

## can be used to evaluate a new object

```python
In [33]: new_r = eval(repr(r))

In [34]: new_r
Out[34]: fanboy(tv='30 Rock')
```


## can be inheritated down to children classes

```python
In [13]: class Animal(object):
         def __init__(self, name):
             self.name = name
         def __str__(self):
             return "Animal name: {name}".format(name=self.name)
    

In [14]: class Mammal(Animal):
         def __init__(self, name, fur_color):
             super().__init__(name=name)
             self.fur_color = fur_color
         def __str__(self):
             return super().__str__() + " fur_color: {color}".format(color=self.fur_c
     olor)
    

In [15]: cat = Mammal("cat", "gray")

In [16]: print(cat)
Animal name: cat fur_color: gray
```
