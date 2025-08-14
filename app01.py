import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineSettings
from PyQt6.QtCore import QUrl
import os

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        lucro = 1000
        despesas = 500

        self.setWindowTitle("My App")
        self.setMinimumSize(QSize(1250, 600))  

        self.browser = QWebEngineView()
        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls,True)

        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "mapa.html"))
        self.browser.setUrl(QUrl.fromLocalFile(file_path))

        tabs = QTabWidget()
        tabs.setDocumentMode(True)
        tabs.setTabPosition(QTabWidget.TabPosition.North)
        tabs.setMovable(True)

        page0 = QWidget()
        layout0 = QHBoxLayout()
        layout1 = QVBoxLayout()

        layout0.addWidget(self.browser)

        layout1.addWidget(QLabel("Cordenadas Do Polígono"))
        layout1.addWidget(QLabel("[10.21,12.21]"))
        layout1.addWidget(QLabel("[142.234,1545.23]"))
        layout1.addWidget(QLabel("[3214.2134,42314.2413]"))
        layout1.addWidget(QLabel("[32165.123,42134.4213]"))
        

        layout0.addLayout(layout1)
        page0.setLayout(layout0)

        page1 = QWidget()
        layout1 = QVBoxLayout()
        self.label1 = QLabel("<h1> Lucro:  %s€ &  Despesas:  %s€ </h1>" % (lucro, despesas))
        layout1.addWidget(self.label1, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        page1.setLayout(layout1)

        tabs.addTab(page0, "MAPA")
        tabs.addTab(page1, "Relatório")
        
        self.setCentralWidget(tabs)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()