# Python 3.12.2

import os
import sys
import time

import cv2
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (QApplication, QComboBox, QFileDialog,
                               QHBoxLayout, QLabel, QMainWindow, QPushButton,
                               QSizePolicy, QVBoxLayout, QWidget, QSlider,
                               QTableWidget, QTableWidgetItem)
from pathlib import Path
import threading

#local imports
from thread import Thread
from viewport import Viewport


class Window(QMainWindow):
        def __init__(self):
                super().__init__()
                # Frontend flags and class variables
                self.live_status = False
                self.media_playback_status = False
                self.confidence_threshold = 0.55
                self.overlap_threshold = 0.55
                self.media_source = os.getcwd()

                # Title and dimensions
                self.setWindowTitle("Vision Drive")
                # self.setFixedSize(QSize(1280, 583))
                self.setGeometry(0, 0, 1280, 600)

                # Thread in charge of updating the image
                self.th = Thread(self, verbose= True)
                self.th.confidence = self.confidence_threshold
                self.th.iou = self.overlap_threshold
                # self.th.finished.connect(self.close)
                self.th.updateFrame.connect(self.setImage)

                # Create a label for the display
                self.viewport = Viewport(self)
                self.viewport.mousePressed.connect(self.viewport_clicked)

                # Model Container
                model_container = QHBoxLayout()
                self.model_combobox = QComboBox()
                for model_file in os.listdir("./models"):
                        self.model_combobox.addItem(model_file)
                self.model_combobox.setFixedHeight(50)
                model_container.addWidget(QLabel("Trained Model:"), 10)
                model_container.addWidget(self.model_combobox, 90)
                
                # Veiw Port Layout
                layout_6 = QVBoxLayout()
                layout_6.addLayout(model_container)
                layout_6.addWidget(self.viewport)

                # Detection Zone Control
                

                # Threshold Control
                threshold_container = QVBoxLayout()
                confidence_threshold_label = QHBoxLayout()
                self.confidence_threshold_slider = QSlider(Qt.Orientation.Horizontal)
                self.confidence_threshold_slider.setValue(round(self.confidence_threshold*100))
                self.confidence_threshold_slider.setRange(0, 100)
                self.confidence_threshold_slider.setMaximumWidth(300)
                self.confidence_threshold_label_value = QLabel(f"{self.confidence_threshold:0.2f}")
                self.confidence_threshold_slider.valueChanged.connect(self.confidence_slider_value_changed)
                self.confidence_threshold_slider.sliderMoved.connect(self.confidence_slider_position)
                self.confidence_threshold_slider.sliderPressed.connect(self.confidence_slider_pressed)
                self.confidence_threshold_slider.sliderReleased.connect(self.confidence_slider_released)
                confidence_threshold_label.addWidget(QLabel("Confidence"))
                confidence_threshold_label.addWidget(self.confidence_threshold_label_value)
                overlap_threshold_label = QHBoxLayout()
                self.overlap_threshold_slider = QSlider(Qt.Orientation.Horizontal)
                self.overlap_threshold_slider.setValue(round(self.overlap_threshold*100))
                self.overlap_threshold_slider.setRange(0, 100)
                self.overlap_threshold_slider.setMaximumWidth(300)
                self.overlap_threshold_label_value = QLabel(f"{self.overlap_threshold:0.2f}")
                self.overlap_threshold_slider.valueChanged.connect(self.overlap_slider_value_changed)
                self.overlap_threshold_slider.sliderMoved.connect(self.overlap_slider_position)
                self.overlap_threshold_slider.sliderPressed.connect(self.overlap_slider_pressed)
                self.overlap_threshold_slider.sliderReleased.connect(self.overlap_slider_released)
                overlap_threshold_label.addWidget(QLabel("Overlap"))
                overlap_threshold_label.addWidget(self.overlap_threshold_label_value)
                threshold_container.addLayout(confidence_threshold_label)
                threshold_container.addWidget(self.confidence_threshold_slider)
                threshold_container.addLayout(overlap_threshold_label)
                threshold_container.addWidget(self.overlap_threshold_slider)

                # Control Panel Layout
                layout_5 = QVBoxLayout()
                self.set_detect_zone_button = QPushButton("Draw Detection Zone")
                self.media_load_button = QPushButton("Open Image or Video File")
                self.live_button = QPushButton("Start Live")
                self.export_button = QPushButton("Export Predictions")
                self.set_detect_zone_button.setFixedHeight(50)
                self.set_detect_zone_button.setMaximumWidth(300)
                self.media_load_button.setMaximumWidth(300)
                self.live_button.setFixedHeight(50)
                self.live_button.setMaximumWidth(300)
                self.export_button.setFixedHeight(50)
                self.export_button.setMaximumWidth(300)
                self.set_detect_zone_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
                self.media_load_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
                self.live_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
                self.export_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
                layout_5.addWidget(self.set_detect_zone_button)
                layout_5.addWidget(self.media_load_button)
                layout_5.addWidget(self.live_button)
                layout_5.addLayout(threshold_container)
                layout_5.addWidget(self.export_button)

                # Inference Panel Layout
                layout_4 = QHBoxLayout()
                layout_4.addLayout(layout_5, 20)
                layout_4.addLayout(layout_6)
                
                # App Title
                app_title_label = QLabel("Vision Drive")
                app_title_label.setFixedHeight(50)

                # App How To
                how_to_use_button = QPushButton("How to Use?")
                how_to_use_button.setFixedHeight(50)

                # App Header Layout
                app_header_layout = QHBoxLayout()
                app_header_layout.addWidget(app_title_label, 90)
                app_header_layout.addWidget(how_to_use_button, 10)

                # Vehicle Counter Tab
                self.vehicle_counter_table = QTableWidget()
                self.vehicle_counter_table.setRowCount(13)
                self.vehicle_counter_table.setColumnCount(3)
                self.vehicle_counter_table.setHorizontalHeaderLabels(["Vehicle Type", "Incoming", "Outgoing"])
                self.vehicle_counter_table.setMaximumWidth(300)

                # Results Layout
                results_layout = QVBoxLayout()
                results_layout.addWidget(QLabel("Traffic Data"))
                results_layout.addWidget(QLabel("Vehicle Counter"))
                results_layout.addWidget(self.vehicle_counter_table)
                results_layout.addWidget(QLabel("Average Speed"))
                # results_layout.addLayout(vehicle_speed_table)

                # Sub Main Layout
                sub_layout = QVBoxLayout()
                sub_layout.addLayout(app_header_layout)
                sub_layout.addLayout(layout_4)

                # Main Layout
                main_layout = QHBoxLayout()
                main_layout.addLayout(sub_layout)
                main_layout.addLayout(results_layout)

                # Central widget
                widget = QWidget(self)
                widget.setLayout(main_layout)
                self.setCentralWidget(widget)

                # Connections
                self.live_button.clicked.connect(self.live_start)
                self.media_load_button.clicked.connect(self.open_file_dialog)
                # self.button2.setEnabled(False)
                self.model_combobox.currentTextChanged.connect(self.set_model)

        def initialize_table(self):
                for i, class_id in enumerate(self.th.CLASS_NAMES_DICT):
                        print(class_id)
                        item_name = QTableWidgetItem(self.th.CLASS_NAMES_DICT[class_id])
                        item_code = QTableWidgetItem()
                        item_color = QTableWidgetItem() 
                        self.vehicle_counter_table.setItem(i, 0, item_name)
                        self.vehicle_counter_table.setItem(i, 1, item_code)
                        self.vehicle_counter_table.setItem(i, 2, item_color)
        
        def kill_thread(self):
                print("Ending Inference...")
                self.th.status = False
                self.th.cap.release()
                cv2.destroyAllWindows()
                self.th.terminate()
                # Give time for the thread to finish
                time.sleep(1)
        
        def start(self):
                self.th.status = True
                if type(self.media_source) == int:
                        print(f"Starting from Live: {self.media_source}")
                else:
                        print(f"Starting from File: {self.media_source}")
                self.th.set_file(self.model_combobox.currentText())
                self.th.set_media_source(self.media_source)
                self.th.start()
                print(threading.active_count())
        
        def media_start(self):
                # self.media_source = r"E:\Batangas CCTV - dataset\dvr_ch1_20240203055922_20240203200203.dav"
                # self.media_source = r"E:\Batangas CCTV - dataset\dvr_ch11_20240202115743_20240202235348.dav"
                if self.media_playback_status:
                        self.media_load_button.setText("Start from a File")
                        self.live_button.setEnabled(True)
                        self.media_playback_status = False
                        self.kill_thread()
                else:
                        self.media_load_button.setText("Stop Media Playback")
                        self.live_button.setEnabled(False)
                        self.media_playback_status = True
                        self.start()

        @Slot()
        def open_file_dialog(self):
                if type(self.media_source)==int:
                        landing_dir = os.getcwd()
                else:
                        landing_dir = self.media_source[:self.media_source.rindex('\\')]
                
                if self.media_playback_status:
                        self.media_start()
                else:
                        filename, ok = QFileDialog.getOpenFileName(self,"Select a File", landing_dir, "Videos (*.mp4 *.mov *.avi *.dav)")

                        if filename:
                                path = Path(filename)
                                self.media_source = str(path)

                        if ok:
                                self.media_start()
                        else:
                                print("File selection unsuccessful")
        
        @Slot(tuple)
        def viewport_clicked(self, position):
                print(position)

        @Slot()
        def set_model(self, text):
                self.th.set_file(text)
                self.initialize_table()

        @Slot(QImage)
        def setImage(self, image):
                self.viewport.setPixmap(QPixmap.fromImage(image))
        
        @Slot()
        def live_start(self):
                self.media_source = 0
                if self.live_status:
                        self.live_button.setText("Start Live")
                        self.media_load_button.setEnabled(True)
                        self.live_status = False
                        self.kill_thread()
                else:
                        self.live_button.setText("End Live")
                        self.media_load_button.setEnabled(False)
                        self.live_status = True
                        self.start()
        @Slot()
        def confidence_slider_value_changed(self, value):
                self.confidence_threshold = value/100
                print(f"Confidence value: {self.confidence_threshold:0.2f}")

        @Slot()
        def confidence_slider_position(self, position):
                print("Confidence slider position", position)

        @Slot()
        def confidence_slider_pressed(self):
                print("Confidence slider pressed!")

        @Slot()
        def confidence_slider_released(self):
                self.th.confidence = self.confidence_threshold
                self.confidence_threshold_label_value.setText(f"{self.confidence_threshold:0.2f}")
                print("Confidence updated")

        @Slot()
        def overlap_slider_value_changed(self, value):
                self.overlap_threshold = value/100
                print(f"Overlap value: {self.overlap_threshold:0.2f}")

        @Slot()
        def overlap_slider_position(self, position):
                print("Overlap slider position", position)

        @Slot()
        def overlap_slider_pressed(self):
                print("Overlap slider pressed!")

        @Slot()
        def overlap_slider_released(self):
                self.th.iou = self.overlap_threshold
                self.overlap_threshold_label_value.setText(f"{self.overlap_threshold:0.2f}")
                print("Overlap updated")

if __name__ == "__main__":
        app = QApplication()
        w = Window()
        w.show()
        sys.exit(app.exec())