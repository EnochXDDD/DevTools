import sys
import logging
from importlib.machinery import SourceFileLoader
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
LOG = logging.getLogger(__name__)
Brain = SourceFileLoader("Brain", "../Brain.py").load_module()


class TimeEstimateTest:

    def test_QtGUI(self):
        @Brain.TimeEstimate(without_any_args=True)
        def on_OK_clicked():
            with Brain.TimeEstimate(block_name="print OK"):
                print("btn_OK is clicked")

        app = QApplication(sys.argv)
        window = QMainWindow()
        window.setFixedSize(640, 480)

        with Brain.TimeEstimate(block_name="add button"):
            widget = QWidget(parent=window)
            layout = QVBoxLayout()
            btn_OK = QPushButton("OK", parent=widget)
            btn_OK.clicked.connect(on_OK_clicked)
            layout.addWidget(btn_OK)
            widget.setLayout(layout)

        window.setCentralWidget(widget)
        window.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    # logging.basicConfig(level=logging.INFO)
    bt = TimeEstimateTest()
    bt.test_QtGUI()
