def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable. Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator). Return:
    An iterable.
    None if the iterable can not be used by the function. """
    if not hasattr(iterable, '__iter__') and not hasattr(iterable, '__next__'):
        raise TypeError(f"'{type(iterable).__name__}' object is not iterable")
    if not callable(function_to_apply):
        raise TypeError(f"'{type(function_to_apply).__name__}' object is not callable")
    result = []
    for item in iterable:
       yield function_to_apply(item)
