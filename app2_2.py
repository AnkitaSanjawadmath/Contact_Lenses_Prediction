import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("Lenses2Prediction.pkl", "rb"))

st.title(":blue[Contact Lenses Prediction]")

Age = st.selectbox("Age", ["Young", "Pre-presbyopic","Presbyopic"])
Age_map = {"Pre-presbyopic":0,"Presbyopic":1,"Young":2}
Age=Age_map[Age]

Spectacle_Prescription = st.selectbox("Spectacle_Prescription", ["Myope", "Hypermetrope"])
Spectacle_Prescription = 1 if Spectacle_Prescription == "Myope" else 0

Astigmatic = st.selectbox("Astigmatic", ["No", "Yes"])
Astigmatic = 1 if Astigmatic == "Yes" else 0

Tear_Production = st.selectbox("Tear_Production", ["Reduced", "Normal"])
Tear_Production = 1 if Tear_Production == "Reduced" else 0

if st.button("Predict Contact Lenses"):
    input_data = np.array([[Age,Spectacle_Prescription,Astigmatic,Tear_Production]])
    prediction = model.predict(input_data)
    if prediction==0:
        pred='Multifocal'
    elif prediction==1:
        pred='Scleral Lenses'
    elif prediction==2:
        pred='Soft Contact Lenses'
    else:
        pred='Soft Toric'
    st.success(f"Prediction: the patient should be fitted with {pred}.")
# {'Multifocal':(0), 'Scleral Lenses':(1), 'Soft Contact Lenses': (2), 'Soft Toric':(3)}
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("LensesNewDataset.csv")
# Rule: If tear production is reduced, they can now wear Scleral lenses
df.loc[df['Tear_Production'] == 'Reduced', 'Lenses'] = 'Scleral Lenses'

# Rule: If they have astigmatism but normal tears, they get Soft Toric instead of Hard
df.loc[(df['Astigmatic'] == 'Yes') & (df['Tear_Production'] == 'Normal'), 'Lenses'] = 'Soft Toric'

# Rule: If they are Presbyopic, they get Multifocals
df.loc[df['Age'] == 'Presbyopic', 'Lenses'] = 'Multifocal'
# Create the figure and plot
fig = plt.figure(figsize=(15, 5))
# Plot 1: Target Class Distribution (The 'Lenses' column)
plt.subplot(1, 2, 1)
sns.countplot(x='Lenses', data=df,  hue='Lenses',legend=False)
plt.title('Distribution of Lens Recommendations')
plt.tight_layout()
# 4. Display the plot in Streamlit
st.pyplot(fig)
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://sandiavision.com/wp-content/uploads/2024/04/SandiaVisionClinic-Contactlenses-Hero.jpg");
    background-size: cover;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("""
    <style>
    /* Target all standard text elements */
    p, div, label {
        color: #FF4B4B;
    }
    </style>
    """, unsafe_allow_html=True)