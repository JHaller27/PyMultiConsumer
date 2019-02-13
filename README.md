# Multiconsumer

Defines a single generator function which consumes any number of parameters
(at least 1), iterates over each collection, and yields a tuple where each
element is the result of calling `next()` with a parameter of each iterator.
The order of the returned tuple is the same as the order that the iterators
are passed in to the `consume()` function.

