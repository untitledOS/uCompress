from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QVBoxLayout, QHBoxLayout, QSizePolicy, QLineEdit, QGroupBox, QComboBox, QLabel, QCheckBox

import sys, platform, subprocess, argparse

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        parser = argparse.ArgumentParser()
        parser.add_argument("path", nargs="?", default=None)
        args = parser.parse_args()
        self.path = args.path

        self.initUI()


    def initUI(self):
        self.setWindowTitle("uCompress")
        self.setGeometry(100, 100, 400, 300)
        
        self.layout = QVBoxLayout()

        self.group_box = QGroupBox(f"Compress '{self.path}'")
        self.layout.addWidget(self.group_box)
        self.group_box_layout = QVBoxLayout()
        self.compress_button = QPushButton("Compress")
        self.group_box.setLayout(self.group_box_layout)

        self.compression_type_layout = QHBoxLayout()
        self.group_box_layout.addLayout(self.compression_type_layout)
        self.compression_type_label = QLabel("Type:")
        self.compression_type_layout.addWidget(self.compression_type_label)
        self.compression_type = QComboBox()
        self.compression_type.addItems(["7-zip archive", "Java archive", "Tar archive", "Tar archive (bzip-compressed)", "Tar archive (compressed)", "Tar archive (gzip-compressed)", "Tar archive (LZ4-compressed)", "Tar archive (lzip-compressed)", "Tar archive (LZMA-compressed)", "Tar archive (XZ-compressed)", "Tar archive (Zstandard-compressed)", "Zip archive"])
        self.compression_type.currentIndexChanged.connect(lambda: self.extension.setText(self.get_file_extension(self.compression_type.currentText())))
        self.compression_type_layout.addWidget(self.compression_type)

        self.extension_layout = QHBoxLayout()
        self.group_box_layout.addLayout(self.extension_layout)
        self.extension_label = QLabel("Extension:")
        self.extension_layout.addWidget(self.extension_label)
        self.extension_checkbox = QCheckBox()
        self.extension_checkbox.setChecked(True)
        self.extension_checkbox.stateChanged.connect(lambda: self.extension.setDisabled(not self.extension_checkbox.isChecked()))
        self.extension_layout.addWidget(self.extension_checkbox)
        self.extension_label_2 = QLabel("Automatically add ")
        self.extension_layout.addWidget(self.extension_label_2)
        self.extension = QLineEdit()
        self.extension.setText("." + self.get_file_extension(self.compression_type.currentText()))
        self.extension_layout.addWidget(self.extension)

        self.group_box_layout.addStretch()

        self.setLayout(self.layout)

    def get_file_extension(self, compression_type):
        file_extensions = {"7-zip archive": "7z", "Java archive": "jar", "Tar archive": "tar", "Tar archive (bzip-compressed)": "tar.bz2", "Tar archive (compressed)": "tar.Z", "Tar archive (gzip-compressed)": "tar.gz", "Tar archive (LZ4-compressed)": "tar.lz4", "Tar archive (lzip-compressed)": "tar.lz", "Tar archive (LZMA-compressed)": "tar.lzma", "Tar archive (XZ-compressed)": "tar.xz", "Tar archive (Zstandard-compressed)": "tar.zst", "Zip archive": "zip"}
        return file_extensions[compression_type]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.setStyle("Windows")
    sys.exit(app.exec_())
