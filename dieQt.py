from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox, QLineEdit, QListWidget
from PyQt5.QtCore import Qt
import sys
import random
import winsound as ws

class PyDie(QWidget):
    def __init__(self):
        super().__init__()

        self.die_values = {"D100":100, "D20": 20, "D12": 12, "D10": 10, "D8": 8, "D6": 6, "D4": 4, "Coin Flip":2, "Custom": 1}
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.result_label = QLabel("Roll a Die")
        self.layout.addWidget(self.result_label)

        self.die_selector = QComboBox()
        self.die_selector.addItems(self.die_values.keys())
        self.die_selector.currentTextChanged.connect(self.die_selector_handler)
        self.layout.addWidget(self.die_selector)

        self.custom_die_entry = QLineEdit()
        self.custom_die_entry.setText("69")
        self.custom_die_entry.setPlaceholderText("Enter Custom Die Value")
        self.custom_die_entry.hide()
        self.layout.addWidget(self.custom_die_entry)

        self.roll_button = QPushButton("Roll")
        self.roll_button.clicked.connect(self.roll_die)
        self.layout.addWidget(self.roll_button)

        self.history = QListWidget()
        self.layout.addWidget(self.history)

        self.setLayout(self.layout)

    def roll_die(self):
        die_type = self.die_selector.currentText()
        roll_result = random.randint(1, self.die_values[die_type])

        if die_type == "Coin Flip":
            roll_result = "Tails" if roll_result == 1 else "Heads"

        if die_type == "Custom":
            custom_die_value = self.custom_die_entry.text()
            if custom_die_value.isnumeric():
                roll_result = random.randint(1, int(custom_die_value))
            else:
                roll_result = "Invalid Custom Die Value"

        #self.history.insertItem(0, f"{'Die Type:' + die_type + ' ' if die_type != 'Coin Flip' else die_type + ' '}Result: {roll_result}")
        if roll_result == "Invalid Custom Die Value":
            self.history.insertItem(0, roll_result)
        else:
            self.history.insertItem(0, f"{'Die Type: D' + self.custom_die_entry.text() + ' ' if (die_type == 'Custom') else ('Die Type: ' + die_type + ' ') }Result: {roll_result} ")
                
        self.result_label.setText(str(roll_result))

        # Generate beep sound
        ws.Beep(random.randrange(37,2500), 100)
        #QApplication.beep()

    def die_selector_handler(self, value):
        if value == "Custom":
            self.custom_die_entry.show()
        else:
            self.custom_die_entry.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PyDie()
    ex.show()

    # Apply dark theme
    app.setStyleSheet("""
    QWidget {
        background-color: #2b2b2b;
        color: #b1b1b1;
    }
    QPushButton {
        background-color: #333333;
        border: 1px solid #555555;
        border-radius: 2px;
        padding: 5px;
    }
    QPushButton:hover {
        background-color: #444444;
    }
    QPushButton:pressed {
        background-color: #555555;
    }
    QComboBox {
        background-color: #333333;
        border: 1px solid #555555;
        border-radius: 2px;
        padding: 5px;
    }
    QComboBox:hover {
        background-color: #444444;
    }
    QComboBox:pressed {
        background-color: #555555;
    }
    QLineEdit {
        background-color: #333333;
        border: 1px solid #555555;
        border-radius: 2px;
        padding: 5px;
    }
    QLineEdit:hover {
        background-color: #444444;
    }
    QLineEdit:pressed {
        background-color: #555555;
    }
    QListWidget {
        background-color: #333333;
        border: 1px solid #555555;
        border-radius: 2px;
        padding: 5px;
    }
    QListWidget:hover {
        background-color: #444444;
    }
    QListWidget:pressed {
        background-color: #555555;
    }
    """)

    sys.exit(app.exec_())