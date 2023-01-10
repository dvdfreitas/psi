

# Data Classes Builders

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

```
class Coordinate:
def __init__(self, lat, lon):
self.lat = lat
self.lon = lon
```

```
>>> from coordinates import Coordinate
>>> moscow = Coordinate(55.76, 37.62)
>>> moscow
<coordinates.Coordinate object at 0x107142f10>
>>> location = Coordinate(55.76, 37.62)
>>> location == moscow
False
>>> (location.lat, location.lon) == (moscow.lat, moscow.lon)
True
```

# Data class builders

Python offers a few ways to build a simple class that is just a collection of fields, with little or no extra functionality. That pattern is known as a “data class” — and data classes is one of the packages that supports this pattern:

- collections.namedtuple - The simplest way—available since Python 2.6.
- typing.NamedTuple - An alternative that requires type hints on the fields—since Python 3.5, with class syntax added in 3.6.
- @dataclasses.dataclass - A class decorator that allows more customization than previous alternatives, adding lots of options and potential complexity—since Python 3.7.

The data class builders covered here provide the necessary __init__,
__repr__, and __eq__ methods automatically, as well as other useful features.

## collections.namedtuple

The collections.namedtuple function is a factory that builds subclasses of tuple
enhanced with field names, a class name, and an informative __repr__. Classes built with namedtuple can be used anywhere where tuples are needed, and in fact many functions of the Python standard library that are used to return tuples now return named tuples for convenience, without affecting the user’s code at all.

Each instance of a class built by namedtuple takes exactly the same amount of memory as a tuple because the field names are stored in the class.

```
>>> from collections import namedtuple
>>> Coordinate = namedtuple('Coordinate', 'lat lon')
>>> issubclass(Coordinate, tuple)
True
>>> moscow = Coordinate(55.756, 37.617)
>>> moscow
Coordinate(lat=55.756, lon=37.617)
>>> moscow == Coordinate(lat=55.756, lon=37.617)
True
```

```
>>> from collections import namedtuple
>>> City = namedtuple('City', 'name country population coordinates')
>>> tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
>>> tokyo
City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722,
139.691667))
>>> tokyo.population
36.933
>>> tokyo.coordinates
(35.689722, 139.691667)
>>> tokyo[1]
'JP'

>>> City._fields
('name', 'country', 'population', 'location')
>>> Coordinate = namedtuple('Coordinate', 'lat lon')
>>> delhi_data = ('Delhi NCR', 'IN', 21.935, Coordinate(28.613889, 77.208889))
>>> delhi = City._make(delhi_data)
>>> delhi._asdict()
{'name': 'Delhi NCR', 'country': 'IN', 'population': 21.935,
'location': Coordinate(lat=28.613889, lon=77.208889)}
>>> import json
>>> json.dumps(delhi._asdict())
'{"name": "Delhi NCR", "country": "IN", "population": 21.935,
"location": [28.613889, 77.208889]}'

>>> Coordinate = namedtuple('Coordinate', 'lat lon reference', defaults=['WGS84'])
>>> Coordinate(0, 0)
Coordinate(lat=0, lon=0, reference='WGS84')
>>> Coordinate._field_defaults
{'reference': 'WGS84'}
```

## typing.NamedTuple

The newer typing.NamedTuple provides the same functionality, adding a type anno‐
tation to each field:

```
>>> import typing
>>> Coordinate = typing.NamedTuple('Coordinate',
...
[('lat', float), ('lon', float)])
>>> issubclass(Coordinate, tuple)
True
>>> typing.get_type_hints(Coordinate)
{'lat': <class 'float'>, 'lon': <class 'float'>}
```

Or

```
Coordinate = typing.NamedTuple('Coordinate', lat=float, lon=float)
```


```
from typing import NamedTuple
class Coordinate(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
```


```
from typing import NamedTuple
class Coordinate(NamedTuple):
    lat: float
    lon: float
    reference: str = 'WGS84'
```

Classes built by typing.NamedTuple don’t have any methods beyond those that collections.namedtuple also generates—and those that are inherited from tuple. The only difference is the presence of the __annotations__ class attribute—which Python completely ignores at runtime.

## @dataclass


The decorator accepts several keyword arguments. This is its signature:

```
@dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
```

The defaults are really the most useful settings for common use cases. The options you are more likely to change from the defaults are:

- ```frozen=True``` - Protects against accidental changes to the class instances.
- ```order=True``` - Allows sorting of instances of the data class.


If the eq and frozen arguments are both True, @dataclass produces a suitable __hash__ method, so the instances will be hashable. If frozen=False (the default), @dataclass will set __hash__ to None, signalling that the instances are unhashable, therefore overriding __hash__ from any superclass.

```
from dataclasses import dataclass
@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float
    def __str__(self):
    ns = 'N' if self.lat >= 0 else 'S'
    we = 'E' if self.lon >= 0 else 'W'
    return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
```

## Post-init Processing
The __init__ method generated by @dataclass only takes the arguments passed and
assigns them—or their default values, if missing—to the instance attributes that are instance fields. But you may need to do more than that to initialize the instance.

If that’s the case, you can provide a __post_init__ method. When that method exists, @dataclass will add code to the generated __init__ to call __post_init__ as the last step.

## Initialization Variables That Are Not Fields

Sometimes you may need to pass arguments to __init__ that are not instance fields. Such arguments are called init-only variables by the dataclasses documentation. To
declare an argument like that, the dataclasses module provides the pseudotype Init Var, which uses the same syntax of typing.ClassVar.

## Code smells

The main idea of object-oriented programming is to place behavior and data together in the same code unit: a class. If a class is widely used but has no significant behavior of its own, it’s possible that code dealing with its instances is scattered (and even duplicated) in methods and functions throughout the system—a recipe for maintenance headaches. That’s why Fowler’s refactorings to deal with a data class involve bringing responsibilities back into it.

Taking that into account, there are a couple of common scenarios where it makes sense to have a data class with little or no behavior.

### Data Class as Scaffolding

In this scenario, the data class is an initial, simplistic implementation of a class to jump-start a new project or module. With time, the class should get its own methods, instead of relying on methods of other classes to operate on its instances. Scaffolding is temporary; eventually your custom class may become fully independent from the builder you used to start it.

### Data Class as Intermediate Representation

A data class can be useful to build records about to be exported to JSON or some
other interchange format, or to hold data that was just imported, crossing some system boundary. Python’s data class builders all provide a method or function to convert an instance to a plain dict, and you can always invoke the constructor with adict used as keyword arguments expanded with **. Such a dict is very close to a JSON record.

In this scenario, the data class instances should be handled as immutable objects — even if the fields are mutable, you should not change them while they are in this intermediate form. If you do, you’re losing the key benefit of having data and behavior close together. When importing/exporting requires changing values, you should implement your own builder methods instead of using the given “as dict” methods or standard constructors.

# Pattern Matching Class Instances

Class patterns are designed to match class instances by type and—optionally—by
attributes.

There are three variations of class patterns: simple, keyword, and positional.

## Simple Class Patterns

The syntax for class patterns looks like a constructor invocation. The following is a class pattern that matches float values without binding a variable (the case body can refer to x directly if needed):

```
match x:
    case float():
        do_something_with(x)
```

## Keyword Class Patterns

```
def match_asian_cities():
    results = []
    for city in cities:
        match city:
            case City(continent='Asia'):
            results.append(city)
    return results
```

## Positional Class Patterns

```
def match_asian_countries_pos():
    results = []
    for city in cities:
        match city:
            case City('Asia', _, country):
    results.append(country)
return results
```