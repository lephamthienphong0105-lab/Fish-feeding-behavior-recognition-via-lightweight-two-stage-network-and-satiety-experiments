from ultralytics import YOLO

model = YOLO("yolo11s-seg.pt")

model.train(
    data="data/dataset.yaml",
    epochs=150,
    imgsz=640,
    batch=8,
    device="mps",
    workers=0,
    patience=30
)