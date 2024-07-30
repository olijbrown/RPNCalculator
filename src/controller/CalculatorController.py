from src.model.CalculatorModel import *
from src.view.CalculatorView import *


class CalculatorController:
    def __init__(self, model: CalculatorModel, view: CalculatorView):
        self.model = model
        self.view = view
        self.view.set_controller(self)

    def evaluate_expression(self, expression):
        try:
            postfixExpression = self.model.infixToPostfix(expression)
            result = str(self.model.RPNCalculator(postfixExpression))
        except Exception as e:
            result = 'Error'
        self.model.stack = []
        self.view.set_expression(result)
