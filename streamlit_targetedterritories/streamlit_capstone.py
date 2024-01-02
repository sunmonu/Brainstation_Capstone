### import libraries
import pandas as pd
import streamlit as st
import joblib

#######################################################################################################################################
### DATA LOADING

### A. define function to load data
@st.cache_data # <- add decorators after tried running the load multiple times
def load_data(path, num_rows=None, encoding='utf-8'):
    df = pd.read_csv(path, nrows=num_rows, encoding=encoding)
    return df

# B. Load data
pop_age_sex_path = "data/PopulationbyAgeandSexCounties.csv"
pop_race_path = "data/PopulationbyRaceCounties.csv"
target_data_path = "data/target.csv"
debt_data_path = "data/household-debt-by-county.csv"
pred_df_path = "data/streamlit_data_TargetedTerritories.csv"

pop_age_sex = load_data(pop_age_sex_path, 50000,encoding='ISO-8859-1')
pop_race = load_data(pop_race_path, 50000,encoding='ISO-8859-1')
target_data = load_data(target_data_path,50000,encoding='ISO-8859-1')
debt_data = load_data(debt_data_path,50000,encoding='ISO-8859-1')
pred_df = load_data(pred_df_path,50000,encoding='ISO-8859-1')




# Main header
st.title('Targeted Territories')
st.subheader("Leveraging Data Science for Store Placement Optimization")
# Introductory text
st.write("""
In this project, we utilize advanced data science techniques to optimize Target store placements. Our methodology includes:

1. **Data Integration:** We combined various demographic datasets with Target store location information, creating an integrated data pool for in-depth analysis.
2. **Predictive Analysis:** We applied machine learning models, including logistic regression for predicting store success and KMeans clustering for market segmentation.

These approaches enable us to make strategic store placement decisions and effectively address the key question: "Where should the next Target store be located?
""")


#Video Presentation
st.subheader("Watch Video Presentation")

link = '[Targeted Territories: Leveraging Data Science for Optimized Store Placement 👩‍💻 - Watch Video](https://www.loom.com/share/fb3c200a0b774f7f9b0202e8de9d1adc)'

st.markdown(link, unsafe_allow_html=True)


def analyze_prediction(row):
    if row['isTarget'] == 1 and row['Predictions'] == 1:
        return "The demographics are ideal for a Target, and there is already a Target here."
    elif row['isTarget'] == 0 and row['Predictions'] == 1:
        return "There is no Target here, but due to the demographics, this would be a good location."
    elif row['isTarget'] == 1 and row['Predictions'] == 0:
        return "The demographics are not ideal for a Target, but there is a Target here."
    elif row['isTarget'] == 0 and row['Predictions'] == 0:
        return "The demographics are not great for a Target, and there is no Target here."

def main():
    st.title("Target Store Predictor")

    st.write("""

This tool allows you to select a county and uses predictive analytics to determine if it's a suitable location for a new Target store.

1. **Select a County:** Choose a county from the dropdown. The app handles counties with the same name in different states for accurate analysis.
2. **Get Predictions:**  Once a county is selected, the app evaluates its viability for a Target store based on demographic and existing store data.
3. **Insightful Results:** Receive immediate feedback on whether the selected county is a promising location for a Target store, supporting informed decision-making.

Explore the tool to understand the potential of various counties for new Target store openings.


""")

    # Allow user to select a county name
    county_name = st.selectbox('Select a County Name', pred_df['County'].unique())

    if county_name:
        # Filter data for the selected county
        selected_data = pred_df[pred_df['County'] == county_name]

        # Run analysis
        selected_data['Analysis_Result'] = selected_data.apply(analyze_prediction, axis=1)

        # Display results for the selected county
        st.write(selected_data.loc[:,['State','Analysis_Result']])

if __name__ == "__main__":
    main()


# The Datasets
st.header('Data Overview')
st.write("""
Please note that all datasets presented here are in their raw, original form. 
For the purposes of our analysis, these datasets underwent a thorough process of cleaning, manipulation, and merging to ensure accuracy and relevance. 
The data was cleaned, merged, and pre-processed inorder to perform comprehensive ML analysis.
""")
st.write("#")


st.subheader("Target Location Data")
st.write("""
This raw dataset, obtained from Kaggle, presents Target store locations operational as of April 2017. 
It features initial, unprocessed data including store addresses, coordinates, opening and remodel dates, and various store capabilities (like integrated Starbucks, CVS). 
""")
st.dataframe(target_data)
st.write("#")


st.subheader("Population by Age and Sex")
st.dataframe(pop_age_sex)

st.subheader("Population by Race")
st.dataframe(pop_race)


st.subheader("Household Debt to Income Data")
st.dataframe(debt_data)




