from pwgen import pwRandom
from pwgen import userName
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QCheckBox
from PyQt5.QtCore import Qt
import sys


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.specChar = False
        self.title = 'Login Generator'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        
        layout = QVBoxLayout()

        # UserName box
        self.label1 = QLabel("Enter first name:")
        self.firstNameBox = QLineEdit(self)
        self.label2 = QLabel("Enter last name")
        self.lastNameBox = QLineEdit(self)

        layout.addWidget(self.label1)
        layout.addWidget(self.firstNameBox)
        layout.addWidget(self.label2)
        layout.addWidget(self.lastNameBox)

        # Password box
        self.label = QLabel("Enter desired password length:")
        self.pwSizeNumBox = QLineEdit(self)

        layout.addWidget(self.label)
        layout.addWidget(self.pwSizeNumBox)

        # Checkbox
        self.checkbox = QCheckBox('Check for special characters', self)
        self.checkbox.stateChanged.connect(self.onStateChange)
        layout.addWidget(self.checkbox)
        
        # Button display
        self.button = QPushButton('Generate Login', self)
        layout.addWidget(self.button)

        # Result display
        self.userResult = QLabel("<font color='blue'><b>LOGIN: </b></font>")
        self.result = QLabel("")
        self.pwResult = QLabel("<font color = 'blue'><b>PASSWORD: </b></font>")
        self.result2 = QLabel("")
    
        layout.addWidget(self.userResult)
        layout.addWidget(self.result)
        layout.addWidget(self.pwResult)
        layout.addWidget(self.result2)

        # Final
        self.button.clicked.connect(self.on_click)
        self.setLayout(layout)
        self.show()

    def onStateChange(self, state):
        if state == Qt.Checked:
            self.specChar = True
        else:
            self.specChar = False
 

    def on_click(self, state):
        first = self.firstNameBox.text()
        last = self.lastNameBox.text()
        user = userName(first, last)

        pwSize = int(self.pwSizeNumBox.text())
        password = pwRandom(pwSize, self.specChar)

        self.result.setText(user)
        self.result2.setText(password)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())