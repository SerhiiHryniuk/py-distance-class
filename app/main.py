from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int) -> Distance:
        if not isinstance(other, Distance):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: Distance | int) -> Distance:
        self.km = self.km + other.km if isinstance(other, Distance) \
            else self.km + other
        return self

    def __mul__(self, other: int) -> Distance | None:
        if not isinstance(other, Distance):
            return Distance(self.km * other)
        return None

    def __truediv__(self, other: int) -> Distance | None:
        if not isinstance(other, Distance):
            return Distance(round(self.km / other, 2))
        return None

    def __eq__(self, other: int) -> bool:
        return self.km == other

    def __lt__(self, other: int) -> bool:
        return self.km < other

    def __gt__(self, other: int) -> bool:
        return self.km > other

    def __le__(self, other: int) -> bool:
        return self.km <= other

    def __ge__(self, other: int) -> bool:
        return self.km >= other
