import unittest
from unittest.mock import MagicMock
import tkinter as tk
from src.view.CalculatorView import CalculatorView


class TestCalculatorView(unittest.TestCase):
    def setUp(self):
        self.view = CalculatorView()
        self.view.root.update()

    def testInitialState(self):
        self.assertEqual(self.view.expression, '')
        self.assertEqual(self.view.label.cget('text'), '')

    def testButtonClick(self):
        self.view.on_button_click(MagicMock(widget=MagicMock(cget=MagicMock(return_value='1'))))
        self.view.on_button_click(MagicMock(widget=MagicMock(cget=MagicMock(return_value='+'))))
        self.view.on_button_click(MagicMock(widget=MagicMock(cget=MagicMock(return_value='2'))))

        self.assertEqual(self.view.expression, '1 + 2')
        self.assertEqual(self.view.label.cget('text'), '1 + 2')

    def testClearButtonClick(self):
        self.view.on_button_click(MagicMock(widget=MagicMock(cget=MagicMock(return_value='1'))))
        self.view.on_button_click(MagicMock(widget=MagicMock(cget=MagicMock(return_value='+'))))
        self.view.on_button_click(MagicMock(widget=MagicMock(cget=MagicMock(return_value='2'))))

        self.view.on_button_click(MagicMock(widget=MagicMock(cget=MagicMock(return_value='C'))))

        self.assertEqual(self.view.expression, '')
        self.assertEqual(self.view.label.cget('text'), '')

    def testEqualsButtonClick(self):
        mock_controller = MagicMock()
        self.view.set_controller(mock_controller)

        # Simulate button clicks to form an expression
        self.view.on_button_click(MagicMock(widget=MagicMock(cget=MagicMock(return_value='1'))))
        self.view.on_button_click(MagicMock(widget=MagicMock(cget=MagicMock(return_value='+'))))
        self.view.on_button_click(MagicMock(widget=MagicMock(cget=MagicMock(return_value='2'))))

        # Simulate equals button click
        self.view.on_button_click(MagicMock(widget=MagicMock(cget=MagicMock(return_value='='))))

        mock_controller.evaluate_expression.assert_called_once_with('1 + 2')

    def tearDown(self):
        self.view.root.destroy()


if __name__ == '__main__':
    unittest.main()