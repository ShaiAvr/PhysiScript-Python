"""A multi-dimensional `Vector` class.

A `Vector` is built from an iterable of numbers or given numbers::

    >>> Vector([1, 2, 3])
    Vector([1.0, 2.0, 3.0])
    >>> Vector.of(0.0, -2.5)
    Vector([0.0, -2.5])
    >>> Vector(range(10)) # doctest: +ELLIPSIS
    Vector([0.0, 1.0, 2.0, 3.0, ..., 9.0])

"""
from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator

    import numpy.typing as npt

    from physiscript.typing import FloatScalar


class Vector:
    """A multi-dimensional `Vector` class."""

    __slots__ = ("_data",)

    _data: npt.NDArray[np.float64]

    def __init__(self, coordinates: Iterable[FloatScalar]) -> None:
        try:
            count = len(coordinates)  # type: ignore[arg-type]
        except TypeError:
            count = -1
        self._data = np.fromiter(coordinates, count=count, dtype=np.float64)

    @classmethod
    def of(cls, *args: FloatScalar) -> Vector:
        return Vector(args)

    def __iter__(self) -> Iterator[float]:
        return self._data.flat  # type: ignore[return-value]

    def __repr__(self) -> str:
        return f"{type(self).__name__}([{', '.join(map(repr, self))}])"

    def __str__(self) -> str:
        return f"<{', '.join(map(str, self))}>"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Vector):
            return np.array_equal(self._data, other._data, equal_nan=True)
        return NotImplemented

    def __abs__(self) -> float:
        return np.sqrt(self._data.dot(self._data))

    def __neg__(self) -> Vector:
        cls = type(self)
        nv = cls.__new__(cls)
        nv._data = -self._data
        return nv

    def __pos__(self) -> Vector:
        cls = type(self)
        pv = cls.__new__(cls)
        pv._data = +self._data
        return pv

    def __bool__(self) -> bool:
        pass
