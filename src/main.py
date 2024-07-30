from src.controller.CalculatorController import CalculatorController
from src.model.CalculatorModel import *
from src.view.CalculatorView import *


if __name__ == "__main__":
    model = CalculatorModel()
    view = CalculatorView()
    controller = CalculatorController(model, view)
    view.run()

