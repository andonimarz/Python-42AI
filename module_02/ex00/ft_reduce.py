def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively. Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator). Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function. """
    if not hasattr(iterable, '__iter__') and not hasattr(iterable, '__next__'):
        raise TypeError(f"'{type(iterable).__name__}' object is not iterable")
    if not callable(function_to_apply):
        raise TypeError(f"'{type(function).__name__}' object is not callable")
    iterator = iter(iterable) if isinstance(iterable, (list, tuple, str)) else iterable
    accumulator = next(iterator)
    for item in iterator:
        accumulator = function_to_apply(accumulator, item)
    return accumulator