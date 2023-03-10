from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFrame
# from userform import icons

class duplicatePayment(QFrame):
    def __init__(self):
        super(duplicatePayment, self).__init__()
        self.setupUi()

    def setupUi(self):
        Frame =self
        Frame.setObjectName("Frame")
        Frame.resize(744, 475)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(Frame)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Frame)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.line_file1Path = QtWidgets.QLineEdit(self.groupBox)
        self.line_file1Path.setObjectName("line_file1Path")
        self.horizontalLayout_2.addWidget(self.line_file1Path)
        self.button_browseFile1 = QtWidgets.QPushButton(self.groupBox)
        self.button_browseFile1.setObjectName("button_browseFile1")
        self.horizontalLayout_2.addWidget(self.button_browseFile1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.tableWidget_file1 = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget_file1.setObjectName("tableWidget_file1")
        self.tableWidget_file1.setColumnCount(0)
        self.tableWidget_file1.setRowCount(0)
        self.verticalLayout_8.addWidget(self.tableWidget_file1)
        self.verticalLayout_7.addLayout(self.verticalLayout_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.listWidget_chooseFile1 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_chooseFile1.setObjectName("listWidget_chooseFile1")
        self.verticalLayout_5.addWidget(self.listWidget_chooseFile1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.button_addTo1 = QtWidgets.QPushButton(self.groupBox)
        self.button_addTo1.setObjectName("button_addTo1")
        self.verticalLayout_2.addWidget(self.button_addTo1)
        self.button_removeTo1 = QtWidgets.QPushButton(self.groupBox)
        self.button_removeTo1.setObjectName("button_removeTo1")
        self.verticalLayout_2.addWidget(self.button_removeTo1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_addToQuantify1 = QtWidgets.QPushButton(self.groupBox)
        self.button_addToQuantify1.setObjectName("button_addToQuantify1")
        self.verticalLayout.addWidget(self.button_addToQuantify1)
        self.button_removeQuantify1 = QtWidgets.QPushButton(self.groupBox)
        self.button_removeQuantify1.setObjectName("button_removeQuantify1")
        self.verticalLayout.addWidget(self.button_removeQuantify1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.listWidget_finalFile1 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_finalFile1.setObjectName("listWidget_finalFile1")
        self.verticalLayout_4.addWidget(self.listWidget_finalFile1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.listWidget_quantify1 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_quantify1.setObjectName("listWidget_quantify1")
        self.verticalLayout_4.addWidget(self.listWidget_quantify1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.listWidget_uniqueFile1 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_uniqueFile1.setObjectName("listWidget_uniqueFile1")
        self.verticalLayout_6.addWidget(self.listWidget_uniqueFile1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.verticalLayout_9.addLayout(self.verticalLayout_7)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Frame)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.line_file2Path = QtWidgets.QLineEdit(self.groupBox_2)
        self.line_file2Path.setObjectName("line_file2Path")
        self.horizontalLayout_4.addWidget(self.line_file2Path)
        self.button_browseFile2 = QtWidgets.QPushButton(self.groupBox_2)
        self.button_browseFile2.setObjectName("button_browseFile2")
        self.horizontalLayout_4.addWidget(self.button_browseFile2)
        self.verticalLayout_11.addLayout(self.horizontalLayout_4)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_20.addWidget(self.label_19)
        self.tableWidget_file1_2 = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget_file1_2.setObjectName("tableWidget_file1_2")
        self.tableWidget_file1_2.setColumnCount(0)
        self.tableWidget_file1_2.setRowCount(0)
        self.verticalLayout_20.addWidget(self.tableWidget_file1_2)
        self.verticalLayout_11.addLayout(self.verticalLayout_20)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_11.addLayout(self.verticalLayout_12)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_13.addWidget(self.label_11)
        self.listWidget_chooseFile2 = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget_chooseFile2.setObjectName("listWidget_chooseFile2")
        self.verticalLayout_13.addWidget(self.listWidget_chooseFile2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem2)
        self.button_addTo2 = QtWidgets.QPushButton(self.groupBox_2)
        self.button_addTo2.setObjectName("button_addTo2")
        self.verticalLayout_15.addWidget(self.button_addTo2)
        self.button_removeTo2 = QtWidgets.QPushButton(self.groupBox_2)
        self.button_removeTo2.setObjectName("button_removeTo2")
        self.verticalLayout_15.addWidget(self.button_removeTo2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem3)
        self.verticalLayout_14.addLayout(self.verticalLayout_15)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.button_addToQuantify2 = QtWidgets.QPushButton(self.groupBox_2)
        self.button_addToQuantify2.setObjectName("button_addToQuantify2")
        self.verticalLayout_16.addWidget(self.button_addToQuantify2)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_16.addWidget(self.pushButton_10)
        self.verticalLayout_14.addLayout(self.verticalLayout_16)
        self.horizontalLayout_5.addLayout(self.verticalLayout_14)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_17.addWidget(self.label_12)
        self.listWidget_finalFile2 = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget_finalFile2.setObjectName("listWidget_finalFile2")
        self.verticalLayout_17.addWidget(self.listWidget_finalFile2)
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_17.addWidget(self.label_13)
        self.listWidget_quantify2 = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget_quantify2.setObjectName("listWidget_quantify2")
        self.verticalLayout_17.addWidget(self.listWidget_quantify2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_17)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_18.addWidget(self.label_14)
        self.listWidget_uniqueFile2 = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget_uniqueFile2.setObjectName("listWidget_uniqueFile2")
        self.verticalLayout_18.addWidget(self.listWidget_uniqueFile2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_18)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.verticalLayout_10.addLayout(self.verticalLayout_11)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_19.addLayout(self.horizontalLayout)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_15 = QtWidgets.QLabel(Frame)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_7.addWidget(self.label_15)
        self.line_numberOfSearch = QtWidgets.QLineEdit(Frame)
        self.line_numberOfSearch.setObjectName("line_numberOfSearch")
        self.horizontalLayout_7.addWidget(self.line_numberOfSearch)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_16 = QtWidgets.QLabel(Frame)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_6.addWidget(self.label_16)
        self.line_percentage = QtWidgets.QLineEdit(Frame)
        self.line_percentage.setObjectName("line_percentage")
        self.horizontalLayout_6.addWidget(self.line_percentage)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_17 = QtWidgets.QLabel(Frame)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_8.addWidget(self.label_17)
        self.line_saveToPath = QtWidgets.QLineEdit(Frame)
        self.line_saveToPath.setObjectName("line_saveToPath")
        self.horizontalLayout_8.addWidget(self.line_saveToPath)
        self.button_browseSaveTo = QtWidgets.QPushButton(Frame)
        self.button_browseSaveTo.setObjectName("button_browseSaveTo")
        self.horizontalLayout_8.addWidget(self.button_browseSaveTo)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)
        self.verticalLayout_19.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_18 = QtWidgets.QLabel(Frame)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_11.addWidget(self.label_18)
        self.comboMatchingAlgorithm = QtWidgets.QComboBox(Frame)
        self.comboMatchingAlgorithm.setObjectName("comboMatchingAlgorithm")
        self.comboMatchingAlgorithm.addItem("")
        self.comboMatchingAlgorithm.addItem("")
        self.horizontalLayout_11.addWidget(self.comboMatchingAlgorithm)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)
        self.progressBar = QtWidgets.QProgressBar(Frame)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_12.addWidget(self.progressBar)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem5)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.button_submit = QtWidgets.QPushButton(Frame)
        self.button_submit.setObjectName("button_submit")
        self.horizontalLayout_10.addWidget(self.button_submit)
        self.button_clear = QtWidgets.QPushButton(Frame)
        self.button_clear.setObjectName("button_clear")
        self.horizontalLayout_10.addWidget(self.button_clear)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_10)
        self.verticalLayout_19.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13.addLayout(self.verticalLayout_19)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.groupBox.setTitle(_translate("Frame", "Raw file Details"))
        self.label_3.setText(_translate("Frame", "Select file"))
        self.button_browseFile1.setText(_translate("Frame", "Browse"))
        self.label_4.setText(_translate("Frame", "Table View"))
        self.label_5.setText(_translate("Frame", "Choose items"))
        self.button_addTo1.setText(_translate("Frame", "Add to >>"))
        self.button_removeTo1.setText(_translate("Frame", "<< Remove"))
        self.button_addToQuantify1.setText(_translate("Frame", "Add to>>"))
        self.button_removeQuantify1.setText(_translate("Frame", "<< Remove"))
        self.label_6.setText(_translate("Frame", "Final items"))
        self.label_8.setText(_translate("Frame", "Quantify items"))
        self.label_7.setText(_translate("Frame", "Unique items"))
        self.groupBox_2.setTitle(_translate("Frame", "Matcer file Details"))
        self.label_9.setText(_translate("Frame", "Select file"))
        self.button_browseFile2.setText(_translate("Frame", "Browse"))
        self.label_19.setText(_translate("Frame", "Table View"))
        self.label_11.setText(_translate("Frame", "Choose items"))
        self.button_addTo2.setText(_translate("Frame", "Add to >>"))
        self.button_removeTo2.setText(_translate("Frame", "<< Remove"))
        self.button_addToQuantify2.setText(_translate("Frame", "Add to >>"))
        self.pushButton_10.setText(_translate("Frame", "<< Remove"))
        self.label_12.setText(_translate("Frame", "Final items"))
        self.label_13.setText(_translate("Frame", "Quantify items"))
        self.label_14.setText(_translate("Frame", "Unique items"))
        self.label_15.setText(_translate("Frame", "No of search"))
        self.label_16.setText(_translate("Frame", "% threshold"))
        self.label_17.setText(_translate("Frame", "Save to"))
        self.button_browseSaveTo.setText(_translate("Frame", "Browse"))
        self.label_18.setText(_translate("Frame", "Choose Model"))
        self.comboMatchingAlgorithm.setItemText(0, _translate("Frame", "Model 1(Recommended)"))
        self.comboMatchingAlgorithm.setItemText(1, _translate("Frame", "Model 2"))
        self.button_submit.setText(_translate("Frame", "Submit"))
        self.button_clear.setText(_translate("Frame", "Clear"))
