Real-Time Fake News Detection using Machine Learning

A Machine Learning application designed to detect and classify news articles as Real or Fake using Natural Language Processing (NLP) and a fine-tuned model.
The system provides real-time predictions through a web interface and aims to combat misinformation effectively.

🔍 Problem Statement

Fake news spreads rapidly and misleads people across social media and news platforms.
This project aims to:
✔ Automatically classify news articles
✔ Provide fast predictions
✔ Assist users in verifying news credibility

🚀 Features

🤖 Machine Learning Model: Fine-tuned NLP model stored via Git LFS

📊 Dataset: Labeled dataset of real and fake news articles

🌐 Web Interface: Flask / Streamlit-based UI for real-time predictions

⚡ Real-Time Prediction: Enter text and get instant classification

🔐 Git LFS Support: For handling large model files efficiently

🧠 How It Works

User inputs a news article

Text is preprocessed using NLP techniques

The trained ML model predicts Real/Fake

Result is displayed instantly via web UI

📁 Project Structure
dataset/                 # True.csv and Fake.csv
local_fake_news_model/   # Model weights & tokenizer (Git LFS)
app.py                   # Main application
requirements.txt         # Python dependencies
README.md                # Project documentation

🛠 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/vedfasate/REAL-TIME-FAKE-NEWS-DETECTION-USING-MACHINE-LEARNING.git
cd REAL-TIME-FAKE-NEWS-DETECTION-USING-MACHINE-LEARNING

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Install Git LFS & pull model files
git lfs install
git lfs pull

4️⃣ Run the application
python app.py


Then open:

http://localhost:5000      
