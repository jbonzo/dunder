# What is `__init__`
* `__init__` is the constructor in python
* python supports Object Orientated programming which means it has the concept of objects, methods, and attributes
* In order to create an object you must construct it with the initial desired attributes
* `__init__` is such constructor

# When should I use `__init__`?
* when constructing objects, silly

# Examples and Explainations

* The first argument __must__ be `self`
    * Technically it can be any variable name, as long as your consistent
    * __BUT__... that would be a dick move

* Reference an attribute via `self` when creating it
    * `self.attribute`
    * No need for declaration
        * This ain't `Java`

* Not every attribute for an object has to be passed in as an argument to  `__init_`
    * Some attributes can be created within `__init__` without being passed in to the constructor, examples below

* Not every attribute has to be set in `__init__`
    * Yes python is the cool Dad and is pretty lenient
    * __BUT__, not everyone likes this. There is a case for initializing everything in `__init__` for self-documenting's sake.
        * "But what if I don't have the means to initialize this attribute yet?" - Some person
        * "Just initialize to `None` in `__init__`" - Me

```python
class ConfusedPerson(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.self_worth = age % len(name)
```

```python
In [1]: from classes import ConfusedPerson

In [2]: ricky = ConfusedPerson("ricky", 21)

In [3]: ricky.self_worth
Out[3]: 1
```

# Super()
* Can't talk `__init__` without `super()`
* Inheritance
* Using `super()` in your `__init__` method is calling the parent class's `__init__`

```python
In [1]: from classes import ConfidentPerson, ConfusedPerson

In [2]: ricky = ConfusedPerson('ricky', 21)

In [3]: ricky.self_worth
Out[3]: 1

In [4]: rick = ConfidentPerson('rick', 21)

In [5]: rick.self_worth
Out[5]: 25

In [6]: rick.name
Out[6]: 'ricky'
```

# References
[`__init__` docs](https://docs.python.org/3/reference/datamodel.html#object.__init__)
