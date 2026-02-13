import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QFile, QEvent
from ui.simcore_ui import Ui_MainWindow

class Program(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if self.isMaximized() or not self.isMaximized():
                try:
                    self.ui.rezisess(self.geometry().width(), self.geometry().height())
                except Exception as e:
                    print(f"ERROR:: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Program()
    window.show()
    app.exec()