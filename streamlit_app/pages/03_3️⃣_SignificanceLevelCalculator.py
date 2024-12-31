import streamlit as st
from scipy.stats import norm, t, chi2
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Significance Level Calculator", page_icon="🧮")

st.title("Significance Level Calculator")

st.markdown(
    """
    This tool helps you calculate p-values and significance levels for common statistical tests.
    Choose a test, input the required values, and determine the statistical significance.

    ### What is the Null Hypothesis (H₀)?
    The null hypothesis (H₀) is a default assumption or statement about a population parameter. It usually states that there is no effect, no difference, or no relationship between variables. For example:
    - In a drug trial, H₀ might state that the drug has no effect on patients compared to a placebo.
    - In a coin flip experiment, H₀ might state that the coin is fair (equal chance of heads and tails).

    ### In statistical terms:
    - **Rejecting the null hypothesis (H₀)** means that the observed data is unlikely to occur if H₀ is true, suggesting there is evidence for the alternative hypothesis.
    - **Failing to reject H₀** means that the data does not provide sufficient evidence to conclude that H₀ is false, though it does not necessarily prove H₀ is true.

    ### What is Alpha (α)?
    Alpha (α) represents the threshold probability for rejecting the null hypothesis. Commonly set to 0.05, it defines the likelihood of rejecting H₀ when it is actually true (Type I error). You can adjust alpha based on the context of your test.
    """
)

# Input for alpha
alpha = st.number_input("Set Significance Level (Alpha, α):", value=0.05, min_value=0.001, max_value=0.1, step=0.001, format="%.3f")

# Input fields for significance level calculation
test_type = st.selectbox("Select Test Type:", ["Z-Test", "T-Test", "Chi-Square Test"])

if test_type == "Z-Test":
    z_score = st.number_input("Enter Z-Score:", value=0.0, step=0.01)
    tail = st.radio("Tail Type:", ["Two-Tailed", "Left-Tailed", "Right-Tailed"])
    if st.button("Calculate p-value"):
        try:
            if tail == "Two-Tailed":
                p_value = 2 * (1 - norm.cdf(abs(z_score)))
                rejection_areas = [(-np.inf, -abs(z_score)), (abs(z_score), np.inf)]
            elif tail == "Left-Tailed":
                p_value = norm.cdf(z_score)
                rejection_areas = [(-np.inf, z_score)]
            else:  # Right-Tailed
                p_value = 1 - norm.cdf(z_score)
                rejection_areas = [(z_score, np.inf)]

            st.write(f"### P-Value: {p_value:.4f}")
            if p_value < alpha:
                st.success("Reject the null hypothesis: The result is statistically significant.")
            else:
                st.warning("Fail to reject the null hypothesis: The result is not statistically significant.")

            # Plot the distribution with rejection regions
            st.write("### Visualisation:")
            x = np.linspace(-4, 4, 1000)
            y = norm.pdf(x)
            fig, ax = plt.subplots()
            ax.plot(x, y, label="Normal Distribution", color="black")
            for area in rejection_areas:
                ax.fill_between(x, 0, y, where=(x >= area[0]) & (x <= area[1]), color="red", alpha=0.5, label="Rejection Region")
            ax.axvline(z_score, color="blue", linestyle="--", label="Z-Score")
            ax.axhline(0, color="gray", linewidth=0.5)
            ax.set_title("Z-Test Visualisation")
            ax.set_xlabel("Z-Score")
            ax.set_ylabel("Density")
            ax.legend()
            st.pyplot(fig)

        except Exception as e:
            st.error(f"An error occurred: {e}")

elif test_type == "T-Test":
    t_score = st.number_input("Enter T-Score:", value=0.0, step=0.01)
    degrees_of_freedom = st.number_input("Enter Degrees of Freedom:", value=1, min_value=1, step=1)
    tail = st.radio("Tail Type:", ["Two-Tailed", "Left-Tailed", "Right-Tailed"])
    if st.button("Calculate p-value"):
        try:
            if tail == "Two-Tailed":
                p_value = 2 * (1 - t.cdf(abs(t_score), df=degrees_of_freedom))
                rejection_areas = [(-np.inf, -abs(t_score)), (abs(t_score), np.inf)]
            elif tail == "Left-Tailed":
                p_value = t.cdf(t_score, df=degrees_of_freedom)
                rejection_areas = [(-np.inf, t_score)]
            else:  # Right-Tailed
                p_value = 1 - t.cdf(t_score, df=degrees_of_freedom)
                rejection_areas = [(t_score, np.inf)]

            st.write(f"### P-Value: {p_value:.4f}")
            if p_value < alpha:
                st.success("Reject the null hypothesis: The result is statistically significant.")
            else:
                st.warning("Fail to reject the null hypothesis: The result is not statistically significant.")

            # Plot the t-distribution with rejection regions
            st.write("### Visualisation:")
            x = np.linspace(-4, 4, 1000)
            y = t.pdf(x, df=degrees_of_freedom)
            fig, ax = plt.subplots()
            ax.plot(x, y, label="T-Distribution", color="black")
            for area in rejection_areas:
                ax.fill_between(x, 0, y, where=(x >= area[0]) & (x <= area[1]), color="red", alpha=0.5, label="Rejection Region")
            ax.axvline(t_score, color="blue", linestyle="--", label="T-Score")
            ax.axhline(0, color="gray", linewidth=0.5)
            ax.set_title("T-Test Visualisation")
            ax.set_xlabel("T-Score")
            ax.set_ylabel("Density")
            ax.legend()
            st.pyplot(fig)

        except Exception as e:
            st.error(f"An error occurred: {e}")

elif test_type == "Chi-Square Test":
    chi_square = st.number_input("Enter Chi-Square Statistic:", value=0.0, step=0.01)
    degrees_of_freedom = st.number_input("Enter Degrees of Freedom:", value=1, min_value=1, step=1)
    if st.button("Calculate p-value"):
        try:
            p_value = 1 - chi2.cdf(chi_square, df=degrees_of_freedom)
            st.write(f"### P-Value: {p_value:.4f}")
            if p_value < alpha:
                st.success("Reject the null hypothesis: The result is statistically significant.")
            else:
                st.warning("Fail to reject the null hypothesis: The result is not statistically significant.")

            # Plot the chi-square distribution with rejection regions
            st.write("### Visualisation:")
            x = np.linspace(0, 10, 1000)
            y = chi2.pdf(x, df=degrees_of_freedom)
            fig, ax = plt.subplots()
            ax.plot(x, y, label="Chi-Square Distribution", color="black")
            ax.fill_between(x, 0, y, where=(x >= chi_square), color="red", alpha=0.5, label="Rejection Region")
            ax.axvline(chi_square, color="blue", linestyle="--", label="Chi-Square Statistic")
            ax.axhline(0, color="gray", linewidth=0.5)
            ax.set_title("Chi-Square Test Visualisation")
            ax.set_xlabel("Chi-Square Statistic")
            ax.set_ylabel("Density")
            ax.legend()
            st.pyplot(fig)

        except Exception as e:
            st.error(f"An error occurred: {e}")

