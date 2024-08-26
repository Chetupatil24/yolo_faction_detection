import os
from pathlib import Path

data = "D:/Projects/yolo_ultralytics/dataset/data.yaml"
task = "train"
model = "D:/Projects/yolo_ultralytics/yolov8x.pt"  # Updated model to YOLOv8m
optimizer = "AdamW"
devices = "cpu"
imgsz = 640
#project = "test"

name = "predict"
epochs = 200
batch = 16
cfg = "D:/Projects/yolo_ultralytics/ultralytics/cfg/default.yaml"
conf = 0.10
source = "D:/Projects/yolo_ultralytics/dataset/Test/images"

if task == "train":
    command = f"yolo detect mode=train model={model} device={devices} data={data} name={name} imgsz={imgsz} epochs={epochs} batch={batch} cfg={cfg}"

elif task == "test":
    command = f"yolo predict mode=predict model={model} data={data} name={name} conf={conf} device={devices} imgsz={imgsz} source={source}"

print(f"Command = {command}")

os.system(command)
