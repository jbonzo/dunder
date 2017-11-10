# Dunder Methods A.K.A Magic Methods

## Dunder?

Double UNDERscore

## What are dunder methods?

### What are methods?
A method is a function that belongs to a class

In python these are usually noted by the dot operator

```python
    In [1]: s = "THIS IS MY ANGRY STRING"
    In [2]: # .lower() is a string method
    In [3]: s.lower()
    Out[3]: 'this is my angry string'
```
### Dunder methods

```python
class Dunder(object):
    def __init__(self, phrase):
        self.phrase = phrase

    def __str__(self):
        return "This Dunder's phrase is {phrase}".format(phrase=self.phrase)

    def __len__(self):
        return len(self.phrase)

    def __add__(self, other):
        return Dunder(self.phrase + other.phrase)
```

* Special methods that aren't explicitly called by the progammer

```python
In [1]: from classes import Dunder

In [2]: myDunder = Dunder("Magic")

In [3]: myDunder.phrase

Out[3]: 'Magic'

In [4]: print(myDunder)
"This Dunder's phrase is Magic"
```

* Usually are related to properties or the state of an object

```python
In [5]: len(myDunder)
Out[5]: 5
```

* Can also dictate the manipulation of an object

```python
In [6]: combinedDunder = myDunder + Dunder("Methods")

In [7]: print(combinedDunder)
"This Dunder's phrase is MagicMethods"
```


# References
[Dunder docs](https://docs.python.org/3/reference/datamodel.html#special-method-name)
