import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QWindow
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from ostylesheet import OGenericStyleSheet

stylesheet = OGenericStyleSheet(font_size=20,
                                margin=(15, 15),
                                padding=(15, 15))


class OComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.items = ['Test', 'Test01']
        self.addItems(self.items)
        self.setStyleSheet("QComboBox {border: 5px solid gray;"
                           "border-radius: 10px;"
                           "padding: 10px 10px;}"
                           "QComboBox::drop-down {border-radius: 15px;"
                           "border: 5px solid gray;"
                           
                           "padding: 15px 15px;}"
                           )


class OCheckBoxes(QGridLayout):
    def __init__(self):
        super().__init__()
        for c in range(10):
            for r in range(5):
                chk = QCheckBox()
                chk.setStyleSheet("QCheckBox {spacing: 15px;}"
                                  "QCheckBox::indicator {width: 35px; height: 35px;}"
                                  )
                self.addWidget(chk, c - 1, r - 1)


class OTextField(QGridLayout):
    def __init__(self):
        super(OTextField, self).__init__()
        label = QLabel('Text Test')
        label.setAlignment(QtCore.Qt.AlignLeft)
        label.setStyleSheet(stylesheet.simple_no_bg())
        text = QTextEdit()
        self.addWidget(label, 1, 1, 1, 1)
        self.addWidget(text, 2, 1, 3, 1)


class OButton(QPushButton):
    def __init__(self, button_name, action=None, corners=15):
        super().__init__()
        if action is None:
            action = self.temp_action
        self.action = action
        self.corners = corners
        self.setText(button_name)
        self.setStyleSheet(stylesheet.flat_and_hover())

        self.clicked.connect(self.action)

    @staticmethod
    def temp_action():
        print('IM CLICKED')


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(800, 600)
        self.setWindowTitle('Tidy Up Your Shit')
        self.layout = QGridLayout()
        self.setStyleSheet(
            f"background: {stylesheet.main_bg_color}"
        )
        button01 = OButton('Tidy Up Your Shit')
        button02 = OButton('Select Location', action=self.file_dialog)

        chk = OCheckBoxes()
        txt = OTextField()
        combobox = OComboBox()

        self.setLayout(self.layout)
        self.layout.addWidget(button01, 2, 1)
        self.layout.addWidget(button02, 1, 1)
        self.layout.addLayout(chk, 3, 1)
        self.layout.addLayout(txt, 1, 2, 4, 1)
        self.layout.addWidget(combobox,4,1,1,2)
        self.show()

    def file_dialog(self):
        try:
            dialog = QFileDialog.getExistingDirectory(self, 'Open File', "")
        except:
            print('Something went wrong')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
