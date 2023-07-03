from PyQt5.QtWidgets import QFileDialog

filename, _ = QFileDialog.getOpenFileName(self, "Open file", "", "mp3 files (*.mp3)")
if filename:
    print("Selected file:", filename)
else:
    print("No file selected")