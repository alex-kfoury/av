# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ioconfig.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import config, sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IOConfig(object):
    def setupUi(self, IOConfig):
        assiLines, varLines = [], []

        IOConfig.setObjectName("IOConfig")
        IOConfig.resize(503, 305)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(IOConfig.sizePolicy().hasHeightForWidth())
        IOConfig.setSizePolicy(sizePolicy)
        IOConfig.setWindowOpacity(1.0)
        self.gridLayout = QtWidgets.QGridLayout(IOConfig)
        self.gridLayout.setObjectName("gridLayout")
        self.genVertLay = QtWidgets.QVBoxLayout()
        self.genVertLay.setObjectName("genVertLay")
        self.assiVertLay = QtWidgets.QVBoxLayout()
        self.assiVertLay.setObjectName("assiVertLay")
        self.line_4 = QtWidgets.QFrame(IOConfig)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.assiVertLay.addWidget(self.line_4)
        self.assiLabel = QtWidgets.QLabel(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assiLabel.sizePolicy().hasHeightForWidth())
        self.assiLabel.setSizePolicy(sizePolicy)
        self.assiLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.assiLabel.setObjectName("assiLabel")
        self.assiVertLay.addWidget(self.assiLabel)
        self.line_3 = QtWidgets.QFrame(IOConfig)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.assiVertLay.addWidget(self.line_3)
        self.assiGridLay = QtWidgets.QGridLayout()
        self.assiGridLay.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.assiGridLay.setObjectName("assiGridLay")
        self.sortielabel = QtWidgets.QLabel(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sortielabel.sizePolicy().hasHeightForWidth())
        self.sortielabel.setSizePolicy(sizePolicy)
        self.sortielabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sortielabel.setObjectName("sortielabel")
        self.assiGridLay.addWidget(self.sortielabel, 0, 2, 1, 1)
        self.addAssiButton = QtWidgets.QToolButton(IOConfig)
        self.addAssiButton.setObjectName("addAssiButton")
        self.assiGridLay.addWidget(self.addAssiButton, 1, 3, 1, 1)
        self.entreelabel = QtWidgets.QLabel(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entreelabel.sizePolicy().hasHeightForWidth())
        self.entreelabel.setSizePolicy(sizePolicy)
        self.entreelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.entreelabel.setObjectName("entreelabel")
        self.assiGridLay.addWidget(self.entreelabel, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.assiGridLay.addWidget(self.label, 0, 0, 1, 1)
        self.assiVertLay.addLayout(self.assiGridLay)
        self.genVertLay.addLayout(self.assiVertLay)
        self.varVertLay = QtWidgets.QVBoxLayout()
        self.varVertLay.setObjectName("varVertLay")
        self.line = QtWidgets.QFrame(IOConfig)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.varVertLay.addWidget(self.line)
        self.varLabel = QtWidgets.QLabel(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.varLabel.sizePolicy().hasHeightForWidth())
        self.varLabel.setSizePolicy(sizePolicy)
        self.varLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.varLabel.setObjectName("varLabel")
        self.varVertLay.addWidget(self.varLabel)
        self.line_2 = QtWidgets.QFrame(IOConfig)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.varVertLay.addWidget(self.line_2)
        self.varGridLay = QtWidgets.QGridLayout()
        self.varGridLay.setObjectName("varGridLay")
        self.addVarButton = QtWidgets.QToolButton(IOConfig)
        self.addVarButton.setObjectName("addVarButton")
        self.varGridLay.addWidget(self.addVarButton, 2, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.valeurLabel = QtWidgets.QLabel(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valeurLabel.sizePolicy().hasHeightForWidth())
        self.valeurLabel.setSizePolicy(sizePolicy)
        self.valeurLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.valeurLabel.setObjectName("valeurLabel")
        self.varGridLay.addWidget(self.valeurLabel, 0, 2, 1, 1)
        self.typeLabel = QtWidgets.QLabel(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typeLabel.sizePolicy().hasHeightForWidth())
        self.typeLabel.setSizePolicy(sizePolicy)
        self.typeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.typeLabel.setObjectName("typeLabel")
        self.varGridLay.addWidget(self.typeLabel, 0, 1, 1, 1)
        self.nomLabel = QtWidgets.QLabel(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nomLabel.sizePolicy().hasHeightForWidth())
        self.nomLabel.setSizePolicy(sizePolicy)
        self.nomLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nomLabel.setObjectName("nomLabel")
        self.varGridLay.addWidget(self.nomLabel, 0, 0, 1, 1)
        self.varVertLay.addLayout(self.varGridLay)
        self.genVertLay.addLayout(self.varVertLay)
        self.buttonHorLay = QtWidgets.QHBoxLayout()
        self.buttonHorLay.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.buttonHorLay.setObjectName("buttonHorLay")
        self.annulerButton = QtWidgets.QPushButton(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.annulerButton.sizePolicy().hasHeightForWidth())
        self.annulerButton.setSizePolicy(sizePolicy)
        self.annulerButton.setObjectName("annulerButton")
        self.buttonHorLay.addWidget(self.annulerButton)
        self.enregistrerButton = QtWidgets.QPushButton(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enregistrerButton.sizePolicy().hasHeightForWidth())
        self.enregistrerButton.setSizePolicy(sizePolicy)
        self.enregistrerButton.setObjectName("enregistrerButton")
        self.buttonHorLay.addWidget(self.enregistrerButton)
        self.validerButton = QtWidgets.QPushButton(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.validerButton.sizePolicy().hasHeightForWidth())
        self.validerButton.setSizePolicy(sizePolicy)
        self.validerButton.setObjectName("validerButton")
        self.buttonHorLay.addWidget(self.validerButton)
        self.genVertLay.addLayout(self.buttonHorLay)
        self.gridLayout.addLayout(self.genVertLay, 0, 0, 1, 1)

        self.retranslateUi(IOConfig)
        QtCore.QMetaObject.connectSlotsByName(IOConfig)

        self.annulerButton.clicked.connect(IOConfig.close)
        self.addAssiButton.clicked.connect(lambda: self.addAssiLine(IOConfig, assiLines))
        self.addVarButton.clicked.connect(lambda: self.addVarLine(IOConfig, varLines))

        self.addAssiLine(IOConfig, assiLines)
        self.addVarLine(IOConfig, varLines)

    def retranslateUi(self, IOConfig):
        _translate = QtCore.QCoreApplication.translate
        IOConfig.setWindowTitle(_translate("IOConfig", "I/O Configurator"))
        self.assiLabel.setText(_translate("IOConfig", "Assignations"))
        self.sortielabel.setText(_translate("IOConfig", "Sortie"))
        self.addAssiButton.setText(_translate("IOConfig", "+"))
        self.entreelabel.setText(_translate("IOConfig", "Entrée"))
        self.label.setText(_translate("IOConfig", "f(x)"))
        self.varLabel.setText(_translate("IOConfig", "Variables"))
        self.addVarButton.setText(_translate("IOConfig", "+"))
        self.valeurLabel.setText(_translate("IOConfig", "Valeur"))
        self.typeLabel.setText(_translate("IOConfig", "Type"))
        self.nomLabel.setText(_translate("IOConfig", "Nom"))
        self.annulerButton.setText(_translate("IOConfig", "Annuler"))
        self.enregistrerButton.setText(_translate("IOConfig", "Enregistrer"))
        self.validerButton.setText(_translate("IOConfig", "Valider"))

    def fillCombo(self, combo, list):
        for x in list: combo.addItem(x)

    def addAssiLine(self, IOConfig, lines):
        lines.append([])
        actualRow = 1+len(lines)

        self.assiGridLay.addWidget(self.addAssiButton, actualRow+1, 3, 1, 1)
        lines[-1].append(QtWidgets.QCheckBox(IOConfig))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(lines[-1][0].sizePolicy().hasHeightForWidth())
        lines[-1][0].setSizePolicy(sizePolicy)
        lines[-1][0].setLayoutDirection(QtCore.Qt.LeftToRight)
        lines[-1][0].setText("")
        lines[-1][0].setChecked(False)
        lines[-1][0].setTristate(False)
        lines[-1][0].setObjectName("checkBox_"+str(actualRow-1))
        self.assiGridLay.addWidget(lines[-1][0], actualRow, 0, 1, 1, QtCore.Qt.AlignHCenter)
        lines[-1].append(QtWidgets.QComboBox(IOConfig))
        lines[-1][1].setObjectName("inputCombo_"+str(actualRow-1))
        self.assiGridLay.addWidget(lines[-1][1], actualRow, 1, 1, 1)
        lines[-1].append(QtWidgets.QComboBox(IOConfig))
        lines[-1][2].setObjectName("outputCombo_"+str(actualRow-1))
        self.assiGridLay.addWidget(lines[-1][2], actualRow, 2, 1, 1)
        lines[-1].append(QtWidgets.QToolButton(IOConfig))
        lines[-1][3].setObjectName("delAssiButton_"+str(actualRow-1))
        self.assiGridLay.addWidget(lines[-1][3], actualRow, 3, 1, 1)

        lines[-1][3].setText("x")

        self.fillCombo(lines[-1][2], config.OUTPUTS)
        self.fillCombo(lines[-1][1], config.INPUTS)

        #lines[-1][3].clicked.connect(lambda: self.delAssiLine(IOConfig, lines, actualRow))

    def addVarLine(self, IOConfig, vars):
        vars.append([])
        actualRow = len(vars)

        self.varGridLay.addWidget(self.addVarButton, actualRow + 1, 3, 1, 1)
        vars[-1].append(QtWidgets.QLineEdit(IOConfig))
        vars[-1][0].setObjectName("nomLine_2")
        self.varGridLay.addWidget(vars[-1][0], actualRow, 0, 1, 1)
        vars[-1].append(QtWidgets.QComboBox(IOConfig))
        vars[-1][1].setObjectName("typeCombo_2")
        self.varGridLay.addWidget(vars[-1][1], actualRow, 1, 1, 1)
        vars[-1].append(QtWidgets.QLineEdit(IOConfig))
        vars[-1][2].setObjectName("valeurLine_2")
        self.varGridLay.addWidget(vars[-1][2], actualRow, 2, 1, 1)
        vars[-1].append(QtWidgets.QToolButton(IOConfig))
        vars[-1][3].setObjectName("delVarButton_2")
        self.varGridLay.addWidget(vars[-1][3], actualRow, 3, 1, 1)

        vars[-1][3].setText("x")

        self.fillCombo(vars[-1][1], config.VARTYPES)

        vars[-1][3].clicked.connect(lambda: self.delVarLine(IOConfig, vars, actualRow))

    def delVarLine(self, IOConfig, vars, n):
        for x in vars[n-1]:
            self.assiGridLay.removeWidget(x)
            x.deleteLater()
        del vars[n-1]

def openWindow():
    app = QtWidgets.QApplication(sys.argv)
    IOConfig = QtWidgets.QWidget()
    ui = Ui_IOConfig()
    ui.setupUi(IOConfig)
    IOConfig.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    openWindow()