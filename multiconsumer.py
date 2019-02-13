# Author: James Haller


def consume(*args):
    """
    Generator which consumes multiple iterables and yields
    a tuple containing one item from each iterable. Ends
    when any collection runs out of elements.
    :param args: Any number of iterables to consume
    :return: A tuple containing the next item from each
             iterable
    """
    iters = tuple([iter(arg) for arg in args])

    while True:
        yield tuple([next(itr) for itr in iters])

