import tkinter as tk
from tkinter import messagebox, font

class TodoApp:
    def __init__(self, master):
        # Set up the main window
        self.master = master
        self.master.title("To-Do List")
        self.master.geometry("850x500")

        # Set the background color to a gradient-like effect using shades of blue
        self.master.configure(bg="#a1c4fd")  # Soft sky-blue background

        self.tasks = []  # List to store the tasks

        # Define custom fonts for the title and tasks
        self.title_font = font.Font(family="Helvetica", size=28, weight="bold")
        self.task_font = font.Font(family="Helvetica", size=22)

        # Create the title label at the top of the app
        self.title_label = tk.Label(self.master, text="To-Do List", font=self.title_font, bg="#a1c4fd", fg="#000000")
        self.title_label.pack(pady=15)

        # Create an entry box for users to input their tasks
        self.task_entry = tk.Entry(self.master, width=30, font=self.task_font, bg="#FFFFFF", fg="#000000", 
                                   highlightbackground="#6DD5FA", highlightthickness=0.5)
        self.task_entry.pack(pady=10)

        # Create and configure the buttons (Add, Mark Complete, Delete)
        self.create_buttons()

        # Create a Listbox to display tasks with a scrollbar for better navigation
        self.create_task_listbox()

    def create_buttons(self):
        """Creates the buttons for adding, marking complete, and deleting tasks."""
        # Add Task Button with vibrant green color
        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task, 
                                    bg="#00B894", fg="#000000", font=self.task_font,
                                    activebackground="#00D9A3", activeforeground="#000000", 
                                    highlightthickness=0, relief="flat")
        self.add_button.pack(pady=5)

        # Mark as Complete Button with a soft blue color
        self.complete_button = tk.Button(self.master, text="Mark as Complete", command=self.mark_complete, 
                                         bg="#0984E3", fg="#000000", font=self.task_font,
                                         activebackground="#74B9FF", activeforeground="#000000", 
                                         highlightthickness=0, relief="flat")
        self.complete_button.pack(pady=5)

        # Delete Task Button with vibrant red color
        self.delete_button = tk.Button(self.master, text="Delete Task", command=self.delete_task, 
                                       bg="#D63031", fg="#000000", font=self.task_font,
                                       activebackground="#FF7675", activeforeground="#000000", 
                                       highlightthickness=0, relief="flat")
        self.delete_button.pack(pady=5)

    def create_task_listbox(self):
        """Creates the Listbox to display the tasks, along with a scrollbar."""
        # Create a frame to contain the Listbox and Scrollbar
        self.frame = tk.Frame(self.master, bg="#a1c4fd")
        self.frame.pack(pady=10)

        # Task Listbox for showing the list of tasks
        self.task_listbox = tk.Listbox(self.frame, width=40, height=10, font=self.task_font, 
                                       bg="#ECF0F1", fg="#000000", selectbackground="#74B9FF", 
                                       selectforeground="#FFFFFF", activestyle="none")
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar for the Listbox
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Link the scrollbar to the Listbox
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

    def add_task(self):
        """Adds a new task to the list."""
        task = self.task_entry.get()
        if task:  # Only add if there is input
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)  # Insert task into the Listbox
            self.task_entry.delete(0, tk.END)  # Clear the entry field after adding
        else:
            messagebox.showwarning("Warning", "Please enter a task.")  # Warn if input is empty

    def mark_complete(self):
        """Marks the selected task as complete by adding a checkmark and graying it out."""
        try:
            index = self.task_listbox.curselection()[0]  # Get the selected task's index
            task = self.task_listbox.get(index)  # Get the task text
            if not task.startswith("✅ "):  # If not already marked as complete
                self.task_listbox.delete(index)  # Remove the old task
                self.task_listbox.insert(index, f"✅{task}")  # Add the modified task
                self.task_listbox.itemconfig(index, fg="grey")  # Mark it as grey
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")  # If no task is selected

    def delete_task(self):
        """Deletes the selected task from the list."""
        try:
            index = self.task_listbox.curselection()[0]  # Get the selected task's index
            self.task_listbox.delete(index)  # Delete the task from the Listbox
            del self.tasks[index]  # Remove the task from the internal task list
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")  # If no task is selected

# Start the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
