from typing import List
from Shape.Shape import Shape

class Rectangle(Shape):
    def __init__(self, vertices: List):
        super().__init__(vertices)
        self.longer_length = max(edge.length for edge in self._edges)
        self.smaller_length = min(edge.length for edge in self._edges)
 
    def compute_area(self):
        area = self.longer_length * self.smaller_length 
        return area  

    def compute_perimeter(self):
        perimeter = 2*(self.smaller_length + self.longer_length)
        return perimeter
