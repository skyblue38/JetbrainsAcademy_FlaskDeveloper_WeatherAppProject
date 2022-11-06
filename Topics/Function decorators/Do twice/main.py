def do_twice(function):
    def wrapper(arguments):
        function(arguments)
        function(arguments)
        return function

    return wrapper
