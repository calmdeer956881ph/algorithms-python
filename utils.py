from typing import MutableSequence, Optional, Sequence, TypeVar


T = TypeVar("T")


def swap(items: MutableSequence[T], first: int, second: int) -> None:
    """Swap two elements in a mutable sequence.

    Args:
        items: Sequence whose elements will be exchanged.
        first: Index of the first element.
        second: Index of the second element.

    Raises:
        IndexError: If either index is outside the sequence.
    """
    items[first], items[second] = items[second], items[first]


def is_sorted(items: Sequence[T], *, reverse: bool = False) -> bool:
    """Return whether a sequence is ordered monotonically.

    Args:
        items: Sequence of mutually comparable values.
        reverse: Check descending order when true; otherwise check ascending
            order.

    Returns:
        True when every adjacent pair is in the requested order. Empty and
        single-element sequences are considered sorted.
    """
    if reverse:
        return all(items[index] >= items[index + 1] for index in range(len(items) - 1))
    return all(items[index] <= items[index + 1] for index in range(len(items) - 1))


def binary_search(items: Sequence[T], target: T) -> Optional[int]:
    """Find a target in an ascending sorted sequence using binary search.

    Args:
        items: Ascending sequence of mutually comparable values.
        target: Value to locate.

    Returns:
        The index of the target, or None when it is absent. If duplicate
        values exist, the index of the first occurrence is returned.
    """
    low = 0
    high = len(items) - 1
    result: Optional[int] = None

    while low <= high:
        middle = low + (high - low) // 2
        if items[middle] < target:
            low = middle + 1
        elif items[middle] > target:
            high = middle - 1
        else:
            result = middle
            high = middle - 1

    return result


def greatest_common_divisor(first: int, second: int) -> int:
    """Compute the greatest common divisor of two integers.

    Args:
        first: First integer.
        second: Second integer.

    Returns:
        The non-negative greatest common divisor. When both arguments are
        zero, zero is returned.
    """
    first, second = abs(first), abs(second)
    while second:
        first, second = second, first % second
    return first