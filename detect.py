from ultralytics import YOLO
import os
import shutil

model = YOLO('best.pt')  # Your YOLOv8 trained model

def detect_object(image_path):
    results = model.predict(source=image_path, save=True, project='runs/detect', name='predict', exist_ok=True)

    output_folder = 'runs/detect/predict'
    output_file = os.path.basename(image_path)
    output_path = os.path.join(output_folder, output_file)
    final_output_path = os.path.join('outputs', output_file)

    # Check if YOLO output file exists
    if os.path.exists(output_path):
        shutil.move(output_path, final_output_path)
    else:
        print("Detection output not found:", output_path)
        raise FileNotFoundError(f"{output_path} not found")

    labels = results[0].names  # class labels
    return labels, final_output_path
