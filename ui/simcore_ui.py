# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Simcore_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
                               QGridLayout, QHBoxLayout, QHeaderView, QLabel,
                               QLineEdit, QMainWindow, QPushButton, QSizePolicy,
                               QSpinBox, QStackedWidget, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget, QMessageBox)
from PySide6 import QtWidgets
from logic_core.historial import PilaHistorial
from qrc import assets_qrc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.main = MainWindow
        self.history = None
        MainWindow.resize(1080, 633)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1080, 0))
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.principal = QFrame(self.centralwidget)
        self.principal.setObjectName(u"principal")
        self.principal.setStyleSheet(u"\n"
                                     "background-color: rgb(18, 19, 22);")
        self.principal.setFrameShape(QFrame.Shape.StyledPanel)
        self.principal.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_3 = QFrame(self.principal)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(1, 1, 1078, 30))
        self.frame_3.setMinimumSize(QSize(0, 30))
        self.frame_3.setMaximumSize(QSize(16777215, 30))
        self.frame_3.setStyleSheet(u"background-color: rgb(32, 35, 40);")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.frame = QFrame(self.principal)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(1, 31, 1080, 600))
        self.frame.setMinimumSize(QSize(1080, 600))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(60, 0))
        self.frame_2.setMaximumSize(QSize(60, 16777215))
        self.frame_2.setStyleSheet(u"background-color: rgb(54, 57, 67);\n"
                                   "background-color: rgb(24, 26, 30);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(60, 0))
        self.label_2.setMaximumSize(QSize(60, 60))

        self.verticalLayout_2.addWidget(self.label_2)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_2.addWidget(self.frame_7)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(60, 60))
        self.pushButton.setMaximumSize(QSize(60, 60))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
                                      "background: none;\n"
                                      "border: 0px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed{\n"
                                      "	background-color: rgb(122, 125, 135);\n"
                                      "}")
        icon = QIcon()
        icon.addFile(u":/programa/add2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(60, 60))
        self.pushButton_2.setMaximumSize(QSize(60, 60))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
                                        "background: none;\n"
                                        "border: 0px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "	background-color: rgb(122, 125, 135);\n"
                                        "}")
        icon1 = QIcon()
        icon1.addFile(u":/programa/history2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(100)
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_2.addWidget(self.frame_8)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(60, 60))
        self.pushButton_3.setMaximumSize(QSize(60, 60))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
                                        "background: none;\n"
                                        "border: 0px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "	background-color: rgb(122, 125, 135);\n"
                                        "}")
        icon2 = QIcon()
        icon2.addFile(u":/programa/play2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.horizontalLayout.addWidget(self.frame_2)

        self.central = QStackedWidget(self.frame)
        self.central.setObjectName(u"central")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(100)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.central.sizePolicy().hasHeightForWidth())
        self.central.setSizePolicy(sizePolicy2)
        self.central.setStyleSheet(u"background-color: rgb(24, 26, 30);\n"
                                   "background-color: rgb(18, 19, 22);")
        self.sin = QWidget()
        self.sin.setObjectName(u"sin")
        self.gridLayout = QGridLayout(self.sin)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(35, 35, 35, 35)
        self.frame_sindatos = QFrame(self.sin)
        self.frame_sindatos.setObjectName(u"frame_sindatos")
        self.frame_sindatos.setStyleSheet(u"background:none;\n"
                                          "background-image: url(:/programa/background_biohazard.png);\n"
                                          "background-repeat: no-repeat;\n"
                                          "background-position: center;\n"
                                          "border: 1px solid rgba(208, 212, 228, 80);\n"
                                          "border-radius: 18px;\n"
                                          "")
        self.frame_sindatos.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_sindatos.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_sindatos)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.frame_sindatos)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background: none;\n"
                                 "color: rgb(18, 19, 22);\n"
                                 "color: rgb(208, 212, 228);\n"
                                 "border: 0px;")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.frame_sindatos, 0, 0, 1, 1)

        self.central.addWidget(self.sin)
        self.con = QWidget()
        self.con.setObjectName(u"con")
        self.gridLayout_7 = QGridLayout(self.con)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(35, 35, 35, 35)
        self.frame_condatos = QFrame(self.con)
        self.frame_condatos.setObjectName(u"frame_condatos")
        self.frame_condatos.setStyleSheet(u"background:none;\n"
                                          "border: 1px solid rgba(208, 212, 228, 80);\n"
                                          "border-radius: 18px;\n"
                                          "")
        self.frame_condatos.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_condatos.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_condatos)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableWidget = QTableWidget(self.frame_condatos)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableWidget.rowCount() < 5):
            self.tableWidget.setRowCount(5)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMaximumSize(QSize(500, 220))
        self.tableWidget.setSizeIncrement(QSize(400, 0))
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
                                       "	\n"
                                       "	background-color: rgb(41, 45, 52);\n"
                                       "	border-radius: 16px;\n"
                                       "	color: rgb(79, 159, 188);\n"
                                       "}\n"
                                       "\n"
                                       "QTableWidgetItem {\n"
                                       "	background-color: rgb(39, 42, 49);\n"
                                       "}\n"
                                       "\n"
                                       "QHeaderView {\n"
                                       "	background-color: rgb(159, 214, 225);\n"
                                       "}\n"
                                       "\n"
                                       "QHeaderView::section {\n"
                                       "	background-color: rgb(39, 42, 49);\n"
                                       "	color: rgb(255, 255, 255);\n"
                                       "    padding: 5px;\n"
                                       "	border: 0px solid rgb(247, 250, 250, 70);\n"
                                       "	font: 75 11pt \"Arial\";\n"
                                       "}\n"
                                       "\n"
                                       "QHeaderView::section:hover {\n"
                                       "	color: rgb(255, 255, 255);\n"
                                       "	background-color: rgb(89, 179, 212);\n"
                                       "}\n"
                                       "\n"
                                       "QTableWidget::item:selected {\n"
                                       "	background-color: rgb(89, 179, 212);\n"
                                       "}")
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(390)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget.verticalHeader().setDefaultSectionSize(35)

        self.horizontalLayout_3.addWidget(self.tableWidget)

        self.gridLayout_7.addWidget(self.frame_condatos, 0, 0, 1, 1)

        self.central.addWidget(self.con)

        self.horizontalLayout.addWidget(self.central)

        self.derecho = QStackedWidget(self.frame)
        self.derecho.setObjectName(u"derecho")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(30)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.derecho.sizePolicy().hasHeightForWidth())
        self.derecho.setSizePolicy(sizePolicy3)
        self.derecho.setStyleSheet(u"background-color: rgb(24, 26, 30);")
        self.derecho.setFrameShape(QFrame.Shape.StyledPanel)
        self.derecho.setFrameShadow(QFrame.Shadow.Raised)
        self.sin_activos = QWidget()
        self.sin_activos.setObjectName(u"sin_activos")
        self.gridLayout_4 = QGridLayout(self.sin_activos)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_6 = QFrame(self.sin_activos)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background:none;\n"
                                   "border: 1px solid rgba(208, 212, 228, 80);\n"
                                   "border-radius: 18px;\n"
                                   "")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(12)
        self.label_3.setFont(font1)
        self.label_3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u"background: none;\n"
                                   "color: rgb(18, 19, 22);\n"
                                   "color: rgb(208, 212, 228);\n"
                                   "border: 0px;")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.gridLayout_4.addWidget(self.frame_6, 0, 0, 1, 1)

        self.derecho.addWidget(self.sin_activos)
        self.con_activos = QWidget()
        self.con_activos.setObjectName(u"con_activos")
        self.gridLayout_9 = QGridLayout(self.con_activos)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frame_9 = QFrame(self.con_activos)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background:none;\n"
                                   "border: 1px solid rgba(208, 212, 228, 80);\n"
                                   "border-radius: 18px;\n"
                                   "")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_9)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_9)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 241, 31))
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.label_4.setFont(font2)
        self.label_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"background: none;\n"
                                   "color: rgb(18, 19, 22);\n"
                                   "color: rgb(208, 212, 228);\n"
                                   "border: 0px;")
        self.tasa_v = QLabel(self.frame_5)
        self.tasa_v.setObjectName(u"tasa_v")
        self.tasa_v.setGeometry(QRect(10, 270, 241, 31))
        font3 = QFont()
        font3.setFamilies([u"Consolas"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.tasa_v.setFont(font3)
        self.tasa_v.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.tasa_v.setAutoFillBackground(False)
        self.tasa_v.setStyleSheet(u"background: none;\n"
                                  "color: rgba(208, 212, 228,180);\n"
                                  "border: 0px;")
        self.nombre_v = QLabel(self.frame_5)
        self.nombre_v.setObjectName(u"nombre_v")
        self.nombre_v.setGeometry(QRect(10, 80, 241, 31))
        self.nombre_v.setFont(font3)
        self.nombre_v.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.nombre_v.setAutoFillBackground(False)
        self.nombre_v.setStyleSheet(u"background: none;\n"
                                    "color: rgba(208, 212, 228,180);\n"
                                    "border: 0px;")
        self.probabilidad_v = QLabel(self.frame_5)
        self.probabilidad_v.setObjectName(u"probabilidad_v")
        self.probabilidad_v.setGeometry(QRect(10, 210, 241, 31))
        self.probabilidad_v.setFont(font3)
        self.probabilidad_v.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.probabilidad_v.setAutoFillBackground(False)
        self.probabilidad_v.setStyleSheet(u"background: none;\n"
                                          "color: rgba(208, 212, 228,180);\n"
                                          "border: 0px;")
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 110, 241, 31))
        self.label_6.setFont(font2)
        self.label_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet(u"background: none;\n"
                                   "color: rgb(18, 19, 22);\n"
                                   "color: rgb(208, 212, 228);\n"
                                   "border: 0px;")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 50, 241, 31))
        self.label_5.setFont(font2)
        self.label_5.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet(u"background: none;\n"
                                   "color: rgb(18, 19, 22);\n"
                                   "color: rgb(208, 212, 228);\n"
                                   "border: 0px;")
        self.tipo_v = QLabel(self.frame_5)
        self.tipo_v.setObjectName(u"tipo_v")
        self.tipo_v.setGeometry(QRect(10, 140, 241, 31))
        self.tipo_v.setFont(font3)
        self.tipo_v.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.tipo_v.setAutoFillBackground(False)
        self.tipo_v.setStyleSheet(u"background: none;\n"
                                  "color: rgba(208, 212, 228,180);\n"
                                  "border: 0px;")
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 180, 241, 31))
        self.label_7.setFont(font2)
        self.label_7.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet(u"background: none;\n"
                                   "color: rgb(18, 19, 22);\n"
                                   "color: rgb(208, 212, 228);\n"
                                   "border: 0px;")
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 300, 241, 31))
        self.label_9.setFont(font2)
        self.label_9.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setStyleSheet(u"background: none;\n"
                                   "color: rgb(18, 19, 22);\n"
                                   "color: rgb(208, 212, 228);\n"
                                   "border: 0px;")
        self.area_v = QLabel(self.frame_5)
        self.area_v.setObjectName(u"area_v")
        self.area_v.setGeometry(QRect(10, 330, 241, 31))
        self.area_v.setFont(font3)
        self.area_v.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.area_v.setAutoFillBackground(False)
        self.area_v.setStyleSheet(u"background: none;\n"
                                  "color: rgba(208, 212, 228,180);\n"
                                  "border: 0px;")
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 240, 241, 31))
        self.label_8.setFont(font2)
        self.label_8.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet(u"background: none;\n"
                                   "color: rgb(18, 19, 22);\n"
                                   "color: rgb(208, 212, 228);\n"
                                   "border: 0px;")

        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setMinimumSize(QSize(0, 170))
        self.frame_10.setMaximumSize(QSize(16777215, 190))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_10)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_4 = QFrame(self.frame_10)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(43, 47, 54);\n"
                                   "border: 0px;")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_24 = QFrame(self.frame_4)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(50)
        sizePolicy4.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy4)
        self.frame_24.setStyleSheet(u"")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_24)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.tasa_v_3 = QLabel(self.frame_24)
        self.tasa_v_3.setObjectName(u"tasa_v_3")
        self.tasa_v_3.setMaximumSize(QSize(16777215, 20))
        self.tasa_v_3.setFont(font3)
        self.tasa_v_3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.tasa_v_3.setAutoFillBackground(False)
        self.tasa_v_3.setStyleSheet(u"background: none;\n"
                                    "color: rgba(208, 212, 228,180);\n"
                                    "border: 0px;")

        self.gridLayout_18.addWidget(self.tasa_v_3, 0, 0, 1, 1)

        self.verticalLayout.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.frame_4)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(100)
        sizePolicy5.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy5)
        self.frame_25.setStyleSheet(u"background-color: rgb(99, 255, 211);\n"
                                    "background-color: rgba(29, 32, 38,80);")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_25)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.dias = QLabel(self.frame_25)
        self.dias.setObjectName(u"dias")
        font4 = QFont()
        font4.setFamilies([u"Unispace"])
        font4.setPointSize(36)
        font4.setBold(True)
        self.dias.setFont(font4)

        self.gridLayout_19.addWidget(self.dias, 0, 0, 1, 1)

        self.verticalLayout.addWidget(self.frame_25)

        self.gridLayout_8.addWidget(self.frame_4, 0, 0, 1, 1)

        self.verticalLayout_3.addWidget(self.frame_10)

        self.gridLayout_9.addWidget(self.frame_9, 0, 0, 1, 1)

        self.derecho.addWidget(self.con_activos)

        self.horizontalLayout.addWidget(self.derecho)

        self.tarjeta = QStackedWidget(self.principal)
        self.tarjeta.setObjectName(u"tarjeta")
        self.tarjeta.setGeometry(QRect(70, 0, 800, 600))
        self.tarjeta.setStyleSheet(u"background: none;")
        self.panel = QWidget()
        self.panel.setObjectName(u"panel")
        self.panel.setStyleSheet(u"background:transparent;")
        self.frame_21 = QFrame(self.panel)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(0, 170, 601, 401))
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(10, 20, 251, 371))
        self.frame_22.setStyleSheet(u"background-color: rgb(24, 26, 30);\n"
                                    "border: 0px;\n"
                                    "border-radius: 18px;\n"
                                    "")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.info_8 = QLabel(self.frame_22)
        self.info_8.setObjectName(u"info_8")
        self.info_8.setGeometry(QRect(10, 20, 165, 21))
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.info_8.sizePolicy().hasHeightForWidth())
        self.info_8.setSizePolicy(sizePolicy6)
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(14)
        self.info_8.setFont(font5)
        self.info_8.setStyleSheet(u"background: none;\n"
                                  "border: 0px;\n"
                                  "color: rgb(98, 126, 152);")
        self.cb_tipo_v = QComboBox(self.frame_22)
        self.cb_tipo_v.addItem("")
        self.cb_tipo_v.addItem("")
        self.cb_tipo_v.addItem("")
        self.cb_tipo_v.addItem("")
        self.cb_tipo_v.setObjectName(u"cb_tipo_v")
        self.cb_tipo_v.setGeometry(QRect(10, 115, 231, 45))
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(100)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.cb_tipo_v.sizePolicy().hasHeightForWidth())
        self.cb_tipo_v.setSizePolicy(sizePolicy7)
        self.cb_tipo_v.setMaximumSize(QSize(354, 45))
        self.cb_tipo_v.setFont(font1)
        self.cb_tipo_v.setStyleSheet(u"border-radius: 10px;\n"
                                     "	background-color: rgba(43, 47, 54, 80);\n"
                                     "	color: rgba(208, 212, 228,160);;\n"
                                     "	padding: 1px;\n"
                                     "	padding-left: 15px;\n"
                                     "	padding-right: 5px;")
        self.le_nombre_virus = QLineEdit(self.frame_22)
        self.le_nombre_virus.setObjectName(u"le_nombre_virus")
        self.le_nombre_virus.setGeometry(QRect(10, 46, 231, 38))
        sizePolicy7.setHeightForWidth(self.le_nombre_virus.sizePolicy().hasHeightForWidth())
        self.le_nombre_virus.setSizePolicy(sizePolicy7)
        self.le_nombre_virus.setMaximumSize(QSize(354, 45))
        self.le_nombre_virus.setFont(font1)
        self.le_nombre_virus.setAutoFillBackground(False)
        self.le_nombre_virus.setStyleSheet(u"QLineEdit{\n"
                                           "	border-radius: 10px;\n"
                                           "	background-color: rgba(43, 47, 54, 80);\n"
                                           "	color: rgba(208, 212, 228,160);;\n"
                                           "	padding: 1px;\n"
                                           "	padding-left: 15px;\n"
                                           "	padding-right: 5px;\n"
                                           "}")
        self.le_nombre_virus.setClearButtonEnabled(False)
        self.info_10 = QLabel(self.frame_22)
        self.info_10.setObjectName(u"info_10")
        self.info_10.setGeometry(QRect(10, 89, 191, 21))
        sizePolicy6.setHeightForWidth(self.info_10.sizePolicy().hasHeightForWidth())
        self.info_10.setSizePolicy(sizePolicy6)
        self.info_10.setFont(font5)
        self.info_10.setStyleSheet(u"background: none;\n"
                                   "border: 0px;\n"
                                   "color: rgb(98, 126, 152);")
        self.info_9 = QLabel(self.frame_22)
        self.info_9.setObjectName(u"info_9")
        self.info_9.setGeometry(QRect(10, 170, 165, 21))
        sizePolicy6.setHeightForWidth(self.info_9.sizePolicy().hasHeightForWidth())
        self.info_9.setSizePolicy(sizePolicy6)
        self.info_9.setFont(font5)
        self.info_9.setStyleSheet(u"background: none;\n"
                                  "border: 0px;\n"
                                  "color: rgb(98, 126, 152);")
        self.dsb_letalidad = QDoubleSpinBox(self.frame_22)
        self.dsb_letalidad.setObjectName(u"dsb_letalidad")
        self.dsb_letalidad.setGeometry(QRect(10, 200, 231, 45))
        self.dsb_letalidad.setFont(font1)
        self.dsb_letalidad.setStyleSheet(u"border-radius: 10px;\n"
                                         "	background-color: rgba(43, 47, 54, 80);\n"
                                         "	color: rgba(208, 212, 228,160);;\n"
                                         "	padding: 1px;\n"
                                         "	padding-left: 15px;\n"
                                         "	padding-right: 5px;")
        self.sb_recuperacion = QSpinBox(self.frame_22)
        self.sb_recuperacion.setObjectName(u"sb_recuperacion")
        self.sb_recuperacion.setGeometry(QRect(10, 290, 231, 45))
        self.sb_recuperacion.setFont(font1)
        self.sb_recuperacion.setStyleSheet(u"border-radius: 10px;\n"
                                           "	background-color: rgba(43, 47, 54, 80);\n"
                                           "	color: rgba(208, 212, 228,160);;\n"
                                           "	padding: 1px;\n"
                                           "	padding-left: 15px;\n"
                                           "	padding-right: 5px;")
        self.sb_recuperacion.setMaximum(365)
        self.info_11 = QLabel(self.frame_22)
        self.info_11.setObjectName(u"info_11")
        self.info_11.setGeometry(QRect(10, 260, 221, 21))
        sizePolicy6.setHeightForWidth(self.info_11.sizePolicy().hasHeightForWidth())
        self.info_11.setSizePolicy(sizePolicy6)
        self.info_11.setFont(font5)
        self.info_11.setStyleSheet(u"background: none;\n"
                                   "color: rgb(208, 212, 228);\n"
                                   "border: 0px;")
        self.frame_23 = QFrame(self.frame_21)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(270, 40, 221, 351))
        self.frame_23.setStyleSheet(u"background-color: rgb(24, 26, 30);\n"
                                    "border: 0px;\n"
                                    "border-radius: 18px;\n"
                                    "")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.info_12 = QLabel(self.frame_23)
        self.info_12.setObjectName(u"info_12")
        self.info_12.setGeometry(QRect(10, 20, 91, 21))
        sizePolicy6.setHeightForWidth(self.info_12.sizePolicy().hasHeightForWidth())
        self.info_12.setSizePolicy(sizePolicy6)
        self.info_12.setFont(font5)
        self.info_12.setStyleSheet(u"background: none;\n"
                                   "border: 0px;\n"
                                   "color: rgb(98, 126, 152);")
        self.sb_poblacion = QSpinBox(self.frame_23)
        self.sb_poblacion.setObjectName(u"sb_poblacion")
        self.sb_poblacion.setGeometry(QRect(10, 45, 201, 45))
        self.sb_poblacion.setFont(font1)
        self.sb_poblacion.setStyleSheet(u"border-radius: 10px;\n"
                                        "	background-color: rgba(43, 47, 54, 80);\n"
                                        "	color: rgba(208, 212, 228,160);;\n"
                                        "	padding: 1px;\n"
                                        "	padding-left: 15px;\n"
                                        "	padding-right: 5px;")
        self.sb_poblacion.setMaximum(7000000)
        self.info_13 = QLabel(self.frame_23)
        self.info_13.setObjectName(u"info_13")
        self.info_13.setGeometry(QRect(10, 95, 221, 21))
        sizePolicy6.setHeightForWidth(self.info_13.sizePolicy().hasHeightForWidth())
        self.info_13.setSizePolicy(sizePolicy6)
        self.info_13.setFont(font5)
        self.info_13.setStyleSheet(u"background: none;\n"
                                   "color: rgb(208, 212, 228);\n"
                                   "border: 0px;")
        self.sb_infectados = QSpinBox(self.frame_23)
        self.sb_infectados.setObjectName(u"sb_infectados")
        self.sb_infectados.setGeometry(QRect(10, 120, 201, 45))
        self.sb_infectados.setFont(font1)
        self.sb_infectados.setStyleSheet(u"border-radius: 10px;\n"
                                         "	background-color: rgba(43, 47, 54, 80);\n"
                                         "	color: rgba(208, 212, 228,160);;\n"
                                         "	padding: 1px;\n"
                                         "	padding-left: 15px;\n"
                                         "	padding-right: 5px;")
        self.sb_infectados.setMaximum(10)
        self.info_14 = QLabel(self.frame_23)
        self.info_14.setObjectName(u"info_14")
        self.info_14.setGeometry(QRect(10, 175, 221, 21))
        sizePolicy6.setHeightForWidth(self.info_14.sizePolicy().hasHeightForWidth())
        self.info_14.setSizePolicy(sizePolicy6)
        self.info_14.setFont(font5)
        self.info_14.setStyleSheet(u"background: none;\n"
                                   "border: 0px;\n"
                                   "color: rgb(208, 212, 228);")
        self.info_15 = QLabel(self.frame_23)
        self.info_15.setObjectName(u"info_15")
        self.info_15.setGeometry(QRect(10, 255, 221, 21))
        sizePolicy6.setHeightForWidth(self.info_15.sizePolicy().hasHeightForWidth())
        self.info_15.setSizePolicy(sizePolicy6)
        self.info_15.setFont(font5)
        self.info_15.setStyleSheet(u"background: none;\n"
                                   "border: 0px;\n"
                                   "color: rgb(208, 212, 228);\n"
                                   "")
        self.sb_capacidadH = QSpinBox(self.frame_23)
        self.sb_capacidadH.setObjectName(u"sb_capacidadH")
        self.sb_capacidadH.setGeometry(QRect(10, 280, 201, 45))
        self.sb_capacidadH.setFont(font1)
        self.sb_capacidadH.setStyleSheet(u"border-radius: 10px;\n"
                                         "	background-color: rgba(43, 47, 54, 80);\n"
                                         "	color: rgba(208, 212, 228,160);;\n"
                                         "	padding: 1px;\n"
                                         "	padding-left: 15px;\n"
                                         "	padding-right: 5px;")
        self.sb_capacidadH.setMaximum(1000)
        self.dsb_area = QDoubleSpinBox(self.frame_23)
        self.dsb_area.setObjectName(u"dsb_area")
        self.dsb_area.setGeometry(QRect(10, 200, 201, 45))
        self.dsb_area.setFont(font1)
        self.dsb_area.setStyleSheet(u"border-radius: 10px;\n"
                                    "	background-color: rgba(43, 47, 54, 80);\n"
                                    "	color: rgba(208, 212, 228,160);;\n"
                                    "	padding: 1px;\n"
                                    "	padding-left: 15px;\n"
                                    "	padding-right: 5px;")
        self.dsb_area.setMaximum(100000000.989999994635582)
        self.tarjeta.addWidget(self.panel)
        self.tarjeta.raise_()
        self.frame_3.raise_()
        self.frame.raise_()

        self.gridLayout_5.addWidget(self.principal, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.central.setCurrentIndex(0)
        self.derecho.setCurrentIndex(0)
        self.label_7.setText("Tasa de Mortalidad")

        QMetaObject.connectSlotsByName(MainWindow)
        self.bindig_buttom()
        self.hide_tarjeta()
        self.show_or_hide = None
        QMetaObject.connectSlotsByName(MainWindow)
        self.simhis = None
        # setupUi

    def bindig_buttom(self):
        self.pushButton.clicked.connect(lambda: self.mostrar_panel())
        self.pushButton_3.clicked.connect(lambda: self.playSim())
        self.pushButton_2.clicked.connect(lambda: self.accion_historial())
        

    def rezisess(self, w, h):
        self.frame.setGeometry(0, 0, w, h)

    def hide_tarjeta(self):
        self.tarjeta.hide()

    def mostrar_panel(self):
        print(self.simhis)
        if self.show_or_hide is None or not (self.show_or_hide):
            self.history = PilaHistorial()
            self.history.apilar_estado(self.simhis)
            self.tarjeta.show()
            self.tarjeta.raise_()
            self.show_or_hide = True
        else:
            self.tarjeta.hide()
            self.show_or_hide = False

    def playSim(self):
        from data_base import DataBase
        from models_clases.virus import Virus
        from models_clases.simulacion import Simulacion
        from logic_core.motorSimulacion import MotorSimulacion

        try:
            if not (len(self.le_nombre_virus.text().strip())):
                QMessageBox.information(self.main, "Simulacion", "NOMBRE VACIO")
            elif int(self.sb_poblacion.value()) <= 0:
                QtWidgets.QMessageBox.information(self.main, "Simulacion", "INFECTADOS INICIALES BAJA")
            elif int(self.sb_infectados.value()) <= 0:
                QtWidgets.QMessageBox.information(self.main, "Simulacion", "NUMERO DE INFECTADOS INICIALES NULO")
            elif int(self.sb_recuperacion.value()) <= 0:
                QtWidgets.QMessageBox.information(self.main, "Simulacion", "TIEMPO DE RECUPERACION NULO")
            elif float(self.dsb_area.value()) <= 0.00:
                QtWidgets.QMessageBox.information(self.main, "Simulacion", "AREA NO VALIDA")
            else:
                datos = [self.le_nombre_virus.text(), self.cb_tipo_v.currentText(), self.dsb_letalidad.value(),
                         self.sb_recuperacion.value(), self.sb_poblacion.value(), self.sb_infectados.value(),
                         self.dsb_area.value(), self.sb_capacidadH.value()]

                virus = Virus(datos[0], datos[1], datos[2], datos[3])
                simCore = Simulacion(datos[4], datos[5], datos[6], datos[7])
                engine = MotorSimulacion(DataBase(), virus, simCore)
                resultados = engine.ejecutar_simulacion()
                self.central.setCurrentIndex(1)
                self.derecho.setCurrentIndex(1)

                self.show_or_hide = True
                self.mostrar_panel()
                self.definir_informacion_derecha(datos[0], str(datos[1]), str(datos[2] * 10) + " %",
                                                 str(resultados[5] * 10) + " %",
                                                 str(datos[3]) + " Km2", str(resultados[6]))
                self.definir_tabla(resultados)
                self.simhis = [datos, resultados]

        except Exception as e:
            print(e)

    def definir_informacion_derecha(self, _nombre, _tipo, _probabilidad, _contagio, _area, _dia):
        self.nombre_v.setText(_nombre)
        self.tipo_v.setText(_tipo)
        self.probabilidad_v.setText(_probabilidad)
        self.tasa_v.setText(_contagio)
        self.area_v.setText(_area)
        self.dias.setText(_dia)

    def definir_tabla(self, datos):
        cell1 = QTableWidgetItem(str(datos[0]))
        cell2 = QTableWidgetItem(str(datos[1]))
        cell3 = QTableWidgetItem(str(datos[2]))
        cell4 = QTableWidgetItem(str(datos[3]))
        cell5 = QTableWidgetItem(str(datos[4]))

        indices = 0
        cell_list = [cell1, cell2, cell3, cell4, cell5]
        for cell in cell_list:
            cell.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(indices, 0, cell)
            indices += 1
            
    def accion_historial(self):
        if self.history is None:
            QMessageBox.information(self.main, "", "NO HAY DATOS EN EL HISTORIAl")
            return False
        else:
            datos = self.history.deshacer_y_mostrar()
            print(datos[0])
            self.definir_informacion_derecha(str(datos[0][0]), str(datos[0][1]), str(datos[0][2]), str(datos[0][3]), str(datos[0][4]), str(datos[0][5]))
            self.definir_tabla(datos[1])
            return True
        
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p><img src=\":/programa/background_biohazard_logo.png\"/></p></body></html>",
                                                        None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#d0d4e4;\">Esperando datos epidemiol\u00f3gicos</span></p></body></html>",
                                                      None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Resultados", None));
        ___qtablewidgetitem1 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Sanos", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Infectados", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Recuperados", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Fallecidos", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"En Espera", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p align=\"center\">Sin datos activos</p></body></html>",
                                                        None))
        self.label_4.setText(
            QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Datos de la Simulacion</p></body></html>",
                                       None))
        self.tasa_v.setText(
            QCoreApplication.translate("MainWindow", u"<html><head/><body><p>label</p><p><br/></p></body></html>",
                                       None))
        self.nombre_v.setText(
            QCoreApplication.translate("MainWindow", u"<html><head/><body><p>label</p><p><br/></p></body></html>",
                                       None))
        self.probabilidad_v.setText(
            QCoreApplication.translate("MainWindow", u"<html><head/><body><p>label</p><p><br/></p></body></html>",
                                       None))
        self.label_6.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p>Tipo de Transmisi\u00f3n</p></body></html>",
                                                        None))
        self.label_5.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p>Nombre del Virus</p><p><br/></p></body></html>",
                                                        None))
        self.tipo_v.setText(
            QCoreApplication.translate("MainWindow", u"<html><head/><body><p>label</p><p><br/></p></body></html>",
                                       None))
        self.label_7.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p>Probabilidad de Contagio</p><p><br/></p></body></html>",
                                                        None))
        self.label_9.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p>\u00c1rea de la simulaci\u00f3n</p></body></html>",
                                                        None))
        self.area_v.setText(
            QCoreApplication.translate("MainWindow", u"<html><head/><body><p>label</p><p><br/></p></body></html>",
                                       None))
        self.label_8.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p>Tasa de Contagio</p><p><br/></p></body></html>",
                                                        None))
        self.tasa_v_3.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Dias Transcurridos</span></p><p align=\"center\"><span style=\" font-size:11pt;\"><br/></span></p></body></html>",
                                                         None))
        self.dias.setText(QCoreApplication.translate("MainWindow",
                                                     u"<html><head/><body><p align=\"center\"><span style=\" color:#d0d4e4;\">365</span></p></body></html>",
                                                     None))
        self.info_8.setText(QCoreApplication.translate("MainWindow",
                                                       u"<html><head/><body><p><span style=\" color:#d0d4e4;\">Virus</span></p></body></html>",
                                                       None))
        self.cb_tipo_v.setItemText(0, QCoreApplication.translate("MainWindow", u"A\u00e9reo", None))
        self.cb_tipo_v.setItemText(1, QCoreApplication.translate("MainWindow", u"Respiratorio", None))
        self.cb_tipo_v.setItemText(2, QCoreApplication.translate("MainWindow", u"Contacto Directo", None))
        self.cb_tipo_v.setItemText(3, QCoreApplication.translate("MainWindow", u"F\u00f3mites", None))

        self.le_nombre_virus.setInputMask("")
        self.le_nombre_virus.setText("")
        self.le_nombre_virus.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre del Virus", None))
        self.info_10.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p><span style=\" color:#d0d4e4;\">Tipo de Transmision</span></p></body></html>",
                                                        None))
        self.info_9.setText(QCoreApplication.translate("MainWindow",
                                                       u"<html><head/><body><p><span style=\" color:#d0d4e4;\">Tasa de Letalidad</span></p></body></html>",
                                                       None))
        self.info_11.setText(QCoreApplication.translate("MainWindow", u"Tiempo de recuperacion", None))
        self.info_12.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p><span style=\" color:#d0d4e4;\">Poblaci\u00f3n</span></p></body></html>",
                                                        None))
        self.info_13.setText(QCoreApplication.translate("MainWindow", u"Infectados al Inicio", None))
        self.info_14.setText(QCoreApplication.translate("MainWindow", u"\u00c1rea de la Simulaci\u00f3n", None))
        self.info_15.setText(QCoreApplication.translate("MainWindow", u"Capacidad Hospitalaria", None))
    # retranslateUi
