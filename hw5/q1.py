import itertools

def flatten(*lists):
    """Returns a single list of containing the elements of the argument lists.
    Elements are in the order they appear.
    If called with no arguments, flatten returns a null list.
    If an argument is not a list, includes that argument as an element of the result list"""
    print(list(itertools.chain(*lists)))
