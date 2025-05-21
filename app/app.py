import gradio as gr
from model import predict

# Define a Gradio interface
iface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs="label",
    title="Image Classifier",
    description="Upload an image and this app will predict its class using MobileNetV2."
)

if __name__ == "__main__":
    iface.launch()