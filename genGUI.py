from pwgen import pwRandom
from pwgen import userName
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QCheckBox
from PyQt5.QtCore import Qt
import sys


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.specChar = False
        self.email = False
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

        # Checkbox for special characters
        self.checkbox = QCheckBox('Check for special characters', self)
        self.checkbox.stateChanged.connect(self.onStateChangeSpecChar)
        layout.addWidget(self.checkbox)

        # Checkbox for email
        self.checkbox2 = QCheckBox('Check for email', self)
        self.checkbox2.stateChanged.connect(self.onStateChangeEmail)
        layout.addWidget(self.checkbox2)

        # Button display
        self.button = QPushButton('Generate Login', self)
        layout.addWidget(self.button)

        # Result display for username
        self.userLabel = QLabel("<font color='blue'><b>LOGIN: </b></font>")
        self.userResult = QLabel("")
        # Button to copy login to clipboard
        self.buttonCopyLogin = QPushButton('Copy USER to Clipboard', self)
        self.buttonCopyLogin.clicked.connect(self.copyUserToClipboard)
        

        # Result display for password
        self.pwLabel = QLabel("<font color = 'blue'><b>PASSWORD: </b></font>")
        self.pwResult = QLabel("")
        # Button to copy password to clipboard
        self.buttonCopyPW = QPushButton('Copy PASSWORD to Clipboard', self)
        self.buttonCopyPW.clicked.connect(self.copyPWToClipboard)
        
    
        layout.addWidget(self.userLabel)
        layout.addWidget(self.userResult)
        layout.addWidget(self.buttonCopyLogin)
        layout.addWidget(self.pwLabel)
        layout.addWidget(self.pwResult)
        layout.addWidget(self.buttonCopyPW)

        # Final
        self.button.clicked.connect(self.on_click)
        self.setLayout(layout)
        self.show()

    # function to add button to copy to clipboar. copy username and/or password and clears previous clipboard
    def copyPWToClipboard(self):
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.pwResult.text(), mode=cb.Clipboard)
    
    def copyUserToClipboard(self):
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.userResult.text(), mode=cb.Clipboard)
        

    def onStateChangeSpecChar(self, state):
        if state == Qt.Checked:
            self.specChar = True
        else:
            self.specChar = False
    
    def onStateChangeEmail(self, state):
        if state == Qt.Checked:
            self.email = True
        else:
            self.email = False
 

    def on_click(self, state):
        first = self.firstNameBox.text()
        last = self.lastNameBox.text()
        user = userName(first, last, self.email)

        pwSize = int(self.pwSizeNumBox.text())
        password = pwRandom(pwSize, self.specChar)

        self.userResult.setText(user)
        self.pwResult.setText(password)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())