import math

import app


class InvalidPermissions(Exception):
    pass


class Calculator:
    @staticmethod
    def validate_operand(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Parameter must be a number")

    @classmethod
    def validate_operands(cls, *operands):
        for operand in operands:
            cls.validate_operand(operand)

    def add(self, x, y):
        self.validate_operands(x, y)
        return x + y

    def substract(self, x, y):
        self.validate_operands(x, y)
        return x - y

    def multiply(self, x, y):
        self.validate_operands(x, y)
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions("User has no permissions")

        return x * y

    def divide(self, x, y):
        self.validate_operands(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        self.validate_operands(x, y)
        return math.pow(x, y)

    def sqrt(self, x):
        self.validate_operand(x)
        if x < 0:
            raise TypeError("Square root is not defined for negative numbers")

        return math.sqrt(x)

    def log10(self, x):
        self.validate_operand(x)
        if x <= 0:
            raise TypeError("Logarithm base 10 is not defined for non-positive numbers")

        return math.log10(x)


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
