# What is `__enter__` and `__exit__`
* The key to context managers
* The coolest thing in python
    * arguably
* Go hand in hand to set up some scenario then safely tear down said scenario
* Most notable is file I/O

```python
In [2]: with open("README.md") as f:
   ...:     print(f.read())
   ...:
# What is `__enter__` and `__exit__`
* The key to context managers
* the coolest thing in python
    * arguably
```

* Without context manager

```python
In [3]: f = open("README.md")

In [4]: print(f.read())
# What is `__enter__` and `__exit__`
* The key to context managers
* the coolest thing in python
    * arguably

In [5]: f.close()
```

* Seems... pretty similar

```python
In [10]: f = open("README.md")

In [11]: # does stuff for 20 lines

In [12]: # forgets to close file
```

* also the above pattern is annoying to remember

## Closer look

* redundant context manager for files

```python
class File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()

In [17]: new_file_object = File("README.md", "r")

In [18]: with new_file_object as f:
    ...:     print(f.read())
    ...:
# What is `__enter__` and `__exit__`
* The key to context managers
* the coolest thing in python
    * arguably

In [19]: f.read()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-19-bacd0e0f09a3> in <module>()
----> 1 f.read()

ValueError: I/O operation on closed file.
```

* Also seen in database connections, network connections, sessions
* Think setup -> do work -> teardown
