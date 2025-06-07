# 🖼️ Image Classifier App

This is a simple image classification web app built with [Gradio](https://gradio.app/) and [PyTorch](https://pytorch.org/). It uses a pretrained model (`resnet18`) to predict the top-3 labels for any uploaded image.

## 🚀 Demo

Try it locally by uploading an image or using one of the built-in examples.

## 📦 Features

- Upload or webcam input
- Top-3 class predictions with confidence
- Pretrained ResNet18 model
- Example images for quick testing
- Clean, easy-to-use UI

## 💻 How to Run

```bash
# Clone the repo
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