# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(356, 523)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.featuresTree = QtWidgets.QTreeWidget(self.centralwidget)
        self.featuresTree.setGeometry(QtCore.QRect(0, 100, 351, 321))
        self.featuresTree.setObjectName("featuresTree")
        self.featuresTree.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        
        self.report_path = ""

        item_0 = QtWidgets.QTreeWidgetItem(self.featuresTree)
        item_0.setCheckState(0, QtCore.Qt.Unchecked)
        item_0.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)

        item_0 = QtWidgets.QTreeWidgetItem(self.featuresTree)
        item_0.setCheckState(0, QtCore.Qt.Unchecked)
        item_0.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)

        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)

        item_0 = QtWidgets.QTreeWidgetItem(self.featuresTree)
        item_0.setCheckState(0, QtCore.Qt.Unchecked)
        item_0.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)

        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)

        self.fileButton = QtWidgets.QPushButton(self.centralwidget)
        self.fileButton.setGeometry(QtCore.QRect(120, 50, 80, 23))
        self.fileButton.setObjectName("fileButton")
        self.fileButton.clicked.connect(self.openFile)

        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(90, 20, 141, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(90, 450, 166, 24))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(self.process_data)
        self.buttonBox.rejected.connect(self.exit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

 


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fuckoo"))
        self.featuresTree.headerItem().setText(0, _translate("MainWindow", "Select Features"))
        __sortingEnabled = self.featuresTree.isSortingEnabled()
        self.featuresTree.setSortingEnabled(False)
        self.featuresTree.topLevelItem(0).setText(0, _translate("MainWindow", "procmemory"))
        self.featuresTree.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "file"))
        self.featuresTree.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "urls"))
        self.featuresTree.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "pid"))
        self.featuresTree.topLevelItem(1).setText(0, _translate("MainWindow", "network"))
        self.featuresTree.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "udp"))
        self.featuresTree.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "tcp"))
        self.featuresTree.topLevelItem(1).child(2).setText(0, _translate("MainWindow", "hosts"))
        self.featuresTree.topLevelItem(1).child(3).setText(0, _translate("MainWindow", "dns"))
        self.featuresTree.topLevelItem(1).child(3).child(0).setText(0, _translate("MainWindow", "request"))
        self.featuresTree.topLevelItem(1).child(4).setText(0, _translate("MainWindow", "domains"))
        self.featuresTree.topLevelItem(2).setText(0, _translate("MainWindow", "behavior"))
        self.featuresTree.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "processes"))
        self.featuresTree.topLevelItem(2).child(0).child(0).setText(0, _translate("MainWindow", "pid"))
        self.featuresTree.topLevelItem(2).child(0).child(1).setText(0, _translate("MainWindow", "process_name"))
        self.featuresTree.topLevelItem(2).child(0).child(2).setText(0, _translate("MainWindow", "ppid"))
        self.featuresTree.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "summary"))
        self.featuresTree.topLevelItem(2).child(1).child(0).setText(0, _translate("MainWindow", "file_created"))
        self.featuresTree.topLevelItem(2).child(1).child(1).setText(0, _translate("MainWindow", "dll_loaded"))
        self.featuresTree.topLevelItem(2).child(1).child(2).setText(0, _translate("MainWindow", "regkey_opened"))
        self.featuresTree.topLevelItem(2).child(1).child(3).setText(0, _translate("MainWindow", "command_line"))
        self.featuresTree.topLevelItem(2).child(1).child(4).setText(0, _translate("MainWindow", "regkey_read"))
        self.featuresTree.topLevelItem(2).child(1).child(5).setText(0, _translate("MainWindow", "regkey_written"))
        self.featuresTree.setSortingEnabled(__sortingEnabled)
        self.fileButton.setText(_translate("MainWindow", "Select File"))
        self.titleLabel.setText(_translate("MainWindow", "Cuckoo Report Filter"))

    def openFile(self):
        self.report_path =  QFileDialog.getExistingDirectory(None, 'Select a directory')
        print(self.report_path)

    def process_data(self):
        if self.report_path:
            self.get_selected_features()
            print('Getting selected features from:'+ str(self.report_path))
        else:
            print('Select a file!')

    def exit(self):
        sys.exit()

    def get_selected_features(self):
        features = []
        for item in self.featuresTree.findItems("", QtCore.Qt.MatchContains | QtCore.Qt.MatchRecursive):
            if (item.checkState(0) == 1): #Partially checked (Solo hijos)
                print("Entro if 1")
                print(item.text(0))
                #if(item.childCount()>0):
                #    print("ES PADRE:") # 
                #    print((item.text(0)))
                #else:
                #    print("ES HIJO:") 
                #    print((item.text(0)))

            elif (item.checkState(0) == 2): #Fully checked    
                features.append(item.text(0))
                
        print(features)
        #We check if a father or sub-father is in the list. If it is, then we call a function to extract every
        #child of that father.
        #If no father is in this list, then we only extract the selected children.
            #if (item.rowCount() == 0 and item.checkState()>0):
            #    print (item.text(),item.checkState())
                

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
