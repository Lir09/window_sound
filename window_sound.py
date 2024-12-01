import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLabel, QSlider, QWidget, QListWidget,
    QHBoxLayout, QPushButton, QTabWidget
)
from PySide6.QtCore import Qt
from pycaw.pycaw import AudioUtilities
from comtypes import CLSCTX_ALL


class VolumeController:
    def __init__(self):
        self.devices = AudioUtilities.GetAllSessions()

    def get_applications(self):
        return [session.Process.name() for session in self.devices if session.Process]

    def set_volume(self, app_name, volume_level):
        for session in self.devices:
            if session.Process and session.Process.name() == app_name:
                volume = session.SimpleAudioVolume
                volume.SetMasterVolume(volume_level / 100, None)
                break

    def mute_volume(self, app_name):
        for session in self.devices:
            if session.Process and session.Process.name() == app_name:
                volume = session.SimpleAudioVolume
                volume.SetMute(1, None)
                break


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application Volume Controller")
        self.setGeometry(100, 100, 500, 400)

        self.controller = VolumeController()
        self.app_list = self.controller.get_applications()

        self.init_ui()

    def init_ui(self):
        tab_widget = QTabWidget()
        main_tab = QWidget()
        about_tab = QWidget()

        # Main Tab Layout
        main_layout = QVBoxLayout()

        # Application List
        self.list_widget = QListWidget()
        self.list_widget.addItems(self.app_list)
        self.list_widget.currentItemChanged.connect(self.update_slider)
        main_layout.addWidget(QLabel("Select Application:"))
        main_layout.addWidget(self.list_widget)

        # Volume Control Layout
        volume_layout = QVBoxLayout()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.valueChanged.connect(self.adjust_volume)

        self.volume_label = QLabel("Volume: 50%")
        self.volume_label.setAlignment(Qt.AlignCenter)

        self.mute_button = QPushButton("Mute")
        self.mute_button.clicked.connect(self.mute_current_app)

        volume_layout.addWidget(QLabel("Adjust Volume:"))
        volume_layout.addWidget(self.slider)
        volume_layout.addWidget(self.volume_label)
        volume_layout.addWidget(self.mute_button)

        main_layout.addLayout(volume_layout)
        main_tab.setLayout(main_layout)

        # About Tab Layout
        about_layout = QVBoxLayout()
        about_layout.addWidget(QLabel("Application Volume Controller v1.0"))
        about_layout.addWidget(QLabel("Developed with PySide6 and Pycaw"))
        about_tab.setLayout(about_layout)

        # Add Tabs
        tab_widget.addTab(main_tab, "Control Volume")
        tab_widget.addTab(about_tab, "About")

        self.setCentralWidget(tab_widget)

    def update_slider(self):
        self.slider.setValue(50)  # Reset slider to 50%

    def adjust_volume(self, value):
        current_app = self.list_widget.currentItem()
        if current_app:
            self.controller.set_volume(current_app.text(), value)
            self.volume_label.setText(f"Volume: {value}%")

    def mute_current_app(self):
        current_app = self.list_widget.currentItem()
        if current_app:
            self.controller.mute_volume(current_app.text())
            self.volume_label.setText("Volume: Muted")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
