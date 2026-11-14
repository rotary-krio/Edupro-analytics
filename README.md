# 🎓 EduPro Learner Analytics Dashboard

A dynamic, interactive web application built with **Streamlit** and **Plotly** to analyze learner demographics, course enrollments, and behavioral patterns on the EduPro online learning platform.

This dashboard transforms raw CSV data into actionable insights, helping stakeholders make data-driven decisions regarding curriculum design, targeted marketing, and platform growth.

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
