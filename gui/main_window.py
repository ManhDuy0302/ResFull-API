import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QPushButton, QLineEdit, QTextEdit, 
                            QListWidget, QMessageBox)
import requests

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Todo List Manager")
        self.setGeometry(100, 100, 600, 400)
        self.api_url = "http://127.0.0.1:5000/todos"
        self.init_ui()
        self.load_todos()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout()

        # Left panel - List of todos
        self.todo_list = QListWidget()
        self.todo_list.itemClicked.connect(self.display_todo)
        layout.addWidget(self.todo_list)

        # Right panel - Todo details and controls
        right_panel = QVBoxLayout()
        
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Todo Title")
        right_panel.addWidget(self.title_input)

        self.desc_input = QTextEdit()
        self.desc_input.setPlaceholderText("Todo Description")
        right_panel.addWidget(self.desc_input)

        # Buttons
        button_layout = QHBoxLayout()
        
        self.add_button = QPushButton("Add Todo")
        self.add_button.clicked.connect(self.add_todo)
        button_layout.addWidget(self.add_button)

        self.update_button = QPushButton("Update Todo")
        self.update_button.clicked.connect(self.update_todo)
        button_layout.addWidget(self.update_button)

        self.delete_button = QPushButton("Delete Todo")
        self.delete_button.clicked.connect(self.delete_todo)
        button_layout.addWidget(self.delete_button)

        right_panel.addLayout(button_layout)
        layout.addLayout(right_panel)
        
        central_widget.setLayout(layout)

    def load_todos(self):
        try:
            response = requests.get(self.api_url)
            todos = response.json()
            self.todo_list.clear()
            for todo in todos:
                self.todo_list.addItem(f"{todo['id']}: {todo['title']}")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Error", f"Failed to load todos: {str(e)}")

    def display_todo(self, item):
        todo_id = int(item.text().split(':')[0])
        try:
            response = requests.get(f"{self.api_url}/{todo_id}")
            todo = response.json()
            self.title_input.setText(todo['title'])
            self.desc_input.setPlainText(todo['description'])
        except requests.RequestException as e:
            QMessageBox.critical(self, "Error", f"Failed to load todo: {str(e)}")

    def add_todo(self):
        data = {
            'title': self.title_input.text(),
            'description': self.desc_input.toPlainText()
        }
        try:
            response = requests.post(self.api_url, json=data)
            if response.status_code == 201:
                self.load_todos()
                self.clear_inputs()
        except requests.RequestException as e:
            QMessageBox.critical(self, "Error", f"Failed to add todo: {str(e)}")

    def update_todo(self):
        selected = self.todo_list.currentItem()
        if not selected:
            QMessageBox.warning(self, "Warning", "Please select a todo to update")
            return
        
        todo_id = int(selected.text().split(':')[0])
        data = {
            'title': self.title_input.text(),
            'description': self.desc_input.toPlainText(),
            'completed': False
        }
        try:
            response = requests.put(f"{self.api_url}/{todo_id}", json=data)
            if response.status_code == 200:
                self.load_todos()
                self.clear_inputs()
        except requests.RequestException as e:
            QMessageBox.critical(self, "Error", f"Failed to update todo: {str(e)}")

    def delete_todo(self):
        selected = self.todo_list.currentItem()
        if not selected:
            QMessageBox.warning(self, "Warning", "Please select a todo to delete")
            return
        
        todo_id = int(selected.text().split(':')[0])
        try:
            response = requests.delete(f"{self.api_url}/{todo_id}")
            if response.status_code == 200:
                self.load_todos()
                self.clear_inputs()
        except requests.RequestException as e:
            QMessageBox.critical(self, "Error", f"Failed to delete todo: {str(e)}")

    def clear_inputs(self):
        self.title_input.clear()
        self.desc_input.clear()