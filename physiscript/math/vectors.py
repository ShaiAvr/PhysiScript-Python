"""vectors."""
from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from collections.abc import Iterable

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
