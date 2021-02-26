# EPAi-Session-6-Closures

## Closures:

link: https://github.com/tapasML/EPAi2_Session6/blob/main/session_6_closures.py

## Part 1:

### Write a closure that takes a function and then check whether the Function passed has a docstring with more than 50 characters. 50 is stored as a free variable -

-> Implentation complete

docstring_meter(size:int) -> 'a closure'

## Part 2:

### Write a closure that gives you the next fibonacci number

-> Implementation complete

next_fib():

## Part 3:

### We wrote a closure that counts (counter) how many times a Function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts

-> Implementation complete

count_invoke(fn: callable)-> callable

## Part 4:

### Modify above such that now we can pass in different dictionary (dict) variables to update different dictionaries

-> Implementation complete

counter_dict(fn : callable , fn_counter : dict) -> callable
