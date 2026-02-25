
---

## ✅ Project Goals

- Preprocess and clean raw email text.
- Train multiple ML models to classify messages.
- Evaluate model performance.
- Create insightful visualizations.
- Tell a meaningful story using data.
- Add interactive plots for better user engagement.

---

## 🧹 Review 1: Data Preprocessing & Summary Statistics

### 📌 Tasks Completed

- Loaded and explored the dataset (`spam.csv`)
- Removed null or redundant entries
- Engineered key features (`label_num`, `message_length`)
- Exported cleaned data (`cleaned_data.csv`)

### 📊 Initial Visualizations

- **Countplot** of ham vs spam labels
- **Boxplot** comparing message lengths
- **WordClouds** for spam and ham messages
- **Summary Statistics** by label group

📓 Notebook: `notebooks/data_preprocessing_and_visualization.ipynb`

---

## 📈 Review 2: Visualizations, Interactivity & Storytelling

### 📊 Key Visualizations

- **Bar Plot** of spam vs ham messages
- **Boxplot** of message lengths by label
- **Histogram** of message length distribution
- **Pie Chart** of label proportions
- **WordClouds** showing common words in spam/ham

### 🌐 Interactivity

- **Interactive Scatter Plot**:
  - Built using `Plotly`
  - Shows relationship between `message_length` and `label`
  - Hover to view actual email text
  - 📁 Saved as: `interactive/interactive_plot.html`

### 📓 Notebook

- `notebooks/review2_visualizations_and_storytelling.ipynb`

---

## 📌 Technologies Used

| Tool/Library   | Purpose                             |
|----------------|-------------------------------------|
| Python         | Main language                       |
| Pandas         | Data loading and manipulation       |
| Seaborn/Matplotlib | Static data visualizations      |
| Plotly         | Interactive visualizations          |
| WordCloud      | Text visualization                  |
| Scikit-learn   | Future modeling and evaluation      |

---

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/PiYuSh7-2/spam-email-detection.git


### Thankyou'll 
