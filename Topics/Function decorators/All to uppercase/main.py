def to_upper(function):
    def wrapper(arguments):
        return function(arguments.upper())

    return wrapper
