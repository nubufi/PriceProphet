import gradio as gr
import requests

url = "http://llama_app:5000/api/predict"


def predict(product):
    myobj = {"product": product}

    x = requests.post(url, json=myobj)
    price = x.json()["price"]
    return f"The price is {price}$"


iface = gr.Interface(
    fn=predict,
    inputs=[gr.Textbox(label="Your message:", lines=6)],
    outputs=[gr.Markdown(label="Response:")],
).launch()
