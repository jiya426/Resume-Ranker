from flask import Flask, render_template, request, send_file
import pandas as pd
import os
import PyPDF2
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

# Extract text
def extract_text(file):
    text = ""
    reader = PyPDF2.PdfReader(file)
    for page in reader.pages:
        text += page.extract_text()
    return text

# Preprocess
def preprocess(text):
    doc = nlp(text.lower())
    return " ".join([t.lemma_ for t in doc if not t.is_stop and not t.is_punct])

@app.route("/", methods=["GET", "POST"])
def index():
    results = None

    if request.method == "POST":
        jd = request.form["jd"]
        files = request.files.getlist("resumes")

        resumes = []
        names = []

        for file in files:
            text = extract_text(file)
            resumes.append(preprocess(text))
            names.append(file.filename)

        jd = preprocess(jd)

        vectorizer = TfidfVectorizer()
        tfidf = vectorizer.fit_transform([jd] + resumes)

        scores = cosine_similarity(tfidf[0:1], tfidf[1:]).flatten()

        df = pd.DataFrame({
            "Resume": names,
            "Score": scores * 100
        })

        df = df.sort_values(by="Score", ascending=False)
        df["Rank"] = range(1, len(df)+1)

        df.to_csv("resume_ranking.csv", index=False)

        results = df.to_html(index=False)

    return render_template("index.html", results=results)
@app.route("/download")
def download_file():
    import os
    path = os.path.join(os.getcwd(), "resume_ranking.csv")
    
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    else:
        return "File not found. Please rank resumes first!"
if __name__ == "__main__":
    app.run(debug=True)