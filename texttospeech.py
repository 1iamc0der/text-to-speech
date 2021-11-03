from PyQt5.QtWidgets import QTextEdit, QWidget,QApplication,QVBoxLayout,QLabel,QPushButton,QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import pyttsx3
engine = pyttsx3.init()



app = QApplication([])

window = QWidget()
window.show()

vline = QVBoxLayout()
text = QPushButton("open txt")
text.setFont(QFont('Arial', 40))
vline.addWidget(text,stretch=30,alignment=Qt.AlignCenter)
window.setLayout(vline)
text_edit = QTextEdit()
vline.addWidget(text_edit)

b = QPushButton("text to speech")
b.setFont(QFont('Arial', 25))
vline.addWidget(b,stretch=10,alignment=Qt.AlignCenter)


rate = engine.getProperty('rate')                          
engine.setProperty('rate', 125)

voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[0].id)

def click():
    engine.say(text_edit.toPlainText())
    engine.runAndWait()
b.clicked.connect(click)

def openfile():
    fname = QFileDialog.getOpenFileName(None, "Select a file...", filter="*.txt")[0]
    f = open(fname,"r")
    text = f.read()
    text_edit.setText(text)
text.clicked.connect(openfile)

app.exec()

