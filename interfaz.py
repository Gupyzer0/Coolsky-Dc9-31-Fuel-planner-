# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(484, 630)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox_taxeo = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_taxeo.setMaximum(20000)
        self.spinBox_taxeo.setProperty("value", 600)
        self.spinBox_taxeo.setObjectName("spinBox_taxeo")
        self.gridLayout.addWidget(self.spinBox_taxeo, 12, 2, 1, 1)
        self.comboBox_num_app = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_num_app.setObjectName("comboBox_num_app")
        self.comboBox_num_app.addItem("")
        self.comboBox_num_app.addItem("")
        self.comboBox_num_app.addItem("")
        self.comboBox_num_app.addItem("")
        self.comboBox_num_app.addItem("")
        self.comboBox_num_app.addItem("")
        self.comboBox_num_app.addItem("")
        self.comboBox_num_app.addItem("")
        self.comboBox_num_app.addItem("")
        self.comboBox_num_app.addItem("")
        self.gridLayout.addWidget(self.comboBox_num_app, 13, 1, 1, 1)
        self.comboBox_distancia = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_distancia.setObjectName("comboBox_distancia")
        self.comboBox_distancia.addItem("")
        self.comboBox_distancia.addItem("")
        self.comboBox_distancia.addItem("")
        self.comboBox_distancia.addItem("")
        self.comboBox_distancia.addItem("")
        self.comboBox_distancia.addItem("")
        self.comboBox_distancia.addItem("")
        self.comboBox_distancia.addItem("")
        self.comboBox_distancia.addItem("")
        self.comboBox_distancia.addItem("")
        self.comboBox_distancia.addItem("")
        self.comboBox_distancia.addItem("")
        self.comboBox_distancia.addItem("")
        self.comboBox_distancia.addItem("")
        self.comboBox_distancia.addItem("")
        self.gridLayout.addWidget(self.comboBox_distancia, 0, 2, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.timeEdit_extra = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_extra.setReadOnly(True)
        self.timeEdit_extra.setObjectName("timeEdit_extra")
        self.gridLayout.addWidget(self.timeEdit_extra, 11, 3, 1, 1)
        self.comboBox_distancia_alterno = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_distancia_alterno.setObjectName("comboBox_distancia_alterno")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.comboBox_distancia_alterno.addItem("")
        self.gridLayout.addWidget(self.comboBox_distancia_alterno, 1, 2, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 15, 1, 1, 1)
        self.comboBox_viento = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_viento.setObjectName("comboBox_viento")
        self.comboBox_viento.addItem("")
        self.comboBox_viento.addItem("")
        self.comboBox_viento.addItem("")
        self.comboBox_viento.addItem("")
        self.comboBox_viento.addItem("")
        self.gridLayout.addWidget(self.comboBox_viento, 3, 2, 1, 2)
        self.lineEdit_combustible_ruta = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_combustible_ruta.setInputMask("")
        self.lineEdit_combustible_ruta.setText("")
        self.lineEdit_combustible_ruta.setReadOnly(True)
        self.lineEdit_combustible_ruta.setObjectName("lineEdit_combustible_ruta")
        self.gridLayout.addWidget(self.lineEdit_combustible_ruta, 8, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 10, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 6, 0, 1, 5)
        self.timeEdit_reserva_final = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_reserva_final.setReadOnly(True)
        self.timeEdit_reserva_final.setObjectName("timeEdit_reserva_final")
        self.gridLayout.addWidget(self.timeEdit_reserva_final, 10, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 8, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 13, 0, 1, 1)
        self.timeEdit_combustible_alterno = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_combustible_alterno.setReadOnly(True)
        self.timeEdit_combustible_alterno.setObjectName("timeEdit_combustible_alterno")
        self.gridLayout.addWidget(self.timeEdit_combustible_alterno, 9, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox_altura = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_altura.setObjectName("comboBox_altura")
        self.comboBox_altura.addItem("")
        self.comboBox_altura.addItem("")
        self.comboBox_altura.addItem("")
        self.comboBox_altura.addItem("")
        self.comboBox_altura.addItem("")
        self.comboBox_altura.addItem("")
        self.comboBox_altura.addItem("")
        self.comboBox_altura.addItem("")
        self.comboBox_altura.addItem("")
        self.comboBox_altura.addItem("")
        self.comboBox_altura.addItem("")
        self.comboBox_altura.addItem("")
        self.comboBox_altura.addItem("")
        self.gridLayout.addWidget(self.comboBox_altura, 2, 2, 1, 2)
        self.lineEdit_reserva_final = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_reserva_final.setText("")
        self.lineEdit_reserva_final.setReadOnly(True)
        self.lineEdit_reserva_final.setObjectName("lineEdit_reserva_final")
        self.gridLayout.addWidget(self.lineEdit_reserva_final, 10, 2, 1, 1)
        self.spinBox_extra = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_extra.setMaximum(20000)
        self.spinBox_extra.setObjectName("spinBox_extra")
        self.gridLayout.addWidget(self.spinBox_extra, 11, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 12, 0, 1, 1)
        self.timeEdit_combustible_ruta = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_combustible_ruta.setReadOnly(True)
        self.timeEdit_combustible_ruta.setObjectName("timeEdit_combustible_ruta")
        self.gridLayout.addWidget(self.timeEdit_combustible_ruta, 8, 3, 1, 1)
        self.lineEdit_combustible_alterno = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_combustible_alterno.setReadOnly(True)
        self.lineEdit_combustible_alterno.setObjectName("lineEdit_combustible_alterno")
        self.gridLayout.addWidget(self.lineEdit_combustible_alterno, 9, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 9, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 65))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 12, 3, 2, 1)
        self.timeEdit_tiempo_total = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_tiempo_total.setReadOnly(True)
        self.timeEdit_tiempo_total.setObjectName("timeEdit_tiempo_total")
        self.gridLayout.addWidget(self.timeEdit_tiempo_total, 15, 3, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 14, 0, 1, 4)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 7, 2, 1, 1)
        self.lineEdit_combustible_total = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_combustible_total.setReadOnly(True)
        self.lineEdit_combustible_total.setObjectName("lineEdit_combustible_total")
        self.gridLayout.addWidget(self.lineEdit_combustible_total, 15, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 7, 3, 1, 1)
        self.lineEdit_num_app = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_num_app.setReadOnly(True)
        self.lineEdit_num_app.setObjectName("lineEdit_num_app")
        self.gridLayout.addWidget(self.lineEdit_num_app, 13, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 4, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 2, 1, 1)
        self.lcdNumber_LW = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber_LW.setDigitCount(6)
        self.lcdNumber_LW.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_LW.setObjectName("lcdNumber_LW")
        self.gridLayout_2.addWidget(self.lcdNumber_LW, 4, 3, 1, 1)
        self.lcdNumber_ZFW = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber_ZFW.setDigitCount(6)
        self.lcdNumber_ZFW.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_ZFW.setObjectName("lcdNumber_ZFW")
        self.gridLayout_2.addWidget(self.lcdNumber_ZFW, 1, 3, 1, 1)
        self.lcdNumber_TOW = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber_TOW.setDigitCount(6)
        self.lcdNumber_TOW.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_TOW.setObjectName("lcdNumber_TOW")
        self.gridLayout_2.addWidget(self.lcdNumber_TOW, 2, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)
        self.spinBox_payload = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_payload.setMaximum(60000)
        self.spinBox_payload.setObjectName("spinBox_payload")
        self.gridLayout_2.addWidget(self.spinBox_payload, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 15, 0, 2, 1)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 11, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 484, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox_viento.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Coolsky DC9-31 Fuel Planner - @PW JT8D-7"))
        self.comboBox_num_app.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_num_app.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_num_app.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_num_app.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_num_app.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox_num_app.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox_num_app.setItemText(6, _translate("MainWindow", "7"))
        self.comboBox_num_app.setItemText(7, _translate("MainWindow", "8"))
        self.comboBox_num_app.setItemText(8, _translate("MainWindow", "9"))
        self.comboBox_num_app.setItemText(9, _translate("MainWindow", "10"))
        self.comboBox_distancia.setItemText(0, _translate("MainWindow", "50"))
        self.comboBox_distancia.setItemText(1, _translate("MainWindow", "100"))
        self.comboBox_distancia.setItemText(2, _translate("MainWindow", "200"))
        self.comboBox_distancia.setItemText(3, _translate("MainWindow", "300"))
        self.comboBox_distancia.setItemText(4, _translate("MainWindow", "400"))
        self.comboBox_distancia.setItemText(5, _translate("MainWindow", "500"))
        self.comboBox_distancia.setItemText(6, _translate("MainWindow", "600"))
        self.comboBox_distancia.setItemText(7, _translate("MainWindow", "700"))
        self.comboBox_distancia.setItemText(8, _translate("MainWindow", "800"))
        self.comboBox_distancia.setItemText(9, _translate("MainWindow", "900"))
        self.comboBox_distancia.setItemText(10, _translate("MainWindow", "1000"))
        self.comboBox_distancia.setItemText(11, _translate("MainWindow", "1100"))
        self.comboBox_distancia.setItemText(12, _translate("MainWindow", "1200"))
        self.comboBox_distancia.setItemText(13, _translate("MainWindow", "1300"))
        self.comboBox_distancia.setItemText(14, _translate("MainWindow", "1400"))
        self.label_4.setText(_translate("MainWindow", "Wind"))
        self.timeEdit_extra.setDisplayFormat(_translate("MainWindow", "hh:mm"))
        self.comboBox_distancia_alterno.setItemText(0, _translate("MainWindow", "20"))
        self.comboBox_distancia_alterno.setItemText(1, _translate("MainWindow", "40"))
        self.comboBox_distancia_alterno.setItemText(2, _translate("MainWindow", "60"))
        self.comboBox_distancia_alterno.setItemText(3, _translate("MainWindow", "80"))
        self.comboBox_distancia_alterno.setItemText(4, _translate("MainWindow", "100"))
        self.comboBox_distancia_alterno.setItemText(5, _translate("MainWindow", "120"))
        self.comboBox_distancia_alterno.setItemText(6, _translate("MainWindow", "140"))
        self.comboBox_distancia_alterno.setItemText(7, _translate("MainWindow", "160"))
        self.comboBox_distancia_alterno.setItemText(8, _translate("MainWindow", "180"))
        self.comboBox_distancia_alterno.setItemText(9, _translate("MainWindow", "200"))
        self.comboBox_distancia_alterno.setItemText(10, _translate("MainWindow", "220"))
        self.comboBox_distancia_alterno.setItemText(11, _translate("MainWindow", "240"))
        self.comboBox_distancia_alterno.setItemText(12, _translate("MainWindow", "260"))
        self.comboBox_distancia_alterno.setItemText(13, _translate("MainWindow", "280"))
        self.comboBox_distancia_alterno.setItemText(14, _translate("MainWindow", "300"))
        self.comboBox_distancia_alterno.setItemText(15, _translate("MainWindow", "320"))
        self.comboBox_distancia_alterno.setItemText(16, _translate("MainWindow", "340"))
        self.comboBox_distancia_alterno.setItemText(17, _translate("MainWindow", "360"))
        self.comboBox_distancia_alterno.setItemText(18, _translate("MainWindow", "380"))
        self.comboBox_distancia_alterno.setItemText(19, _translate("MainWindow", "400"))
        self.comboBox_distancia_alterno.setItemText(20, _translate("MainWindow", "420"))
        self.comboBox_distancia_alterno.setItemText(21, _translate("MainWindow", "440"))
        self.comboBox_distancia_alterno.setItemText(22, _translate("MainWindow", "460"))
        self.comboBox_distancia_alterno.setItemText(23, _translate("MainWindow", "480"))
        self.comboBox_distancia_alterno.setItemText(24, _translate("MainWindow", "500"))
        self.comboBox_distancia_alterno.setItemText(25, _translate("MainWindow", "520"))
        self.comboBox_distancia_alterno.setItemText(26, _translate("MainWindow", "540"))
        self.comboBox_distancia_alterno.setItemText(27, _translate("MainWindow", "560"))
        self.comboBox_distancia_alterno.setItemText(28, _translate("MainWindow", "580"))
        self.comboBox_distancia_alterno.setItemText(29, _translate("MainWindow", "600"))
        self.comboBox_distancia_alterno.setItemText(30, _translate("MainWindow", "620"))
        self.comboBox_distancia_alterno.setItemText(31, _translate("MainWindow", "640"))
        self.comboBox_distancia_alterno.setItemText(32, _translate("MainWindow", "660"))
        self.comboBox_distancia_alterno.setItemText(33, _translate("MainWindow", "680"))
        self.comboBox_distancia_alterno.setItemText(34, _translate("MainWindow", "700"))
        self.comboBox_distancia_alterno.setItemText(35, _translate("MainWindow", "720"))
        self.comboBox_distancia_alterno.setItemText(36, _translate("MainWindow", "740"))
        self.comboBox_distancia_alterno.setItemText(37, _translate("MainWindow", "760"))
        self.comboBox_distancia_alterno.setItemText(38, _translate("MainWindow", "780"))
        self.comboBox_distancia_alterno.setItemText(39, _translate("MainWindow", "800"))
        self.label_6.setText(_translate("MainWindow", "Total"))
        self.comboBox_viento.setItemText(0, _translate("MainWindow", "+100"))
        self.comboBox_viento.setItemText(1, _translate("MainWindow", "+50"))
        self.comboBox_viento.setItemText(2, _translate("MainWindow", "0"))
        self.comboBox_viento.setItemText(3, _translate("MainWindow", "-50"))
        self.comboBox_viento.setItemText(4, _translate("MainWindow", "-100"))
        self.lineEdit_combustible_ruta.setPlaceholderText(_translate("MainWindow", "------------------"))
        self.label_3.setText(_translate("MainWindow", "Altitude"))
        self.label_14.setText(_translate("MainWindow", "Final reserve"))
        self.timeEdit_reserva_final.setDisplayFormat(_translate("MainWindow", "hh:mm"))
        self.label.setText(_translate("MainWindow", "Distance"))
        self.label_11.setText(_translate("MainWindow", "Route fuel"))
        self.label_10.setText(_translate("MainWindow", "Instrumental Approaches"))
        self.timeEdit_combustible_alterno.setDisplayFormat(_translate("MainWindow", "hh:mm"))
        self.label_2.setText(_translate("MainWindow", "Distance to alternate"))
        self.comboBox_altura.setItemText(0, _translate("MainWindow", "7000"))
        self.comboBox_altura.setItemText(1, _translate("MainWindow", "13000"))
        self.comboBox_altura.setItemText(2, _translate("MainWindow", "15000"))
        self.comboBox_altura.setItemText(3, _translate("MainWindow", "17000"))
        self.comboBox_altura.setItemText(4, _translate("MainWindow", "19000"))
        self.comboBox_altura.setItemText(5, _translate("MainWindow", "21000"))
        self.comboBox_altura.setItemText(6, _translate("MainWindow", "23000"))
        self.comboBox_altura.setItemText(7, _translate("MainWindow", "25000"))
        self.comboBox_altura.setItemText(8, _translate("MainWindow", "27000"))
        self.comboBox_altura.setItemText(9, _translate("MainWindow", "29000"))
        self.comboBox_altura.setItemText(10, _translate("MainWindow", "31000"))
        self.comboBox_altura.setItemText(11, _translate("MainWindow", "33000"))
        self.comboBox_altura.setItemText(12, _translate("MainWindow", "35000"))
        self.lineEdit_reserva_final.setPlaceholderText(_translate("MainWindow", "4000"))
        self.label_13.setText(_translate("MainWindow", "Taxi"))
        self.timeEdit_combustible_ruta.setDisplayFormat(_translate("MainWindow", "hh:mm"))
        self.lineEdit_combustible_alterno.setPlaceholderText(_translate("MainWindow", "------------------"))
        self.label_12.setText(_translate("MainWindow", "Fuel to alterante"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.timeEdit_tiempo_total.setDisplayFormat(_translate("MainWindow", "hh:mm"))
        self.label_16.setText(_translate("MainWindow", "Fuel (Lbs)"))
        self.lineEdit_combustible_total.setPlaceholderText(_translate("MainWindow", "------------------"))
        self.label_17.setText(_translate("MainWindow", "Time"))
        self.lineEdit_num_app.setPlaceholderText(_translate("MainWindow", "------------------"))
        self.groupBox.setTitle(_translate("MainWindow", "Weigth"))
        self.label_8.setText(_translate("MainWindow", "LW:"))
        self.label_7.setText(_translate("MainWindow", "TOW:"))
        self.label_9.setText(_translate("MainWindow", "ZFW:"))
        self.label_5.setText(_translate("MainWindow", "Payload"))
        self.label_15.setText(_translate("MainWindow", "Extra (2500lbs x hour)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

