from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox, QLineEdit, QListWidget, QCheckBox
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import sys
import random
import winsound as ws

class PyDie(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('resources/icon.ico'))
        self.die_values = {"D100":100, "D20": 20, "D12": 12, "D10": 10, "D8": 8, "D6": 6, "D4": 4, "Coin Flip":2, "Custom": 1}
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PyDie")
        
        self.layout = QVBoxLayout()
        self.setMinimumWidth(300)
       
        self.result_label = QLabel("Roll a Die")
        self.layout.addWidget(self.result_label)

        #Dropdown to select die type, D20 by default
        self.die_selector = QComboBox()
        self.die_selector.addItems(self.die_values.keys())
        self.die_selector.setCurrentText("D20")
        self.die_selector.currentTextChanged.connect(self.die_selector_handler)
        self.layout.addWidget(self.die_selector)

        self.custom_die_entry = QLineEdit()
        self.custom_die_entry.setText("69")
        self.custom_die_entry.setPlaceholderText("Enter Custom Die Value")
        self.custom_die_entry.hide()
        self.layout.addWidget(self.custom_die_entry)

        ##Checkbox to allow user to indicate if they want to run multiple rolls
        self.roll_multi_checkbox = QCheckBox("Roll Multiple Times?")
        self.roll_multi_checkbox.stateChanged.connect(self.multi_checkbox_handler)
        self.layout.addWidget(self.roll_multi_checkbox)

        #Number input to allow user to indicate how many times they want to roll. Hidden until checkbox is checked
        self.multi_roll_input = QLineEdit()
        self.multi_roll_input.setPlaceholderText("Enter Number of Rolls")
        self.layout.addWidget(self.multi_roll_input)
        self.multi_roll_input.hide()
        

        self.roll_button = QPushButton("Roll")
        self.roll_button.clicked.connect(self.roll_die)
        self.layout.addWidget(self.roll_button)

        self.history = QListWidget()
        self.layout.addWidget(self.history)
        self.history.insertItem(0, "Welcome to PyDie! Roll a die to get started.")
        
        self.setLayout(self.layout)

        #Settings button, shown in botleft of window, small and unobtrusive
        #Button shows a cogwheel icon
        self.settings_button = QPushButton("Settings")
        self.settings_button.setIcon(QtGui.QIcon("resources/settings.png"))
        self.settings_button.setFixedSize(64, 25)
        self.settings_button.clicked.connect(self.settings_button_handler)
        self.layout.addWidget(self.settings_button, alignment=Qt.AlignRight)

        #Checkbox to toggle roll sounds, enabled by default
        self.sound_checkbox = QCheckBox("Roll/Flip Sounds")
        self.sound_checkbox.setIcon(QtGui.QIcon("resources/sound.png"))
        self.sound_checkbox.setChecked(True)
        
        

       

    def roll_die(self):
        
        die_type = self.die_selector.currentText()
        roll_result = random.randint(1, self.die_values[die_type])
        multi_roll = False  

        if self.roll_multi_checkbox.isChecked():
            #User has selected multi roll, so get the number of rolls from the input
            num_rolls = self.multi_roll_input.text()
            multi_roll = True

            if num_rolls.isnumeric():
                #Insert a divider to separate the rolls
                self.history.insertItem(0,"---------------------------")
            else:
                self.history.insertItem(0, "Invalid Number of Rolls!")
                return
        else:
            #User hasn't enabled multi roll, so set num_rolls to 1    
            num_rolls = 1
            multi_roll = False
           
        for i in range(int(num_rolls)):
            print(f"Roll {i+1} of {num_rolls}")
            if die_type == "Coin Flip":
                print("Coin Flip")
                roll_result = random.randint(1, self.die_values[die_type])
                roll_result = "Tails" if roll_result == 1 else "Heads"
            elif die_type == "Custom":
                print("Custom Die, Size:" + self.custom_die_entry.text())
                roll_result = random.randint(1, int(self.custom_die_entry.text()))
            else:
                roll_result = random.randint(1, self.die_values[die_type])
                    
            self.history.insertItem(0, f"{'Die Type: D' + self.custom_die_entry.text() + ' ' if (die_type == 'Custom') else ('Die Type: ' + die_type + ' ') }| Result: {roll_result} ")
        
        if multi_roll:
            self.history.insertItem(0,"----Multi Roll Complete, Rolled " + num_rolls + " Times----")
                

        # Check if flip or roll and play correct sound
        if(self.sound_checkbox.isChecked()):
            if(die_type == "Coin Flip"):
                ws.PlaySound("resources/coinflip.wav", ws.SND_ASYNC)
            else:
                ws.PlaySound("resources/dieroll.wav", ws.SND_ASYNC)

    ## Input handler functions
            
    def die_selector_handler(self, value):
        if value == "Custom":
            self.custom_die_entry.show()
        else:
            self.custom_die_entry.hide()

    def multi_checkbox_handler(self, state):
        if state == Qt.Checked:
            self.roll_button.setText("Roll Multiple")
            self.multi_roll_input.show()
        else:
            self.roll_button.setText("Roll")
            self.multi_roll_input.hide()
    
    def settings_button_handler(self):
        print("Settings Button Clicked")
        #Open settings window:
        self.sound_checkbox.show()
        
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