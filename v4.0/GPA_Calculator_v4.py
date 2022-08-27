from PyQt6 import QtCore, QtGui, QtWidgets


def get_term(line):
    """
    Gets and returns the term of the course
    :param line: A list representing a line of text with course information
    :return: A string representing the term of the course
    """
    return line[0:4]


def get_credits(line):
    """
    Gets and returns the number of credits the course is worth
    :param line: A list representing a line of text with course information
    :return: A string representing the credits of the course
    """
    return line[19:23]


def get_grade(line):
    """
    Gets and returns the grade obtained in the course
    :param line: A list representing a line of text with course information
    :return: A string representing the letter grade of the course
    """
    if line[-1] == "+":
        return line[-2:]
    return line[-1]


def get_code(line):
    """
    Gets and returns the course code of the course
    :param line: A list representing a line of text with course information
    :return: A string representing the course code of the course
    """
    return line[8:17]


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """
        Creates and arranges all visual elements of the GUI
        :param MainWindow:
        :return:None
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 607)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(390, 30, 69, 22))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 30, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 30, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(510, 30, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(550, 30, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 80, 721, 371))
        self.textBrowser.setReadOnly(False)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 30, 71, 23))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 470, 271, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 500, 231, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(730, 470, 41, 16))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 530, 311, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.calculate)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
        Renames many widgets in the GUI and adds text to them
        :param MainWindow:
        :return:None
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GPA Calculator"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "ALL"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "FW"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "SU"))
        self.label.setText(_translate("MainWindow", "Department:"))
        self.label_2.setText(_translate("MainWindow", "Session:"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "(i.e., \"MATH\" or \"ALL\")"))
        self.lineEdit.echoMode()
        self.label_3.setText(_translate("MainWindow", "Year:"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "(i.e., \"21\" or \"ALL\")"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.label_4.setText(_translate("MainWindow", "Your Grade Point Total:"))
        self.label_5.setText(_translate("MainWindow", "Your Credit Total:"))
        self.label_7.setText(_translate("MainWindow", "Your Grade Point Average:"))

    def calculate(self):
        """
        Calculates GPA, Grade Point Total, and Credit Total and updates the GUI accordingly
        :return:None
        """
        letter_to_gp = {
            "A+": 9.0,
            "A": 8.0,
            "B+": 7.0,
            "B": 6.0,
            "C+": 5.0,
            "C": 4.0,
            "D+": 3.0,
            "D": 2.0,
            "E": 1.0
        }

        gpt = 0
        ct = 0
        transcript_text = self.textBrowser.toPlainText()
        course_code = self.lineEdit.displayText().upper()
        year = self.lineEdit_2.displayText()
        term = self.comboBox_2.currentText()

        for x in transcript_text.splitlines():
            if (course_code == "ALL" or get_code(x).__contains__(course_code)) and letter_to_gp.get(
                    get_grade(x)) is not None:
                if (get_term(x).__contains__(term) or term == "ALL") and (get_term(x).__contains__(year)
                                                                          or year == "ALL"):
                    gpt += float(get_credits(x)) * letter_to_gp.get(get_grade(x))
                    ct += float(get_credits(x))
        if ct == 0:
            self.label_4.setText("Error: No courses found")
            self.label_5.setText("")
            self.label_7.setText("")
        else:
            self.label_4.setText("Your Grade Point Total: {}".format(gpt))
            self.label_5.setText("Your Credit Total: {}".format(ct))
            self.label_7.setText("Your Grade Point Average: {:.4f}".format(gpt / ct))
            gpt = 0
            ct = 0


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
