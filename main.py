from Shapes import Triangle
from Shapes import Rectangle 
from Space.Point  import Point 



def main():
    p1 = Point(0, 0)
    p2 = Point(4, 0)
    p3 = Point(4, 3)
    p4 = Point(0, 3)

    triangle = Triangle([p1, p2, p3])
    print("Area del triángulo:", triangle.compute_area())
    print("Perímetro del triángulo:", triangle.compute_perimeter())
    print("Ángulos internos del triángulo:", triangle.inner_angles)
    print("¿Es el triángulo regular?", triangle.get_is_regular())

    rectangle = Rectangle([p1, p2, p3, p4])
    print("\nÁrea del rectángulo:", rectangle.compute_area())
    print("Perímetro del rectángulo:", rectangle.compute_perimeter())
    print("Ángulos internos del rectángulo:", rectangle.inner_angles)
    print("¿Es el rectángulo regular?", rectangle.get_is_regular())

    
if __name__ == "__main__":
    main()
