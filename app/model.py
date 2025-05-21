import torch
from torchvision import models, transforms
from PIL import Image
import requests

# Load pretrained MobileNetV2
model = models.mobilenet_v2(pretrained=True)
model.eval()

# Preprocessing pipeline for input images
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],  # Standard ImageNet means
        std=[0.229, 0.224, 0.225]    # Standard ImageNet stds
    )
])

# Load ImageNet class labels
LABELS_URL = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
labels = requests.get(LABELS_URL).text.strip().split("\n")

def predict(image: Image.Image) -> dict[str, float]:
    """Takes a PIL image and returns the top prediction label."""
    image_tensor = preprocess(image).unsqueeze(0)  # Add batch dimension
    with torch.no_grad():
        logits = model(image_tensor)
        probs = torch.nn.functional.softmax(logits[0], dim=0)
        top_probs, top_indices = torch.topk(probs, 3)

    results = {labels[idx]: float(prob) for idx, prob in zip(top_indices, top_probs)}
    return results