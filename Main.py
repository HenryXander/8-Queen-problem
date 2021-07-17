import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from Puzzle import Puzzle


class MyWindow(QMainWindow):
    def __init__(self, sequence):
        super(MyWindow, self).__init__()
        self.setGeometry(600, 200, 600, 600)
        self.setWindowTitle("Puzzle")

        self.sequence = sequence #array of steps to the solution
        self.stap = -1
        self.initUI()

    def initUI(self):
        self.lcdNumber_1 = QtWidgets.QLCDNumber(self)
        self.lcdNumber_1.setGeometry(0, 100, 190, 100)
        self.lcdNumber_1.setObjectName("spot_1")

        self.lcdNumber_2 = QtWidgets.QLCDNumber(self)
        self.lcdNumber_2.setGeometry(200, 100, 190, 100)
        self.lcdNumber_2.setObjectName("spot_2")

        self.lcdNumber_3 = QtWidgets.QLCDNumber(self)
        self.lcdNumber_3.setGeometry(400, 100, 190, 100)
        self.lcdNumber_3.setObjectName("spot_3")


        self.lcdNumber_4 = QtWidgets.QLCDNumber(self)
        self.lcdNumber_4.setGeometry(0, 210, 190, 100)
        self.lcdNumber_4.setObjectName("spot_4")


        self.lcdNumber_5 = QtWidgets.QLCDNumber(self)
        self.lcdNumber_5.setGeometry(200, 210, 190, 100)
        self.lcdNumber_5.setObjectName("spot_5")


        self.lcdNumber_6 = QtWidgets.QLCDNumber(self)
        self.lcdNumber_6.setGeometry(400, 210, 190, 100)
        self.lcdNumber_6.setObjectName("spot_6")


        self.lcdNumber_7 = QtWidgets.QLCDNumber(self)
        self.lcdNumber_7.setGeometry(0, 320, 190, 100)
        self.lcdNumber_7.setObjectName("spot_7")


        self.lcdNumber_8 = QtWidgets.QLCDNumber(self)
        self.lcdNumber_8.setGeometry(200, 320, 190, 100)
        self.lcdNumber_8.setObjectName("spot_8")


        self.lcdNumber_9 = QtWidgets.QLCDNumber(self)
        self.lcdNumber_9.setGeometry(400, 320, 190, 100)
        self.lcdNumber_9.setObjectName("spot_9")

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateGrid)
        self.timer.start(1500)
    def updateGrid(self):
        self.timer.stop()
        if (self.stap != len(self.sequence) - 1):
            self.stap += 1
            self.volgorde = self.sequence[self.stap]

            if self.volgorde[0] == 0:
                self.lcdNumber_1.setVisible(False)
            else:
                self.lcdNumber_1.setVisible(True)
                self.lcdNumber_1.setProperty("intValue", self.volgorde[0])

            if self.volgorde[1] == 0:
                self.lcdNumber_2.setVisible(False)
            else:
                self.lcdNumber_2.setVisible(True)
                self.lcdNumber_2.setProperty("intValue", self.volgorde[1])
            if self.volgorde[2] == 0:
                self.lcdNumber_3.setVisible(False)
            else:
                self.lcdNumber_3.setVisible(True)
                self.lcdNumber_3.setProperty("intValue", self.volgorde[2])
            if self.volgorde[3] == 0:
                self.lcdNumber_4.setVisible(False)
            else:
                self.lcdNumber_4.setVisible(True)
                self.lcdNumber_4.setProperty("intValue", self.volgorde[3])
            if self.volgorde[4] == 0:
                self.lcdNumber_5.setVisible(False)
            else:
                self.lcdNumber_5.setVisible(True)
                self.lcdNumber_5.setProperty("intValue", self.volgorde[4])
            if self.volgorde[5] == 0:
                self.lcdNumber_6.setVisible(False)
            else:
                self.lcdNumber_6.setVisible(True)
                self.lcdNumber_6.setProperty("intValue", self.volgorde[5])
            if self.volgorde[6] == 0:
                self.lcdNumber_7.setVisible(False)
            else:
                self.lcdNumber_7.setVisible(True)
                self.lcdNumber_7.setProperty("intValue", self.volgorde[6])
            if self.volgorde[7] == 0:
                self.lcdNumber_8.setVisible(False)
            else:
                self.lcdNumber_8.setVisible(True)
                self.lcdNumber_8.setProperty("intValue", self.volgorde[7])
            if self.volgorde[8] == 0:
                self.lcdNumber_9.setVisible(False)
            else:
                self.lcdNumber_9.setVisible(True)
                self.lcdNumber_9.setProperty("intValue", self.volgorde[8])

            self.timer.start(1500)

def window():
    start = [1, 4, 6, 0, 8, 5, 7, 3, 2]
    puz = Puzzle(start)
    counter = 0
    succes = False
    while (succes == False and counter < 1000):
        succes = puz.selectNext()
        counter += 1
    print("solution found:", end = ' ')
    print(succes)
    end = puz.getSelected()
    goal = end.getState()
    sequence = puz.getPath()
    sequence.reverse()
    sequence.append(goal)
    print("length of path:", end = ' ')
    print(len(sequence))
    print("amount of nodes in the queue:", end = ' ')
    print(len(puz.Nodes))

    app = QApplication(sys.argv)
    win = MyWindow(sequence)
    win.show()


    sys.exit(app.exec_())

window()
