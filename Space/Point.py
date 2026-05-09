

class Point:
    def __init__(self, x: float, y:float):
        self._x = x
        self._y = y

    def __str__(self):
        return f"Point({self._x}, {self._y})"    
    
    def compute_distance(self,other : "Point") -> float:
        distance = ((self._x - other._x)**2 + (self._y - other._y)**2)**0.5
        return distance 
     
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def set_x(self, new_x: float):
        self._x = new_x

    def set_y(self, new_y: float):
        self._y = new_y