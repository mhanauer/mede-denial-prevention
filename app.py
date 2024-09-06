import streamlit as st
import pandas as pd
import random

# Function to generate random data
def generate_data(num_rows):
    claim_ids = [random.randint(1000, 9999) for _ in range(num_rows)]
    cpt_codes = random.choices(['99213', '80050', '99214', '99381', '99215', '85025', '93000'], k=num_rows)
    diagnoses = random.choices(['Hypertension', 'Diabetes', 'Asthma'], k=num_rows)
    predictions = [random.uniform(0, 100) for _ in range(num_rows)]  # Generate random percentages
    
    data = {
        'Claim ID': claim_ids,
        'CPT Code': cpt_codes,
        'Diagnosis': diagnoses,
        'Claim Denial Prediction (%)': [round(p, 2) for p in predictions]  # Round to 2 decimal places
    }
    
    return pd.DataFrame(data)

# Generate 50 rows of data
df = generate_data(50)

# Sort the DataFrame by "Claim Denial Prediction (%)" (highest percentage first)
df_sorted = df.sort_values(by='Claim Denial Prediction (%)', ascending=False)

# Title of the app
st.title('Claim Denial Prediction Table (Sorted by Highest Likelihood of Denial)')
st.markdown("""This demo showcases Mede's denial prediction tool, helping providers assess the likelihood of a claim being denied before submission, thus reducing denial risks. """")
# Display the DataFrame
st.write('Displaying 50 rows of claim denial prediction data, sorted by highest likelihood of denial:')
st.dataframe(df_sorted)
