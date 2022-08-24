from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import random
import matplotlib.pyplot as plt
import numpy as np


class Calculation():
    def __init__(self) -> None:
        self.test_case_number = 100
        self.no_of_prisoner = 100
        self.data = ""
        self.no_of_pass = None
        self.percentage = None
        self.test_case = np.array(
            [i for i in range(1, self.test_case_number+1)])
        self.passes = []

    def set_data(self, test_case_number, no_of_prisoner) -> None:
        self.test_case_number = test_case_number
        self.no_of_prisoner = no_of_prisoner
        self.data = ""
        self.test_case = [i for i in range(1, self.test_case_number+1)]

    def calculate(self):
        self.data = "No of Prisoner who Passed\n"
        total_pass = 0
        arr = np.array([])
        for i in range(1, self.test_case_number+1):
            nums = [i for i in range(1, self.no_of_prisoner+1)]
            random.shuffle(nums)
            no_of_pass = 0
            for j in range(self.no_of_prisoner):
                count = 1
                ind = j+1
                while True:
                    if nums[ind-1] == j+1:
                        break
                    else:
                        ind = nums[ind-1]
                        count += 1
                if count > int(self.no_of_prisoner/2):
                    pass
                else:
                    no_of_pass += 1
            arr = np.append(arr, no_of_pass)
            self.data += f"Test Case {i}: {no_of_pass}\n"
            if no_of_pass == self.no_of_prisoner:
                total_pass += 1
        self.no_of_pass = total_pass
        self.percentage = round((total_pass/self.test_case_number)*100, 4)
        self.data += f"\nFinal Percentage: {self.percentage}%"
        self.passes = arr

    def get_data(self):
        print(self.data)
        print(f"Total: {self.test_case_number}")
        print(f"No of Prisoner: {self.no_of_prisoner}")
        print(f"No of Pass: {self.no_of_pass}")
        print(f"Percentage: {self.percentage}")

    def plot_graph(self):
        plt.bar(self.test_case, self.passes, width=1.0)
        # plt.show()
        # plt.plot(self.test_case, self.passes)
        plt.plot([0, self.test_case_number], [
                 self.no_of_prisoner/2, self.no_of_prisoner/2])
        plt.xlabel("Test Case")
        plt.ylabel("No of Prisoner who Passed")
        plt.savefig("graph.png")
        plt.clf()


class Ui_PrisonerPuzzle(object):
    def setupUi(self, PrisonerPuzzle):
        self.Calculation = Calculation()
        PrisonerPuzzle.setObjectName("PrisonerPuzzle")
        PrisonerPuzzle.resize(1440, 900)
        PrisonerPuzzle.setMinimumSize(QtCore.QSize(1440, 900))
        PrisonerPuzzle.setMaximumSize(QtCore.QSize(1440, 900))

        self.main_widget = QtWidgets.QWidget(PrisonerPuzzle)
        self.main_widget.setObjectName("main_widget")
        self.title = QtWidgets.QLabel(self.main_widget)
        self.title.setGeometry(QtCore.QRect(340, 30, 760, 90))
        font1 = QtGui.QFont()
        font1.setFamily("Monotype Corsiva")
        font1.setPointSize(40)
        self.title.setFont(font1)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.total_label = QtWidgets.QLabel(self.main_widget)
        self.total_label.setGeometry(QtCore.QRect(50, 150, 410, 50))

        font = QtGui.QFont()
        font.setPointSize(20)

        self.total_label.setFont(font)
        self.total_label.setObjectName("total_label")
        self.no_of_prisoner_label = QtWidgets.QLabel(self.main_widget)
        self.no_of_prisoner_label.setGeometry(QtCore.QRect(845, 150, 390, 50))

        self.no_of_prisoner_label.setFont(font)
        self.no_of_prisoner_label.setObjectName("no_of_prisoner_label")
        self.total = QtWidgets.QLineEdit(self.main_widget)
        self.total.setGeometry(QtCore.QRect(465, 147, 150, 55))

        self.total.setFont(font)
        self.total.setMaxLength(4)
        self.total.setObjectName("total")
        self.no_of_prisoner = QtWidgets.QLineEdit(self.main_widget)
        self.no_of_prisoner.setGeometry(QtCore.QRect(1240, 147, 150, 55))

        self.no_of_prisoner.setFont(font)
        self.no_of_prisoner.setMaxLength(4)
        self.no_of_prisoner.setObjectName("no_of_prisoner")
        self.lego = QtWidgets.QLabel(self.main_widget)
        self.lego.setGeometry(QtCore.QRect(1140, 230, 300, 370))
        self.lego.setText("")
        self.lego.setPixmap(QtGui.QPixmap("pic1.png"))
        self.lego.setScaledContents(True)
        self.lego.setWordWrap(False)
        self.lego.setObjectName("lego")
        self.pass_percent = QtWidgets.QProgressBar(self.main_widget)
        self.pass_percent.setEnabled(True)
        self.pass_percent.setGeometry(QtCore.QRect(50, 790, 1340, 60))

        self.pass_percent.setFont(font)
        self.pass_percent.setProperty("value", 0)
        self.pass_percent.setTextVisible(True)
        self.pass_percent.setInvertedAppearance(False)
        self.pass_percent.setObjectName("pass_percent")
        self.data = QtWidgets.QPlainTextEdit(self.main_widget)
        self.data.setGeometry(QtCore.QRect(50, 630, 1340, 100))

        self.data.setFont(font)
        self.data.setReadOnly(True)
        self.data.setPlainText("")
        self.data.setObjectName("data")
        self.pass_percent_label = QtWidgets.QLabel(self.main_widget)
        self.pass_percent_label.setGeometry(QtCore.QRect(50, 735, 410, 50))
        self.pass_percent_label.setFont(font)
        self.pass_percent_label.setObjectName("pass_percent_label")
        self.graph = QtWidgets.QLabel(self.main_widget)
        self.graph.setGeometry(QtCore.QRect(50, 210, 810, 410))
        self.graph.setAutoFillBackground(True)
        self.graph.setText("")
        self.graph.setObjectName("graph")
        self.graph.setScaledContents(True)

        self.simulate_button = QtWidgets.QPushButton(self.main_widget)
        self.simulate_button.setGeometry(QtCore.QRect(890, 300, 280, 75))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(30)
        self.simulate_button.setFont(font)
        self.simulate_button.setObjectName("simulate_button")
        self.simulate_button.clicked.connect(
            partial(self.simulate_button_clicked))

        self.reset_button = QtWidgets.QPushButton(self.main_widget)
        self.reset_button.setGeometry(QtCore.QRect(890, 465, 280, 75))
        self.reset_button.setFont(font)
        self.reset_button.setObjectName("reset_button")
        self.reset_button.clicked.connect(partial(self.reset_button_clicked))

        self.label = QtWidgets.QLabel(self.main_widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1440, 900))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("bg.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.title.raise_()
        self.total_label.raise_()
        self.no_of_prisoner_label.raise_()
        self.total.raise_()
        self.no_of_prisoner.raise_()
        self.lego.raise_()
        self.pass_percent.raise_()
        self.data.raise_()
        self.pass_percent_label.raise_()
        self.graph.raise_()
        self.simulate_button.raise_()
        self.reset_button.raise_()
        PrisonerPuzzle.setCentralWidget(self.main_widget)
        self.menubar = QtWidgets.QMenuBar(PrisonerPuzzle)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 26))
        self.menubar.setObjectName("menubar")
        PrisonerPuzzle.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PrisonerPuzzle)
        self.statusbar.setObjectName("statusbar")
        PrisonerPuzzle.setStatusBar(self.statusbar)

        self.retranslateUi(PrisonerPuzzle)
        QtCore.QMetaObject.connectSlotsByName(PrisonerPuzzle)

    def simulate_button_clicked(self):
        total_no = self.total.text()
        no_of_prisoner = self.no_of_prisoner.text()
        try:
            total_no = int(total_no)
            no_of_prisoner = int(no_of_prisoner)
        except ValueError:
            self.data.setPlainText("Please enter valid number")
            return
        if total_no < 1 or no_of_prisoner < 2:
            self.data.setPlainText("Please enter valid number")
            return
        self.data.setPlainText("Calculating...")
        self.pass_percent.setProperty("value", 0)
        self.Calculation.set_data(total_no, no_of_prisoner)
        self.Calculation.calculate()
        self.pass_percent.setProperty("value", self.Calculation.percentage)
        self.data.setPlainText(self.Calculation.data)
        self.Calculation.plot_graph()
        self.graph.setPixmap(QtGui.QPixmap("graph.png"))

    def reset_button_clicked(self):
        self.total.setText("")
        self.no_of_prisoner.setText("")
        self.data.setPlainText("")
        self.pass_percent.setValue(0)
        self.graph.setPixmap(QtGui.QPixmap(""))

    def retranslateUi(self, PrisonerPuzzle):
        _translate = QtCore.QCoreApplication.translate
        PrisonerPuzzle.setWindowTitle(
            _translate("PrisonerPuzzle", "Prisoner Puzzle"))
        self.title.setText(_translate(
            "PrisonerPuzzle", "100 Prisoner Puzzle Simulation"))
        self.total_label.setText(_translate(
            "PrisonerPuzzle", "Total Number of Test Case:"))
        self.no_of_prisoner_label.setText(_translate(
            "PrisonerPuzzle", "Total Number of Prisoner:"))
        self.pass_percent.setFormat(_translate("PrisonerPuzzle", "%p%"))
        self.pass_percent_label.setText(_translate(
            "PrisonerPuzzle", "Pass Percentage:-"))
        self.simulate_button.setText(_translate("PrisonerPuzzle", "Simulate"))
        self.reset_button.setText(_translate("PrisonerPuzzle", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PrisonerPuzzle = QtWidgets.QMainWindow()
    ui = Ui_PrisonerPuzzle()
    ui.setupUi(PrisonerPuzzle)
    PrisonerPuzzle.show()
    sys.exit(app.exec_())
