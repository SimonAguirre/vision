# Python 3.12.2


from tqdm import tqdm
from ultralytics import YOLO

import supervision as sv

import os
import sys
import time

import cv2
from PySide6.QtCore import Qt, QThread, Signal, Slot
from PySide6.QtGui import QAction, QImage, QKeySequence, QPixmap
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox,
                               QHBoxLayout, QLabel, QMainWindow, QPushButton,
                               QSizePolicy, QVBoxLayout, QWidget)


class Thread(QThread):
        updateFrame = Signal(QImage)
        tracker = sv.ByteTrack()
        box_annotator = sv.BoundingBoxAnnotator()
        label_annotator = sv.LabelAnnotator()
        
        def __init__(self, parent=None):
                QThread.__init__(self, parent)
                self.trained_file = None        # Weights
                self.status = True              # Inference status
                self.cap = True                 
                self.confidence = 0.3
                self.iou = 0.3
                self.model = None

                
        def set_file(self, fname):
                # The data comes with the 'opencv-python' module
                self.trained_file = fname
                print(f"getting model: {self.trained_file}")
                self.model = YOLO(self.trained_file)
                self.CLASS_NAMES_DICT = dict(self.model.model.names)
                
        def run(self):
                self.cap = cv2.VideoCapture(0)
                while self.status: 
                        start_time = time.time()
                        # cascade = cv2.CascadeClassifier(self.trained_file)
                        ret, frame = self.cap.read()
                        if not ret:
                                continue
                        
                        results = self.model(
                                frame,
                                verbose=False,
                                conf=self.confidence, 
                                iou=self.iou
                        )[0]
                        detections = sv.Detections.from_ultralytics(results)
                        detections = self.tracker.update_with_detections(detections)
                        
                        """
                        # Reading frame in gray scale to process the pattern
                        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                        detections = cascade.detectMultiScale(gray_frame, scaleFactor=1.1,
                                                   minNeighbors=5, minSize=(30, 30))
                        """
                        annotated_frame = self.box_annotator.annotate(
                                scene=frame.copy(),
                                detections=detections
                        )
                             
                        labels = [
                                f"#{tracker_id} {self.CLASS_NAMES_DICT[class_id]} {confidence:0.2f}"
                                # f"{detect[4]}"
                                for _, _, confidence, class_id, tracker_id, _
                                # for detect
                                in detections
                        ]
                        
                        annotated_labeled_frame = self.label_annotator.annotate(
                                scene=annotated_frame, 
                                detections=detections,
                                labels = labels
                        )
                        
                        """
                        # Drawing green rectangle around the pattern
                        for (x, y, w, h) in detections:
                                pos_ori = (x, y)
                                pos_end = (x + w, y + h)
                                color = (0, 255, 0)
                                cv2.rectangle(frame, pos_ori, pos_end, color, 2)
                                
                        """
                        # Reading the image in RGB to display it
                        color_frame = cv2.cvtColor(annotated_labeled_frame, cv2.COLOR_BGR2RGB)
                        
                        
                        # Creating and scaling QImage
                        h, w, ch = color_frame.shape
                        img = QImage(color_frame.data, w, h, ch * w, QImage.Format_RGB888)
                        scaled_img = img.scaled(640, 480, Qt.KeepAspectRatio)
                        
                        
                        # Emit signal
                        self.updateFrame.emit(scaled_img)
                        print(f"Inference: {(time.time()-start_time)*1000:.3f} ms | {(1/(time.time()-start_time)):.1f} fps")
                sys.exit(-1)


class Window(QMainWindow):
        def __init__(self):
                super().__init__()
                # Title and dimensions
                self.setWindowTitle("Vision Drive")
                self.setGeometry(0, 0, 800, 500)

                """
                # Main menu bar
                self.menu = self.menuBar()
                self.menu_file = self.menu.addMenu("File")
                exit = QAction("Exit", self, triggered=qApp.quit)  # noqa: F821
                self.menu_file.addAction(exit)

                self.menu_about = self.menu.addMenu("&About")
                about = QAction("About Qt", self, shortcut=QKeySequence(QKeySequence.HelpContents),
                        triggered=qApp.aboutQt)  # noqa: F821
                self.menu_about.addAction(about)
                """
                
                # Create a label for the display camera
                self.label = QLabel(self)
                self.label.setFixedSize(640, 480)

                # Thread in charge of updating the image
                self.th = Thread(self)
                self.th.finished.connect(self.close)
                self.th.updateFrame.connect(self.setImage)

                # Model group
                self.group_model = QGroupBox("Trained model")
                self.group_model.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
                model_layout = QHBoxLayout()

                self.combobox = QComboBox()
                self.combobox.addItem('yolov8s.pt')
                self.combobox.addItem('yolov8m.pt')
                # for xml_file in os.listdir(cv2.data.haarcascades):
                #         if xml_file.endswith(".xml"):
                #                 self.combobox.addItem(xml_file)

                model_layout.addWidget(QLabel("File:"), 10)
                model_layout.addWidget(self.combobox, 90)
                self.group_model.setLayout(model_layout)

                # Buttons layout
                buttons_layout = QHBoxLayout()
                self.button1 = QPushButton("Start")
                self.button2 = QPushButton("Stop/Close")
                self.button1.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
                self.button2.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
                buttons_layout.addWidget(self.button2)
                buttons_layout.addWidget(self.button1)

                right_layout = QHBoxLayout()
                right_layout.addWidget(self.group_model, 1)
                right_layout.addLayout(buttons_layout, 1)

                # Main layout
                layout = QVBoxLayout()
                layout.addWidget(self.label)
                layout.addLayout(right_layout)

                # Central widget
                widget = QWidget(self)
                widget.setLayout(layout)
                self.setCentralWidget(widget)

                # Connections
                self.button1.clicked.connect(self.start)
                self.button2.clicked.connect(self.kill_thread)
                self.button2.setEnabled(False)
                self.combobox.currentTextChanged.connect(self.set_model)

        @Slot()
        def set_model(self, text):
                self.th.set_file(text)

        @Slot()
        def kill_thread(self):
                print("Finishing...")
                self.button2.setEnabled(False)
                self.button1.setEnabled(True)
                self.th.cap.release()
                cv2.destroyAllWindows()
                self.status = False
                self.th.terminate()
                # Give time for the thread to finish
                time.sleep(1)

        @Slot()
        def start(self):
                print("Starting...")
                self.button2.setEnabled(True)
                self.button1.setEnabled(False)
                self.th.set_file(self.combobox.currentText())
                self.th.start()

        @Slot(QImage)
        def setImage(self, image):
                self.label.setPixmap(QPixmap.fromImage(image))


if __name__ == "__main__":
        # SOURCE_WEIGHTS_PATH = 'yolov8s.pt'
        # SOURCE_VIDEO_PATH = './video.mp4'
        # TARGET_VIDEO_PATH = './video_out.mp4'
        # CONFIDENCE_THRESHOLD = 0.3
        # IOU_THRESHOLD = 0.3

        # model = YOLO(SOURCE_WEIGHTS_PATH)

        # tracker = sv.ByteTrack()
        # box_annotator = sv.BoundingBoxAnnotator()
        # label_annotator = sv.LabelAnnotator()
        # frame_generator = sv.get_video_frames_generator(source_path=SOURCE_VIDEO_PATH)
        # video_info = sv.VideoInfo.from_video_path(video_path=SOURCE_VIDEO_PATH)

        # with sv.VideoSink(target_path=TARGET_VIDEO_PATH, video_info=video_info) as sink:
        #         for frame in tqdm(frame_generator, total=video_info.total_frames):
                        # results = model(
                        #         frame,
                        #         verbose=False,
                        #         conf=CONFIDENCE_THRESHOLD, 
                        #         iou=IOU_THRESHOLD
                        # )[0]
                        # detections = sv.Detections.from_ultralytics(results)
                        # detections = tracker.update_with_detections(detections)

                        # annotated_frame = box_annotator.annotate(
                        #         scene=frame.copy(),
                        #         detections=detections
                        # )

                        # annotated_labeled_frame = label_annotator.annotate(
                        #         scene=annotated_frame, 
                        #         detections=detections
                        # )
                        
                        # sink.write_frame(frame=annotated_labeled_frame)

        app = QApplication()
        w = Window()
        w.show()
        sys.exit(app.exec())