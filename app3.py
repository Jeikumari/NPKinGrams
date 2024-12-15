import streamlit as st
import pandas as pd

# Define standard values for 100g samples
standard_values = {
    'Sample': ['Livestock Manure', 'Energy Crops', 'Harvest Remains', 'Food Waste', 'Dairy Product Waste', 'Agro Processing Waste', 'OFMSW', 'Sewage Sludge', 'Yard Trimmings', 'Egg Shells', 'Bread and Bakery waste', 'Weeds', 'Wood chips', 'Wood ash', 'Saw dust', 'Sugar cane bagasse', 'Olive press cake', 'Ground nut press cake', 'Caster press cake', 'Coconut husk', 'Sea weed', 'Algae', 'Water hyacinth', 'Paper waste', 'Fruit pomace', 'Vegetable waste', 'Fabric waste', 'Mushroom compost', 'Vermicast', 'Grape pomace', 'Rice hulls', 'Corn stover', 'Sunflower stalks and seeds', 'Wool waste', 'Nuts shell'],
    'Weight (g)': [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
    'Nitrogen (%)': [1.5, 15, 4.1, 1.42, 3.5, 0.45, 1.43, 2.5, 1.43, 1.2, 1.3, 3.3, 0.15, 0.1, 0.07, 0.3, 1.2, 7.3, 1.5, 0.3, 1.5, 1.5, 1.5, 0.55, 1.15, 1.5, 0.4, 1.1, 1.5, 1.2, 1.9, 1.35, 1.0, 1.5, 0.4],
    'Phosphorus (%)': [0.75, 23, 0.15, 0.45, 0.45, 0.16, 0.46, 1.76, 0.26, 0.4, 0.25, 0.5, 0.04, 1.5, 0.01, 0.1, 0.5, 3, 0.2, 0.1, 0.75, 0.75, 0.6, 0.12, 0.37, 0.5, 0.07, 0.7, 1.5, 0.4, 0.48, 0.48, 0.5, 0.3, 0.07],
    'Potassium (%)': [0.55, 10, 1, 0.97, 0.25, 0.97, 0.76, 0.4, 1.06, 0.1, 0.45, 4.05, 0.15, 3.5, 0.07, 0.5, 1.0, 2.2, 0.5, 0.5, 1.5, 1.5, 1.0, 0.22, 0.57, 1.02, 0.15, 1.3, 0.75, 1.0, 0.81, 1.65, 1.2, 0.5, 0.15]
}

df_standard = pd.DataFrame(standard_values)

# Define function to calculate NPK in grams
def calculate_npk_in_grams(sample, weight):
    standard_sample = df_standard[df_standard['Sample'] == sample].iloc[0]
    npk_values = {
        'Nitrogen (g)': (standard_sample['Nitrogen (%)'] / 100) * weight,
        'Phosphorus (g)': (standard_sample['Phosphorus (%)'] / 100) * weight,
        'Potassium (g)': (standard_sample['Potassium (%)'] / 100) * weight
    }
    return npk_values

# Create Streamlit application
def npk_app():
    st.title("NPK Analysis")
    st.write("Select a sample and enter the weight to get the NPK values in grams.")
    
    sample = st.selectbox("Select Sample", df_standard['Sample'].tolist())
    weight = st.number_input("Enter Weight (g)", min_value=0.0, format="%f")
    
    if st.button("Analyze"):
        npk_values = calculate_npk_in_grams(sample, weight)
        st.write(f"Nitrogen (g): {npk_values['Nitrogen (g)']:.2f}")
        st.write(f"Phosphorus (g): {npk_values['Phosphorus (g)']:.2f}")
        st.write(f"Potassium (g): {npk_values['Potassium (g)']:.2f}")
        
if __name__ == "__main__":
    npk_app()