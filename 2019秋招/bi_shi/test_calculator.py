
# 测试代码
from unittest import TestCase
from bi_shi.calculator import Calculator

class TestCalculator(TestCase):
    def test_multiply(self):
        sleep(0.1)
        self.fail()


class TestCalculator(TestCase):
    def test_add(self):
        self.calculator = Calculator()
        self.assertEqual(self.calculator.add(3,4),7)
        # self.fail()
