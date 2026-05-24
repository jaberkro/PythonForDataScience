def ft_filter(function, iterable):
    """Filter any iterable, by testing each element with a function. \
    Keep all elements of which the function returns True"""

    return [x for x in iterable if function(x)]
