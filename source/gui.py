from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.Qt import Qt
import sys

def main(): 
    app     = QtWidgets.QApplication(sys.argv)
    tree    = QtWidgets.QTreeWidget()
    headerItem  = QtWidgets.QTreeWidgetItem()
    item    = QtWidgets.QTreeWidgetItem()

    for i in range(3):
        parent = QtWidgets.QTreeWidgetItem(tree)
        parent.setText(0, "Parent {}".format(i))
        parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
        for x in range(5):
            child = QtWidgets.QTreeWidgetItem(parent)
            child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
            child.setText(0, "Child {}".format(x))
            child.setCheckState(0, Qt.Unchecked)
    tree.show() 
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()