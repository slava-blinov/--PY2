class Quadrilateral:
    def __init__(self, sides: list[int]):
        """
       Создание и подготовка к работе объекта "Quadrilateral"

        :param sides: Список с длинами сторон четырехугольника
        """
        self.sides = sides

    @property
    def sides(self) -> list[int]:
        """Вовзвращает список сторон четырехугольника"""
        return self._sides

    @sides.setter
    def sides(self, sides: list[int]):
        """
        Проверка введенных данных для сторон четырехугольника

        :param sides: Список с длинами сторон четырехугольника
        """
        if not isinstance(sides, list):
            raise TypeError("Длины сторон задаются списком")
        if len(sides) != 4:
            raise ValueError("Длина списка сторон должна быть равна 4")
        if not all(isinstance(side, int) for side in sides):
            raise TypeError("Длина каждой стороны задается целым числом")
        self._sides = sides

    def perimeter(self) -> int:
        """
        Нахождение периметра четырехугольника

        :return:  значение периметра четырехугольника
        """
        return sum(self.sides)

    def area(self):
        """Нахождение площади четырехугольника"""
        ...

    def __str__(self):
        return f"{self.__class__.__name__} со сторонами {self.sides!r}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.sides!r})"


class Square(Quadrilateral):
    def __init__(self, length: int):
        """
        Создание и подготовка к работе объекта "Square"

        :param length: длина стороны квадрата
        """
        super().__init__([length] * 4)

    @property
    def length(self) -> int:
        """Возвращает длину стороны квадрата"""
        return self.sides[0]

    @length.setter
    def length(self, new_length: int):
        """
        изменение длины квадрата

        :param new_length: новое значение длины квадарата
        """
        self.sides = [new_length] * 4

    def area(self) -> int:
        """
        нахождение площади квадрата

        :return: площадь квадрата
        """
        return self.length ** 2

    def __repr__(self):
        return f"{self.__class__.__name__}({self.length!r})"


class Rectangle(Quadrilateral):
    def __init__(self, width: int, height: int):
        """
         Создание и подготовка к работе объекта "Rectangle"


        :param width: ширина прямоугольника
        :param height: высота прямоугольника
        """
        super().__init__([width, height, width, height])

    @property
    def width(self) -> int:
        """Возвращает ширину прямоугольника"""
        return self.sides[0]

    @width.setter
    def width(self, new_width):
        """
        Изменение ширину прямоугольника

        :param new_width: измененная ширина прямоугольника
        """
        self.sides = [new_width, self.height, new_width, self.height]

    @property
    def height(self) -> int:
        """Возвращает высоту прямоугольника"""
        return self.sides[1]

    @height.setter
    def height(self, new_height):
        """
        изменение высоты прямоугольника

        :param new_height: измененное значение высоты прямоугольника
        """
        self.sides = [self.width, new_height, self.width, new_height]

    def area(self) -> int:
        """
        Считаем площадь прямоугольника

        :return:  значение площади прямоугольника
        """
        return self.width * self.height

    def __repr__(self):
        return f"{self.__class__.__name__}({self.width!r}, {self.height!r})"


if __name__ == "__main__":
    # Write your solution here
    quad = Quadrilateral([1, 2, 3, 4])
    print(quad)
    print(repr(quad))
    print(quad.perimeter())
    print(quad.area())

    square = Square(2)
    print(square)
    print(repr(square))
    print(square.perimeter())
    print(square.area())

    rect = Rectangle(3, 4)
    print(rect)
    print(repr(rect))
    print(rect.perimeter())
    print(rect.area())
