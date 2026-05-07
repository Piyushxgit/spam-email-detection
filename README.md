# 🚫 Spam Email Detection Web App


A comprehensive Machine Learning project to classify text messages or emails as **"Spam"** (unwanted/malicious) or **"Ham"** (legitimate). This project includes raw data preprocessing, exploratory data analysis via interactive visualizations, and a fully functional Streamlit web application powered by a custom-trained **Scikit-Learn Naive Bayes Classifier**.

---

## ✅ Project Overview & Goals

The primary goal of this application is to serve as both an educational Data Science toolkit and a practical, user-friendly utility for detecting spam.
- Preprocess and clean raw text data.
- Explore characteristics like message length and word frequency.
- Train and evaluate traditional Machine Learning models (`MultinomialNB`).
- Expose the trained model via a **Streamlit Web Dashboard**.
- Ensure non-technical users can interact easily using automation scripts.

---

## 🚀 Quick Start (Running the App)

We have provided simple, clickable scripts so anyone can run the Web App instantly without understanding the underlying code.

**On Windows:**
Simply double-click on `run_app.bat` inside the project folder. This will automatically install requirements, train the ML model, and open the app in your browser window.

**On Mac / Linux:**
Open your terminal, navigate to the folder, and run:
```bash
<<<<<<< Updated upstream
git clone https://github.com/PiYuSh7-2/spam-email-detection.git


### Thankyou'll 
=======
bash run_app.sh
```

---

## 📦 Build & Deployment (For Developers)

If you are a developer looking to explore the code, modify the data, or deploy this project to a server, follow these steps.

### Local Development Setup:
1. Clone the repository:
   ```bash
   git clone https://github.com/PiYuSh7-2/spam-email-detection.git
   cd spam-email-detection
   ```
2. Create and activate a Python virtual environment:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Train the Machine Learning Model. (This forces the code to read the CSV, extract features, and save `.pkl` files):
   ```bash
   python train_model.py
   ```
5. Launch the Streamlit application natively in dev mode:
   ```bash
   streamlit run app.py
   ```

### Production Deployment Notes:
To deploy this application publicly (e.g., via Heroku, Render, or Streamlit Cloud):
- The `requirements.txt` file is already optimized for standard deployment environments.
- Ensure the trained objects (`models/spam_classifier_model.pkl` and `models/count_vectorizer.pkl`) are committed to your repository OR ensure `train_model.py` is configured as a pre-build step before the server boots up.

---

## 📌 Tech Stack & Architecture

| Component | Tool/Library | Purpose |
|---|---|---|
| **Core Logic** | Python | Main programming language |
| **Data Handling** | Pandas | Data loading, manipulation, and CSV parsing |
| **Machine Learning** | Scikit-learn | Features extraction (`CountVectorizer`), Classification (`MultinomialNB`) |
| **Front-End/UI** | Streamlit | Rapid Web Application interface |
| **Visualizations** | Seaborn, Matplotlib, Plotly | Static and interactive charts |
| **Text Viz** | WordCloud | Highlighting common spam vs ham vocabulary |

**Architectural Flow:**
`app.py` acts as the frontend controller. It loads the pre-trained `.pkl` artifacts (saved locally by `train_model.py`). When a user types text in the UI, it passes the text through the `CountVectorizer` object to create a feature array, which is then fed to the `MultinomialNB` model object to predict `1` (Spam) or `0` (Ham).

---

## 📂 Project Structure Overview

```text
spam-email-detection/
│
├── data/
│   ├── spam.csv                 # Raw dataset
│   └── cleaned_data.csv         # Processed dataset (generated via notebooks)
│
├── models/                      # Generated automatically by train_model.py
│   ├── count_vectorizer.pkl     # Saved feature extractor
│   └── spam_classifier_model.pkl# Saved Naive Bayes model
│
├── notebooks/                   # Jupyter exploratory notebooks
│   ├── data_preprocessing_and_visualization.ipynb
│   └── visualizations_and_storytelling.ipynb
│
├── interactive/                 # Exported interactive dashboard files
│   └── interactive_plot.html
│
├── app.py                       # Main Streamlit web application
├── train_model.py               # Script to train ML model & save .pkl files
├── run_app.bat                  # Automation script for Windows
├── run_app.sh                   # Automation script for Mac/Linux
├── requirements.txt             # Dependency definitions
└── README.md                    # Project documentation
```

---

## 🧪 Testing

*Presently, there is no formal testing suite (e.g., PyTest) configured for the front-end components.* 
However, you can observe the model's performance metrics directly on training.
When executing `python train_model.py`, the terminal will log the **Test Set Accuracy Metrics**. The baseline Naive Bayes model achieves `~98.5%` accuracy.

To run informal tests on the ML pipeline:
```bash
python train_model.py
```

---

## 🤝 Contribution Guidelines & Code of Conduct

1. **Fork the Repository** and clone it locally.
2. **Create a Feature Branch** (`git checkout -b feature/AmazingFeature`).
3. Commit your changes. Focus on clear, concise, descriptive commit messages.
4. **Push to the Branch** (`git push origin feature/AmazingFeature`).
5. Open a **Pull Request** referencing the issue you are fixing.

**Code of Conduct:**
Please maintain a friendly and collaborative environment. Be respectful when creating issues or participating in Pull Request reviews.

---

## 📝 Known Issues & FAQ

**Q: "I am getting `Command 'python' not found` when running the `.sh` script on Linux."**
*Fix:* You may have `python3` installed rather than `python`. Open `run_app.sh` in a text editor and change occurrences of `python` to `python3`.

**Q: "The app crashes on startup saying `FileNotFoundError: No such file or directory: 'models/spam_classifier_model.pkl'`."**
*Fix:* The app cannot find the trained model. Ensure you have run python `train_model.py` at least once before executing `streamlit run app.py`. (The `.bat`/`.sh` scripts handle this automatically).

**Q: Does this filter catch modern phishing links?**
*Fix:* The current dataset is heavily based on older SMS spam and short promotional emails. Highly sophisticated, context-aware modern phishing emails may slip through.

---

## 🔄 Migration Note
**v2.0 (Current):** The project has migrated from simply being a collection of Jupyter Notebooks for Exploratory Data Analysis into a fully deployed standalone Streamlit Web Application using saved persistent Scikit-Learn `.pkl` model artifacts.

---

### Authors & Licensing
Built and maintained by **Piyushxgit** & Contributors. 

*Thank you for exploring!*
>>>>>>> Stashed changes
