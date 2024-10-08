import tkinter as tk
from tkinter import messagebox
import string
import random

class PasswordGeneratorApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        # Define the color scheme
        self.bg_color = "#FFFFFF"  # Light background color
        self.title_color = "#2980B9"  # Bright blue for the title
        self.label_color = "#000000"  # Black for labels
        self.btn_color = "#3a3a3a"  # Dark gray for buttons
        self.entry_bg_color = "#ECF0F1"  # Light gray for entry fields
        self.entry_fg_color = "#000000"  # Black for text in entry fields
        self.radio_bg_color = "#ECF0F1"  # Light gray for radio buttons
        self.radio_select_color = "#16A085"  # Teal for selected radio buttons
        self.password_fg_color = "#1c0505"  # Dark color for password display

        # Set the main window background color
        self.root.config(bg=self.bg_color)

        # Title label
        self.title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 26, "bold"),
                                     bg=self.bg_color, fg=self.title_color)
        self.title_label.pack(pady=30)

        # Label for password length input
        self.length_label = tk.Label(root, text="Desired Password Length:", font=("Helvetica", 16, "bold"),
                                      bg=self.bg_color, fg=self.label_color)
        self.length_label.pack(pady=10)

        # Entry field for password length
        self.length_entry = tk.Entry(root, font=("Helvetica", 16), width=10, bg=self.entry_bg_color,
                                      fg=self.entry_fg_color, insertbackground=self.entry_fg_color)
        self.length_entry.pack(pady=10)

        # Label for password strength selection
        self.strength_title_label = tk.Label(root, text="Select Password Strength:", font=("Helvetica", 16, "bold"),
                                              bg=self.bg_color, fg=self.label_color)
        self.strength_title_label.pack(pady=20)

        # Frame for radio buttons
        self.strength_frame = tk.Frame(root, bg=self.bg_color)
        self.strength_frame.pack(pady=10)

        # Variable to hold the selected password strength
        self.strength_var = tk.StringVar(value="easy")

        # Radio buttons for password strength options
        self.easy_radio = tk.Radiobutton(self.strength_frame, text="Easy", variable=self.strength_var, value="easy",
                                          font=("Helvetica", 14), bg=self.radio_bg_color, fg=self.label_color,
                                          selectcolor=self.radio_select_color, activebackground=self.bg_color)
        self.easy_radio.grid(row=0, column=0, padx=15)

        self.moderate_radio = tk.Radiobutton(self.strength_frame, text="Moderate", variable=self.strength_var,
                                              value="moderate", font=("Helvetica", 14), bg=self.radio_bg_color,
                                              fg=self.label_color, selectcolor=self.radio_select_color, activebackground=self.bg_color)
        self.moderate_radio.grid(row=0, column=1, padx=15)

        self.hard_radio = tk.Radiobutton(self.strength_frame, text="Hard", variable=self.strength_var, value="hard",
                                          font=("Helvetica", 14), bg=self.radio_bg_color, fg=self.label_color,
                                          selectcolor=self.radio_select_color, activebackground=self.bg_color)
        self.hard_radio.grid(row=0, column=2, padx=15)

        # Button to generate the password
        self.generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 16, "bold"),
                                          bg="#3a3a3a", fg="#000000", command=self.generate_password,
                                          activebackground="#555555", activeforeground="#FFFFFF")
        self.generate_button.pack(pady=20)

        # Button to clear the generated password
        self.clear_button = tk.Button(root, text="Clear", font=("Helvetica", 16, "bold"), bg="#3a3a3a",
                                      fg="#000000", command=self.clear_password,
                                      activebackground="#555555", activeforeground="#FFFFFF")
        self.clear_button.pack(pady=10)

        # Label to display the generated password
        self.password_label = tk.Label(root, text="", font=("Helvetica", 18, "bold"), bg=self.bg_color,
                                       fg=self.password_fg_color, wraplength=450)
        self.password_label.pack(pady=20)

    def generate_password(self):
        """Generate a random password based on user inputs."""
        try:
            # Get the desired length of the password
            length = int(self.length_entry.get())
            if length < 1:
                raise ValueError("Password length must be at least 1!")

            # Determine character set based on selected strength
            strength = self.strength_var.get()
            if strength == "easy":
                characters = string.ascii_lowercase  # Only lowercase letters
            elif strength == "moderate":
                characters = string.ascii_letters + string.digits  # Letters and digits
            else:
                characters = string.ascii_letters + string.digits + string.punctuation  # Include punctuation

            # Generate the password
            password = ''.join(random.choice(characters) for _ in range(length))

            # Display the generated password
            self.password_label.config(text=password)
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    def clear_password(self):
        """Clear the password label and input field."""
        self.password_label.config(text="")
        self.length_entry.delete(0, tk.END)
        self.strength_var.set("easy")  # Reset to default strength

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
