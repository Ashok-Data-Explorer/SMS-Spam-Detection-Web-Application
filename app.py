from flask import Flask, request, render_template, flash, redirect
import pickle
import re
import logging
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

# Load the model and vectorizer
try:
    with open('best_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('vectorizer.pkl', 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
except Exception as e:
    model, vectorizer = None, None
    logging.error(f"Error loading model or vectorizer: {e}")

lemmatizer = WordNetLemmatizer()

# Preprocessing function
def lemmatizing(content):
    content = re.sub(r'http\S+|www\S+|https\S+', '', content, flags=re.MULTILINE)
    content = re.sub(r'@\w+', '', content)
    content = re.sub('[^a-zA-Z]', ' ', content)
    content = content.lower()
    content = content.split()
    content = [lemmatizer.lemmatize(word) for word in content if word not in stopwords.words('english')]
    return ' '.join(content)

@app.route('/')
def home():
    return render_template('index.html', prediction_text=None)

@app.route('/predict', methods=['POST'])
def predict():
    if not model or not vectorizer:
        flash("Model or vectorizer not loaded. Please contact the administrator.", "error")
        return redirect('/')

    if request.method == 'POST':
        message = request.form['message']

        # Check for empty message
        if not message.strip():
            flash("Please enter a message to predict.", "warning")
            return redirect('/')

        # Check if message exceeds 160 characters
        if len(message) > 160:
            flash("The message is too long (more than 160 characters). Please shorten it and try again.", "warning")
            return redirect('/')

        # Preprocess and predict
        processed_message = lemmatizing(message)
        message_vector = vectorizer.transform([processed_message])
        prediction = model.predict(message_vector)[0]
        label = "Spam" if prediction == 1 else "Ham"
        
        # Set prediction text based on the result
        prediction_text = f"Predicted Label: {label}"
        
        return render_template('index.html', prediction_text=prediction_text)

@app.route('/feedback', methods=['POST'])
def feedback():
    feedback_text = request.form['feedback']

    # Log the feedback in the console (optional)
    logging.info(f"User feedback: {feedback_text}")

    # Save feedback to a text file
    with open("feedback.txt", "a") as feedback_file:
        feedback_file.write(f"{feedback_text}\n---\n")  # Separate feedback entries with a line

    # Flash message to thank the user
    flash("Thank you for your feedback!", "success")
    return redirect('/')

@app.route('/admin/feedback')
def view_feedback():
    # Read all feedback from the file
    try:
        with open("feedback.txt", "r") as feedback_file:
            feedback_content = feedback_file.read()
        # Display feedback in HTML format
        return f"<h1>User Feedback</h1><pre>{feedback_content}</pre>"
    except FileNotFoundError:
        return "<h1>User Feedback</h1><p>No feedback has been submitted yet.</p>"

if __name__ == "__main__":
    app.run(debug=True)
