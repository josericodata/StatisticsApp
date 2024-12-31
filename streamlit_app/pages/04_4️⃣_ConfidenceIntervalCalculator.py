# 03_ConfidenceIntervalCalculator.py
import streamlit as st
from scipy.stats import norm, t
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Confidence Interval Calculator", page_icon="📏")

st.title("Confidence Interval Calculator")

st.markdown(
    """
    This tool allows you to calculate confidence intervals for means or proportions based on your input data.
    Confidence intervals provide a range of values that likely contain the population parameter of interest, 
    meaning we are 'confident' that the true value lies within this range given the specified level of confidence.

    ### How to use:
    - Enter the relevant statistics (mean, standard deviation, sample size) or proportions (successes and trials).
    - Choose the desired confidence level.
    - Input a specific x-axis value or p-value to evaluate its position relative to the confidence interval.
    - The tool will calculate and display the confidence interval and state whether the given value lies within the interval.

    ### What is Alpha (α)?
    Alpha (α) represents the complement of the confidence level (1 - Confidence Level). For example, a 95% confidence level corresponds to an alpha of 0.05.
    The alpha value determines the probability of observing a result outside the confidence interval if the null hypothesis is true.
    """
)

# Select calculation type
calc_type = st.selectbox("Select Calculation Type:", ["Mean", "Proportion"])

if calc_type == "Mean":
    # Input fields for confidence interval for a mean
    sample_mean = st.number_input("Enter Sample Mean:", value=0.0)
    sample_std_dev = st.number_input("Enter Sample Standard Deviation:", value=1.0, min_value=0.0, format="%.2f")
    sample_size = st.number_input("Enter Sample Size:", value=30, min_value=1, step=1)
    confidence_level = st.slider("Select Confidence Level (%):", 80, 99, 95)
    x_value = st.number_input("Enter X-Axis Value to Check (optional):", value=0.0)

    if st.button("Calculate Confidence Interval"):
        try:
            # Calculate standard error
            standard_error = sample_std_dev / np.sqrt(sample_size)

            # Determine z or t critical value
            if sample_size >= 30:
                critical_value = norm.ppf(1 - (1 - confidence_level / 100) / 2)
            else:
                critical_value = t.ppf(1 - (1 - confidence_level / 100) / 2, df=sample_size - 1)

            # Calculate margin of error
            margin_of_error = critical_value * standard_error

            # Confidence interval
            lower_bound = sample_mean - margin_of_error
            upper_bound = sample_mean + margin_of_error

            st.write(f"### Confidence Interval:")
            st.success(f"({lower_bound:.2f}, {upper_bound:.2f})")

            # Check if x_value lies within the confidence interval
            if lower_bound <= x_value <= upper_bound:
                st.info(f"With a {confidence_level}% confidence level, the value {x_value:.2f} lies within the confidence interval.")
            else:
                st.warning(f"With a {confidence_level}% confidence level, the value {x_value:.2f} lies outside the confidence interval.")

            # Plot confidence interval
            st.write("### Visualisation:")
            fig, ax = plt.subplots()
            x = np.linspace(lower_bound - 2, upper_bound + 2, 500)
            y = norm.pdf(x, loc=sample_mean, scale=standard_error)
            ax.plot(x, y, label="Normal Distribution", color="black")
            ax.axvline(lower_bound, color="red", linestyle="--", label=f"Lower Bound ({lower_bound:.2f})")
            ax.axvline(upper_bound, color="red", linestyle="--", label=f"Upper Bound ({upper_bound:.2f})")
            ax.axvline(sample_mean, color="blue", linestyle="--", label=f"Mean ({sample_mean:.2f})")
            ax.axvline(x_value, color="purple", linestyle="-", label=f"X-Value ({x_value:.2f})")
            ax.fill_between(x, 0, y, where=(x >= lower_bound) & (x <= upper_bound), color="green", alpha=0.2, label="Confidence Interval")
            ax.set_title("Confidence Interval for Mean")
            ax.set_xlabel("Values")
            ax.set_ylabel("Density")
            ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=1)
            st.pyplot(fig)

        except Exception as e:
            st.error(f"An error occurred: {e}")

elif calc_type == "Proportion":
    # Input fields for confidence interval for a proportion
    successes = st.number_input("Enter Number of Successes:", value=0, min_value=0, step=1)
    trials = st.number_input("Enter Number of Trials:", value=1, min_value=1, step=1)
    confidence_level = st.slider("Select Confidence Level (%):", 80, 99, 95)
    x_value = st.number_input("Enter Proportion to Check (optional):", value=0.0, min_value=0.0, max_value=1.0, step=0.01)

    if st.button("Calculate Confidence Interval"):
        try:
            # Calculate sample proportion
            sample_proportion = successes / trials

            # Standard error for proportion
            standard_error = np.sqrt(sample_proportion * (1 - sample_proportion) / trials)

            # Z critical value (large sample assumption)
            critical_value = norm.ppf(1 - (1 - confidence_level / 100) / 2)

            # Margin of error
            margin_of_error = critical_value * standard_error

            # Confidence interval
            lower_bound = sample_proportion - margin_of_error
            upper_bound = sample_proportion + margin_of_error

            st.write(f"### Confidence Interval:")
            st.success(f"({lower_bound:.2f}, {upper_bound:.2f})")

            # Check if x_value lies within the confidence interval
            if lower_bound <= x_value <= upper_bound:
                st.info(f"With a {confidence_level}% confidence level, the value {x_value:.2f} lies within the confidence interval.")
            else:
                st.warning(f"With a {confidence_level}% confidence level, the value {x_value:.2f} lies outside the confidence interval.")

            # Plot confidence interval
            st.write("### Visualisation:")
            fig, ax = plt.subplots()
            x = np.linspace(0, 1, 500)
            y = norm.pdf(x, loc=sample_proportion, scale=standard_error)
            ax.plot(x, y, label="Normal Distribution", color="black")
            ax.axvline(lower_bound, color="red", linestyle="--", label=f"Lower Bound ({lower_bound:.2f})")
            ax.axvline(upper_bound, color="red", linestyle="--", label=f"Upper Bound ({upper_bound:.2f})")
            ax.axvline(sample_proportion, color="blue", linestyle="--", label=f"Proportion ({sample_proportion:.2f})")
            ax.axvline(x_value, color="purple", linestyle="--", label=f"X-Value ({x_value:.2f})")
            ax.fill_between(x, 0, y, where=(x >= lower_bound) & (x <= upper_bound), color="green", alpha=0.2, label="Confidence Interval")
            ax.set_title("Confidence Interval for Proportion")
            ax.set_xlabel("Proportion Values")
            ax.set_ylabel("Density")
            ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=1)
            st.pyplot(fig)

        except Exception as e:
            st.error(f"An error occurred: {e}")

