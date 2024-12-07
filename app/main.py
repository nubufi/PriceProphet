from flask import Flask, jsonify, request
from model.llama_model import LLaMAModel
from dotenv import load_dotenv
import os

load_dotenv()
hf_token = os.getenv("HF_TOKEN", "")

if not hf_token:
    raise ValueError("no HF_TOKEN provided")

app = Flask(__name__)
print("Downloading module, please wait till you see a completed message")
model = LLaMAModel(hf_token)
print("Downloading completed")


@app.route("/api/predict", methods=["POST"])
def predict():
    data = request.get_json()
    input_text = data.get("input_text", "")
    result = model.predict(input_text)
    return jsonify({"price": result})


@app.route("/")
def health():
    return "Hello world"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
