import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import os

def train_and_save_model():
    print("Loading data...")
    # Read the dataset
    df = pd.read_csv('data/spam.csv', encoding='latin-1')
    
    # Keep only the necessary columns and rename them
    df = df[['v1', 'v2']]
    df.columns = ['label', 'message']
    
    # Map labels to binary values
    df['label_num'] = df.label.map({'ham': 0, 'spam': 1})
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        df['message'], df['label_num'], test_size=0.2, random_state=42
    )
    
    print("Training model...")
    # Initialize the CountVectorizer
    vectorizer = CountVectorizer(stop_words='english')
    X_train_dtm = vectorizer.fit_transform(X_train)
    
    # Initialize and train the Naive Bayes model
    nb_model = MultinomialNB()
    nb_model.fit(X_train_dtm, y_train)
    
    # Evaluate model
    X_test_dtm = vectorizer.transform(X_test)
    accuracy = nb_model.score(X_test_dtm, y_test)
    print(f"Model trained with accuracy: {accuracy:.4f}")
    
    # Save the model and vectorizer
    os.makedirs('models', exist_ok=True)
    joblib.dump(nb_model, 'models/spam_classifier_model.pkl')
    joblib.dump(vectorizer, 'models/count_vectorizer.pkl')
    print("Model and Vectorizer saved in the 'models/' directory.")

if __name__ == '__main__':
    train_and_save_model()
