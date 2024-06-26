#destyan abiyyu ghani setyoko A710230046
#Kartika ariyani A710230047
#Yuliana Ambarwati A710230076

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import pyqtSlot

class SMSApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('SMS App')
        self.setGeometry(100, 100, 300, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.phone_label = QLabel('Enter phone number:', self)
        layout.addWidget(self.phone_label)

        self.phone_textbox = QLineEdit(self)

        layout.addWidget(self.phone_textbox)

        self.message_label = QLabel('Enter your message:', self)
        layout.addWidget(self.message_label)

        self.message_textbox = QLineEdit(self)
        layout.addWidget(self.message_textbox)

        self.send_button = QPushButton('Send SMS', self)
        layout.addWidget(self.send_button)

        self.send_button.clicked.connect(self.on_click)

        self.central_widget.setLayout(layout)

    @pyqtSlot()
    def on_click(self):
        phone_number = self.phone_textbox.text()
        message = self.message_textbox.text()
        print(f'SMS Sent to {phone_number}: {message}')
        self.message_label.setText(f'SMS Sent to {phone_number}: {message}')
        self.phone_textbox.clear()
        self.message_textbox.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SMSApp()
    ex.show()
    sys.exit(app.exec_())