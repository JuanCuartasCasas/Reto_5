from typing import List
import math
from Shape.Shape import Shape
from Space.Point import Point 

class Triangle(Shape):
    def __init__(self, vertices: List):
        super().__init__(vertices)

    def set_vertices(self, new: List[Point]):
        
        if len(self._vertices) != 3:
            print("El triangulo solamente debe poseer 3 ángulos")
            
        else:
            super().set_vertices(new)
	
    def compute_area(self):
        a = self._edges[0].length
        b = self._edges[1].length
        c = self._edges[2].length
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area