

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Mental Health Data Visualization")

# File uploader for CSV
uploaded_file = st.file_uploader("Upload mental health data (CSV)", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file
    data = pd.read_csv(uploaded_file)
    st.write("### Data Preview")
    st.dataframe(data)
    # st.write(data.columns)

    # Dropdown for State and Year selection
    state = st.selectbox("Select State", data['State'].unique())
    year = st.selectbox("Select Year", data['Year'].unique())

    # Filter data based on State and Year
    filtered_data = data[(data['State'] == state) & (data['Year'] == year)]

    if filtered_data.empty:
        st.error("No data available for the selected State and Year.")
    else:
        # X and Y columns
        x_column = 'Total Number of Survey Respondents'
        y_column = 'Percentage With Mental Distress'

        # Plot type selection
        graph_type = st.selectbox(
            "Select Graph Type",
            ["Line", "Scatter", "Bar"]
        )

        # Plot button
        if st.button("Plot Graph"):
            fig, ax = plt.subplots()

            if graph_type == "Line":
                ax.plot(filtered_data[x_column], filtered_data[y_column], marker='o')
            elif graph_type == "Scatter":
                ax.scatter(filtered_data[x_column], filtered_data[y_column])
            elif graph_type == "Bar":
                ax.bar(filtered_data[x_column], filtered_data[y_column])

            # Set dynamic titles and labels
            ax.set_title(f"{state} {year} {graph_type} Chart")
            ax.set_xlabel("Total Number of Survey Respondents")
            ax.set_ylabel("Percentage With Mental Distress")

            st.pyplot(fig)

else:
    st.info("Please upload a CSV file to get started.")
