def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable. Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator). Return:
    An iterable.
    None if the iterable can not be used by the function. """
    if not hasattr(iterable, '__iter__') and not hasattr(iterable, '__next__'):
        raise TypeError(f"'{type(iterable).__name__}' object is not iterable")
    if not callable(function_to_apply):
        raise TypeError(f"'{type(function).__name__}' object is not callable")
    iterator = iter(iterable)
    for item in iterator:
        if function_to_apply(item):
            yield item

