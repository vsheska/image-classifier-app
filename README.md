## Image Classification Web Application

## Project Overview
An interactive web application that performs real-time image classification using deep learning. Built with PyTorch and Gradio, this application demonstrates the practical implementation of machine learning models in a user-friendly interface.

## Key Features
- Real-time image classification using ResNet18
- Interactive web interface built with Gradio
- Multiple input methods:
  - File upload functionality
  - Example images for quick testing
- Top-3 prediction confidence scores
- Clean and intuitive user interface

## Technical Stack
- **Deep Learning Framework**: PyTorch
- **Model Architecture**: ResNet18 (pretrained)
- **Web Interface**: Gradio
- **Language**: Python 3.x

## Installation & Usage

### Prerequisites
- Python 3.x
- pip package manager

### Setup
1. Clone the repository
```bash
git clone https://github.com/vsheska/image-classifier-app.git
cd image-classifier-app
```

# (Optional) Create a virtual environment
```
python -m venv venv
source venv/bin/activate  # on Windows use `venv\Scripts\activate`
```

# Install dependencies
```
pip install -r requirements.txt
```
# Run the app
```
python app/app.py
```
The application will be available at `http://localhost:7860`

## Project Structure
The project maintains a clean, modular organization:

image-classifier-app/
├── app/                    # Main application directory
│   ├── app.py             # Web interface implementation
│   └── model.py           # Model implementation and inference
├── .gradio                # Gradio configuration
├── .venv                  # Virtual environment (not tracked in git)
├── examples/              # Example images for testing
├── .gitattributes        # Git attributes configuration
├── .gitignore            # Git ignore configuration
└── requirements.txt       # Project dependencies

## How It Works
1. The application uses a pre-trained ResNet18 model, which has been trained on the ImageNet dataset
2. Users can upload an image through the web interface
3. The model processes the image and returns the top 3 predicted classes with confidence scores
4. Results are displayed instantly in the user interface

## Example Usage
1. Launch the application following the installation steps or visit the app hosted on [AWS](http://3.86.215.140:7860/).
2. Upload an image using the interface or try one of the provided example images
3. View the model's predictions and confidence scores

## Future Enhancements
- Support for multiple model architectures
- Custom model training capabilities
- Batch processing for multiple images
- Enhanced visualization of model predictions
- Performance metrics and analytics

## Author
Vincenzo Heska
- GitHub: https://github.com/vsheska
- LinkedIn: https://www.linkedin.com/in/vincenzo-heska/