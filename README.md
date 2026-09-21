# Contact_Lenses_Prediction
A medical classification model identifying patient suitability for contact lenses using a Decision Tree Classifier on the classic UCI Lenses dataset. Modernized with clinical rules for soft toric, scleral, and multifocal prescriptions, it functions as an automated clinical decision tool.
# Contact Lenses Prediction Model

## 📖 Project Overview

### 1. Introduction to Prediction Model
The Lenses Dataset is a classic classification problem originally sourced from the UCI Machine Learning Repository. It consists of 24 clinical case studies tracking patient eye health. The data utilizes key categorical attributes—**Age**, **Spectacle Prescription**, **Astigmatism**, and **Tear Production Rate**—to accurately determine the appropriate medical intervention.

### 2. Real-World Application
In modern clinical settings, this model functions as a **Clinical Decision Support System (CDSS)** across several domains:
* **Optometry Automation:** Assisting junior practitioners and technicians in quickly screening patients for lens suitability.
* **Medical Triage:** Efficiently identifying high-risk patients who require specific lens types.
* **Retail & E-commerce:** Powering online vision assessment tools that suggest specific contact lens products based on a user's existing prescription and current eye conditions.

### 3. Problem Statement
Manual classification of contact lens types is highly subjective, prone to human error, and varies between individual practitioners. Furthermore, identifying the complex interplay between multiple physiological factors (like tear production combined with astigmatism) is difficult to scale. A consistent, algorithmic approach is required to map patient attributes to the correct lens type to ensure patient safety and comfort.

### 4. Objective of the Project
* **Automate Classification:** Correctly categorize patients into four modernized classes: *Soft Toric Lenses, Soft Contact Lenses, Scleral Lenses,* or *Multifocal*.
* **Extract Medical Rules:** Identify the most significant "Root" factor in eye health (e.g., determining which physiological attribute carries the most critical weight).
* **Minimize Misdiagnosis:** Achieve 100% accuracy on the provided 24-case "gold standard" training subset to prevent recommending a lens type that causes physical discomfort or medical risk.
* **Algorithm Choice:** **Supervised Machine Learning – Decision Tree Classifier**, selected because the target variable (*Lenses*) is categorical.

---

## 🔄 Dataset Modernization Layer

The original UCI Lenses dataset relies on outdated prescription patterns (which heavily defaulted patients to "No Lenses" or uncomfortable "Hard Lenses"). This project modernizes the data targeting modern optometry solutions using the following rules:

1. **Scleral Alternative:** Patients with *Reduced Tear Production* who previously couldn't wear lenses are mapped to modern, high-moisture **Scleral Lenses**.
2. **Soft Toric Upgrade:** Patients with *Astigmatism* but *Normal Tears* are upgraded to **Soft Toric Lenses** instead of rigid hard lenses.
3. **Multifocal Integration:** Aging patients categorized as *Presbyopic* are correctly assigned **Multifocal Lenses**.

### Modernization Logic Applied:
```python
# Rule 1: Reduced tear production accommodates Scleral lenses
df.loc[df['Tear_Production'] == 'Reduced', 'Lenses'] = 'Scleral Lenses'

# Rule 2: Astigmatism with normal tears upgrades to Soft Toric
df.loc[(df['Astigmatic'] == 'Yes') & (df['Tear_Production'] == 'Normal'), 'Lenses'] = 'Soft Toric'

# Rule 3: Presbyopic age classifications use Multifocals
df.loc[df['Age'] == 'Presbyopic', 'Lenses'] = 'Multifocal'
```

---

## 🛠️ Repository Structure

```text
├── Dataset.csv             # Dataset to train the model
├── lenses_Prediction.ipynb # Jupyter Notebook containing data modernization, EDA, and Decision Tree training
├── Model.pkl               # Serialized Decision Tree Classifier model file
└── Dashboard.py            # Streamlit application script providing the interactive UI dashboard
```

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com
cd your-repo-name
```

### 2. Initialize Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On Mac/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install streamlit scikit-learn pandas numpy
```

---

## 💻 Running the Dashboard

To launch the interactive clinical decision support application, run:
```bash
streamlit run app.py
```

### Under the Hood: Loading the Classification Model
The application loads the serialized decision tree using the following syntax to map user inputs to predictions:
```python
import pickle

# Load the trained Decision Tree Classifier
model = pickle.load(open("Model.pkl", "rb")))

# The model evaluates inputs to predict one of the four categorical lens classifications
# prediction = classifier_model.predict([[age_encoded, prescription_encoded, astigmatic_encoded, tear_encoded]])
```
