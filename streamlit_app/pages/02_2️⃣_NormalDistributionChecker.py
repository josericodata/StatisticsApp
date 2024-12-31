# 01_NormalDistributionGenerator.py
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm, shapiro

st.set_page_config(page_title="Normal Distribution Checker", page_icon="🧮")

st.title("Normal Distribution Checker")

st.markdown(
    """
    Input your data below, and we'll analyse its distribution and compare it to a standard Normal Distribution (mean=0, standard deviation=1).
    You can either upload a CSV file or paste the data.
    """
)

# Input data options
uploaded_file = st.file_uploader("Upload a CSV file:", type=["csv"])
user_input = st.text_area("Or enter your numerical data (comma-separated):", "")

if st.button("Analyse"):
    try:
        if uploaded_file is not None:
            # Load data from CSV file
            df = pd.read_csv(uploaded_file)
            st.write("### Uploaded Data Preview:")
            st.write(df.head())

            # Assume data is in the first column
            data = df.iloc[:, 0].dropna().values
        elif user_input:
            # Process input data from text area
            raw_data = user_input.replace("\n", ",")
            data = np.array([float(x) for x in raw_data.split(",") if x.strip() != ""])
        else:
            st.warning("Please upload a file or input numerical data.")
            exit()

        # Calculate mean and standard deviation
        mean = np.mean(data)
        std_dev = np.std(data)

        st.write("### Input Data Statistics:")
        st.write(f"Mean: {mean}")
        st.write(f"Standard Deviation: {std_dev}")

        # Perform Shapiro-Wilk test for normality
        st.write("### Shapiro-Wilk Test for Normality:")
        shapiro_stat, shapiro_p = shapiro(data)
        st.write(f"Statistic: {shapiro_stat}, p-value: {shapiro_p}")

        if shapiro_p > 0.05:
            st.success("The data follows a Normal Distribution based on the Shapiro-Wilk test.")
        else:
            st.warning("The data does not follow a Normal Distribution based on the Shapiro-Wilk test.")

        # Plot the data against a Normal Distribution
        st.write("### Data Visualisation:")
        fig, ax = plt.subplots()

        # Histogram of input data
        ax.hist(data, bins=30, density=True, alpha=0.6, color='blue', label="Input Data")

        # Plot standard normal distribution curve
        x = np.linspace(min(data), max(data), 1000)
        ax.plot(x, norm.pdf(x, 0, 1), 'r--', label="Standard Normal (mean=0, std_dev=1)")

        # Plot actual data's normal curve
        ax.plot(x, norm.pdf(x, mean, std_dev), 'g-', label=f"Actual (mean={mean:.2f}, std_dev={std_dev:.2f})")

        ax.set_title("Normal Distribution Comparison")
        ax.set_xlabel("Values")
        ax.set_ylabel("Density")

        # Place legend outside the graph
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=1)

        st.pyplot(fig)

    except Exception as e:
        st.error(f"An error occurred: {e}")

