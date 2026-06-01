from pathlib import Path

ROOT = Path(__file__).resolve().parent

DATASET_DIR = ROOT / 'dataset'
DATA_DIR = ROOT / 'data'
OUTPUT_DIR = ROOT / 'outputs'
MODEL_DIR = ROOT / 'models'

# --- Bổ sung các cấu hình còn thiếu cho tool fix_verify_annotations ---
YOLO_DS_DIR = DATA_DIR / 'dataset'
YOLO_YAML = DATA_DIR / 'dataset.yaml'
IMAGE_EXT = ('.jpg', '.jpeg', '.png')
EVAL_PLOTS_DIR = OUTPUT_DIR / 'eval_plots'

FRAME_SIZE = (1280, 720)
FPS_EXTRACT = 2

CLASSES = {
    'strong': 0,
    'middle': 1,
    'weak': 2,
    'none': 3
}

YOLO_MODEL = 'yolo11n-seg.pt'
CONF_THRESHOLD = 0.4

WINDOW_SIZE = 30