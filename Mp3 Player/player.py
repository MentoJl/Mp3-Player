from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import sys
import os
import json


class Ui_Dialog(object):

    playlist = {}
    media = None
    player = QMediaPlayer()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(436, 501)
        Dialog.setMinimumSize(QtCore.QSize(436, 501))
        Dialog.setMaximumSize(QtCore.QSize(436, 501))
        Dialog.setStyleSheet("background-color: rgb(26, 26, 36);\n"
"color: rgb(193, 193, 210);")
        self.musicList = QtWidgets.QListWidget(Dialog)
        self.musicList.setGeometry(QtCore.QRect(0, 190, 441, 311))
        self.musicList.setObjectName("musicList")
        self.load_Button = QtWidgets.QPushButton(Dialog)
        self.load_Button.setGeometry(QtCore.QRect(0, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.load_Button.setFont(font)
        self.load_Button.setObjectName("load_Button")
        self.delete_Button = QtWidgets.QPushButton(Dialog)
        self.delete_Button.setGeometry(QtCore.QRect(90, 160, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delete_Button.setFont(font)
        self.delete_Button.setObjectName("delete_Button")
        self.previous_Button = QtWidgets.QPushButton(Dialog)
        self.previous_Button.setGeometry(QtCore.QRect(10, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.previous_Button.setFont(font)
        self.previous_Button.setStyleSheet("color: rgb(193, 193, 210);")
        self.previous_Button.setObjectName("previous_Button")
        self.unwind_Button = QtWidgets.QPushButton(Dialog)
        self.unwind_Button.setGeometry(QtCore.QRect(80, 90, 61, 31))
        self.unwind_Button.setObjectName("unwind_Button")
        self.play_Button = QtWidgets.QPushButton(Dialog)
        self.play_Button.setGeometry(QtCore.QRect(220, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.play_Button.setFont(font)
        self.play_Button.setObjectName("play_Button")
        self.rewind_Button = QtWidgets.QPushButton(Dialog)
        self.rewind_Button.setGeometry(QtCore.QRect(290, 90, 61, 31))
        self.rewind_Button.setObjectName("rewind_Button")
        self.next_Button = QtWidgets.QPushButton(Dialog)
        self.next_Button.setGeometry(QtCore.QRect(360, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.next_Button.setFont(font)
        self.next_Button.setObjectName("next_Button")
        self.replay_Button = QtWidgets.QPushButton(Dialog)
        self.replay_Button.setGeometry(QtCore.QRect(150, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.replay_Button.setFont(font)
        self.replay_Button.setObjectName("replay_Button")
        self.music_Slider = QtWidgets.QSlider(Dialog)
        self.music_Slider.setGeometry(QtCore.QRect(0, 30, 431, 31))
        self.music_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.music_Slider.setObjectName("music_Slider")
        self.start = QtWidgets.QLabel(Dialog)
        self.start.setGeometry(QtCore.QRect(0, 70, 51, 16))
        self.start.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.start.setObjectName("start")
        self.end = QtWidgets.QLabel(Dialog)
        self.end.setGeometry(QtCore.QRect(360, 70, 71, 16))
        self.end.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.end.setObjectName("end")
        self.savePlaylist_Button = QtWidgets.QPushButton(Dialog)
        self.savePlaylist_Button.setGeometry(QtCore.QRect(220, 160, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.savePlaylist_Button.setFont(font)
        self.savePlaylist_Button.setObjectName("savePlaylist_Button")
        self.loadPlaylist_Button = QtWidgets.QPushButton(Dialog)
        self.loadPlaylist_Button.setGeometry(QtCore.QRect(320, 160, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loadPlaylist_Button.setFont(font)
        self.loadPlaylist_Button.setObjectName("loadPlaylist_Button")
        self.volume_Slider = QtWidgets.QSlider(Dialog)
        self.volume_Slider.setGeometry(QtCore.QRect(130, 62, 171, 20))
        self.volume_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.volume_Slider.setObjectName("volume_Slider")
        self.start_2 = QtWidgets.QLabel(Dialog)
        self.start_2.setGeometry(QtCore.QRect(60, 66, 61, 20))
        self.start_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.start_2.setObjectName("start_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 441, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.events()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.load_Button.setText(_translate("Dialog", "Load"))
        self.delete_Button.setText(_translate("Dialog", "Delete"))
        self.previous_Button.setText(_translate("Dialog", "⯬"))
        self.unwind_Button.setText(_translate("Dialog", "-00:10"))
        self.play_Button.setText(_translate("Dialog", "▶"))
        self.rewind_Button.setText(_translate("Dialog", "+00:10"))
        self.next_Button.setText(_translate("Dialog", "⯮"))
        self.replay_Button.setText(_translate("Dialog", "⭮"))
        self.start.setText(_translate("Dialog", "00:00"))
        self.end.setText(_translate("Dialog", "00:00"))
        self.savePlaylist_Button.setText(_translate("Dialog", "Save Playlist"))
        self.loadPlaylist_Button.setText(_translate("Dialog", "Load Playlist"))
        self.start_2.setText(_translate("Dialog", "Volume:"))
        self.label.setText(_translate("Dialog", ""))

    def loadFile(self):
        self.filepath, extension = QFileDialog.getOpenFileName(self.load_Button, "Open file", "../", "Mp3 files (*.mp3)")
        
        if self.filepath and not os.path.basename(self.filepath) in self.playlist:
            self.filename = os.path.basename(self.filepath)
            self.playlist[self.filename] = self.filepath
            self.musicList.addItem(self.filename)
        else:
            self.filename = ""
            self.filepath = ""

    def deleteFile(self):
        if self.musicList.currentItem():
            del self.playlist[self.musicList.currentItem().text()]
            row = self.musicList.row(self.musicList.currentItem())
            item = self.musicList.currentItem()
            self.musicList.takeItem(row)
            del item

    def another_Sound(self, value):
        if self.musicList.currentItem():
            self.musicList.setCurrentRow(self.musicList.currentRow() + value)
            self.load_Sound()

    def play_Sound(self):
        if self.player.isAudioAvailable() and self.player.state() == QMediaPlayer.PlayingState:
            self.play_Button.setText("⏸️")
            self.player.pause()
        else:
            self.play_Button.setText("▶️")
            self.player.play()

    def load_Sound(self):
        if self.musicList.currentItem():
            self.media = QMediaContent(QUrl.fromLocalFile(self.playlist[self.musicList.currentItem().text()]))
            self.label.setText(self.musicList.currentItem().text())
            self.player.setMedia(self.media)
            self.music_Slider.setValue(0)
            self.music_Slider.setSingleStep(1)
            self.player.durationChanged.connect(self.duration_changed)
            self.player.play()
        
    def convert_Time(self, min, sec):
        string = ""
        if min < 10:
            string += "0" + str(min)
        else:
            string += str(min)
        string += ":"
        if sec < 10:
            string += "0" + str(sec)
        else:
            string += str(sec)
        return string

    def duration_changed(self):
        self.end.setText(self.convert_Time(int(int(self.player.duration() / 1000) / 60), int(self.player.duration() / 1000) % 60))
        self.music_Slider.setMinimum(0)
        self.music_Slider.setMaximum(int(self.player.duration() / 1000))
        self.music_Slider.setSingleStep(1)
        self.music_Slider.setValue(0)
        self.volume_Slider.setMinimum(0)
        self.volume_Slider.setMaximum(100)
        self.volume_Slider.setValue(100)

    def changeMusicPos(self):
        if int(self.player.position() / 1000) != self.music_Slider.value():
            self.player.setPosition(self.music_Slider.value() * 1000)

    def updateSlider(self):
        self.music_Slider.setValue(int(self.player.position() / 1000))
        self.start.setText(self.convert_Time(int(int(self.player.position() / 1000) / 60), int(int(self.player.position() / 1000) % 60)))

    def changeVolume(self, value):
        self.player.setVolume(value)

    def unwind(self):
        self.music_Slider.setValue(int(self.player.position() / 1000) - 10)
        self.player.setPosition(self.music_Slider.value() * 1000)

    def rewind(self):
        self.music_Slider.setValue(int(self.player.position() / 1000) + 10)
        self.player.setPosition(self.music_Slider.value() * 1000)

    def replay(self):
        self.player.stop()
        self.player.play()

    def savePlaylist(self):
        with open('playlist.json', 'w') as file:
            json.dump(self.playlist, file, indent=4)

    def loadPlaylist(self):
        filepath, extension = QFileDialog.getOpenFileName(self.load_Button, "Open file", "../", "JSON files (*json)")
        with open(filepath, 'r') as file:
            self.playlist = json.load(file)
        for music_name in self.playlist:
            self.musicList.addItem(music_name)

    def events(self):
        try:
            self.load_Button.clicked.connect(lambda: self.loadFile())
            self.delete_Button.clicked.connect(lambda: self.deleteFile())
            self.play_Button.clicked.connect(lambda: self.play_Sound())
            self.unwind_Button.clicked.connect(lambda: self.unwind())
            self.rewind_Button.clicked.connect(lambda: self.rewind())
            self.musicList.itemDoubleClicked.connect(lambda: self.load_Sound())
            self.music_Slider.sliderMoved.connect(lambda: self.changeMusicPos())
            self.music_Slider.valueChanged.connect(lambda: self.changeMusicPos())
            self.player.positionChanged.connect(lambda: self.updateSlider())
            self.volume_Slider.valueChanged.connect(lambda: self.changeVolume(self.volume_Slider.value()))
            self.next_Button.clicked.connect(lambda: self.another_Sound(1))
            self.previous_Button.clicked.connect(lambda: self.another_Sound(-1))
            self.replay_Button.clicked.connect(lambda: self.replay())
            self.savePlaylist_Button.clicked.connect(lambda: self.savePlaylist())
            self.loadPlaylist_Button.clicked.connect(lambda: self.loadPlaylist())
        except Exception as error:
            self.label.setText(f"Error: {error}")

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_Dialog()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())