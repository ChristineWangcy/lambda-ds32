# pylint: disable=trailing-whitespace
'''docstring'''
import math
import sys
from typing import Any


def example1():
    '''docstring'''
    # THIS IS A LONG COMMENT AND should be wrapped to fit within a 72 character limit
    some_tuple = (1, 2, 3, 'a')
    some_variable = {
        "long": 'Long code lines should be wrapped within 79 character to \
            prevent page cutoff stuff',
        "other": [math.pi, 100, 200, 300, 9999292929292, "This is a long \
            string that looks gross and goes beyond what it should"],
        "more": {"inner": "This whole logical line should be wrapped"},
        "data": [444, 5555, 222, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5]
    }
    return (some_tuple, some_variable)


def example2():
    '''docstring'''
    return {"has_key() is deprecated": True}


class Example3():
    '''docstring'''

    def __init__(self, bar1):
        self.bar1 = bar1

    def int_bar(self):
        '''docstring'''
        result = Any()
        if isinstance(self.bar1):
            bar1 = self.bar1
            bar1 += 1
            bar1 = bar1 * bar1
            result = bar1
        else:
            somestring = "INDENTATION IN MULTIPLE STRINGS SHOULD NOT BE TOUCHED \
                only actual code should be reindented, THIS IS MORE CODE."
            result = (sys.path, somestring)
        return result

    def method1(self):
        '''docstring'''
        return self.bar1


print(example1())
print(example2())
example = Example3(7)
print(example)
