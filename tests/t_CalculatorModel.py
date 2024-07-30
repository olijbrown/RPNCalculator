import unittest

from src.model.CalculatorModel import CalculatorModel


class TestCalculatorModel(unittest.TestCase):
    def setUp(self):
        self.calculator = CalculatorModel()

    def testTokenise(self):
        self.assertEqual(self.calculator._tokenise('1 + 2'), ['1', '+', '2'])

    def testInfixToPostfix(self):
        self.assertEqual(self.calculator.infixToPostfix('1 + 2'), ['1', '2', '+'])

    def testRPNCalculator(self):
        self.assertEqual(self.calculator.RPNCalculator(['1', '2', '+']), 3.0)

    def testZeroDivision(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.RPNCalculator(['1', '0', '/'])

    def testInvalidExpression(self):
        with self.assertRaises(IndexError):
            self.calculator.RPNCalculator(['1', '2', '+', '+'])

    def testIntegration(self):
        expression = '1 + 2'
        postfixExpression = self.calculator.infixToPostfix(expression)
        result = self.calculator.RPNCalculator(postfixExpression)
        self.assertEqual(result, 3.0)


if __name__ == '__main__':
    unittest.main()
