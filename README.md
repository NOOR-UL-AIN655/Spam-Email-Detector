# 📧 Spam Email Detector — NLP & Machine Learning

An end-to-end **Spam Email Detection** project that uses **Natural Language Processing (NLP)** and **Machine Learning** to classify emails as **Spam** or **Ham (Legitimate)**.

The project includes data exploration, text preprocessing, TF-IDF feature extraction, machine learning classification, model evaluation, and a Streamlit web application for real-time predictions.

---

##  Project Overview

Spam emails are unwanted or potentially harmful messages that can contain misleading offers, advertisements, or malicious links.

This project builds a machine learning system that analyzes the text of an email and predicts whether it is:

*  **Spam**
*  **Ham**

### Project Workflow

**Email Text → Text Preprocessing → TF-IDF → Machine Learning Model → Spam/Ham Prediction**

---

##  Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Scikit-learn**
* **TF-IDF**
* **Multinomial Naive Bayes**
* **Joblib**
* **Streamlit**

---

##  Project Pipeline

### 1. Data Collection

The project uses a Kaggle email dataset containing labeled email messages.

The dataset contains two main fields:

* `text` — email content
* `spam` — target label

---

### 2. Data Cleaning

The dataset was checked for:

* Missing values
* Invalid labels
* Duplicate records
* Unnecessary columns

Invalid labels and duplicate records were removed before model training.

---

### 3. Exploratory Data Analysis (EDA)

Several exploratory analyses were performed:

* Spam vs Ham distribution
* Email length analysis
* Average email length comparison
* Boxplot of email lengths
* Inspection of sample Spam and Ham emails
* Missing-value and duplicate-value checks

EDA helped understand the characteristics and distribution of the dataset before applying machine learning.

---

##  Natural Language Processing (NLP)

Since emails are text data, they cannot be directly provided to a traditional machine learning classifier.

### Text Preprocessing

Email text was cleaned by:

* Converting text to lowercase
* Removing punctuation and special characters
* Removing unnecessary spaces

### TF-IDF

**Term Frequency–Inverse Document Frequency (TF-IDF)** was used to convert email text into numerical features.

This allows the machine learning model to learn patterns from the words appearing in emails.

---

##  Machine Learning

Two classification algorithms were evaluated:

### 1. Logistic Regression

Accuracy:

**98.07%**

### 2. Multinomial Naive Bayes

Accuracy:

**98.33%**

Multinomial Naive Bayes achieved the better test accuracy and was selected as the main model for the application.

---

##  Model Evaluation

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

### Final Model

**Multinomial Naive Bayes**

**Test Accuracy: 98.33%**

For the Spam class, the model achieved approximately:

* Precision: **1.00**
* Recall: **0.93**
* F1-score: **0.96**

---

##  Streamlit Web Application

A Streamlit interface was created so users can enter an email and receive a real-time prediction.

### Example

**Input:**

> Congratulations! You have won a $10,000 cash prize. Click here to claim your reward now!

**Output:**

 **SPAM EMAIL**

The application loads the trained model and TF-IDF vectorizer instead of retraining the model every time a prediction is made.

---

## Project Structure

```text
Spam-Email-Detector/
│
├── app.py
├── spam_email_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
└── README.md
```

### File Description

| File                   | Purpose                               |
| ---------------------- | ------------------------------------- |
| `app.py`               | Streamlit web application             |
| `spam_email_model.pkl` | Trained Multinomial Naive Bayes model |
| `tfidf_vectorizer.pkl` | Saved TF-IDF vectorizer               |
| `requirements.txt`     | Required Python libraries             |
| `README.md`            | Project documentation                 |

---

## How to Run Locally

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Spam-Email-Detector
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## Key Learning Outcomes

Through this project, I implemented an end-to-end NLP and machine learning workflow including:

* Data cleaning
* Exploratory Data Analysis
* Text preprocessing
* TF-IDF feature extraction
* Machine learning classification
* Model comparison
* Performance evaluation
* Model serialization
* Real-time prediction
* Streamlit application development

---

## Future Improvements

Possible future improvements include:

* Adding word and character n-grams
* Handling email-specific features such as URLs and HTML content
* Improving text preprocessing
* Testing additional machine learning algorithms
* Adding prediction confidence/probability
* Deploying the application publicly

---

## Author

**Noor-Ul-Ain**

Artificial Intelligence Student | Machine Learning & Data Analytics

---

##  Live Demo

Try the deployed Spam Email Detector:

 [Open Live App](https://spam-email-detector-kxkzqzvgkxnguzj4rc3evz.streamlit.app/)
