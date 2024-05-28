import csv
import tkinter as tk
from tkinter import ttk

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

def load_csv_data(file_path):
    data_stack = Stack()
    header = []
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # Get header
            for row in csv_reader:
                data_stack.push(row)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error occurred: {e}")

    return header, data_stack

def delete_selected_row():
    selected_item = treeview.focus()
    if selected_item:
        try:
            index = int(selected_item.split('I')[-1]) - 1
            deleted_row = data_stack.items.pop(index)
            treeview.delete(selected_item)
            undo_stack.push((index, deleted_row))
        except IndexError:
            print("Error: Index out of range.")

def undo_delete():
    if not undo_stack.is_empty():
        try:
            index, undone_row = undo_stack.pop()
            data_stack.items.insert(index, undone_row)
            treeview.insert('', index, values=undone_row, iid=f'I{index+1}')
        except IndexError:
            print("Error: Index out of range.")


def display_csv_data():
    global treeview, data_stack, undo_stack
    
    file_path = 'C:\\DSA\\Scraping Mid Project\\DSA Final Project\\books.csv'
    header, data_stack = load_csv_data(file_path)
    undo_stack = Stack()

    root = tk.Tk()
    root.title("CSV Data Display")

    root.configure(background='#6417FF')  # Use hex color code for background

    treeview_frame = tk.Frame(root, bg='white')  # Change treeview frame background color
    treeview_frame.pack(pady=10)

    treeview = ttk.Treeview(treeview_frame, columns=header, show='headings')
    treeview.pack()

    for col in header:
        treeview.heading(col, text=col, anchor='center')  # Center-align column headers
        treeview.column(col, anchor='center')  # Center-align cell data

    for idx, row in enumerate(data_stack.items):
        treeview.insert('', 'end', values=row, iid=f'I{idx+1}')

    button_frame = tk.Frame(root, bg='#6417FF')  # Use hex color code for button frame
    button_frame.pack(pady=10)

    delete_button = tk.Button(button_frame, text="Delete", command=delete_selected_row, bg='#F3F8FF', fg='black')
    delete_button.pack(side=tk.LEFT, padx=5)

    undo_button = tk.Button(button_frame, text="Undo", command=undo_delete, bg='#F3F8FF', fg='black')
    undo_button.pack(side=tk.LEFT, padx=5)

    root.mainloop()

display_csv_data()