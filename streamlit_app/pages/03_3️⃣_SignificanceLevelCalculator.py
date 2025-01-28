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
    The null hypothesis (H₀) is a default assumption or statement about a population parameter. It usually states that there is no effect, no difference, or no relationship between variables.

    ### What is Alpha (α)?
    Alpha (α) represents the threshold probability for rejecting the null hypothesis. Commonly set to 0.05, it defines the likelihood of rejecting H₀ when it is actually true (Type I error).
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
                critical_value = norm.ppf(1 - alpha / 2)
                rejection_areas = [(-np.inf, -critical_value), (critical_value, np.inf)]
            elif tail == "Left-Tailed":
                p_value = norm.cdf(z_score)
                critical_value = norm.ppf(alpha)
                rejection_areas = [(-np.inf, critical_value)]
            else:  # Right-Tailed
                p_value = 1 - norm.cdf(z_score)
                critical_value = norm.ppf(1 - alpha)
                rejection_areas = [(critical_value, np.inf)]

            st.write(f"### P-Value: {p_value:.4f}")
            if p_value < alpha:
                st.success("Reject the null hypothesis: The result is statistically significant.")
            else:
                st.warning("Fail to reject the null hypothesis: The result is not statistically significant.")

            # Plot the distribution with a **static** rejection region
            st.write("### Visualisation:")
            x = np.linspace(-4, 4, 1000)
            y = norm.pdf(x)
            fig, ax = plt.subplots()
            ax.plot(x, y, label="Normal Distribution", color="black")

            for area in rejection_areas:
                ax.fill_between(x, 0, y, where=(x >= area[0]) & (x <= area[1]), color="red", alpha=0.5, label="Rejection Region")

            ax.scatter([z_score], [norm.pdf(z_score)], color="blue", s=100, label="P-Value (Z-Score)")
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
                critical_value = t.ppf(1 - alpha / 2, df=degrees_of_freedom)
                rejection_areas = [(-np.inf, -critical_value), (critical_value, np.inf)]
            elif tail == "Left-Tailed":
                p_value = t.cdf(t_score, df=degrees_of_freedom)
                critical_value = t.ppf(alpha, df=degrees_of_freedom)
                rejection_areas = [(-np.inf, critical_value)]
            else:  # Right-Tailed
                p_value = 1 - t.cdf(t_score, df=degrees_of_freedom)
                critical_value = t.ppf(1 - alpha, df=degrees_of_freedom)
                rejection_areas = [(critical_value, np.inf)]

            st.write(f"### P-Value: {p_value:.4f}")
            if p_value < alpha:
                st.success("Reject the null hypothesis: The result is statistically significant.")
            else:
                st.warning("Fail to reject the null hypothesis: The result is not statistically significant.")

            # Static rejection region for T-Test
            st.write("### Visualisation:")
            x = np.linspace(-4, 4, 1000)
            y = t.pdf(x, df=degrees_of_freedom)
            fig, ax = plt.subplots()
            ax.plot(x, y, label="T-Distribution", color="black")

            for area in rejection_areas:
                ax.fill_between(x, 0, y, where=(x >= area[0]) & (x <= area[1]), color="red", alpha=0.5, label="Rejection Region")

            ax.scatter([t_score], [t.pdf(t_score, df=degrees_of_freedom)], color="blue", s=100, label="P-Value (T-Score)")
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
            critical_value = chi2.ppf(1 - alpha, df=degrees_of_freedom)

            st.write(f"### P-Value: {p_value:.4f}")
            if p_value < alpha:
                st.success("Reject the null hypothesis: The result is statistically significant.")
            else:
                st.warning("Fail to reject the null hypothesis: The result is not statistically significant.")

            # Static rejection region for Chi-Square Test
            st.write("### Visualisation:")
            x = np.linspace(0, 10, 1000)
            y = chi2.pdf(x, df=degrees_of_freedom)
            fig, ax = plt.subplots()
            ax.plot(x, y, label="Chi-Square Distribution", color="black")

            ax.fill_between(x, 0, y, where=(x >= critical_value), color="red", alpha=0.5, label="Rejection Region")
            ax.scatter([chi_square], [chi2.pdf(chi_square, df=degrees_of_freedom)], color="blue", s=100, label="P-Value (Chi-Square)")

            ax.axhline(0, color="gray", linewidth=0.5)
            ax.set_title("Chi-Square Test Visualisation")
            ax.set_xlabel("Chi-Square Statistic")
            ax.set_ylabel("Density")
            ax.legend()
            st.pyplot(fig)

        except Exception as e:
            st.error(f"An error occurred: {e}")
            