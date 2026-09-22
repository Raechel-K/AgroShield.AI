import tensorflow as tf
import numpy as np
from pathlib import Path
from PIL import Image

# -----------------------------
# Configuration
# -----------------------------

MODEL_PATH = "model/agroshield_model.keras"
IMAGE_SIZE = (224, 224)

# -----------------------------
# Disease information
# -----------------------------

DISEASE_INFO = {
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot":
        "Gray Leaf Spot - a fungal disease affecting maize leaves.",

    "Corn_(maize)___Common_rust_":
        "Common Rust - a fungal disease causing rust-colored spots.",

    "Corn_(maize)___healthy":
        "Healthy corn leaf.",

    "Potato___Early_blight":
        "Early Blight - a fungal disease that causes dark lesions on potato leaves.",

    "Potato___Late_blight":
        "Late Blight - a serious disease causing dark lesions and leaf damage.",

    "Potato___healthy":
        "Healthy potato leaf.",

    "Tomato___Early_blight":
        "Early Blight - a fungal disease causing dark circular lesions.",

    "Tomato___Late_blight":
        "Late Blight - a disease causing dark, water-soaked lesions.",

    "Tomato___healthy":
        "Healthy tomato leaf."
}

# -----------------------------
# Recommendation
# -----------------------------

RECOMMENDATIONS = {
    "healthy":
        "No disease detected. Continue regular crop monitoring.",

    "Early_blight":
        "Remove severely affected leaves, improve airflow, avoid overhead watering, and consult local agricultural guidance.",

    "Late_blight":
        "Remove affected plant material, avoid overhead watering, and seek agricultural guidance for appropriate disease management.",

    "Common_rust":
        "Monitor the crop closely and consult local agricultural guidance if symptoms spread.",

    "Cercospora":
        "Remove heavily affected leaves where appropriate and consult local agricultural guidance for disease management."
}

# -----------------------------
# Find a test image
# -----------------------------

test_dir = Path("processed_dataset/test")

image_files = list(test_dir.rglob("*.JPG"))

if not image_files:
    raise FileNotFoundError("No JPG images found in the test dataset.")

image_path = image_files[0]

print("Testing image:")
print(image_path)

# -----------------------------
# Load model
# -----------------------------

print("\nLoading AgroShield model...")

model = tf.keras.models.load_model(MODEL_PATH)

# -----------------------------
# Load image
# -----------------------------

image = Image.open(image_path).convert("RGB")

image = image.resize(IMAGE_SIZE)

image_array = np.array(image)

image_array = np.expand_dims(image_array, axis=0)

# -----------------------------
# Prediction
# -----------------------------

predictions = model.predict(image_array, verbose=0)

predicted_index = np.argmax(predictions[0])

confidence = float(predictions[0][predicted_index])

# Get class names from directory structure
class_names = sorted([
    folder.name
    for folder in test_dir.iterdir()
    if folder.is_dir()
])

predicted_class = class_names[predicted_index]

# -----------------------------
# Display result
# -----------------------------

print("\n==============================")
print("      AGROSHIELD AI")
print("==============================")

print("\nPrediction:")
print(predicted_class)

print(f"\nConfidence: {confidence * 100:.2f}%")

print("\nDisease information:")
print(
    DISEASE_INFO.get(
        predicted_class,
        "Information unavailable."
    )
)

print("\nRecommendation:")

recommendation = "Continue monitoring the crop."

for key, value in RECOMMENDATIONS.items():
    if key in predicted_class:
        recommendation = value
        break

print(recommendation)

print("\n==============================")