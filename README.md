

---

# SMS Spam Detection Web Application

This web application is built with Flask and is designed to classify SMS messages as either **Spam** or **Ham** (not spam). It also allows users to provide feedback, which is stored and viewable in an admin section.

---

## 📋 Features

**What does this application do?**
- **SMS Spam Detection**: Users can enter an SMS message and receive a prediction on whether it is spam or not.
- **User Feedback**: Users can submit feedback on the application, which is saved in a text file and viewable in the admin section.
- **Flash Messages**: The app provides flash messages for user notifications, such as warnings for overly long messages or confirmation after submitting feedback.
- **Character Counter**: Displays a real-time character count for the input message, turning red if it exceeds the 160-character limit.
- **Admin Feedback View**: Allows admins to view all collected feedback through a dedicated route.

## 🛠️ Tech Stack

**What technologies are used in this project?**
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning Model**: Pickled model for spam detection (requires `scikit-learn`)
- **Storage**: Feedback saved in a `feedback.txt` file

## ⚙️ Prerequisites

**What do you need before setting up this project?**
- **Python 3.6+**
- **Virtual environment (optional but recommended)**

### Required Python Libraries

Install these dependencies using `pip`:

```bash
pip install -r requirements.txt
```

Where `requirements.txt` includes:
- `flask`
- `nltk`
- `scikit-learn`

### NLTK Data Download

This app uses NLTK for natural language processing. You’ll need to download some datasets:

```python
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
```

## 🚀 Setup

**How to install and run the application locally:**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ashok-Data-Explore/SMS-Spam-Detection-Web-Application
   cd SMS-Spam-Detection-Web-Application
   ```

2. **Set Up Virtual Environment** (Optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Flask Environment**:
   - Set `FLASK_APP` environment variable:
     ```bash
     export FLASK_APP=app.py  # For Windows use `set FLASK_APP=app.py`
     ```
   - Set `FLASK_ENV` for development:
     ```bash
     export FLASK_ENV=development  # For Windows use `set FLASK_ENV=development`
     ```

5. **Run the Application**:
   ```bash
   flask run
   ```

6. **Access the Application**:
   - Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 🔍 Usage

### SMS Spam Detection

1. **Enter Message**: Type an SMS message in the input box.
2. **Get Prediction**: Click **Predict** to classify the message as **Spam** or **Ham**.
3. **Display Duration**: The result will display for 5 seconds and then automatically disappear.

### Character Count and Limits

- **Real-time Count**: The character count updates as you type.
- **Exceeds Limit**: If the message exceeds 160 characters, the counter turns red.
- **Warning Message**: Messages over 160 characters are not processed, and a flash message warns the user.

### Feedback Submission

1. **Submit Feedback**: Enter your feedback in the "Your Feedback" section.
2. **Confirmation Message**: After clicking **Submit Feedback**, a confirmation message will appear, and your feedback will be saved to `feedback.txt`.



## 📁 File Structure

```
.
├── app.py                # Main Flask application
├── feedback.txt          # Stores user feedback
├── requirements.txt      # Python dependencies
├── templates
│   └── index.html        # Main HTML template
├── static
    └── styles.css        # Custom CSS file

```



## 📜 License

This project is licensed under the MIT License.

---
