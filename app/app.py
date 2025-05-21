import gradio as gr
from model import predict

# Define a Gradio interface
iface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs="label",
    title="Image Classifier",
    description="Upload an image and this app will predict its class using MobileNetV2.",
    examples=[
        ["examples/dog.jpg"],
        ["examples/bike.jpg"],
        ["examples/pizza.jpg"]
    ],
    article="""
   <p>Dog photo by <a href="https://unsplash.com/@mtsjrdl?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">mtsjrdl</a> on 
   <a href="https://unsplash.com/photos/white-and-brown-long-coated-dog-5yAhL8ViUVg?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a></p>
   <p>Bike photo by <a href="https://unsplash.com/@streetsh?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">streetsh</a> on 
   <a href="https://unsplash.com/photos/black-and-orange-road-bike-parked-beside-white-wall-vZAk_n9Plfc?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a><p>
   <p>Pizza photo by <a href="https://unsplash.com/@thenixcompany?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">The Nix Company</a> on 
   <a href="https://unsplash.com/photos/sliced-pizza-on-white-ceramic-plate-evA8uQLsUaE?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a></p>
   """
)

if __name__ == "__main__":
    iface.launch()