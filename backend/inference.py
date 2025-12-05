from ultralytics import YOLO
import os

# Load the YOLOv8 model (replace with the correct path to your best.pt model)
model = YOLO('models/best.pt')

def run_inference(image_path):
    # Perform inference on the image
    results = model(image_path)

    # YOLOv8 returns a list, so get the first result
    result = results[0]

    # Define the directory where you want to save the result
    save_dir = 'runs/detect/exp'
    os.makedirs(save_dir, exist_ok=True)  # Ensure the directory exists

    # Create the output path by combining the save directory with the original filename
    output_image_path = os.path.join(save_dir, os.path.basename(image_path))

    # Save the result image (the `save=True` ensures the image is saved)
    result.plot(save=True, filename=output_image_path)

    # Return the path to the saved image
    return {'output_image': output_image_path}
