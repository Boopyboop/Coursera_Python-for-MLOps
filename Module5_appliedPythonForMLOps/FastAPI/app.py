"""
FastAPI application for RoBERTa sentiment analysis using ONNX Runtime.

Features:
- Serves a static HTML page at the root endpoint.
- POST /predict endpoint for sentiment classification.
- Request body validation using Pydantic models.
- Interactive documentation via /docs (Swagger UI).
- Optionally exports the HuggingFace RoBERTa model to ONNX format if missing.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
import onnxruntime as ort
import numpy as np
from transformers import RobertaTokenizer, RobertaForSequenceClassification
import os
import torch
from pathlib import Path

# ------------------------
# Configuration
# ------------------------

MODEL_PATH = "roberta-sequence-classification.onnx"  # Path to ONNX model
DEVICE = "cpu"  # Can be set to "cuda" if GPU is available

# ------------------------
# ONNX Export Function (called if model missing)
# ------------------------

def export_onnx_model():
    """
    Exports the HuggingFace RobertaForSequenceClassification model to ONNX format.
    Run this function automatically if ONNX model does not exist.
    """

    print(f"ONNX model not found at {MODEL_PATH}. Exporting now...")

    # Load the PyTorch model from HuggingFace
    model = RobertaForSequenceClassification.from_pretrained("roberta-base", num_labels=2)
    model.eval()

    # Create dummy inputs for the export (batch size 1, sequence length 128)
    tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
    dummy_input = tokenizer(
        "This is a dummy input for ONNX export.",
        return_tensors="pt",
        padding="max_length",
        truncation=True,
        max_length=128,
    )

    # Define output path for ONNX model
    output_path = Path(MODEL_PATH)

    # Export the model to ONNX
    torch.onnx.export(
        model,                                         # model being run
        (dummy_input["input_ids"], dummy_input["attention_mask"]),  # model input (tuple)
        str(output_path),                              # where to save the model
        export_params=True,                            # store trained parameter weights inside the model file
        opset_version=14,                              # ONNX version to export the model to
        input_names=["input_ids", "attention_mask"],  # model's input names
        output_names=["logits"],                       # model's output names
        dynamic_axes={
            "input_ids": {0: "batch_size", 1: "sequence"},
            "attention_mask": {0: "batch_size", 1: "sequence"},
            "logits": {0: "batch_size"},
        }
    )
    print(f"Model exported to {output_path}")

# ------------------------
# FastAPI App Initialization
# ------------------------

app = FastAPI(title="RoBERTa Sentiment Analysis API")

# ------------------------
# Load Tokenizer
# ------------------------

tokenizer = RobertaTokenizer.from_pretrained("roberta-base")

# ------------------------
# Check ONNX model existence and export if missing
# ------------------------

if not os.path.isfile(MODEL_PATH):
    export_onnx_model()

# ------------------------
# Load ONNX Model Session
# ------------------------

session = ort.InferenceSession(MODEL_PATH, providers=["CPUExecutionProvider"])

# ------------------------
# Pydantic Model for POST Body
# ------------------------

class SentimentRequest(BaseModel):
    text: str  # Single text string to analyze

# ------------------------
# Helper Functions
# ------------------------

def preprocess(text: str):
    """
    Tokenizes the input text for RoBERTa and returns NumPy arrays.
    """
    tokens = tokenizer(
        text,
        return_tensors="np",
        padding=True,
        truncation=True,
        max_length=128
    )
    return {
        "input_ids": tokens["input_ids"],
        "attention_mask": tokens["attention_mask"]
    }

def predict_sentiment(text: str):
    """
    Runs inference on the ONNX model and returns sentiment label.
    """
    inputs = preprocess(text)
    ort_inputs = {
        "input_ids": inputs["input_ids"],
        "attention_mask": inputs["attention_mask"]
    }
    ort_outs = session.run(None, ort_inputs)
    logits = ort_outs[0]
    prediction = np.argmax(logits, axis=1).item()
    return "positive" if prediction == 1 else "negative"

# ------------------------
# Routes
# ------------------------

@app.get("/")
def serve_homepage():
    """
    Serves the static HTML homepage from the static directory.
    """
    file_path = os.path.join("static", "index.html")
    return FileResponse(file_path)

@app.post("/predict")
def predict(request: SentimentRequest):
    """
    Predicts sentiment for the given input text.
    """
    sentiment = predict_sentiment(request.text)
    return {"sentiment": sentiment}

# ------------------------
# Notes:
# ------------------------
# - Static HTML file should be placed at: static/index.html
# - Run with:
#       uvicorn main:app --host 0.0.0.0 --port 8000
# - Access interactive docs at: http://127.0.0.1:8000/docs
