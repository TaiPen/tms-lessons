import math


class Rational:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator
        self.__normalise()

    def __str__(self):
        return f"{self.__numerator} / {self.__denominator}"

    def __mul__(self, other):
        return Rational(self.__numerator * other.__numerator, self.__denominator * other.__denominator)

    def __truediv__(self, other):
        return Rational(self.__numerator * other.__denominator, self.__denominator * other.__numerator)

    def __add__(self, other):
        return Rational(self.__numerator * other.__denominator + other.__numerator * self.__denominator,
                        self.__denominator * other.__denominator)

    def __sub__(self, other):
        return Rational(self.__numerator * other.__denominator - other.__numerator * self.__denominator,
                        self.__denominator * other.__denominator)

    def __gt__(self, other):
        return self.__numerator / self.__denominator > other.__numerator / other.__denominator

    def __lt__(self, other):
        return self.__numerator / self.__denominator < other.__numerator / other.__denominator

    def __ge__(self, other):
        return self.__numerator / self.__denominator >= other.__numerator / other.__denominator

    def __le__(self, other):
        return self.__numerator / self.__denominator <= other.__numerator / other.__denominator

    def __eq__(self, other):
        return self.__numerator / self.__denominator == other.__numerator / other.__denominator

    def __normalise(self):
        if self.__denominator < 0:
            self.__numerator = self.__numerator * -1
            self.__denominator = self.__denominator * -1
        nod = math.gcd(self.__numerator, self.__denominator)
        if nod > 1:
            self.__numerator = int(self.__numerator / nod)
            self.__denominator = int(self.__denominator / nod)


if __name__ == '__main__':
    print(Rational(2, -4))
    fraction = Rational(2, 4)
    assert str(fraction) == '1 / 2'
    assert Rational(2, 3) * Rational(3, 4) == Rational(6, 12)
    assert Rational(2, 3) / Rational(3, 4) == Rational(8, 9)
    assert Rational(2, 3) + Rational(3, 4) == Rational(17, 12)
    assert Rational(2, 3) - Rational(3, 4) == Rational(-1, 12)
    assert Rational(2, 3) > Rational(2, 4)
    assert Rational(2, 4) < Rational(2, 3)
    assert Rational(2, 3) >= Rational(4, 6)
    assert Rational(4, 6) <= Rational(2, 3)
    assert Rational(2, 3) == Rational(4, 6)
    print(fraction.__str__())
    print(fraction.__mul__(Rational(3, 4)))
    print(fraction.__truediv__(Rational(3, 4)))
    print(fraction.__add__(Rational(3, 4)))
    print(fraction.__sub__(Rational(3, 4)))
    print(Rational(1, 4) * (Rational(3, 2) + Rational(1, 8)) + Rational(156, 100))
