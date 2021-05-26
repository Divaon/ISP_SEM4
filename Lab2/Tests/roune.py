
from inspect import isfunction, getsource


def _function_equals(real_thing, pretender):
    """
    Checks if two functions are the equal thing. For this to pass
    the code and names of the functions should be identical.
    :param real_thing:
    :param pretender:
    :return: True or False
    """
    if not isfunction(pretender):
        return False
    return getsource(real_thing) == getsource(pretender)


def equals(real_thing, pretender):
    """
    Checks if the `pretender` can be 'duct-typed' as `real_thing`.
    We don't care about types or order here, we care if I can pass
    `pretender` to something expecting `real_thing` and so nothing
     blows up.
    :param real_thing:
    :param pretender:
    :return: True or False
    """
    if real_thing == pretender:
        return True
    if isfunction(real_thing):
        return _function_equals(real_thing, pretender)
    attributes = [x for x in dir(real_thing) if not x.startswith('__')]
    for attribute in attributes:
        if not equals(real_thing.__getattribute__(attribute), pretender.__getattribute__(attribute)):
            return False
    return True