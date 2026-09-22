🌿 AgroShield.AI

AI-Powered Plant Disease Detection System

AgroShield.AI is a full-stack AI application that detects crop diseases from leaf images using deep learning. Farmers and agricultural users can upload a photo of a plant leaf and receive an instant disease prediction through a modern web interface.

---

✨ Features

- 🌱 AI-based leaf disease detection
- 📷 Upload images for instant prediction
- 🤖 TensorFlow/Keras trained model
- ⚡ FastAPI REST API backend
- 🎨 React + Vite responsive frontend
- 📊 Dataset preprocessing & training pipeline

---

🛠 Tech Stack

Technology| Purpose
React + Vite| Frontend
FastAPI| Backend API
TensorFlow / Keras| AI Model
Python| Model & Backend
Git + GitHub| Version Control

---

📁 Project Structure

AgroShield.AI/
│

├── frontend/               # React frontend

├── backend/                # FastAPI backend

├── notebooks/              # Data processing & training scripts

├── dataset/                # Original dataset

├── processed_dataset/      # Processed images

├── model/                  # Trained AI model

├── screenshots/            # App screenshots

├── .gitignore

└── PROJECT_PLAN.md

---

🚀 Getting Started

Clone the repository:

git clone https://github.com/Raechel-K/AgroShield.AI.git
cd AgroShield.AI

Create virtual environment:

python -m venv .venv
.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Start Backend:

uvicorn backend.main:app --reload

Start Frontend:

cd frontend
npm install
npm run dev

---

🧠 AI Workflow

1. Download & verify dataset
2. Preprocess leaf images
3. Train TensorFlow model
4. Save trained ".keras" model
5. Predict disease from uploaded images

---

🌍 Future Roadmap

- Disease treatment recommendations
- Multilingual support
- Mobile Flutter application
- Weather-aware crop advisory
- Farmer dashboard & analytics

---

🐱‍👤🐱‍👤 NOTE:
Current Status :- Works on 2 crops ( Maize and Tomato leaf), will add on more crops in the future.
HAHA 🌷 DHANYABAD 🌷

---

👩‍💻 Author

Riya Kachhap

AI • Full Stack Development • Computer Vision

«Building intelligent technology for sustainable agriculture.»
