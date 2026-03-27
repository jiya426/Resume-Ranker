# 📄 AI-Powered Resume Ranker

## 🚀 Project Overview

The **AI-Powered Resume Ranker** is a Machine Learning + NLP-based web application that automatically ranks resumes based on their relevance to a given job description.

It helps recruiters quickly identify the most suitable candidates by analyzing resumes and comparing them with job requirements.

---

## 🧠 Technologies Used

* **Python**
* **SpaCy (NLP preprocessing)**
* **Scikit-learn (TF-IDF, Cosine Similarity)**
* **Flask (Web Framework)**
* **HTML & CSS (Frontend UI)**
* **PyPDF2 (PDF text extraction)**

---

## ⚙️ How It Works

1. **Extract Text**

   * Extracts text from uploaded PDF resumes using PyPDF2

2. **Text Preprocessing**

   * Converts text to lowercase
   * Removes stopwords and punctuation
   * Applies lemmatization using SpaCy

3. **Feature Extraction**

   * Uses TF-IDF to convert text into numerical vectors

4. **Similarity Calculation**

   * Uses Cosine Similarity to compare resumes with job description

5. **Ranking**

   * Assigns scores and ranks resumes based on similarity

---

## 🎯 Features

✔ Upload multiple resumes (PDF)
✔ Enter custom job description
✔ Automatic resume ranking
✔ Displays score and rank
✔ Download results as CSV
✔ Clean and user-friendly interface

---

## 📁 Project Structure

```
Resume-Ranker/
│
├── app.py
├── notebook.ipynb
├── resume_ranking.csv
├── resumes/
├── templates/
│   └── index.html
```

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```
git clone https://github.com/your-username/Resume-Ranker.git
cd Resume-Ranker
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

*(or manually install: spacy, sklearn, flask, pandas, PyPDF2)*

### 3. Download SpaCy Model

```
python -m spacy download en_core_web_sm
```

### 4. Run the Flask App

```
python app.py
```

### 5. Open in Browser

```
http://127.0.0.1:5000/
```

---

## 📊 Sample Output

| Resume      | Score | Rank |
| ----------- | ----- | ---- |
| resume1.pdf | 85.2  | 1    |
| resume2.pdf | 72.5  | 2    |

---

## 🧠 Algorithms Used

* **TF-IDF (Term Frequency - Inverse Document Frequency)**
* **Cosine Similarity**

---

## 💡 Use Cases

* Recruitment automation
* Resume screening
* HR analytics
* Candidate shortlisting

---

## 🎓 Learning Outcomes

* Applied NLP techniques in real-world problem
* Built end-to-end ML project
* Developed web app using Flask
* Learned text similarity and ranking

---

## 🔮 Future Improvements

* Skill extraction & highlighting
* Resume keyword matching visualization
* Support for multiple job roles
* Use of advanced models like BERT

---

## 📌 Conclusion

This project demonstrates how Machine Learning and NLP can automate the recruitment process by efficiently ranking resumes based on job requirements, saving time and improving hiring decisions.

---

## 👨‍💻 Author

**Jiya Jain**

---

