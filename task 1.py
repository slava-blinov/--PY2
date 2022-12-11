import doctest


# TODO Написать 3 класса с документацией и аннотацией типов
class Bird:
    def __init__(self, color: str, kind: str, position: list):
        if not isinstance(color, str) or not isinstance(kind, str):
            raise TypeError("характеристика должна являться строкой")
        if not isinstance(position, list):
            raise TypeError("Позиция должны задаваться списком")

        for kord in position:
            if not isinstance(kord, (int, float)):
                raise TypeError("координаты должны быть числами")
        self.color = color
        self.kind = kind
        self.position = position

    def fly(self, new_position: list):
        """
        Метод позволяет птичке летать по разным местам,
        а нам понять по каким конткретно

        >>> bird = Bird("gray", "sinichka", [1, 2, 4])
        >>> bird.fly([1,5,10])
        >>> bird.position == [1,5,10]
        True

        :param new_position:  новая позиция птички
        """
        if not isinstance(new_position, list):
            raise TypeError("Позиция должны задаваться списком")

        for kord in new_position:
            if not isinstance(kord, (int, float)):
                raise TypeError("координаты должны быть числами")
        self.position = new_position

    def peck(self):
        """
        метод позволяет птичке питаться, обороняться и нападать

        >>> bird = Bird("gray", "sinichka", [1, 2, 4])
        >>> bird.peck()
        """

        ...


class Car:
    def __init__(self, make: str, model: str, is_broken: bool):
        if not isinstance(make, str):
            raise TypeError("марка должна являться строкой")
        if not isinstance(model, str):
            raise TypeError("модель должны задаваться строкой")
        if not isinstance(is_broken, bool):
            raise TypeError("переменная is_broken должна иметь тип bool")

        self.make = make
        self.model = model
        self.is_broken = is_broken

    def drive(self):
        """
        Метод позволяет машине ездить

        >>> car = Car("lada", "priora", True)
        >>> car.drive()
        """
        if self.is_broken:
            self.repair()

        ...  # реализация езды

    def repair(self):
        """
        Метод позволяет чинить машину

        >>> car = Car("lada", "priora", True)
        >>> car.repair()

        """
        if self.is_broken:
            # машину надо чинить
            ...
            self.is_broken = False
        else:
            raise Exception("невозможно отремонтировать исправную машину")


class Ball:
    def __init__(self, size: str, material: str,):
        if not isinstance(size, str):
            raise TypeError("размер должен являться строкой")
        if not isinstance(material, str):
            raise TypeError("материал должен являться строкой")

        self.size = size
        self.material = material

    def kick(self):
        """
        метод позволяет пинать мяч

        >>> ball = Ball("big", "rubber")
        >>> ball.kick()
        """

        ...

    def catch(self):
        """
        метод позволяет ловить мяч

        >>> ball = Ball("big", "rubber")
        >>> ball.catch()
        """

        ...

    
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
