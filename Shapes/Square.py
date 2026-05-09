from typing import List
from Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, vertices: List):
        super().__init__(vertices)

    def compute_area(self):
        area = self._edges[0].length ** 2
        return area
 
    def compute_perimeter(self):
        perimeter = 4 * self._edges[0].length
        return perimeter
