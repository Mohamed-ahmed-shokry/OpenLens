import sys

from PySide6.QtWidgets import QApplication, QWidget


def main() -> int:
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("OpenLens")
    window.resize(480, 320)
    window.show()

    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
