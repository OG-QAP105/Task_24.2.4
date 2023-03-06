# import pytest
from app.calculator import Calculator

class TestCalc:
    """Класс набора тестов для тестирования калькулятора"""
    def setup(self):
        self.calc = Calculator

    def test_adding(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_substraction(self):
        assert self.calc.subtraction(self, 2, 1) == 1

    def test_multiply(self):
        assert self.calc.multiply(self, 5, 5) == 25

    def test_division(self):
        assert self.calc.division(self, 10, 2) == 5

    def teardown(selfself):
        print("Выполнение метода teardown")



