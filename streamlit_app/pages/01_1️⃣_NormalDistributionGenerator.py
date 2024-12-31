# 01_NormalDistributionGenerator.py
import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Normal Distribution Generator", page_icon="🧮")

st.title("Normal Distribution Generator")

st.markdown(
    """
    This tool allows you to generate a dataset based on a Normal Distribution.
    Specify the mean, standard deviation, and the size of the dataset, then click Generate.
    You can copy the dataset or download it as a CSV file.

    Once you have generated the dataset, head over to the [Normal Distribution Checker](./NormalDistributionChecker) page to analyse the data.
    """
)

# Input fields
mean = st.number_input("Population Mean (μ):", value=0.0)
std_dev = st.number_input("Standard Deviation (σ):", value=1.0, min_value=0.0, format="%.2f")
size = st.number_input("Size of Dataset:", value=100, min_value=1, max_value=5000, step=1)

if st.button("Generate"):
    try:
        # Generate normal distribution data
        data = np.random.normal(loc=mean, scale=std_dev, size=int(size))

        # Display generated data
        st.write("### Generated Dataset:")
        st.dataframe(pd.DataFrame(data, columns=["Values"]))

        # Provide options to copy or download the data
        csv = pd.DataFrame(data, columns=["Values"]).to_csv(index=False)
        st.download_button(label="Download CSV", data=csv, file_name="normal_distribution.csv", mime="text/csv")

        st.text_area("Copy the data:", value=", ".join(map(str, data)), height=200)

    except Exception as e:
        st.error(f"An error occurred: {e}")

