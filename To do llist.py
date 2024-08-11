import tkinter as tk
from tkinter import messagebox, simpledialog
import json
from datetime import datetime

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        # Initialize tasks
        self.tasks = self.load_tasks()

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Task listbox
        self.task_listbox = tk.Listbox(self.root, height=15, width=80)
        self.task_listbox.pack(pady=20)

        # Scrollbar for the listbox
        scrollbar = tk.Scrollbar(self.root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        # Buttons
        btn_add_task = tk.Button(self.root, text="Add Task", width=12, command=self.add_task)
        btn_add_task.pack(side=tk.LEFT, padx=20)

        btn_delete_task = tk.Button(self.root, text="Delete Task", width=12, command=self.delete_task)
        btn_delete_task.pack(side=tk.LEFT, padx=20)

        btn_update_task = tk.Button(self.root, text="Update Task", width=12, command=self.update_task)
        btn_update_task.pack(side=tk.LEFT, padx=20)

        btn_complete_task = tk.Button(self.root, text="Complete Task", width=12, command=self.complete_task)
        btn_complete_task.pack(side=tk.LEFT, padx=20)

        btn_view_tasks = tk.Button(self.root, text="View Tasks", width=12, command=self.view_tasks)
        btn_view_tasks.pack(side=tk.LEFT, padx=20)

        btn_filter_category = tk.Button(self.root, text="Filter by Category", width=15, command=self.filter_by_category)
        btn_filter_category.pack(side=tk.LEFT, padx=20)

        btn_filter_due_date = tk.Button(self.root, text="Filter by Due Date", width=15, command=self.filter_by_due_date)
        btn_filter_due_date.pack(side=tk.LEFT, padx=20)

        # Initialize task listbox with existing tasks
        self.update_task_listbox()

    def add_task(self):
        title = simpledialog.askstring("Add Task", "Enter task title:")
        if title:
            description = simpledialog.askstring("Add Task", "Enter task description:")
            category = simpledialog.askstring("Add Task", "Enter task category:")
            due_date = simpledialog.askstring("Add Task", "Enter due date (YYYY-MM-DD):")
            priority = simpledialog.askstring("Add Task", "Enter priority (High, Medium, Low):")

            task = {
                'title': title,
                'description': description,
                'category': category,
                'due_date': due_date,
                'priority': priority,
                'completed': False
            }
            self.tasks.append(task)
            self.save_tasks()
            self.update_task_listbox()

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.save_tasks()
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Delete Task", "Please select a task to delete.")

    def update_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            task = self.tasks[index]
            title = simpledialog.askstring("Update Task", "Enter new task title:", initialvalue=task['title'])
            if title:
                description = simpledialog.askstring("Update Task", "Enter new task description:", initialvalue=task['description'])
                category = simpledialog.askstring("Update Task", "Enter new task category:", initialvalue=task['category'])
                due_date = simpledialog.askstring("Update Task", "Enter new due date (YYYY-MM-DD):", initialvalue=task['due_date'])
                priority = simpledialog.askstring("Update Task", "Enter new priority (High, Medium, Low):", initialvalue=task['priority'])

                updated_task = {
                    'title': title,
                    'description': description,
                    'category': category,
                    'due_date': due_date,
                    'priority': priority,
                    'completed': task['completed']
                }
                self.tasks[index] = updated_task
                self.save_tasks()
                self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Update Task", "Please select a task to update.")

    def complete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks[index]['completed'] = True
            self.save_tasks()
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Complete Task", "Please select a task to mark as complete.")

    def view_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Completed" if task['completed'] else "Pending"
            self.task_listbox.insert(tk.END, f"{task['title']} - {task['category']} - Due: {task['due_date']} - {status}")

    def filter_by_category(self):
        category = simpledialog.askstring("Filter by Category", "Enter category to filter tasks:")
        if category:
            filtered_tasks = [task for task in self.tasks if task['category'].lower() == category.lower()]
            self.display_filtered_tasks(filtered_tasks)

    def filter_by_due_date(self):
        due_date = simpledialog.askstring("Filter by Due Date", "Enter due date (YYYY-MM-DD) to filter tasks:")
        try:
            datetime.strptime(due_date, '%Y-%m-%d')
            filtered_tasks = [task for task in self.tasks if task['due_date'] == due_date]
            self.display_filtered_tasks(filtered_tasks)
        except ValueError:
            messagebox.showwarning("Filter by Due Date", "Invalid date format. Please use YYYY-MM-DD.")

    def display_filtered_tasks(self, filtered_tasks):
        self.task_listbox.delete(0, tk.END)
        if filtered_tasks:
            for task in filtered_tasks:
                status = "Completed" if task['completed'] else "Pending"
                self.task_listbox.insert(tk.END, f"{task['title']} - {task['category']} - Due: {task['due_date']} - {status}")
        else:
            self.task_listbox.insert(tk.END, "No tasks found.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Completed" if task['completed'] else "Pending"
            self.task_listbox.insert(tk.END, f"{task['title']} - {task['category']} - Due: {task['due_date']} - {status}")

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as f:
                tasks = json.load(f)
        except FileNotFoundError:
            tasks = []
        return tasks

    def save_tasks(self):
        with open('tasks.json', 'w') as f:
            json.dump(self.tasks, f, indent=4)

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
