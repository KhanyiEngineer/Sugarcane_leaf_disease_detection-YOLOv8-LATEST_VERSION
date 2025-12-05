Sugar Leaf Disease Detection System Using YOLOv8

# Sugarcane Leaf Disease Detection System Using YOLOv8

This project is a deep learning-based system designed to detect diseases in maize leaves, focusing primarily on Sugarcane leaf disease It uses the YOLOv8 (You Only Look Once) object detection model to perform real-time detection on uploaded images. The system is built using Python, Flask for the backend API, and YOLOv8 for the object detection model.

## Features
- **Sugar cane Leaf Disease Detection**: Detects and classifies Sugarcane Leaf diseases from uploaded images.
- **Flask Backend**: A web server built with Flask to handle image uploads and return results.
- **YOLOv8 Model**: Utilizes the latest YOLOv8 model for efficient and accurate object detection.
- **Image Inference**: After image upload, the system runs inference and returns the result with the detected disease.
- **Real-Time Performance**: Fast image preprocessing and inference for real-time feedback.

## Project Structure

├── backend
│   ├── uploads                # Directory for uploaded images
│   ├── runs                   # Directory for saving inference results
│   ├── models                 # Pre-trained YOLOv8 model
│   ├── webapp.py              # Flask server code
│   ├── inference.py           # Inference logic and image processing
│   └── static                 # Frontend static files (optional)
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
└── yolov8_env                 # Virtual environment (optional)

## Installation

### Prerequisites
- Python 3.9 or later
- pip (Python package installer)

### Clone the Repository

git clone https:https://github.com/SAMGREENHEAD/Sugarcane_leaf_disease_detection-YOLOv8.git
cd sugarcane-disease-detection


### Set Up Virtual Environment (Optional)

python -m venv yolov8_env
source yolov8_env/bin/activate   # On Windows: yolov8_env\Scripts\activate


### Install Dependencies
Install the required packages by running:

pip install -r requirements.txt


### YOLOv8 Model
Download the pre-trained YOLOv8 model (`best.pt`) and place it in the `models` directory. This can be trained using your dataset or downloaded from a reliable source.

## Running the Project

### Start the Flask Server

cd backend
python webapp.py


The server will start on `http://127.0.0.1:5000/`. You can access it from a browser or use a tool like Postman to send image requests.

### Using the API
To detect diseases in sugarcane leaf images, send a POST request to the `/upload` endpoint with the image file:

POST /upload


#### Example (Using cURL)

curl -X POST -F "file=@/path/to/your/image.jpeg" http://127.0.0.1:5000/upload


The server will return the result, including the detected disease and the image with the bounding box.

## Inference Logic

The inference pipeline is handled in the `inference.py` file, where the YOLOv8 model is loaded and used to process the uploaded image. The result is saved in the `runs/detect/exp` directory.

### Key Code Snippet (Inference)

from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('models/best.pt')

def run_inference(image_path):
    # Perform inference
    results = model(image_path)
    result = results[0]
    
    # Save the result
    save_dir = 'runs/detect/exp'
    result.plot(save=True, filename=output_image_path)
    return {'output_image': output_image_path}


## Future Improvements
- Add support for detecting more sugarcane leaf diseases.
- Improve the web interface for better user experience.
- Train the model on a larger, more diverse dataset for increased accuracy.
- Optimize the inference time for faster results.
- Invest in the use of advanced/state of the art GPUs.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



### Explanation:
- **Project Overview**: It introduces the project and highlights its core functionality.
- **Installation**: Provides a step-by-step guide to setting up the project.
- **Usage**: Explains how to interact with the API.
- **Inference Logic**: Gives a brief overview of the inference process.
- **Future Improvements**: Lists potential areas for expansion.
- **Contributing** and **License**: Standard sections for open-source projects.

## Contributors

- **Khanyisile Tapiwa Magagula** (@KhanyiEngineer) – Project lead, data collection and preparation, model development and fine-tuning
- **Samkelo Msibi** (@Samgreenhead) – Data preparation, collaborative research, deployment, testing
