import sys

from PySide6.QtWidgets import QApplication, QWidget

from openlens.hotkey import GlobalHotkeyListener


def main() -> int:
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("OpenLens")
    window.resize(480, 320)
    window.show()

    listener = GlobalHotkeyListener(lambda: print("Capture hotkey pressed"))
    listener.start()
    app.aboutToQuit.connect(listener.stop)

    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
