# ==============================================================================
# 🎓 EduPro Learner Analytics Dashboard
# ==============================================================================
# 
# --- README.md ---
# 
# # 🎓 EduPro Learner Analytics Dashboard
# 
# A dynamic, interactive web application built with **Streamlit** and **Plotly** 
# to analyze learner demographics, course enrollments, and behavioral patterns 
# on the EduPro online learning platform.
# 
# This dashboard transforms raw CSV data into actionable insights, helping 
# stakeholders make data-driven decisions regarding curriculum design, targeted 
# marketing, and platform growth.
# 
# ---
# 
# ## 📸 Features at a Glance
# 
# - **Auto-Loading Data:** The app automatically detects and loads data from a local `data/` folder.
# - **Interactive Global Filters:** Use the sidebar to filter the entire dashboard by Age Group, Gender, Course Category, and Course Level.
# - **5 Analytical Modules:**
#   1. **📊 Overview:** High-level KPIs and course type distributions.
#   2. **👥 Demographics:** Age and gender breakdowns of the learner base.
#   3. **📚 Course Analysis:** Popular categories and the Top 10 most enrolled courses.
#   4. **🎯 Preferences:** Heatmaps cross-referencing demographics with course levels.
#   5. **📈 Insights:** Engagement metrics, active learner concentration, and enrollment trends.
# - **Modern UI/UX:** A sleek dark-mode interface featuring bold typography and a custom Violet/Blue gradient color palette.
# 
# ---
# 
# ## 📂 Project Structure
# 
# Ensure your project folder is structured exactly like this:
# 
# ```text
# edupro_analytics/
# │
# ├── app.py                  # The main Streamlit application (this file)
# ├── README.md               # Project documentation
# │
# └── data/                   # The folder containing your CSV files
#     ├── Users.csv
#     ├── Courses.csv
#     ├── Transactions.csv
#     └── Teachers.csv
# ```
# 
# ---
# 
# ## 🚀 How to Run the Project
# 
# ### 1. Prerequisites
# Make sure you have Python installed (version 3.8 or higher). 
# 
# ### 2. Install Required Libraries
# Open your terminal, navigate to your project folder, and run:
# ```bash
# pip install streamlit pandas plotly
# ```
# 
# ### 3. Run the Application
# Start the Streamlit server by running:
# ```bash
# streamlit run app.py
# ```
# 
# ### 4. View the Dashboard
# A new tab should automatically open in your default web browser. If it doesn't, 
# navigate to the URL shown in your terminal (usually http://localhost:8501).
# 
# ---
# 
# ## 🛠️ Tech Stack
# - **Language:** Python 3
# - **Web Framework:** Streamlit
# - **Data Manipulation:** Pandas
# - **Data Visualization:** Plotly Express
# 
# ---
# 
# ## 🧠 Key Analytical Questions Answered
# - *Which age groups are the most active on the platform?*
# - *How do enrollment patterns differ by gender?*
# - *What course categories and specific courses attract the highest volume of learners?*
# - *Are there specific course levels (Beginner, Intermediate, Advanced) that certain demographics prefer?*
# - *What percentage of the platform's enrollments come from the top 10% of "power users"?*
# 
# ---
# 
# ## 🐛 Troubleshooting
# - **"Data files not found" Error:** Make sure you have a folder named `data` in the same directory as `app.py`, and that it contains the 4 CSV files exactly as named above.
# - **Module Not Found:** If you get an error about missing `streamlit` or `pandas`, ensure you ran the `pip install` command.
# - **Charts not loading properly:** Ensure your CSV files are not empty and contain the correct column headers (e.g., `CourseRating`, `UserID`).
# 
# ---
# 
# ## 👨‍💻 Author
# **[Krishiv Kage]**  
# *Data Analytics Intern*  
# *Unified Mentor*  
# 
# ==============================================================================
# --- END OF README ---
# ==============================================================================
