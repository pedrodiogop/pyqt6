import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineSettings
from PyQt6.QtCore import QUrl, QObject, pyqtSlot
from PyQt6.QtWebChannel import QWebChannel
import os
from layout_colorwidget import Color



class Bridge(QObject):
    def __init__(self, label):
        super().__init__()
        self.label = label

    @pyqtSlot(float, float)
    def sendCoordinates(self, lat, lng):
        print(f"Coordenadas recebidas: {lat}, {lng}")
        self.label.setText(f"Coordenadas: {lat:.6f}, {lng:.6f}")
        self.label.repaint()  # Garante atualização imediata




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Varaiveis 
        lucro = 1000
        despesas = 500

        # Função Carrega Ficheiro .html 
        def create_map(html_file):
            browser = QWebEngineView()
            browser.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls,True)
            browser.setUrl(QUrl.fromLocalFile(html_file))
            return browser
        
        # Configurações da Janela
        self.setWindowTitle("My App")
        self.setMinimumSize(QSize(1250, 600))  

        # Tabs 
        tabs = QTabWidget()
        tabs.setDocumentMode(True)
        tabs.setTabPosition(QTabWidget.TabPosition.North)
        tabs.setMovable(True)

        # Tab 1 

        page0 = QWidget()
        layout0 = QHBoxLayout()
        layout1 = QVBoxLayout()

        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "map/mapa.html"))
        browser = create_map(file_path)
        layout0.addWidget(browser)

        layout1.addWidget(QLabel("Cordenadas Do Polígono"))
        layout1.addWidget(QLabel("[10.21,12.21]"))
        layout1.addWidget(QLabel("[142.234,1545.23]"))
        layout1.addWidget(QLabel("[3214.2134,42314.2413]"))
        layout1.addWidget(QLabel("[32165.123,42134.4213]"))
        layout1.addWidget(QLabel("[32165.123,42134.4213]"))


        layout0.addLayout(layout1)
        page0.setLayout(layout0)

        # Tab 2

        page1 = QWidget()
        layout1 = QVBoxLayout()
        label1 = QLabel("<h1> Lucro:  %s€ &  Despesas:  %s€ </h1>" % (lucro, despesas))
        layout1.addWidget(label1, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        page1.setLayout(layout1)

        # Tab 3 Testes

        page2 = QWidget()
        layout0 = QHBoxLayout()
        layout1 = QVBoxLayout()
        
        coord_label = QLabel("Clique no mapa...")

        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "map01/mapa_01.html"))
        browser = create_map(file_path)
        layout0.addWidget(browser)
        layout1.addWidget(coord_label)

        # Criar a "ponte" e o canal
        # Criar canal
        channel = QWebChannel()
        bridge = Bridge(coord_label)  # Passar label
        channel.registerObject("bridge", bridge)
        browser.page().setWebChannel(channel)



        layout0.addLayout(layout1)
        page2.setLayout(layout0)

       
        tabs.addTab(page0, "App")
        tabs.addTab(page1, "Relatório")
        tabs.addTab(page2, "Testes")
        
        self.setCentralWidget(tabs)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()