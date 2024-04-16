# Form implementation generated from reading ui file 'UI/MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 552)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(243, 242, 248);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainTabLabel = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.mainTabLabel.setFont(font)
        self.mainTabLabel.setObjectName("mainTabLabel")
        self.verticalLayout.addWidget(self.mainTabLabel)
        self.searchBar = QtWidgets.QLineEdit(parent=self.frame)
        self.searchBar.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.searchBar.setFont(font)
        self.searchBar.setToolTip("")
        self.searchBar.setStatusTip("")
        self.searchBar.setStyleSheet("background-color: rgb(228, 227, 233);\n"
"margin: 2 px;\n"
"border-radius: 2px;")
        self.searchBar.setText("")
        self.searchBar.setObjectName("searchBar")
        self.verticalLayout.addWidget(self.searchBar)
        self.verticalLayout_3.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_button = QtWidgets.QPushButton(parent=self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy)
        self.add_button.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.add_button.setFont(font)
        self.add_button.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"margin-right: 2 px;\n"
"margin-left: 2px;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(224, 224, 224);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(224, 224, 224, 40);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/add_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.add_button.setIcon(icon)
        self.add_button.setObjectName("add_button")
        self.horizontalLayout.addWidget(self.add_button)
        self.edit_button = QtWidgets.QPushButton(parent=self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_button.sizePolicy().hasHeightForWidth())
        self.edit_button.setSizePolicy(sizePolicy)
        self.edit_button.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.edit_button.setFont(font)
        self.edit_button.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"margin-right: 2 px;\n"
"margin-left: 2px;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(224, 224, 224);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(224, 224, 224, 40);\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/edit_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.edit_button.setIcon(icon1)
        self.edit_button.setObjectName("edit_button")
        self.horizontalLayout.addWidget(self.edit_button)
        self.delete_button = QtWidgets.QPushButton(parent=self.frame_2)
        self.delete_button.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setKerning(False)
        self.delete_button.setFont(font)
        self.delete_button.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"margin-right: 2 px;\n"
"margin-left: 2px;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(224, 224, 224);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(224, 224, 224, 40);\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/delete_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.delete_button.setIcon(icon2)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout.addWidget(self.delete_button)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.table_of_notes = QtWidgets.QTableView(parent=self.frame_3)
        self.table_of_notes.setStyleSheet("QTableView {\n"
"    background-color: rgb(228, 227, 233);\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QTableView::section {\n"
"    background-color: rgb(214, 214, 214);\n"
"    color: rgb(255, 255, 255);\n"
"    height: 50px;\n"
"    font-size: 14pt;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    border-style: none;\n"
"    border-button: rgba(255, 255, 255, 40);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    border: none;\n"
"    color: rgba(255, 255, 255, 40)\n"
"}")
        self.table_of_notes.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_of_notes.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_of_notes.setShowGrid(False)
        self.table_of_notes.setObjectName("table_of_notes")
        self.table_of_notes.horizontalHeader().setDefaultSectionSize(135)
        self.verticalLayout_4.addWidget(self.table_of_notes)
        self.verticalLayout_3.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainTabLabel.setText(_translate("MainWindow", "My notes"))
        self.searchBar.setPlaceholderText(_translate("MainWindow", "Search"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.edit_button.setText(_translate("MainWindow", "Edit"))
        self.delete_button.setText(_translate("MainWindow", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
