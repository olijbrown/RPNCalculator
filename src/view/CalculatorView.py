import tkinter as tk


class CalculatorView:
    def __init__(self):
        self.expression = ''

        self.root = tk.Tk()
        self.root.title('Calculator')
        self.root.resizable(False, False)

        self.label = tk.Label(self.root, text='', font=("Arial", 24), anchor='e', bg='white', fg='black')
        self.label.grid(row=0, column=0, columnspan=4, sticky='we', padx=5, pady=5)

        buttons = [
            'C', '(', ')', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '='
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            b = tk.Button(self.root, text=button, font=("Arial", 18), width=12 if button == '=' else 4, height=2)
            b.grid(row=row_val, column=col_val, columnspan=2 if button == '=' else 1, padx=5, pady=5)
            b.bind('<Button-1>', self.on_button_click)

            col_val += 2 if button == '=' else 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, event):
        button_text = event.widget.cget('text')

        if button_text == 'C':
            self.expression = ''
        elif button_text == '=':
            self.controller.evaluate_expression(self.expression)
            return  # exit early as the controller will update the view
        elif button_text == '(':
            self.expression += button_text + ' '
        elif button_text == ')':
            self.expression += ' ' + button_text
        elif button_text == '+' or button_text == '-' or button_text == '/' or button_text == '*':
            self.expression += ' ' + button_text + ' '
        else:
            self.expression += button_text

        self.update_label()

    def update_label(self):
        self.label.config(text=self.expression)

    def set_controller(self, controller):
        self.controller = controller

    def set_expression(self, expression):
        self.expression = expression
        self.update_label()

    def run(self):
        self.root.mainloop()
