# Two kinds of errors: syntax errors and exceptions
# https://docs.python.org/3/tutorial/errors.html

# Lists
# List is a data container, can contain other data types, even containers.
# List is a data type for mutable ordered sequence of elements.

# As a data type, out of float, int and string, Lists are most similar to
# strings.
# Similarities:
# Both support len(), zero indexing and slicing (ex. [:5] [2:4]), and
# membership operators: in and not in. we can also use in and not in to return a
# bool of whether an element exists within our list, or if one string is a
# substring of another.
# Both are ordered, so indexing works well.
# Differences:
# Lists are mutable, strings are not.
list[3] = 'foo' # ok
string[3] = 'a' # error
# Unlike strings, bracket notation can also be used to change individual items
# of a list. ... In Python, when we use the = operator to "copy" a list to another
# variable, the list is not actually replicated. Instead, both variables now
# simply point to the same list.
lista = [1,2,'3']
listb = lista
lista[2] = 4
print(listb[2]) # prints 4
sorted(lista) # sorted() returns a copy of a list in order from smallest to
# largest, leaving the list unchanged.
