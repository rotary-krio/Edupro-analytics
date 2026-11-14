# 🎓 EduPro Learner Analytics Dashboard

A dynamic, interactive web application built with **Streamlit** and **Plotly** to analyze learner demographics, course enrollments, and behavioral patterns on the EduPro online learning platform.

This dashboard transforms raw CSV data into actionable insights, helping stakeholders make data-driven decisions regarding curriculum design, targeted marketing, and platform growth.

---
# 🔍 Research Paper
# Google Docs:https://drive.google.com/drive/folders/1DvGgyeEIGqeX4JNbmeIzzl6PJ3wo8W0H?usp=drive_link

---

## 📸 Features at a Glance

- **Auto-Loading Data:** The app automatically detects and loads data from a local `data/` folder.
- **Interactive Global Filters:** Use the sidebar to filter the entire dashboard by Age Group, Gender, Course Category, and Course Level.
- **5 Analytical Modules:**
  1. **📊 Overview:** High-level KPIs and course type distributions.
  2. **👥 Demographics:** Age and gender breakdowns of the learner base.
  3. **📚 Course Analysis:** Popular categories and the Top 10 most enrolled courses.
  4. **🎯 Preferences:** Heatmaps cross-referencing demographics with course levels.
  5. **📈 Insights:** Engagement metrics, active learner concentration, and enrollment trends.
- **Modern UI/UX:** A sleek dark-mode interface featuring bold typography and a custom Violet/Blue gradient color palette.

---

## 🛠️ Tech Stack

Language: Python 3
Web Framework: Streamlit
Data Manipulation: Pandas
Data Visualization: Plotly Express

---
### ⚡ Zero-Setup Data Loading: Automatically detects and merges multiple CSV datasets on startup—no manual uploads required!

### 🎛️ Global Dynamic Filtering: An interactive sidebar allows users to filter the entire dashboard by Age Group, Gender, Course Category, and Skill Level in real-time.

### 📈 5 Comprehensive Modules: Dive deep into Overview, Demographics, Course Analysis, Preferences, and Behavioral Insights.

### 🔥 Advanced Heatmap Analysis: Visually uncover hidden preferences, such as which age groups flock to which specific course categories.

### 👑 Power User Identification: Tracks enrollment concentration to reveal how the top 10% of learners drive platform engagement.

### 🎨 Custom UI Styling: Built with custom CSS for a sleek, high-contrast dark mode that makes the data pop.

---

## 👨‍💻 Author

Krishiv Kage\
rotarykrio@gmail.com\
Data Analytics Intern\
Unified Mentor

---

## 📂 Project Structure

Ensure your project folder is structured exactly like this:

```text
edupro_analytics/
│
├── app.py                  # The main Streamlit application (this file)
├── README.md               # Project documentation
├── Research_Paper.pdf      # Detailed EDA and insights
├── Executive_Summary.pdf   # Stakeholder summary
│
└── data/                   # The folder containing your CSV files
    ├── Users.csv
    ├── Courses.csv
    ├── Transactions.csv
    └── Teachers.csv
