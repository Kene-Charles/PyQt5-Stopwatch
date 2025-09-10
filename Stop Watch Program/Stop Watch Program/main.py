
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer, QTime, Qt

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("stop", self)
        self.reset_button = QPushButton("reset", self)
        self.time_label = QLabel("00:00:00:00", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stop Watch")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)



        self.time_label.setAlignment(Qt.AlignCenter)

        self.setLayout(vbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)



        vbox.addLayout(hbox)



        self.start_button.setObjectName("start_button")
        self.stop_button.setObjectName("stop_button")
        self.reset_button.setObjectName("reset_button")

        def make_shadow(button):
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(60)  # How soft the shadow is
            shadow.setOffset(-2, -2)  # X, Y offset
            shadow.setColor(QColor("black"))
            button.setGraphicsEffect(shadow)


        for btn in [self.start_button, self.stop_button, self.reset_button]:
            make_shadow(btn)



        self.setStyleSheet("""
            QPushButton{
                font-size: 40px;
                font-family: Arial;
                width: 200px;
                height: 200px;
                margin: 50px;
                font-family: calibri;
                font-weight: bold;
                
                
                border-radius: 100px;
                color: black;
            }
            QPushButton#start_button{
                background-color: green;
            }
            QPushButton#stop_button{
                background-color: red;
            }
            QPushButton#reset_button{
                background-color: blue;
            }
            QPushButton#start_button:hover{
                box-shadow: 15px 15px 2px black;
            }
            QPushButton#stop_button:hover{
                box-shadow: 5px 5px 20px black;
            }
            QPushButton#reset_button:hover{
                box-shadow: 5px 5px 20px black;
            }
            QLabel{
                font-size: 150px;
                background-color: blue;
                font-weight: bold;
                
                
            }
        """)
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_time)

    def enter_event(self):
        pass

    def leave_event(self):
        pass

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))


    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))
        






if __name__ == "__main__":
    app = QApplication(sys.argv)
    stop_watch = StopWatch()
    stop_watch.show()
    sys.exit(app.exec_())
