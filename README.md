# Real-Time Fake News Detection using Machine Learning

This project is a Machine Learning application designed to detect and classify news articles as either **Real** or **Fake**. It utilizes Natural Language Processing (NLP) and a fine-tuned model to provide real-time predictions.

## 🚀 Features
* **Machine Learning Model:** Uses a fine-tuned model (stored via Git LFS).
* **Dataset:** Trained on a comprehensive dataset of labeled news articles.
* **Web Interface:** Built with Flask/Streamlit for real-time user interaction.

## 📁 Project Structure
* `dataset/`: Contains the `True.csv` and `Fake.csv` data files.
* `local_fake_news_model/`: Contains the model weights and tokenizer.
* `app.py`: The main application entry point.

## 🛠️ Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/vedfasate/REAL-TIME-FAKE-NEWS-DETECTION-USING-MACHINE-LEARNING.git](https://github.com/vedfasate/REAL-TIME-FAKE-NEWS-DETECTION-USING-MACHINE-LEARNING.git)

 2.Install dependencies:
 Bash
 pip install -r requirements.txt

 3.Install Git LFS: (Required to download the large model files)
 Bash
 git lfs pull

 4.Run the application:
 Bash
 python app.py
