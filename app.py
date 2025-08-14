import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QVBoxLayout, QLabel
from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setMinimumSize(QSize(800, 600))  # Set a fixed size for the window
        #self.setMaximumSize(QSize(800, 900))  # Set a fixed size for the window
        
        layout = QVBoxLayout()
        self.label = QLabel("<h1> Hello, Diana </h1>")
        self.button = QPushButton("Clica em mim!")

        widget = Color("red")
        
        self.button.setMinimumSize(QSize(200, 100))  # Set a fixed size for the window
        self.button.setMaximumSize(QSize(400, 300))  # Set a fixed size for the window

        self.button.clicked.connect(self.on_button_clicked)

        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(widget)    

        window = QWidget()
        window.setLayout(layout)

        self.setCentralWidget(window)

    def on_button_clicked(self):
        self.label.setText("<h1> Tens Perguntas??</h1>")  
        self.button.setText("Pedro Resolve Tudo!")

app = QApplication([])


window = MainWindow()
window.show()

app.exec()