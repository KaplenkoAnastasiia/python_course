from typing import NamedTuple
import abc


class Point2D(NamedTuple):
    """
    A point in 2-dimensional space.
    Implemented as NamedTuple (so it is immutable), but simple class can be used instead.
    """
    x: float
    y: float

    def __str__(self):
        return f"({self.x}, {self.y})"


class Shape2D(abc.ABC):
    """
    An abstract shape in 2-dimensional space. Examples of 2D shapes are rectangle, circle, etc.
    """

    @property
    @abc.abstractmethod
    def area(self) -> float:
        """Area of the shape."""
        raise NotImplementedError

    @abc.abstractmethod
    def __contains__(self, point: Point2D) -> bool:
        """Check if the point is inside the shape.
        Support semantics like `if point in shape`"""
        raise NotImplementedError

    @abc.abstractmethod
    def __str__(self) -> str:
        """Get string representation of the shape."""
        raise NotImplementedError
