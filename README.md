# 📧 Spam Email Detection System

An NLP-powered machine learning application that classifies messages as **Spam** or **Not Spam** using **TF-IDF Vectorization** and **Multinomial Naive Bayes**. The project includes a user-friendly Streamlit web interface for real-time predictions.

---

## 🚀 Live Demo

**Deployed Application:**
[Add your Streamlit URL here]

---

## 📸 Screenshots

### Home Page

![Home Page](images/home-page.png)

### Spam Detection Example

![Spam Prediction](images/spam-prediction.png)

### Not Spam Detection Example

![Not Spam Prediction](images/not-spam-prediction.png)

---

## 📖 Project Overview

Spam emails and messages are a common problem in digital communication. This project uses **Natural Language Processing (NLP)** techniques to automatically classify messages into:

* 🚨 Spam
* ✅ Not Spam

The application processes text data, extracts meaningful features using TF-IDF, and uses a machine learning classifier to predict the category.

---

## ✨ Features

* Text preprocessing and cleaning
* TF-IDF feature extraction
* Multinomial Naive Bayes classifier
* Real-time predictions
* Confidence score display
* Interactive Streamlit web interface
* Model persistence using Joblib

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Libraries & Frameworks

* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib

### Machine Learning Concepts

* Natural Language Processing (NLP)
* Text Preprocessing
* TF-IDF Vectorization
* Supervised Learning
* Text Classification

---

## 📂 Project Structure

```text
spam-email-detector/
│
├── app.py
├── train_model.py
├── spam.csv
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
└── images/
    ├── home-page.png
    ├── spam-prediction.png
    └── not-spam-prediction.png
```

---

## ⚙️ Installation & Setup

### Clone Repository

```bash
git clone https://github.com/your-username/spam-email-detector.git
cd spam-email-detector
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

**Windows**

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🏋️ Model Training

Train the machine learning model:

```bash
python train_model.py
```

Expected output:

```text
Accuracy: 96.59%
Model saved successfully!
```

This generates:

```text
model.pkl
vectorizer.pkl
```

---

## ▶️ Run Application

Start the Streamlit app:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 🧪 Sample Test Cases

### Spam Message

```text
Congratulations! You have won ₹50,000.
Click here to claim your reward.
```

Prediction:

```text
🚨 SPAM
```

### Normal Message

```text
Hey Bhavya,
Let's meet tomorrow at 10 AM.
```

Prediction:

```text
✅ NOT SPAM
```

---

## 📊 Model Performance

| Metric             | Score                   |
| ------------------ | ----------------------- |
| Accuracy           | 96.59%                  |
| Algorithm          | Multinomial Naive Bayes |
| Feature Extraction | TF-IDF                  |

---

## 🎯 Learning Outcomes

Through this project, I gained hands-on experience in:

* Natural Language Processing (NLP)
* Text Classification
* Feature Engineering
* Machine Learning Model Training
* Model Evaluation
* Streamlit Deployment
* GitHub Project Management

---

## 🔮 Future Enhancements

* Email phishing detection
* Multi-category email classification
* Gmail integration
* Chrome extension support
* Transformer-based models (BERT/DistilBERT)
* Email summarization using LLMs

---

## 👨‍💻 Author

**Bhavya Teja Penke**

GitHub: https://github.com/Bhavyateja04

LinkedIn: https://linkedin.com/in/bhavya1220

Email: [bhavyapenke@gmail.com](mailto:bhavyapenke@gmail.com)

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
