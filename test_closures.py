import pytest
# from numpy.random import randint
import closures
import os
import inspect
import re
import random

README_CONTENT_CHECK_FOR = [
    'dict',
    'fibonacci',
    'Function',
    'counter',
    'docstring',
    'add',
    'mul',
    'closure'
]


CHECK_FOR_THINGS_NOT_ALLOWED = []


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r", encoding="utf8")
    readme_words = readme.read().split()
    readme.close()
    assert len(
        readme_words) >= 100, "Make your README.md file interesting! Add atleast 100 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            print(c)
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You haven't well described your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(closures, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_function_doc_string():
    '''
    Test case to check whether the functions have docstrings or not.
    '''
    functions = inspect.getmembers(closures, inspect.isfunction)
    for function in functions:
        assert function[1].__doc__


def test_function_annotations():
    '''
    Test case to check whether the functions have annotations or not.
    '''
    functions = inspect.getmembers(closures, inspect.isfunction)
    for function in functions:
        assert function[1].__annotations__


def test_doc_checker():
    dc = closures.scan_fn(50)
    fib = closures.fib()
    assert dc(
        closures.counter) == True, "Something wrong with the doc_check function."
    assert dc(fib) == True, "Something wrong with the doc_check function."


def test_doc_checker_parameter_type():
    with pytest.raises(TypeError):
        dc = closuresfib = closures.scan_fn()
        dc("Just messing around")


def test_fibonacci():
    fib = closures.fib()
    assert fib() == 1, "Something wrong with the fibonacci function."
    assert fib() == 1, "Something wrong with the fibonacci function."
    assert fib() == 2, "Something wrong with the fibonacci function."
    fib = closures.fib()
    for i in range(10):
        fib()
    # Checking for 11th fibonacci number
    assert fib() == 89, "Something wrong with the fibonacci function."


def test_func_count():
    def add(a, b):
        return a+b

    def mul(a, b):
        return a*b

    def div(a, b):
        return b and a/b
    fc = closuresfib = closures.counter()
    for _ in range(10):
        fc(add, 2, 5)
    for _ in range(7):
        fc(mul, 2, 5)
    for _ in range(15):
        fc(div, 2, 5)
    for _ in range(3):
        fc(print, "Apple")

    assert closures.func_count['add'] == 10, "Something wrong with the func_count function."
    assert closures.func_count['mul'] == 7, "Something wrong with the func_count function."
    assert closures.func_count['div'] == 15, "Something wrong with the func_count function."
    assert closures.func_count['print'] == 3, "Something wrong with the func_count function."


def test_func_count_parameter_type():
    with pytest.raises(TypeError):
        fc = closures.counter()
        fc("This is not a function and should throw error!")


def test_func_count_custom():
    def add(a, b):
        return a+b

    def mul(a, b):
        return a*b

    def div(a, b):
        return b and a/b

    dict_1 = dict()
    fc = closures.counter_users(dict_1)

    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)

    for _ in range(a):
        fc(add, 2, 5)
    for _ in range(b):
        fc(mul, 2, 5)
    for _ in range(c):
        fc(div, 2, 5)
    for _ in range(d):
        fc(print, "Apple")

    assert dict_1['add'] == a, "Something wrong with the func_count function."
    assert dict_1['mul'] == b, "Something wrong with the func_count function."
    assert dict_1['div'] == c, "Something wrong with the func_count function."
    assert dict_1['print'] == d, "Something wrong with the func_count function."

    dict_2 = dict()
    fc_new = closures.counter_users(dict_2)

    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)

    for _ in range(a):
        fc_new(add, 2, 5)
    for _ in range(b):
        fc_new(mul, 2, 5)
    for _ in range(c):
        fc_new(div, 2, 5)
    for _ in range(d):
        fc_new(print, "Apple")

    assert dict_2['add'] == a, "Something wrong with the func_count function."
    assert dict_2['mul'] == b, "Something wrong with the func_count function."
    assert dict_2['div'] == c, "Something wrong with the func_count function."
    assert dict_2['print'] == d, "Something wrong with the func_count function."


def test_func_count_custom_parameter_type():
    with pytest.raises(TypeError):
        fc = closures.counter_users(1)

    with pytest.raises(TypeError):
        fc = closures.counter({})
        fc("This is not a function and should throw error!")
