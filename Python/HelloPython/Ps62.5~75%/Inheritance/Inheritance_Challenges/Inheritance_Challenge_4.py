class Shape:
    def draw(self):
        print("도형 그리기")
    
class Circle(Shape):
    def draw(self):
        print("원을 그립니다.")

shape = Shape()
shape.draw()

circle = Circle()
circle.draw()