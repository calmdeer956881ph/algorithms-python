"""Shared helper functions for algorithm implementations."""

from random import Random
from time import perf_counter
from typing import Callable, Iterable, List, MutableSequence, Optional, Tuple, TypeVar

T = TypeVar("T")
K = TypeVar("K")
R = TypeVar("R")


def swap(items: MutableSequence[T], first: int, second: int) -> None:
    """Swap two elements of a mutable sequence in place.

    Args:
        items: Sequence whose elements will be exchanged.
        first: Index of the first element.
        second: Index of the second element.

    Raises:
        IndexError: If either index is outside the sequence.
    """
    items[first], items[second] = items[second], items[first]


def is_sorted(
    values: Iterable[T],
    *,
    key: Optional[Callable[[T], K]] = None,
    reverse: bool = False,
) -> bool:
    """Return whether values are ordered according to the requested direction.

    Args:
        values: Values to inspect.
        key: Optional function used to obtain each comparison key.
        reverse: Check descending order when true; ascending order otherwise.

    Returns:
        True for an ordered, empty, or single-item iterable; otherwise false.
    """
    iterator = iter(values)

    try:
        previous_value = next(iterator)
    except StopIteration:
        return True

    previous_key = key(previous_value) if key is not None else previous_value

    for value in iterator:
        current_key = key(value) if key is not None else value
        if reverse:
            if previous_key < current_key:  # type: ignore[operator]
                return False
        elif previous_key > current_key:  # type: ignore[operator]
            return False
        previous_key = current_key

    return True


def random_int_list(
    size: int,
    minimum: int = 0,
    maximum: int = 100,
    *,
    seed: Optional[int] = None,
) -> List[int]:
    """Create a reproducible list of uniformly distributed random integers.

    Args:
        size: Number of integers to generate.
        minimum: Smallest permitted value, inclusive.
        maximum: Largest permitted value, inclusive.
        seed: Optional seed for deterministic generation.

    Returns:
        A newly allocated list containing the generated integers.

    Raises:
        ValueError: If size is negative or minimum exceeds maximum.
    """
    if size < 0:
        raise ValueError("size must be non-negative")
    if minimum > maximum:
        raise ValueError("minimum must not exceed maximum")

    generator = Random(seed)
    return [generator.randint(minimum, maximum) for _ in range(size)]


def measure_time(
    function: Callable[..., R],
    *args: object,
    **kwargs: object,
) -> Tuple[R, float]:
    """Execute a callable and return its result with elapsed wall-clock time.

    Args:
        function: Callable to execute.
        *args: Positional arguments forwarded to the callable.
        **kwargs: Keyword arguments forwarded to the callable.

    Returns:
        A pair containing the callable's result and elapsed seconds.

    Raises:
        Exception: Propagates any exception raised by the callable.
    """
    started_at = perf_counter()
    result = function(*args, **kwargs)
    elapsed = perf_counter() - started_at
    return result, elapsed