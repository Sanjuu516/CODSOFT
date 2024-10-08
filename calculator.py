import tkinter as tk
from tkinter import ttk

class SimpleCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")
        master.geometry("400x300")  # Increased size
        master.resizable(False, False)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', font=('Arial', 12))
        style.configure('TLabel', font=('Arial', 12))
        style.configure('TEntry', font=('Arial', 12))

        self.create_widgets()

    def create_widgets(self):
        # Frame for input fields and operation
        input_frame = ttk.Frame(self.master, padding="10 10 10 10")
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # First number input
        ttk.Label(input_frame, text="First Number:").grid(row=0, column=0, padx=5, pady=10, sticky="e")
        self.first_number = ttk.Entry(input_frame, width=20)
        self.first_number.grid(row=0, column=1, padx=5, pady=10)

        # Second number input
        ttk.Label(input_frame, text="Second Number:").grid(row=1, column=0, padx=5, pady=10, sticky="e")
        self.second_number = ttk.Entry(input_frame, width=20)
        self.second_number.grid(row=1, column=1, padx=5, pady=10)

        # Operation choice
        ttk.Label(input_frame, text="Operation:").grid(row=2, column=0, padx=5, pady=10, sticky="e")
        self.operation = ttk.Combobox(input_frame, values=["+", "-", "*", "/"], width=5, font=('Arial', 12))
        self.operation.grid(row=2, column=1, padx=5, pady=10, sticky="w")
        self.operation.set("+")  # default value

        # Calculate button
        self.calculate_button = ttk.Button(self.master, text="Calculate", command=self.calculate, padding="10 5")
        self.calculate_button.grid(row=1, column=0, pady=20)

        # Result display
        self.result_var = tk.StringVar()
        self.result_var.set("Result: ")
        self.result_label = ttk.Label(self.master, textvariable=self.result_var, font=('Arial', 14, 'bold'))
        self.result_label.grid(row=2, column=0, pady=10)

        # Configure grid weights
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=1)

    def calculate(self):
        try:
            num1 = float(self.first_number.get())
            num2 = float(self.second_number.get())
            op = self.operation.get()

            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 == 0:
                    raise ValueError("Cannot divide by zero")
                result = num1 / num2
            else:
                raise ValueError("Invalid operation")

            self.result_var.set(f"Result: {result:.2f}")
        except ValueError as e:
            self.result_var.set(f"Error: {str(e)}")
        except Exception as e:
            self.result_var.set("Error: Invalid input")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    root.mainloop()