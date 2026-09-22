from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import tensorflow as tf
import numpy as np
import io

app = FastAPI(title="AgroShield AI API")

# Allow React frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load trained model
MODEL_PATH = "model/agroshield_model.keras"
model = tf.keras.models.load_model(MODEL_PATH)

# IMPORTANT: Keep this order exactly the same as the training classes
CLASS_NAMES = [
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___healthy",
    "Potato___Early_blight",
    "Potato___healthy",
    "Potato___Late_blight",
    "Tomato___Early_blight",
    "Tomato___healthy",
    "Tomato___Late_blight",
]

DISEASE_INFO = {
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot":
        "Gray Leaf Spot is a fungal disease affecting maize leaves.",

    "Corn_(maize)___Common_rust_":
        "Common Rust is a fungal disease that produces rust-colored spots on maize leaves.",

    "Corn_(maize)___healthy":
        "The maize leaf appears healthy.",

    "Potato___Early_blight":
        "Early Blight is a fungal disease commonly affecting potato leaves.",

    "Potato___healthy":
        "The potato leaf appears healthy.",

    "Potato___Late_blight":
        "Late Blight is a serious disease affecting potato plants.",

    "Tomato___Early_blight":
        "Early Blight is a fungal disease affecting tomato leaves.",

    "Tomato___healthy":
        "The tomato leaf appears healthy.",

    "Tomato___Late_blight":
        "Late Blight is a serious disease affecting tomato plants.",
}


@app.get("/")
def home():
    return {
        "message": "AgroShield AI API is running!"
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Read uploaded image
    image_bytes = await file.read()

    # Convert image to RGB
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    # Resize to model input size
    image = image.resize((224, 224))

    # Convert image to numpy array
    image_array = np.array(image)

    # Normalize pixels
    image_array = image_array / 255.0

    # Add batch dimension
    image_array = np.expand_dims(image_array, axis=0)

    # Prediction
    predictions = model.predict(image_array, verbose=0)

    # Get highest probability class
    predicted_index = np.argmax(predictions[0])
    confidence = float(predictions[0][predicted_index])

    disease = CLASS_NAMES[predicted_index]

    return {
        "disease": disease,
        "confidence": round(confidence * 100, 2),
        "information": DISEASE_INFO.get(
            disease,
            "No information available."
        )
    }