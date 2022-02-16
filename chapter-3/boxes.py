"""
Chapter 3
Recursion
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Box:
    def __init__(self, name: str):
        self.name = name
        self.boxes: list[Box] = []

    def add_box(self, box: Box):
        self.boxes.append(box)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


def open_box(box: Box):
    print(f"opening {box.name}!")
    for b in box.boxes:
        open_box(b)
    # return


if __name__ == "__main__":
    A = Box("A")
    B = Box("B")
    C = Box("C")
    D = Box("D")
    A.add_box(B)
    A.add_box(C)
    B.add_box(D)

    open_box(A)
