import pandas as pd
import string
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

df = pd.read_csv(
    "spam.csv",
    sep="\t",
    names=["label", "text"]
)

def clean_text(text):
    text = str(text).lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

df["text"] = df["text"].apply(clean_text)

X = df["text"]
y = df["label"]

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

from sklearn.metrics import classification_report

print("Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))

joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model saved successfully!")