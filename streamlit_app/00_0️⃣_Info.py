import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Streamlit Statistics Calculator", page_icon="🧮")

# Generate the current timestamp dynamically
current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

st.markdown(
"""
# 🧮 **Statistics Calculator**
### **Analyse Data and Perform Key Statistical Tests**

**The Statistics Calculator app is designed to help users analyse numerical data and conduct essential statistical tests with ease. Built using Python and Streamlit, this app provides intuitive tools for statistical exploration and analysis.**

## 🛠️ **How It's Built**

The Statistics Calculator leverages the following technologies:

- **Streamlit** - For creating an intuitive and interactive web interface.
- **NumPy** - For efficient numerical calculations.
- **SciPy** - For performing statistical tests.
- **Matplotlib** - For visualising data and test results.
- **Pandas** - For handling and processing datasets.

## 🧑‍💻 **Key Features**

1. **Normal Distribution Generator**:
   - Generate datasets based on the Normal Distribution.
   - Specify parameters such as mean, standard deviation, and sample size.
   - Download the generated data or copy it directly from the app.

2. **Normal Distribution Checker**:
   - Analyse your dataset to determine if it follows a Normal Distribution.
   - Perform statistical tests like the Shapiro-Wilk test.
   - Visualise your data against a theoretical normal curve.

3. **Significance Level Calculator**:
   - Calculate p-values for Z-tests, T-tests, and more.
   - Visualise acceptance and rejection regions.
   - Determine if the null hypothesis (H₀) can be rejected at a given significance level.

4. **Confidence Interval Calculator**:
   - Compute confidence intervals for means and proportions.
   - Visualise confidence intervals with shaded regions.
   - Determine whether specific values fall within the confidence interval.

## 🚀 **Getting Started**

### **Local Installation**

1. Clone the repository:
```bash
git clone https://github.com/user/StatisticsApp.git
```
**Hint:** Replace `user` with `josericodata` in the URL above. I am deliberately asking you to pause here so you can support my work. If you appreciate it, please consider giving the repository a star or forking it. Your support means a lot—thank you! 😊

2. Navigate to the project directory:

```bash

cd StatisticsApp

```

3. Create a virtual environment:
```bash
python3 -m venv venvStats
```

4. Activate the virtual environment:
```bash
source venvStats/bin/activate
```

5. Install requirements:
```bash
pip install -r requirements.txt
```

6. Navigate to the app directory:
```bash
cd streamlit_app
```

7. Run the app:
```bash
streamlit run 00_0️⃣_Info.py
```

The app will be live at `http://localhost:8501`.

## 🌟 **Future Enhancements**

Planned features include:

- Additional statistical tests, including Chi-square and ANOVA.
- Support for uploading and analysing larger datasets.
- Advanced visualisations for data exploration.

## 🎓 **Motivation**

This project comes after graduating from CCT College in Dublin, Ireland. The goal of this app is to help users understand how statistics work by making abstract concepts more tangible through visualisations. I hope this tool empowers you to explore and learn statistics with ease.

## 🔧 **Environment Setup**

This app has been built and tested in the following environment:

- **Operating System**: Ubuntu 22.04.5 LTS (Jammy)
- **Python Version**: Python 3.10.12

## 📋 **Important Notes**

- **Statistical Knowledge**: While the app simplifies statistical analysis, a basic understanding of statistics will enhance the user experience.
- **Input Data**: Ensure your input data is clean and formatted correctly to avoid errors.


### 🤝 **Open Pull Requests**
If you need a specific statistical tool, feel free to contact me by opening a pull request on GitHub or via email at **maninastre@gmail.com**.

## ⚠️ **Disclaimer**

This app is intended for educational and demonstration purposes only. The results are not guaranteed to be error-free and should not be used for critical decision-making.


"""
)

# Display the timestamp in a Streamlit app
st.write("### 🔄 Last Updated")
st.write(f"The app was last updated on: **{current_timestamp}**")

